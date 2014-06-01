import matplotlib.pyplot as plt
import numpy as np

## The purpose of this program is to evaluate how the holding period of a risky
## asset, such as a stock mutual fund, with reinvestment of dividends affects
## the risk (std deviation) of the annualized cumulative return (as defined in
## http://en.wikipedia.org/wiki/Rate_of_return#Geometric_average_rate_of_return).
## Monte-Carlo simulation is used to demonstrate that extended holding periods
## indeed decrease the risk as measured by the annualized cumulative rate
## (geometric average rate).


## Edit these parameters all you like... within reason!

mu, sigma = 0.08, 0.2   # mean and std deviation of the one-year return
                        # these values are reasonable for equity funds

years = [1,5,20]   # the different holding periods we will consider

num = 500000   # the number of different random outcomes to simulate



## Editing these lines may cause loss of functionality!

final = np.ones((num,len(years)))   # initialize the final data array

for index in range(len(years)):
    #print index
    holder = np.ones(num)   # initialize a somewhat temporary array
    for step in range(0,years[index]):
        #print '\t' + str(step)
        temp = np.random.normal(mu,sigma,num) # fill with randomly distributed numbers
        #print '\t\t' + str(temp[0])
        holder = np.multiply(holder,np.add(temp,1))   # evolve the total return by one year
        #print '\t\t\t' + str(holder[0])
    final[:,index] = np.power(holder,1./float(years[index]))   # annualize data, store in final array

final = np.subtract(final,1.)
final = np.multiply(final,100.)
plt.hist((final[:,0],final[:,1],final[:,2]),bins=200,histtype='step',normed=True,label=(str(years[0]) + ' years',str(years[1]) + ' years',str(years[2]) + ' years' ))
plt.title('Annualized Cumulative Return vs Holding Period')
plt.xlabel('Anualized Cumulative Return [%]')
plt.ylabel('Probability')
plt.xlim(-50,60)
plt.legend()
plt.text(-40,0.08,'$\mu=$' + str(100*mu) + '$\% ,\ \sigma=$' + str(100*sigma) + '$\%$') 
plt.show()


