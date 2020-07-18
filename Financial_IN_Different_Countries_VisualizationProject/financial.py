import pandas as pandas
import matplotlib.pyplot as pyplot
import matplotlib as mat
import seaborn as sns

data=pandas.read_excel("C:\\IIT\\Python Data Science\\Financial_IN_Different_Countries_VisualizationProject\\global_crisis_data_20160923(2).xlsx", sheet_name="Sheet1")
data.drop( ["exch_usd_alt1","exch_usd_alt2","<", "exch_usd_alt3","Domestic_Debt_ Notes/Sources", "Defaults_External_Notes","conversion_notes", "Banking_Crisis_Notes"], axis=1, inplace=True )

countries,years,cc3  = (data.Country.unique()[1:]),  (data.Year.unique()[1:]), (data.CC3.unique()[1:])

print(data.columns)
print()
# pyplot.figure(figsize=(15,5))
# ax= sns.scatterplot(x=data['Country'], y=data['Year'], data=data['Independence'])

# pyplot.xticks(
#     rotation=90,
#     horizontalalignment='right',
#     fontweight='light',
#     fontsize='x-large'

# )

pyplot.show()