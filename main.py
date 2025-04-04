import pandas as pd
from visualization_functions import plot_line_chart, plot_bar_chart, plot_pie_chart, plot_scatter, plot_histogram, plot_box_plot

# Load the dataset
df = pd.read_csv("dataset.csv")

# Plot line chart: Sales over Date
plot_line_chart(df, 'Date', 'Sales')

# Plot bar chart: Total Sales by Region
plot_bar_chart(df, 'Region', 'Sales')

# Pie Chart: Sales by Region
plot_pie_chart(df, 'Region', 'Sales')

# Scatter Plot: Sales Trend
plot_scatter(df, 'Date', 'Sales')

# Histogram: Sales Distribution
plot_histogram(df, 'Sales')

# Box Plot: Sales by Region
plot_box_plot(df, 'Region', 'Sales')


