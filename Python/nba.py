import pandas as pd
import numpy as np
import scipy.stats as stats
import re   #regular expression library
import matplotlib.pyplot as plt

def string_to_float(string):   #convert string to float
        a = string.split(',')
        valor=''
        i=0
        while len(a)>i:
            valor+=a[i]
            i+=1
        return float(valor)


nba_df=pd.read_csv("nba.csv")
    
cities=pd.read_html("cities.html")[1]
cities=cities.iloc[:-1,[0,3,5,6,7,8]]
    
cities = cities.replace('—', np.nan)
cities = cities.replace('\[.*\]','', regex=True)
cities = cities.replace(r'^\s*$', np.nan, regex=True)
cities.rename(columns={'Population (2016 est.)[8]':'Population'},inplace=True)
    
cities['Population'] = cities['Population'].apply(lambda x : string_to_float(x))
cities.dropna(subset=['NBA'], inplace=True)
cities.set_index('NBA', inplace=True)
    
pop_lista=[]
for i in range(28):
    pop_lista.append(float(cities.iloc[i]['Population']))
        
    
nba_df['team'] = nba_df['team'].str.replace('(\*)','',regex=True)
nba_df['team'] = nba_df['team'].str.replace('\s\(.*\)','',regex=True)
nba_df.set_index('team', inplace=True)
teams = ['New York Knicks','Brooklyn Nets','Los Angeles Lakers','Los Angeles Clippers','Golden State Warriors',
            'Chicago Bulls','Dallas Mavericks','Washington Wizards','Philadelphia 76ers','Boston Celtics',
             'Minnesota Timberwolves','Denver Nuggets','Miami Heat','Phoenix Suns','Detroit Pistons','Toronto Raptors',
            'Houston Rockets','Atlanta Hawks','Cleveland Cavaliers','Charlotte Hornets','Indiana Pacers','Milwaukee Bucks',
            'New Orleans Pelicans','Orlando Magic','Portland Trail Blazers','Utah Jazz','San Antonio Spurs',
             'Sacramento Kings','Oklahoma City Thunder','Memphis Grizzlies']
    
win_loss=[]
for i in teams:
    team_2018 = nba_df.loc[i].iloc[0]
    win_loss.append(float(team_2018.loc['W'])/(float(team_2018.loc['W'])+float(team_2018.loc['L'])))
    
media1 = (win_loss[0]+win_loss[1])/2
media2 = (win_loss[2]+win_loss[3])/2
win_loss_lista = [media1,media2]+win_loss[4:]
    
population_by_region = pop_lista # pass in metropolitan area population from cities
win_loss_by_region = win_loss_lista # pass in win/loss ratio from nba_df in the same order as cities["Metropolitan area"]
        
corr, p_val = stats.pearsonr(population_by_region, win_loss_by_region)

plt.plot(population_by_region, win_loss_by_region, 'b')
plt.ylabel('win/loss')
plt.xlabel('population/city')
plt.title('Correlation win/loss and population')
plt.text(1.6e7,0.7,r'Corr = -0.0985',c='r')
plt.show()