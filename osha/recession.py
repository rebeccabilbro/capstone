
import pandas as pd
import matplotlib.pyplot as plt

year=['1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995',
      '1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007',
      '2008','2009','2010','2011','2012','2013','2014']

data_array = []


def unemployment_data():
    f = pd.read_csv("../data/unemployment_data.csv")
    df = pd.DataFrame(f)
    df_mean = df.mean()[0:]
    df_rate = pd.DataFrame(data=df_mean, columns=['RATE'])

    return df_rate

def construction_starts():
    construction_file = pd.read_csv("../data/construction_starts.csv")
    df = pd.DataFrame(construction_file)
    return df

def run():
    rates = unemployment_data()
    starts = construction_starts()
    ax = plt.gca()
    ax.set_xlabel('Year', fontsize=14, color='b')
    ax.set_ylabel('Unemployment', fontsize=11, color='b')
    ax.plot(year,rates,color='red')
    ax2 = ax.twinx()
    ax2.set_ylabel('Construction Starts', fontsize=11, color='b')
    ax2.plot(year,starts["Total"],color='blue')
    plt.show()

if __name__ == '__main__':
    run()