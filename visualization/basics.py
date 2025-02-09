import matplotlib.pyplot as plt

# Basic line plot
x_values = [1, 2, 3, 4]
y_values = [10, 20, 30, 40]
plt.plot(x_values, y_values)
plt.show()

# Line plot with labels and title
plt.plot([1, 2, 3], [10, 20, 30], label="Trend")
plt.title("Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()
plt.show()

# Bar chart with categories
categories = ["A", "B", "C"]
category_values = [10, 15, 7]
plt.bar(categories, category_values, color="blue")
plt.title("Bar Chart")
plt.show()

# Histogram with green bars
histogram_data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(histogram_data, bins=4, color="green", edgecolor="black")
plt.title("Histogram")
plt.show()

# Scatter plot with red points
x_points = [1, 2, 3, 4, 5]
y_points = [10, 12, 25, 30, 45]
plt.scatter(x_points, y_points, color="red")
plt.title("Scatter")
plt.show()
