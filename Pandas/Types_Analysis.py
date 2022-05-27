import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")

ax = sns.swarmplot(x=tips["total_bill"])

plt.show()