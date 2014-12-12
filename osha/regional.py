# Team Colonials Data Analysis
# Tests the hypothesis that the fatality/catastrophe plateau is
# masking significant increases in certain parts of the country
# as incidents drop off in other places.
#
# Author:   Rebecca Bilbro (bilbro@gmail.com)
# Created:  Dec 4, 2014
#


##########################################################################
## Imports
##########################################################################

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from sklearn.linear_model import LinearRegression


##########################################################################
## Visualizations
##########################################################################
statedata = pd.read_csv("../data/incidents_state_totals.csv", usecols=range(2), index_col='state')

def state_view():
    statedata.plot(kind='bar', stacked=False, figsize=(16, 4))
    plt.title("Frequency of fatalities and catastrophic events by state")
    plt.xlabel("United States")
    plt.ylabel("Frequency")
    plt.show()

def no_outliers():
    fifty = statedata.drop(statedata.index[[4,41]])
    fifty.plot(kind='bar', stacked=False, figsize=(16, 4))
    plt.title("Frequency of fatalities and catastrophic events by state (except CA and SD)")
    plt.xlabel("United States")
    plt.ylabel("Frequency")
    plt.show()

def change_over_time():
    statehistory = pd.read_csv("../data/incidents_state_totals.csv", index_col='state')
    statehistory.drop('totals', axis=1, inplace=True)
    statehistory.drop('totals_to_1990', axis=1, inplace=True)
    statehistory.drop('totals_since_2010', axis=1, inplace=True)
    statehistory = statehistory.drop(statedata.index[[4,41]])
    statehistory.plot(kind='bar', stacked=True, figsize=(16, 8))
    plt.title("State change in fatal and catastrophic events over time")
    plt.xlabel("United States")
    plt.ylabel("Frequency")
    plt.show()

##########################################################################
## Computations
##########################################################################
statetotals = pd.read_csv("../data/incidents_state_totals.csv")
df = pd.DataFrame(statetotals, columns=['state', 'totals_to_1995' , 'totals_to_2000', 'totals_to_2005', 'totals_to_2010'])

def state_totals():
    change = []

    for index, row in df.iterrows():
        n = ((row['totals_to_1995']-row['totals_to_2005'])+ (row['totals_to_2000']-row['totals_to_2010']))/2
        change.append((n, row['state']))
    rank = sorted(change, key=lambda x: x[0])

def coeff_anal():
    #Alabama, Georgia, South Carolina, Virginia
    SE = [(df.loc[0, 'totals_to_1995'] + df.loc[10, 'totals_to_1995'] + df.loc[40, 'totals_to_1995']+ df.loc[46, 'totals_to_1995']),
          (df.loc[0, 'totals_to_2000'] + df.loc[10, 'totals_to_2000'] + df.loc[40, 'totals_to_2000']+ df.loc[46, 'totals_to_2000']),
          (df.loc[0, 'totals_to_2005'] + df.loc[10, 'totals_to_2005'] + df.loc[40, 'totals_to_2005']+ df.loc[46, 'totals_to_2005']),
          (df.loc[0, 'totals_to_2010'] + df.loc[10, 'totals_to_2010'] + df.loc[40, 'totals_to_2010']+ df.loc[46, 'totals_to_2010'])]

    #Connecticut, Massachusetts, New Hampshire, New York
    NE = [(df.loc[6, 'totals_to_1995'] + df.loc[21, 'totals_to_1995'] + df.loc[29, 'totals_to_1995'] + df.loc[31, 'totals_to_1995']),
          (df.loc[6, 'totals_to_2000'] + df.loc[21, 'totals_to_2000'] + df.loc[29, 'totals_to_2000'] + df.loc[31, 'totals_to_2000']),
          (df.loc[6, 'totals_to_2005'] + df.loc[21, 'totals_to_2005'] + df.loc[29, 'totals_to_2005'] + df.loc[31, 'totals_to_2005']),
          (df.loc[6, 'totals_to_2010'] + df.loc[21, 'totals_to_2010'] + df.loc[29, 'totals_to_2010'] + df.loc[31, 'totals_to_2010'])]

    print stats.pearsonr(SE, NE)

def run():
    state_view()
    no_outliers()
    change_over_time()
    state_totals()
    coeff_anal()
    
if __name__ == '__main__':
    run()
