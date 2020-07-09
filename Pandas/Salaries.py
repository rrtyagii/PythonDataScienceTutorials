import pandas as pd
import numpy as np

data = pd.read_csv('Salaries.csv')
# #newData = data[~data['BasePay'].isin(['Not Provided'])]
# newData = data[~data['BasePay'].str.contains('Not Provided', na=False)]
# print(newData['BasePay'].mean())
# df = data.select_dtypes(object)
# mask = ~df.apply(lambda series: series.str.contains('Not Provided')).any(axis=1)
# no_eco = data[mask]
#print (data['BasePay'].mean())

print(data[data['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
print()
print(data[data['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits'])
print()
print(data[data['TotalPayBenefits']==data["TotalPayBenefits"].max()]['EmployeeName'])
print()
print(data.loc[data['TotalPayBenefits'].idxmax()])
print()
print(data.loc[data['TotalPayBenefits'].idxmin()])
print(data.groupby('Year').mean())
print(data['JobTitle'].nunique())
print()
print(data['JobTitle'].value_counts().head(10))
print(sum(data[data['Year']==2013]['JobTitle'].value_counts() == 1))

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

#print(sum(data['JobTitle'].apply(lambda x: chief_string(x))))

data['title_len'] = data['JobTitle'].apply(len)
print(data[['TotalPayBenefits', 'title_len']].corr())
