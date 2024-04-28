"""auction_agarwal.py: module providing a User and Auction class to represent an online 
second-price ad auction and its users"""

import numpy as np

class User:
    '''Class to represent a user with a secret probability of clicking an ad.
    There are num_users Users, numbered from 0 to num_users - 1. The number
    corresponding to a user will be called its user_id. Each user has a secret
    probability of clicking, whenever it is shown an ad. The probability is the
    same, no matter which Bidder gets to show the ad, and the probability never
    changes. The events of clicking on each ad are mutually independent. When a
    user is created, the secret probability is drawn from a uniform distribution
    from 0 to 1.'''

    def __init__(self):
        '''Generating a probability between 0 and 1 from a uniform distribution'''
        self.__probability = np.random.uniform(0, 1)

    def __repr__(self):
        '''User object with secret probability'''
        return f'User(click probability={self.__probability})'

    def __str__(self):
        '''User object with a secret likelihood of clicking on an ad'''
        return f'User(click probability={self.__probability})'

    def show_ad(self):
        '''Returns True to represent the user clicking on an ad or False otherwise'''
        return np.random.choice([True, False], p=[self.__probability, 1 - self.__probability])

class Auction:
    '''Class to represent an online second-price ad auction:
    The Auction is a game, involving a set of Bidders on one side, and a set of
    Users on the other. Each round represents an event in which a User navigates
    to a website with a space for an ad. When this happens, the Bidders will place
    bids, and the winner gets to show their ad to the User. The User may click on
    the ad, or not click, and the winning Bidder gets to observe the User's
    behavior. This is a second price sealed-bid Auction.'''

    def __init__(self, users, bidders):
        '''Initializing users, bidders, and dictionary to store balances for each bidder 
        in the auction'''
        self.users = users
        self.bidders = bidders
        self.balances = {bidder: 0 for bidder in list(range(len(bidders)))}

    def __repr__(self):
        '''Return auction object with users and qualified bidders'''
        return f'Auction(users={self.users}, bidders={self.bidders})'

    def __str__(self):
        '''Return auction object with users and qualified bidders'''
        return f'Auction(users={self.users}, bidders={self.bidders})'

    def execute_round(self):
        '''Executes a single round of an auction, completing the following steps:
            - random user selection
            - bids from every qualified bidder in the auction
            - selection of winning bidder based on maximum bid
            - selection of actual price (second-highest bid)
            - showing ad to user and finding out whether or not they click
            - notifying winning bidder of price and user outcome and updating balance
            - notifying losing bidders of price'''
        if len(self.bidders) > 1:
            # Choose user at random
            random_user_id = np.random.randint(0, len(self.users))
            random_user = self.users[random_user_id]

            # Create the bidders list (list of qualified bidders):
            list_of_bids = [bidder.bid(random_user_id) for bidder in self.bidders]

            # Pick winning bid (store its index),
            # and if there is a tie, choose one of the highest values at random:
            the_winner = np.random.choice([index_of_bid for index_of_bid, bid in
                                            enumerate(list_of_bids) if bid == max(list_of_bids)])

            # Second-highest bid should be selected for actual price:
            actual_price = sorted(list_of_bids)[-2]

            # Show ad to user and find out whether or not they click:
            clicked = False
            if random_user.show_ad():
                clicked = True

            # Notify winning bidder of price and user outcome as well as losing bidders of price:
            for bidder in self.bidders:
                if bidder == self.bidders[the_winner]:
                    # Update the balance:
                    if clicked:
                        self.balances[the_winner] += 1
                    # Update balance of winner by subtracting the second highest bid (actual_price)
                    # If the balance goes below -1000, the bidder is disqualified from the auction:
                    self.balances[the_winner] = round(self.balances[the_winner] - actual_price, 3)
                    if self.balances[the_winner] < -1000:
                        self.bidders.pop(the_winner)
                    bidder.notify(True, actual_price, clicked)
                else:
                    bidder.notify(False, actual_price, None)
