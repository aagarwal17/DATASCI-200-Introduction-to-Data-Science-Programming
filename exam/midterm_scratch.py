def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """

    # Write code here and update return statement with your dictionary
    retweetDict = {} 
    for tweet in tweet_list: # Iterate through tweets
        # If the string is too short or too long, it is not a tweet
        if len(tweet) < 1 or len(tweet) > 280:
            continue
        words = tweet.split() # Split tweet based on white-space/separate words
        # Iterate over each word and their index to be able to look at next word
        for index, word in enumerate(words):
            if word == 'RT' and words[index+1][0] == '@':
                retweeted_username = words[index+1][1:-1] # Get the retweeted username, without @ and :
                # If the string is too short or twoo long, it is not a username
                if len(retweeted_username) < 1 or len(retweeted_username) > 14:
                    continue
                # Make sure username only has alphanumeric characters
                if any(not char.isalnum() for char in retweeted_username):
                    continue
                # Add username to dictionary if doesn't exist (second param in get function) or update count by 1
                retweetDict[retweeted_username] = retweetDict.get(retweeted_username, 0) + 1
    return retweetDict

def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""
    subgrid = ""
    
    # Invalid top, bottom, left, right inputted, then just return empty subgrid
    if top >= bottom or left >= right:
        return subgrid
    
    for row in range(top, bottom):
        for col in range(left, right):
            # Check if each row, col value in subgrid has deposit
            # Any function returns True if current row, col exists in deposits, False otherwise
            cell_with_deposit = any(d[0] == row and d[1] == col for d in deposits)
            
            # If row,col value has a deposit, add X to subgrid. Otherwise, add -
            if cell_with_deposit:
                subgrid += "X"
            else:
                subgrid += "-"
        subgrid += "\n" # Need new line after iterating through current row

    return subgrid

def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""

    # Do not alter the function header.  
    # Just fill in the code so it returns the correct number of tons.
    totalTons = 0
    
    #Iterate through list of deposits
    for deposit in deposits:
        row, col, tons = deposit #Each tuple has 3 values
        
        # If the deposit exists within the subgrid bounds, then we can add the amount to total_tons
        if top <= row < bottom and left <= col < right:
            totalTons += tons
    return totalTons

def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    date_counts = {} # Dictionary to store how many same dates there are
    # O(n) time complexity to iterate through each person in dates_list:
    for person in dates_list:
        # If the birthday is already encountered, update its count/value by 1. Otherwise, set the value to 1
        if person in date_counts:
            date_counts[person] += 1
        else:
            date_counts[person] = 1
    # This problem boils down to n choose 2, where n is the count of same birthdays for a given day, and 2 represents that we want all the pairs
    # Our dictionary stores birthdays with count 1, but when doing the permutation, the calculation still comes to 0
    # n choose 2 is n!/((n-2)! 2!) = (n(n-1)(n-2)!)/((n-2)! * 2!) = n(n-1)/2! = n(n-1)/2, as I use below
    # We then just sum these permutation values to get the pair count needed [overall O(n) time complexity]
    return int(sum([(val)*(val-1)/2 for val in date_counts.values()]))
# I had a question about the wording of this problem but I couldn't ask because I would've run out of time for the exam.
# My understanding of "duplicate the functionality of this algorithm" is that my algorithm needs to produce the same result,
# not that it has to work the same way in O(n) time. That is why I designed my solution this way