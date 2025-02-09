import matplotlib.pyplot as plt
import seaborn as sns

# Line plot
years = [2010, 2011, 2012, 2013]
sales = [100, 120, 140, 160]
plt.plot(years, sales, label="sales", color="blue", marker="o")
plt.title("sales over years")
plt.xlabel("Years")
plt.ylabel("sales")
plt.legend()
plt.show()

# Bar chart
categories = ["Electronics", "Clothing", "Groceries"]
revenue = [250, 400, 150]
plt.bar(categories, revenue, color="green")
plt.title("Revenue by Category")
plt.xlabel("Categories")
plt.ylabel("Revenue")
plt.show()

# Scatter Plot
hours_studied = [1, 2, 3, 4, 5]
exam_scores = [50, 55, 65, 70, 100]
plt.scatter(hours_studied, exam_scores, color="red")
plt.title("Hours Studied vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")
plt.show()


# Correlation metrics
df = sns.load_dataset("iris")
corr_matrix = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
