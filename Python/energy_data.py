#packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


#in this function I did: cleaning, replacing, slicing, merging and so on for three differents data sets
# The funtion returns the net data set for the top 15 countries on journal contributions in Energy area.
def net_data():
    x = pd.ExcelFile('Energy Indicators.xls')
    energy = x.parse(skiprows=17,skip_footer=(38))  #skipping the header and the footer
    energy = energy[[energy.columns[1],energy.columns[3],energy.columns[4],energy.columns[5]]]
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', 
    '% Renewable']] =  energy[['Energy Supply','Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = 1000000*energy['Energy Supply']
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong',
                                                   'United Kingdom of Great Britain and Northern Ireland':'United Kingdom',
                                                   'Republic of Korea':'South Korea',
                                                   'United States of America':'United States',
                                                   'Iran (Islamic Republic of)':'Iran'})
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")

    GDP = pd.read_csv('world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({'Korea, Rep.':'South Korea','Iran, Islamic Rep.':'Iran',
        'Hong Kong SAR, China':'Hong Kong'})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP.columns = ['Country','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']

    ScimEn = pd.read_excel(io='scimago.xlsx')
    ScimEn = ScimEn[:15]
    df = pd.merge(ScimEn,energy,how='inner',left_on='Country',right_on='Country')
    new_df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    new_df = new_df.set_index('Country')
    
    return new_df


# this plot helps to understand the above DataFrame net_data()
def plot_data():
    df = net_data()
    ax = df.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*df['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(df.index):
        ax.annotate(txt, [df['Rank'][i], df['% Renewable'][i]], ha='center')

    plt.show()

#plt.show()
'''print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")'''


#top15 countries for average GDP (Gross Domestic Product) for 2006 to 2015 in crescent order
def avg_gdp():
    df = net_data()
    avgGDP = df[['2006','2007','2008','2009','2010','2011','2012','2013',
                    '2014','2015']].mean(axis = 1).rename('avgGDP').sort_values(ascending= True)
    return pd.Series(avgGDP)

# return the mean energy suply per capita for the 15 countries
def mean_esc():
    df = net_data()
    return np.nanmean(df['Energy Supply per Capita'])

# here a created a new column named 'Ratio Citations' and the idea was to return the maximum value for this columns 
#and the country that has the highest ratio 
def ratio_citations():
    df = net_data()
    df['Ratio Citations'] = df['Self-citations']/df['Citations']
    return ('China',np.max(df['Ratio Citations']))


#returns the correlation between the number of citable documents per capita and
#the energy supply per capita
def corr_energy():
    df = net_data()
    df['Population'] = (df['Energy Supply'].dropna())/(df['Energy Supply per Capita'].dropna())
    df['Citable Documents per Capita'] = (df['Citable documents'].dropna())/(df['Population'].dropna())
    a = df['Citable Documents per Capita'].dropna()
    b = df['Energy Supply per Capita'].dropna()
    corr, p_value = pearsonr(a, b)
    return corr

#here you can visualize a scatter plot for the function corr_energy()
def plot1():    
    df = net_data()
    df['PopEst'] = df['Energy Supply'] / df['Energy Supply per Capita']
    df['Citable docs per Capita'] = df['Citable documents'] / df['PopEst']
    df.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])
    plt.show()


# new column with a 1 if the country's % Renewable value is at or above 
#the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median
def series_renew():
    df = net_data()
    median = np.nanmedian(df['% Renewable'].astype(np.float))
    df['HighRenew'] = df['% Renewable'].apply(lambda x : 1 if x>=median else 0)
    series = df['HighRenew'].copy()
    series.index = df.index
    return series


#returns a new DataFrame that displays the sample size (numbers of countries in each Continent), 
#and the sum, mean, and std deviation for the estimated population of each country
def answer_eleven():
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    df = net_data()
    df['size'] = None
    df['Pop'] = df.iloc[:,7]/df.iloc[:,8]
    df['Continent'] = None
    for i in range(len(df)):
        df.iloc[i,20] = 1
        df.iloc[i,22]= ContinentDict[df.index[i]]
    ans = df.set_index('Continent').groupby(level=0)['Pop'].agg({'size': np.size, 'sum': np.sum, 
                                                                 'mean': np.mean,'std': np.std})
    ans = ans[['size', 'sum', 'mean', 'std']]
    return ans