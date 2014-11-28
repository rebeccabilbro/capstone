# Part of the Data Analysis project submission for Team Colonials
# Program that determines the correlation between fatalities during recession periods
#
# Author:   Bala Venkatesan (venkatesan_bala@yahoo.com)
# Created:  Nov 27, 2014
#


##########################################################################
## Imports
##########################################################################

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from numpy import corrcoef, sum, log, arange
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks

##########################################################################
## Constants
##########################################################################
year=['1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995',
      '1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007',
      '2008','2009','2010','2011','2012','2013','2014']

rates_array = []

## Load unemployment data file
def unemployment_data():
    f = pd.read_csv("../data/unemployment_data.csv")
    df = pd.DataFrame(f)
    df_mean = df.mean()[0:]
    df_rate = pd.DataFrame(data=df_mean, columns=['RATE'])
    x = 0
    for idx, val in enumerate(df_rate.values):
        rates_array.append(float(val))

    return df_rate

## Load construction starts data file
def construction_starts():
    construction_file = pd.read_csv("../data/construction_starts.csv")
    df = pd.DataFrame(construction_file)
    return df


def unemployment_construction_correlation():

    rates = unemployment_data()
    starts = construction_starts()
    # calculating Pearson Correlation Coefficient
    print stats.pearsonr(starts["Total"], rates_array)

    # plottng the graph.

    ax = plt.gca()
    ax.set_xlabel('Year', fontsize=14, color='b')
    ax.set_ylabel('Unemployment', fontsize=11, color='b')
    ax.plot(year,rates,color='red')


    ax2 = ax.twinx()
    ax2.set_ylabel('Construction Starts', fontsize=11, color='b')
    ax2.plot(year,starts["Total"],color='blue')
    plt.show()


    plt.scatter(rates_array, starts["Total"], s=25, c='red', alpha=0.5)
    ax3 = plt.gca()
    ax3.set_ylabel('Construction Starts', fontsize=11, color='b')
    ax3.set_xlabel('Unemployment', fontsize=11, color='r')

    ##includes the correlation fit line
    m,b = np.polyfit(rates_array, starts["Total"],1)
    plt.plot(rates_array, starts["Total"], rates_array, np.array(rates_array) * m + b)
    plt.show()


## program to run analysis
def run():
    unemployment_construction_correlation()




if __name__ == '__main__':
    run()