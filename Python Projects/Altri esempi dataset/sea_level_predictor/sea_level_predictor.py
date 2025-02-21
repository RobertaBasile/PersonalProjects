"""
Sea Level Predictor

This project analyzes a dataset of global average sea level change since 1880
and predicts the sea level change through the year 2050. The dataset contains 
the global average sea level change measured by the CSIRO (Commonwealth Scientific 
and Industrial Research Organisation) and NOAA (National Oceanic and Atmospheric Administration).

The goal is to visualize the sea level change using various plots and to fit 
regression lines that predict future sea level rise.

Data source:
Global Average Absolute Sea Level Change, 1880-2014 from the US Environmental Protection Agency using data from CSIRO, 2015; NOAA, 2015.

Tasks:
1. Import the data from 'epa-sea-level.csv' using Pandas.
2. Create a scatter plot with 'Year' as the x-axis and 'CSIRO Adjusted Sea Level' 
   as the y-axis using Matplotlib.
3. Calculate and plot a line of best fit for the entire dataset, extending the 
   line to predict sea level rise through 2050 using the linregress function 
   from scipy.stats.
4. Calculate and plot a line of best fit using only data from the year 2000 
   to the most recent year in the dataset, extending the line to predict sea 
   level rise through 2050.
5. Label the x-axis as 'Year', the y-axis as 'Sea Level (inches)', and title the 
   plot as 'Rise in Sea Level'.

Development:
Write the code in 'sea_level_predictor.py'. For development, you can use 'main.py' 
to test your code.



"""


import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import the data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = intercept + slope * x_pred
    ax.plot(x_pred, y_pred, color='red', label='Fitted Line 1880-2050')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred_recent = pd.Series(range(2000, 2051))
    y_pred_recent = intercept_recent + slope_recent * x_pred_recent
    ax.plot(x_pred_recent, y_pred_recent, color='green', label='Fitted Line 2000-2050')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot
    plt.savefig('sea_level_plot.png')
    
   # Show plot
    plt.show()
    
    return plt.gca()

# Main function to execute the draw_plot function
if __name__ == "__main__":
    draw_plot()