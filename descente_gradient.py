import matplotlib.pyplot as plt

import numpy as np

def f(x):
    return(pow(x-4,4)+2)

print
    
def descente(f,x0,tolerence):
    h = 0.00001
    for i in range(1,1000000):
        df = ( f(x0+h)-f(x0) )/h
        if (abs (df) <= tolerence):
            print(df)
            return(x0)
        epsilon = 1/i
        x0 = x0 - epsilon * df
        
x0 = -100
        
sol = descente(f,x0,1)

print(sol)

x = np.arange(-10,20,0.1)

plt.plot(x,f(x))

#plt.plot()

