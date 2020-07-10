import seaborn as seaborn
import pandas as pandas
import matplotlib.pyplot as plt
plt.show()

data= pandas.read_csv('Pandas\\Salaries.csv')
data.head() 
tips= seaborn.load_dataset('tips')
#tips.head()
seaborn.distplot(tips['total_bill'], kde= False,bins=30)

seaborn.jointplot(x='tip', y='total_bill', data=tips, kind='reg')
seaborn.pairplot(tips, hue='sex', palette='coolwarm')




