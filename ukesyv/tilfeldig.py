
# import the required libraries  
import random  
import matplotlib.pyplot as plt  
    
# store the random numbers in a list  
nums = []  
mu = 1.5
sigma = 10
    
for i in range(1000):  
    temp = random.lognormvariate(mu, sigma)  
    print(temp)
    nums.append(temp)  

        
 #plotting a graph  
plt.hist(nums, bins = 200)  
plt.show() 