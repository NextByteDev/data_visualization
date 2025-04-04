import matplotlib.pyplot as plt
import seaborn as sns

def plot_line_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title(f'Line Chart: {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.show()

def plot_bar_chart(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=df[x_col], y=df[y_col])
    plt.title(f'Bar Chart: {y_col} by {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_scatter_plot(df, x_col, y_col):
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_col], df[y_col])
    plt.title(f'Scatter Plot: {y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()

def plot_histogram(df, column):
    plt.figure(figsize=(10, 6))
    plt.hist(df[column], bins=20, edgecolor='black')
    plt.title(f'Histogram: Distribution of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
