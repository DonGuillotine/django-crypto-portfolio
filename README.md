Crypto Portfolio Management System
==================================

I built a Django project that allows users to manage their cryptocurrency portfolios by utilizing API calls to the CoinGecko cryptocurrency API. This application was built with a TDD (Test Driven Approach), The following features are implemented:

User Authentication
-------------------

-   Users can sign up, log in, and log out of the system.
-   Passwords are securely stored and hashed using Django's built-in authentication system.

![Screenshot (196)](https://user-images.githubusercontent.com/89584431/231948630-9a0ed657-5817-43f5-b5b0-4d4c336fce34.png)


Referral System
---------------

-   Users can invite other users to join the platform using a referral link
-   Referral links are tracked and the referrer receives a bonus when a new user signs up using their link

![Screenshot (193)](https://user-images.githubusercontent.com/89584431/231945891-26eac306-8a03-4b77-94ca-8f120ee3f1c4.png)


Crypto-Currency Wallets
-----------------------

-   Users can Sell or delete cryptocurrencies to their wallet

![Screenshot (192)](https://user-images.githubusercontent.com/89584431/231945679-c920bbd7-664f-4880-b96b-e84465b198f2.png)

-   Each cryptocurrency has a name, current price, and quantity which the user can add to their portfolio

![Screenshot (191)](https://user-images.githubusercontent.com/89584431/231945367-0751bd8e-d222-48bf-80f1-d868aea667fd.png)

-   Users can see a detail view of their portfolio, which shows the value of each cryptocurrency in their wallet and the total value of their portfolio

![Screenshot (190)](https://user-images.githubusercontent.com/89584431/231945186-326ed496-afa9-4b47-93e6-befee7557e55.png)

-   Users can search for new Cryptocurrencies to add to their portfolio

![Screenshot (195)](https://user-images.githubusercontent.com/89584431/231946845-719a2d87-1f94-45a6-8919-c9807a656093.png)

-   Users can View their Previous Holdings

![Screenshot (194)](https://user-images.githubusercontent.com/89584431/231946100-a7e09d1e-a4e2-4c67-8be2-e143e7e3ef39.png)


Homepage
--------

-   The homepage shows the 24-hour price and percentage change of the top 10 ranked cryptocurrencies
-   It also displays the 24-hour price and percentage change of the currencies

![Screenshot (189)](https://user-images.githubusercontent.com/89584431/231944713-60b31f47-488f-4389-82ef-c66d08266bff.png)


![Screenshot (188)](https://user-images.githubusercontent.com/89584431/231944599-81f5c591-e684-45e6-a5d8-45d0baded477.png)


Installation
------------

1.  Clone the repository: `git clone https://github.com/DonGuillotine/django-crypto-portfolio`
2.  Install a virtual environment `pip install virtualenv` (If you don't have one)
3.  Create a virtual environment `virtualenv env`
4.  To Activate the virtual environment `cd Scripts` then type `activate` to activate the virtual environment. Finally change directory back to the project root with `cd ..`
5.  Install the required packages: `pip install -r requirements.txt`
6.  Apply database migrations: `python manage.py migrate`
7.  Create a Superuser: `python manage.py createsuperuser`
8.  Change Directory `cd crypto_portfolio`
9.  In the `settings.py` change `SECRET_KEY = config('SECRET_KEY')` to `SECRET_KEY = "ANY-RANDOM-KEY"`
10. Run the server: `python manage.py runserver`

Usage
-----

1.  Open your web browser and go to `http://localhost:8000`
2.  Register for an account or log in if you already have one
3.  Add cryptocurrencies to your wallet and track your portfolio value
4.  Invite other users to join the platform using your referral link
