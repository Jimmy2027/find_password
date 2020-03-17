import pandas as pd
from itertools import product

pw_to_try_df = pd.DataFrame(columns = ['username', 'password'])

"""
Write your guesses for your username and password in following arrays:
"""
possible_usernames = []
possible_passwords = []


for un, pw in product(possible_usernames, possible_passwords):
    temp = pd.DataFrame([[un, pw]], columns=['username', 'password'])
    pw_to_try_df = pw_to_try_df.append(pd.DataFrame([[un, pw]], columns=['username', 'password']))

pw_to_try_df['worked']=-1
pw_to_try_df.to_csv('possibilities.csv')
