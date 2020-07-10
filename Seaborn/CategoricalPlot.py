import seaborn as sns
import numpy as numpy

tips = sns.load_dataset('tips')
tips.head()

sns.barplot(x='sex', y='tip', data= tips)
sns.barplot(x='sex', y='tip', data= tips, estimator = numpy.std)
# estimator: callable that maps vector -> scalar, optional
# Statistical function to estimate within each categorical bin

sns.countplot(x='sex', data=tips)
sns.boxplot(x='day', y='total_bill', data=tips)
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')

sns.violinplot(x='day', y='total_bill', data=tips, split = True)

sns.stripplot(x='day', y='total_bill', data=tips, jitter=True)