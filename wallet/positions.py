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
    


class Positions():
    def __init__(self):
        self.positions = []
        self.money_in = 0

    # A method to add a new Position object to the positions list
    def add(self, inID, inSymbol, inEntryPrice, inEntryAmount, date='-', dbID=''):
        # start the timer
        start = time.time()  
        # Increment Money put into portfolio
        self.money_in += inEntryAmount  
        # Create a new Position object with the given parameters and add it to the positions list
        position = Position(inID, inSymbol, inEntryPrice, inEntryAmount, date, dbID)
        self.positions.append(position)
        np.append(self.positions, position)  # add the new position to the numpy array
        end = time.time()  # stop the timer
        # Print the time taken to add the new holding
        print(f'{end-start} seconds to add holding.')


    # A method to display all the Position objects in the positions list
    def display(self):
        positions = np.asarray(self.positions)  # convert the list to a numpy array
        for position in positions:  # iterate through the numpy array and print each Position object
            print(position)


    # A method to get the cumulative value of all the Position objects in the positions list
    def get_cumulative_value(self):
        try:
            cumulative_value = 0
            positions = np.asarray(self.positions)  # convert the list to a numpy array
            for position in positions:  # iterate through the numpy array and calculate the cumulative value
                cumulative_value += position.current_value
            return round(cumulative_value,2)  # round the cumulative value to 2 decimal places
        except ZeroDivisionError:
            return 0  # if there are no positions, return 0


    # A method to get the cumulative profit or loss of all the Position objects in the positions list
    def get_cumulative_pl(self):
        try:
            pl = round((self.get_cumulative_value() - self.money_in),2)  # calculate the profit or loss
            return pl  # return the profit or loss rounded to 2 decimal places
        except ZeroDivisionError:
            return 0  # if there are no positions, return 0


    # A method to get the cumulative profit or loss percentage of all the Position objects in the positions list
    def get_cumulative_pl_percent(self):
        try:
            pl_percent = ((self.get_cumulative_value() / self.money_in - 1)) * 100  # calculate the profit or loss percentage
            return round(pl_percent,2)  # return the profit or loss percentage rounded to 2 decimal places
        except ZeroDivisionError:
            return 0  # if there are no positions, return 0


class PreviousPosition():

    # Initialize the class with some instance variables
    def __init__(self, inID, inSymbol, inEntryPrice, inEntryAmount, inExitPrice, date='-', inExitDate='-', dbID=''):
        self.coin_id = inID
        self.symbol = inSymbol
        self.entry_price = inEntryPrice
        self.entry_amount = inEntryAmount
        self.date = date
        self.exit_price = inExitPrice
        self.exit_date = inExitDate
        self.dbID = dbID

        # Calculate the sold value, profit or loss, and profit or loss percentage
        self.value_sold = self.get_value_sold()
        self.pl = self.get_PL()
        self.pl_percent = self.get_PL_Percent()

    # Calculate the value sold
    def get_value_sold(self):
        sold_val = round(((self.entry_amount / self.entry_price) * self.exit_price),2)
        return sold_val

    # Calculate the profit or loss
    def get_PL(self):
        difference = round(self.value_sold - self.entry_amount,2)
        return difference

    # Calculate the profit or loss percentage
    def get_PL_Percent(self):
        percent_change = round((((self.pl)/ self.entry_amount) * 100),2)
        return percent_change

    # Define the string representation of the class
    def __str__(self):
        return f'{self.symbol}: | {self.entry_price} | {self.entry_amount} | {self.current_price} | {self.current_value} | {self.pl} | {self.pl_percent} | {self.date}'



class PreviousPositions():
    # Initialize an empty list to store previous positions and set initial money invested to 0
    def __init__(self):
        self.previous_positions = []
        self.money_in = 0

    # Add a new previous position to the list, and increment the total amount of money invested
    def add(self, inID, inSymbol, inEntryPrice, inEntryAmount, inExitPrice, inExitDate='-', date='-', dbID=''):
        start = time.time() # Start a timer to measure performance
        self.money_in += inEntryAmount # Increment Money put into portfolio
        position = PreviousPosition(inID, inSymbol, inEntryPrice, inEntryAmount, inExitPrice, date, inExitDate, dbID) # Create a new previous position object
        self.previous_positions.append(position) # Add the new position object to the list of previous positions
        np.append(self.previous_positions, position) # Append the new position object to the numpy array of previous positions
        end = time.time() # End the timer
        print(f'{end-start} seconds to add holding.') # Print the time it took to add the new position object


    # Print out all previous positions
    def display(self):
        positions = np.asarray(self.positions) # Convert the list of previous positions to a numpy array
        for position in positions: # Iterate through each previous position object in the array
            print(position) # Print out the details of the previous position


    # Calculate the total value of all previous positions combined
    def get_cumulative_value(self):
        try:
            # Initialize the cumulative value variable to 0
            cumulative_value = 0 
            # Convert the list of previous positions to a numpy array
            positions = np.asarray(self.previous_positions) 
             # Iterate through each previous position object in the array
            for position in positions:
                # Add the value sold for each previous position to the cumulative value
                cumulative_value += position.value_sold 
                # Round and return the cumulative value
            return round(cumulative_value,2) 
        # Handle the case where the money invested is 0
        except ZeroDivisionError: 
            return 0


    # Calculate the total profit or loss of all previous positions combined
    def get_cumulative_pl(self):
        try:
            # Calculate the profit or loss by subtracting the total money invested from the cumulative value
            pl = round((self.get_cumulative_value() - self.money_in),2) 
            # Return the profit or loss
            return pl 
        # Handle the case where the money invested is 0
        except ZeroDivisionError:
            return 0


    # Calculate the total profit or loss percentage of all previous positions combined
    def get_cumulative_pl_percent(self):
        try:
            # Calculate the profit or loss percentage by dividing the cumulative value by the money invested, subtracting 1, and multiplying by 100
            pl_percent = ((self.get_cumulative_value() / self.money_in - 1)) * 100 
            # Round and return the profit or loss percentage
            return round(pl_percent,2) 
        # Handle the case where the money invested is 0
        except ZeroDivisionError: 
            return 0
