import pylab as pl
import numpy as np

#Specify Datafile
datafile = 'C:\Users\Dr Al-Otaiby\Documents\dataproject\osha_data.csv'

#Open CSV File
csvfile = open(datafile)

#Initialize List
sic_list = []
fatality_list = []

#Read CSV Records and compile the lists
for each_line in csvfile:
    list_row = each_line.split(',')
    if list_row[0] == 'SIC':
        continue
    sic_list.append( list_row[0] )
    fatality_list.append( list_row[1] )

#Close CSV File
csvfile.close( )

#Initialize Dictionary
sic_dict = {}

#Count the number of times each SIC code in list 
for sic in sic_list:
  if sic in sic_dict:
      sic_dict[sic] = sic_dict[sic] + 1
  else:
      sic_dict[sic] = 1

#Work Out Percentages
sic_pct_dict = {}
number_of_sic_codes = len( sic_list )
for sic in sic_dict:
    sic_pct_dict[sic] = float( sic_dict[sic] ) / number_of_sic_codes * 100

#Print Out Top 25 SIC Codes Used
loop = 0
chart_dict = {}
for sic in sorted(sic_pct_dict, key=sic_pct_dict.get, reverse=True):
    chart_dict[sic] = sic_pct_dict[sic]
    print sic, sic_dict[sic], sic_pct_dict[sic] 
    loop = loop + 1
    if loop >= 25:
        break

#Graph The Top 25 SIC codes used
X = np.arange( len( chart_dict ) )
pl.bar(X, chart_dict.values(), align='center', width=0.5)
pl.xticks(X, chart_dict.keys())
ymax = max( chart_dict.values() ) + 1
pl.ylim(0, ymax)
pl.show()

print '*** End of Program ***'
