import matplotlib.pyplot as plt
import pandas as pd  # Add this line to fix the error

def plot_line_chart(df, x_col, y_col):
    """Plots a line chart from the dataframe."""
    df[x_col] = pd.to_datetime(df[x_col])  # Convert date column if needed
    plt.figure(figsize=(10, 5))
    plt.plot(df[x_col], df[y_col], marker='o')
    plt.title(f'{y_col} over {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_bar_chart(df, category_col, value_col):
    """Plots a bar chart showing the sum of value_col per category_col."""
    grouped = df.groupby(category_col)[value_col].sum().reset_index()
    plt.figure(figsize=(8, 5))
    plt.bar(grouped[category_col], grouped[value_col], color='skyblue')
    plt.title(f'Total {value_col} by {category_col}')
    plt.xlabel(category_col)
    plt.ylabel(f'Total {value_col}')
    plt.tight_layout()
    plt.show()

def plot_pie_chart(df, category_col, value_col):
    """Plots a pie chart showing the percentage of value_col per category_col."""
    grouped = df.groupby(category_col)[value_col].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(grouped, labels=grouped.index, autopct='%1.1f%%', startangle=140)
    plt.title(f'{value_col} Distribution by {category_col}')
    plt.axis('equal')  # Equal aspect ratio makes the pie chart round.
    plt.tight_layout()
    plt.show()

def plot_scatter(df, x_col, y_col):
    """Plots a scatter plot for two columns."""
    df[x_col] = pd.to_datetime(df[x_col])  # Ensure x_col is datetime if needed
    plt.figure(figsize=(10, 5))
    plt.scatter(df[x_col], df[y_col], color='purple', alpha=0.6)
    plt.title(f'{y_col} vs {x_col}')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_histogram(df, col, bins=10):
    """Plots a histogram for a single column."""
    plt.figure(figsize=(8, 5))
    plt.hist(df[col], bins=bins, color='skyblue', edgecolor='black')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_box_plot(df, category_col, value_col):
    """Plots a box plot to show distribution of value_col by category_col."""
    plt.figure(figsize=(8, 5))
    ax = plt.gca()
    df.boxplot(column=value_col, by=category_col, ax=ax, grid=True)
    plt.title(f'{value_col} by {category_col}')
    plt.suptitle('')  # This line removes the default subtitle
    plt.xlabel(category_col)
    plt.ylabel(value_col)
    plt.tight_layout()
    plt.show()


