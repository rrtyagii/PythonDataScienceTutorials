import numpy as np
import pandas as pandas
from numpy.random import randn

np.random.seed(101)

df = pandas.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
#print(df[['W','Y']])
df['New'] = df['W']+df['Y']
(df.drop('New', axis=1, inplace =True))
df.drop('D', axis=0, inplace=True)
#print(df.loc[['A','C'],['W','X']])

outside =["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside, inside))
hier_index=pandas.MultiIndex.from_tuples(hier_index)

#print(hier_index)

newDF= pandas.DataFrame(randn(6,2),hier_index,['A','B'])
newDF.index.names=['Groupd', 'Num']
#print(newDF.loc['G1'].loc[1]['B'])

print(newDF.xs(3,level='Num'))