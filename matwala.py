from cProfile import label

# For normal functions

import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0,10)
y=2*x
# plt.plot(x,y,marker='o',label='y=2x')
# plt.title('Plot of y=2x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.grid()
# plt.xlim(0,50)
# plt.ylim(0,50)
# plt.show()

#  For OOP(object oriented programming) or complex functions

a=np.linspace(0,10,11)
b=a**4
fig=plt.figure()
axes=fig.add_axes([0,0,1,1])
axes.plot(a,b)
axes.set_title('Plot of b=a**4')
axes.set_xlabel('a')
axes.set_ylabel('b')


# Small axes

axes2=fig.add_axes([0.2, 0.5, 0.5, 0.5])
axes2.plot(x,y)
axes2.plot(x,y)
axes2.set_title('Plot of y=2x')
axes2.set_xlabel('a')
axes2.set_ylabel('b')


plt.show()
