import pandas as pd
import matplotlib.pyplot as plt


# bar plot for daily number of coronavirus cases

df = pd.read_csv('us-daily.csv',parse_dates=['date'],index_col=['date'])
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.bar(df.index.values,
        df['positiveIncrease'],
        color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Daywise Increase in cases",
       title="Daily Total Corona Cases")

# Rotate tick marks on x-axis
plt.setp(ax.get_xticklabels(), rotation=45)
plt.savefig('daywise_cases_bar_plot.png')
plt.show()