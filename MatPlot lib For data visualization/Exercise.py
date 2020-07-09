import numpy as np
import matplotlib.pyplot as plt
plt.show()

x = np.arange(0,100)
y=x*2
z=x**2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color='blue', lw=3, ls='--')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

ax1= fig.add_axes( [0,0,1,1] )
ax2= fig.add_axes( [0.2,0.5,0.2,0.2] )

ax1.plot(x,y,color='blue', lw=2, ls='--')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
#ax.set_title('title')

ax2.plot(x,y,color='blue', lw=2, ls='-.')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
#ax.set_title('title')