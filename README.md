# 📊 Simple Data Visualization Tool

A beginner-friendly Python project that reads data from a CSV file and visualizes it using various types of charts. It helps users better understand data by offering intuitive graphical insights.

## 📁 Dataset

The project uses a sample dataset called `dataset.csv` with the following columns:

- `Date` (e.g., "2024-01-01")  
- `Sales` (e.g., 1500)  
- `Region` (e.g., "North", "South", etc.)

> 🗂️ You can replace the dataset with your own, as long as it follows the same column structure.

## 📊 Visualizations

The tool currently supports the following visualizations:

### ✅ Line Chart: Sales Over Time
Displays trends in sales data across dates.

### ✅ Bar Chart: Total Sales by Region
Sums and compares total sales in each region.

### ✅ Pie Chart: Sales Distribution by Region
Shows how sales are split among regions.

### ✅ Box Plot: Sales by Region
Displays the distribution, median, and outliers of sales for each region.

## 🔧 How It Works

1. `main.py` loads the dataset and calls functions to generate each plot.
2. Each function is defined in `visualization_functions.py` and uses **Matplotlib** and **Pandas**.
3. The charts open in a pop-up window using `plt.show()`.

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/data_visualization.git
cd data_visualization
```

### 2. Ensure Python is Installed (Recommended: Python 3.7+)

### 3. Install Required Libraries

```bash
pip install pandas matplotlib
```

### 4. Run the Script

```bash
python main.py
```
Each chart will be displayed one after the other.

# 🧠 What You’ll Learn
- How to load and manipulate data with Pandas

- How to visualize data using Matplotlib

- How to split logic into multiple clean Python files

# 🚀 Future Improvements
- Add options for interactive plots (e.g., using Plotly or Seaborn)

- Allow user to choose which plot to generate from command-line

- Support additional chart types like scatter plots or histograms

- Improve error handling and input validation


Feel free to fork this project, play with your own datasets, and build cool visualizations! 🎨📈
