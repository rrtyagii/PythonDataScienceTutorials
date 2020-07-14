import pandas as pandas
import matplotlib.pyplot as pyplot
import matplotlib as mat
import seaborn as sns

data=pandas.read_excel("C:\\IIT\\Python Data Science\\FinancialCrisisVisualizationProject\\global_crisis_data_20160923.xlsx", sheet_name="Sheet1")
data.drop( ["exch_usd_alt1","exch_usd_alt2", "exch_usd_alt3","Domestic_Debt_ Notes/Sources", "Defaults_External_Notes","conversion_notes", "Banking_Crisis_Notes"], axis=1, inplace=True )
#print(data.info() )
countries,years,cc3  = (data.Country.unique()[1:]),  (data.Year.unique()[1:]), (data.CC3.unique()[1:])
print(countries)
print(cc3)
