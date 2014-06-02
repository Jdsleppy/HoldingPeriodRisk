import matplotlib.pyplot as plt
import numpy as np

## The purpose of this program is to evaluate how the holding period of a risky
## asset, such as a stock mutual fund, with reinvestment of dividends affects
## the risk as defined by the std deviation of the annualized cumulative return
## (http://en.wikipedia.org/wiki/Rate_of_return#Geometric_average_rate_of_return),
## and risk as defined by negative total returns.
## Monte-Carlo simulation is used to demonstrate that extended holding periods
## increase the annualized cumulative rate of return (geometric average rate),
## but lead to a higher probability of large negative returns!


## Edit these parameters all you like... within reason!

mu, sigma = 0.08, 0.2   # mean and std deviation of the one-year return
                        # these values are reasonable for equity funds

years = [1,5,20]   # the different holding periods we will consider

num = 500000   # the number of different random outcomes to simulate



## Editing these lines may cause loss of functionality!

years.sort()

finalRate = np.ones((num,len(years)))   # initialize the final data arrays
finalReturn = np.ones((num,len(years)))


for index in range(len(years)):
    #print index
    holder = np.ones(num)   # initialize a somewhat temporary array
    for step in range(0,years[index]):
        #print '\t' + str(step)
        temp = np.random.normal(mu,sigma,num) # fill with randomly distributed numbers
        #print '\t\t' + str(temp[0])
        holder = np.multiply(holder,np.add(temp,1))   # evolve the total return by one year
        #print '\t\t\t' + str(holder[0])

    holder = np.multiply(holder,pow(1.02,float(years[-1] - step - 1)))   # finish investment with risk-free asset

    finalRate[:,index] = np.power(holder,1./float(years[-1]))   # annualize data, store in final array
    finalReturn[:,index] = np.subtract(holder,1)   # store data in final array

finalRate = np.subtract(finalRate,1.)
finalRate = np.multiply(finalRate,100.)

finalReturn = np.multiply(finalReturn,100)

plt.figure(1)
plt.hist((finalRate[:,0],finalRate[:,1],finalRate[:,2]),bins=1000,histtype='step',normed=True,label=(str(years[0]) + ' years',str(years[1]) + ' years',str(years[2]) + ' years' ))
plt.title('Annualized Rate vs Risky Asset Holding Period')
plt.xlabel('Anualized Cumulative Return [%]')
plt.ylabel('Probability')
plt.xlim(-5,20)
plt.legend()
#plt.text(-20,0.06,'$\mu=$' + str(100*mu)) #+ '$\% ,\ \sigma=$' + str(100*sigma) + '$\%$')
plt.plot()

plt.figure(2)
plt.hist((finalReturn[:,0],finalReturn[:,1],finalReturn[:,2]),bins=5000,histtype='step',normed=True,label=(str(years[0]) + ' years',str(years[1]) + ' years',str(years[2]) + ' years' ))
plt.title('Total Returns vs Risk Asset Holding Period')
plt.xlabel('Total Return [%]')
plt.ylabel('Probability')
plt.xlim(-100,1000)
plt.legend()
plt.plot()
plt.show()


