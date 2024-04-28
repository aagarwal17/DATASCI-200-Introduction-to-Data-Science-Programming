"""bidder_agarwal.py: module providing a Bidder class to represent a bidder in an 
online second-price ad auction"""

import random
import numpy as np

class Bidder:
    '''Class to represent a bidder in an online second-price ad auction.
    There is a set of Bidders. Each Bidder begins with a balance of 0 dollars.
    The objective is to finish the game with as high a balance as possible.
    At some points during the game, the Bidder's balance may become negative.
    If you  Bidder's balance goes below -1000 dollars then your Bidder will 
    be disqualified from the Auction and further bidding.'''

    def __init__(self, num_users, num_rounds):
        '''Setting initial balance to 0, number of users, number of rounds, and round counter'''
        self.__balance = 0
        self.num_users = num_users
        self.num_rounds = num_rounds

        self.round_counter = 0

        self.counts_users_clicked = {}
        self.user_ids_called = []

    def __repr__(self):
        '''Return Bidder object with balance'''
        return f'Bidder(balance={self.__balance})'

    def __str__(self):
        '''Return Bidder object with balance'''
        return f'Bidder(balance={self.__balance})'

    def bid(self, user_id):
        '''Returns a non-negative bid amount, rounded to 3 decimal places'''

        # Store the current user id
        self.user_ids_called.append(user_id)

        # Decrement num_rounds and increment round_counter:
        self.num_rounds -= 1
        self.round_counter += 1

        # By storing the number of times each user has been clicked, we can decide how much to bid:

        # If we haven't had at least as many rounds as there are users,
        # just bid a random number between 0 and 1:
        if self.round_counter < self.num_users:
            return round(np.random.random(), 3)
        # If we have had at least as many rounds as there are users,
        # we can start using the user_id to decide how much to bid.
        # If the user_id is not in the dictionary, it hasn't clicked yet.
        elif user_id not in self.counts_users_clicked:
            return round(np.random.random(), 3)
        # If the ratio of user click wins to rounds is less than 10%, bid random num between 0 and 1
        elif 0 < self.counts_users_clicked[user_id]/self.round_counter < .10:
            return round(np.random.random(), 3)
        # If the ratio of user click wins to rounds is less than 50%, bid random num between 1 and 2
        elif .10 <= self.counts_users_clicked[user_id]/self.round_counter < .50:
            return round(random.uniform(1,2), 3)
        # If the ratio of user click wins to rounds is less than 100%, bid random num between 2 & 10
        elif .50 <= self.counts_users_clicked[user_id]/self.round_counter < 1:
            return round(random.uniform(2,10), 3)
        # If the ratio of user click wins to rounds is 100%, bid random num between 10 and 100
        else:
            return round(random.uniform(10,100), 3)

    def notify(self, auction_winner, price, clicked = None):
        '''Updates bidder attributes based on results from an auction round.
        This is used to send information about what happened in a round back to the Bidder. 
        Here, auction_winner is a boolean to represent whether the given Bidder won 
        the auction (True) or not (False). clicked is the amount of the second bid, 
        which the winner pays. If the given Bidder won the auction, clicked will 
        contain a boolean value to represent whether the user clicked on the ad. 
        If the given Bidder did not win the auction, clicked will always contain None.'''

        # If the bidder won the auction and user clicked, increment user's click count by 1:
        if auction_winner is True and clicked is True:
            self.__balance -= price
            if self.user_ids_called[-1] not in self.counts_users_clicked:
                self.counts_users_clicked[self.user_ids_called[-1]] = 1
            else:
                self.counts_users_clicked[self.user_ids_called[-1]] += 1
        # If the bidder won the auction and user didn't click, don't increment user's click count:
        elif auction_winner is True and clicked is None:
            if self.user_ids_called[-1] not in self.counts_users_clicked:
                self.counts_users_clicked[self.user_ids_called[-1]] = 0
        # If the bidder lost the auction, don't increment user's click count:
        else:
            pass
