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


ao_dict = {}
for ao in ao_list:
  if ao in ao_dict:
      ao_dict[ao] = ao_dict[ao] + 1
  else:
      ao_dict[ao] = 1

fifty = pd.DataFrame(statedata)
fifty = fifty[np.abs(fifty.totals-fifty.totals.mean())<=(3*fifty.totals.std())] 
fifty.plot(kind='bar', stacked=False, figsize=(16, 4))
plt.title("Frequency of fatalities and catastrophic events by state (except CA)")
plt.xlabel("United States")
plt.ylabel("Frequency")
plt.show()

