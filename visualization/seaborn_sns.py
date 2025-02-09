import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Heatmap
data = np.random.rand(5,5)
sns.heatmap(data, annot=True, cmap="coolwarm")
plt.title("heatmap")
plt.show()

# Pair plot
df = pd.DataFrame({
    "A": np.random.rand(50),
    "B": np.random.rand(50),
    "C": np.random.rand(50),
    "D": np.random.randint(0, 3, size=50)
})

sns.pairplot(df, hue="D", palette="viridis")
plt.title("Pairplot")
plt.show()
