Crypto Portfolio Management System
==================================

This is a Django project that allows users to manage their cryptocurrency portfolios by utilizing API calls to the CoinGecko cryptocurrency API. The following features are implemented:

User Authentication
-------------------

-   Users can sign up, log in, and log out of the system
-   Passwords are securely stored and hashed using Django's built-in authentication system

Referral System
---------------

-   Users can invite other users to join the platform using a referral link
-   Referral links are tracked and the referrer receives a bonus when a new user signs up using their link

Crypto-Currency Wallets
-----------------------

-   Users can add and remove cryptocurrencies to their wallet
-   Each cryptocurrency has a name, current price, and quantity which the user can add to their portfolio
-   Users can see a detail view of their portfolio, which shows the value of each cryptocurrency in their wallet and the total value of their portfolio

Homepage
--------

-   The homepage shows the 24-hour price and percentage change of the top 10 ranked cryptocurrencies
-   It also displays the 24-hour price and percentage change of the currencies in the user's portfolio

Installation
------------

1.  Clone the repository: `git clone https://github.com/DonGuillotine/django-crypto-portfolio`
2.  Install the required packages: `pip install -r requirements.txt`
3.  Apply database migrations: `python manage.py migrate`
4.  Create a Superuser: `python manage.py createsuperuser`
5.  Run the server: `python manage.py runserver`

Usage
-----

1.  Open your web browser and go to `http://localhost:8000`
2.  Register for an account or log in if you already have one
3.  Add cryptocurrencies to your wallet and track your portfolio value
4.  Invite other users to join the platform using your referral link
