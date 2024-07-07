import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], marker='o', color='b', label='Original Data')
    
    # Linear regression for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], intercept + slope * df['Year'], 'r', label='Best Fit Line (1880-2014)')
    
    # Linear regression from year 2000
    recent_years = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_years['Year'], recent_years['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], intercept_recent + slope_recent * df['Year'], 'g', label='Best Fit Line (2000-2014)')
    
    # Predict sea level rise in 2050
    plt.plot([df['Year'].min(), 2050], [intercept + slope * df['Year'].min(), intercept + slope * 2050], 'r--', label='Predicted Rise (1880-2050)')
    plt.plot([2000, 2050], [intercept_recent + slope_recent * 2000, intercept_recent + slope_recent * 2050], 'g--', label='Predicted Rise (2000-2050)')
    
    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save and return the plot
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Uncomment the following line to test the function locally
# draw_plot()
