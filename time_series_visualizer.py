import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean the data
df_clean = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # Copy and reset index for plotting
    df_plot = df_clean.copy()
    df_plot.reset_index(inplace=True)
    
    # Convert date to datetime format
    df_plot['date'] = pd.to_datetime(df_plot['date'])
    
    # Extract month and year for easier plotting
    df_plot['year'] = df_plot['date'].dt.year
    df_plot['month'] = df_plot['date'].dt.month_name()
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(14, 6))
    
    # Plot the line chart
    ax.plot(df_plot['date'], df_plot['value'], color='r', linewidth=1)
    
    # Set labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save and return the plot
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and reset index for plotting
    df_plot = df_clean.copy()
    df_plot.reset_index(inplace=True)
    
    # Convert date to datetime format
    df_plot['date'] = pd.to_datetime(df_plot['date'])
    
    # Extract year and month
    df_plot['year'] = df_plot['date'].dt.year
    df_plot['month'] = df_plot['date'].dt.month_name()
    
    # Group by year and month to calculate average page views
    df_avg = df_plot.groupby(['year', 'month'])['value'].mean().reset_index()
    
    # Pivot table for plotting
    df_pivot = df_avg.pivot(index='year', columns='month', values='value')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot.reindex(columns=month_order)
    
    # Set up the figure and plot
    fig, ax = plt.subplots(figsize=(14, 10))
    df_pivot.plot(kind='bar', ax=ax)
    
    # Set labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Page Views per Month (2016-2019)')
    ax.legend(title='Months', labels=month_order)
    
    # Save and return the plot
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df_clean.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    
    # Order months correctly
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box = df_box.sort_values(by='date')
    
    # Set up the figure with two subplots
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))
    
    # Year-wise box plot
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    
    # Month-wise box plot
    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=ax[1])
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    
    # Save and return the plot
    fig.savefig('box_plot.png')
    return fig
