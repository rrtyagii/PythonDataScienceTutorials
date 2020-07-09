import matplotlib as mat
import matplotlib.pyplot as pplt
import numpy as np
import pandas as pandas
## MatplotLib Part 1



#%matplotlib inline

x=np.linspace(0,5,11)
y=x**2
x
y

#Functional way to plot 
pplt.plot(x,y)
pplt.xlabel('X label')
pplt.ylabel('Y label')
pplt.title("Title")

pplt.subplot(1,2,1)
pplt.plot(x,y,'r')

pplt.subplot(1,2,2)
pplt.plot(y,x,'b')

#Object Oriented Way to plot

fig = pplt.figure()

#add_axes takes a list of 4 vlaues i.e left, bottom, width, height argument between 0 and 1
axes = fig.add_axes([0.1,0.1,0.8,0.8]) 
axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Title')

# axes1= fig.add_axes( [0.1,0.1,0.8,0.8] )
# axes2 = fig.add_axes( [0.2,0.5,0.4,0.3] )
print()

#matplotlib part2

# tuple unpacking
fig, axes3 = pplt.subplots(nrows =3, ncols=3)
pplt.tight_layout()



