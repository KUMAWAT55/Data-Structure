from math import log
#log function
import numpy as np
import matplotlib.pyplot as plt
def func_BigO_cal():
    plt.style.use('bmh')
    #Matplotlib Style
    n=np.linspace(1,10,1000)
    #Return evenly spaced numbers over a specified interval.
    labels=['constant','logarithmic','Linear','Log Linear','Quadratic','Cubic','Exponential']
    Big_O=[np.ones(n.shape),np.log(n),n,n*np.log(n),n**2,n**3,2**n]
    plt.figure(figsize=(6,5))
    plt.ylim(0,50)
    plt.ylabel('Relative Runtime')
    plt.xlabel('n')
    for i in range(len(Big_O)):
        #Plotting
        plt.plot(n,Big_O[i],label=labels[i])
    plt.legend(labels)
    plt.show()



if __name__ == '__main__':
    func_BigO_cal()