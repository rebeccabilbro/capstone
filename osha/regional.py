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
from numpy import corrcoef, sum, log, arange
from numpy.random import rand
from pylab import pcolor, show, colorbar, xticks, yticks

##########################################################################
## Constants
##########################################################################
year=['1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995',
      '1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007',
      '2008','2009','2010','2011','2012','2013','2014']


incidents = "../data/incidents_year_state.csv"
csvfile = open(incidents)

ao_list = []
fatality_list = []
for each_line in csvfile:
    list_row = each_line.split(',')
    if list_row[0] == 'report_id':
        continue
    ao_list.append(list_row[0])
    fatality_list.append(list_row[1])
csvfile.close( )

state_dict = {}
ao_dict = {}
for ao in ao_list:
  if ao in ao_dict:
      ao_dict[ao] = ao_dict[ao] + 1
  else:
      ao_dict[ao] = 1
  if   month == "12" or month == "1" or month == "2":
      season = "Winter"
  elif month == "3" or month == "4" or month == "5":
      season = "Spring"
  elif month == "6" or month == "7" or month == "8":
      season = "Summer"
  else:
      season = "Fall"
  if season in season_dict:
      season_dict[season] = season_dict[season] + 1
  else:
      season_dict[season] = 1

month_pct_dict = {}
season_pct_dict = {}
number_of_month_codes = len( month_list )
for month in month_dict:
    month_pct_dict[month] = float( month_dict[month] ) / number_of_month_codes * 100
for season in season_dict:
    season_pct_dict[season] = float( season_dict[season] ) / number_of_month_codes * 100
