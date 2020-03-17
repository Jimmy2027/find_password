import pandas as pd


while(True):
    possibilities = pd.read_csv('possibilities.csv')
    username = list(possibilities.loc[possibilities['worked'] == -1]['username'].values)[0]
    password = list(possibilities.loc[possibilities['worked'] == -1]['password'].values)[0]
    print('Try: \n Username: {}      Password: {}'.format(username, password))
    worked = input('Did it work? y/n')
    if worked == 'n':
        possibilities.replace({'username': username, 'password': password}, 0)
        possibilities.loc[(possibilities['username'] == username) & (possibilities['password'] == password), 'worked'] = 0
        possibilities.to_csv('possibilities.csv',index= False)
    elif worked == 'y':
        possibilities.loc[(possibilities['username'] == username) & (possibilities['password'] == password), 'worked'] = 1
        possibilities.to_csv('possibilities.csv')
        break
    else:
        print('wrong input')
        break