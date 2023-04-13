# Import the NumPy library for numerical calculations
import numpy as np  

# Import the time library for time-related functionality
import time  

# Import the CoinGeckoAPI class from the pycoingecko library
from pycoingecko import CoinGeckoAPI  


# Define the Position class
class Position():
    # Define the __init__ method to initialize the Position object
    def __init__(self, inID, inSymbol, inEntryPrice, inEntryAmount, date='-', dbID=''):
        # Create a new CoinGeckoAPI object
        self.cg = CoinGeckoAPI()
        # Initialize the Position object with the following attributes
        # The ID of the cryptocurrency
        self.coin_id = inID 
        # The symbol of the cryptocurrency
        self.symbol = inSymbol 
        # The price at which the cryptocurrency was purchased
        self.entry_price = inEntryPrice 
        # The amount of cryptocurrency that was purchased
        self.entry_amount = inEntryAmount 
        # The current price of the cryptocurrency
        self.current_price = self.get_price()  
        # The current value of the cryptocurrency
        self.current_value = self.get_cur_val()  
        # The profit or loss of the position
        self.pl = self.get_PL()  
        # The profit or loss percentage of the position
        self.pl_percent = self.get_PL_Percent()  
        # The date on which the position was opened
        self.date = date  
        # The ID of the position in the database (if applicable)
        self.dbID = dbID  


    # Define the get_price method to retrieve the current price of the cryptocurrency from the CoinGeckoAPI
    def get_price(self):
        return self.cg.get_price(ids=self.coin_id.lower(), vs_currencies="usd")[self.coin_id.lower()]["usd"]


    # Define the get_cur_val method to calculate the current value of the position
    def get_cur_val(self):
        cur_val = round(((self.entry_amount / self.entry_price) * self.current_price),2)
        return cur_val


    # Define the get_PL method to calculate the profit or loss of the position
    def get_PL(self):
        difference = round(self.current_value - self.entry_amount,2)
        return difference
    

    # Define the get_PL_Percent method to calculate the profit or loss percentage of the position
    def get_PL_Percent(self):
        percent_change = round((((self.pl)/ self.entry_amount) * 100),2)
        return percent_change


    # Define the __str__ method to return a string representation of the Position object
    def __str__(self):
        return f'{self.dbID} - {self.symbol}: | {self.entry_price} | {self.entry_amount} | {self.current_price} | {self.current_value} | {self.pl} | {self.pl_percent} | {self.date}'
