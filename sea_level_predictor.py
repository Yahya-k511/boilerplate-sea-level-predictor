import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df=pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')



    # Create scatter plot
    plt.figure(figsize=(14,6))
    area = np.pi * (20 * np.random.rand(50))**2
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title(('rise insea level')
              
    


    # Create first line of best fit
      res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = range(1880, 2051)
    plt.plot(years, res.intercept + res.slope * years, 'r')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    plt.plot(years_recent, res_recent.intercept + res_recent.slope * years_recent, 'g')


    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    return plt.gca()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
