import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime, timedelta


# bar plot for daily number of coronavirus cases
plt.style.use('seaborn')

#data = pd.read_csv('us-daily.csv')
data = pd.read_csv('us-daily.csv',parse_dates=['date'])
#data['date'] = pd.to_datetime(data['date'])
#data.sort_values('date', inplace = True)

#print(data.head())

cases_date = data['date']
cases_count = data['positive']

plt.plot_date(cases_date, cases_count, linestyle = 'solid')
plt.gcf().autofmt_xdate()

plt.title('Cases Over time')
plt.xlabel('Dates')
plt.ylabel('Total Cases')

plt.savefig('total_cases_line_plot.png')
plt.tight_layout()
plt.show()

