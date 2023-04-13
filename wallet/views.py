from django.shortcuts import render, redirect
from .models import Holding
from .positions import *
from .helper_functions import get_price, get_fg, txtToArray, cum_up_or_down
from .forms import HoldingForm
from datetime import date
import os


def holdings(request):
    if request.user.id:
        module_dir = os.path.dirname(__file__) 
        #  Full path to text.
        file_path = os.path.join(module_dir, './static/portfolio/text/coin_list.txt')   
        coin_list = txtToArray(file_path)

        # Holdings from database
        holdings_db = Holding.objects.filter(trader=request.user.id).filter(sold=False) 

        # Holdings as objects will be outputted to the front end
        portfolio = Positions() 
        for holding in holdings_db:
            portfolio.add(holding.coin_id, holding.symbol, float(holding.entry_price), float(holding.entry_amount), date=holding.entry_date, dbID=holding.id)
        
        btc = f'{get_price("bitcoin"):,}'
        eth = f'{get_price("ethereum"):,}'
        fg = get_fg()
        fg_class = get_fg(classification=True)


        if request.method == "POST":
            form = HoldingForm(request.POST)
            print("validating")
            print(form.errors)
            print(form.fields["use_mv_entry"])
            if form.is_valid():
                
                print("Holdings")
                obj = form.save(commit=False)
                obj.trader = request.user
                if request.POST.get("use_mv_entry"):
                    obj.entry_price = get_price(obj.coin_id.lower())
                obj.save()
                return redirect('holdings')
        else:
            form = HoldingForm()

        cum_pl = portfolio.get_cumulative_pl()
        stance = cum_up_or_down(cum_pl)

        portfolio.display()
        return render(request, 'portfolio/holdings.html', {
            'coin_list': coin_list,
            'BTC': btc,
            'ETH': eth,
            'FG': fg,
            'FG_class': fg_class,
            'portfolio': portfolio,
            'stance': stance,
            'cum_val': f'{portfolio.get_cumulative_value():,}',
            'cum_pl': f'{cum_pl:,}',
            'cum_pl_perc': f'{portfolio.get_cumulative_pl_percent():,}',
            'form': form,
            'current': True
        })
    else:
        return redirect('user-portfolio')
