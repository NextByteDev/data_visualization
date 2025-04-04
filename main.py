import pandas as pd
from visualization_functions import plot_line_chart, plot_bar_chart, plot_scatter_plot, plot_histogram

# Load the dataset
df = pd.read_csv('dataset.csv')

# Call the functions to create different visualizations
plot_line_chart(df, 'Date', 'Sales')  # This will plot a line chart using 'Date' and 'Sales' columns
plot_bar_chart(df, 'CategoryColumn', 'ValueColumn')
plot_scatter_plot(df, 'Date', 'Sales')
plot_histogram(df, 'ValueColumn')
