incidents.py

import pylab as pl
import numpy as np



#Specify Datafile
datafile = 'C:\Users\lopeaw01\Desktop\Analytics\osha_month.csv'

#Open CSV File
csvfile = open(datafile)

#Initialize List
month_list = []
fatality_list = []

#Read CSV Records and compile the lists
for each_line in csvfile:
    list_row = each_line.split(',')
    if list_row[0] == 'Month':
        continue
    month_list.append( list_row[0] )
    fatality_list.append( list_row[1] )

#Close CSV File
csvfile.close( )

#Initialize Dictionary
month_dict = {}
season_dict = {}

#Count the number of times each month accidents occur 
for month in month_list:
  if month in month_dict:
      month_dict[month] = month_dict[month] + 1
  else:
      month_dict[month] = 1
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
      
#Work Out Percentages
month_pct_dict = {}
season_pct_dict = {}
number_of_month_codes = len( month_list )
for month in month_dict:
    month_pct_dict[month] = float( month_dict[month] ) / number_of_month_codes * 100
for season in season_dict:
    season_pct_dict[season] = float( season_dict[season] ) / number_of_month_codes * 100

#Print Out 
print 'Month Details'
print '-------------'
for month in sorted(month_pct_dict, key=month_pct_dict.get, reverse=True):
    print month, month_dict[month], month_pct_dict[month] 

print ' '
print 'Season Details'
print '--------------'
chart_dict = {}
for season in sorted(season_pct_dict, key=season_pct_dict.get, reverse=True):
    chart_dict[season] = season_pct_dict[season]
    print season, season_dict[season], season_pct_dict[season] 
    
#Graph The Season
X = np.arange( len( chart_dict ) )
pl.bar(X, chart_dict.values(), align='center', width=0.5)
pl.xticks(X, chart_dict.keys())
ymax = max( chart_dict.values() ) + 1
pl.ylim(0, ymax)
pl.show()

print ' '
print '*** End of Program ***'
