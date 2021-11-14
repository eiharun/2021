#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Method 1
import time
start_time = time.time()
prime = ''
for n in range (0, 101):
    for i in range(2, n):
        if n % i == 0:
            #print(n, "is not a prime number")
            prime = "no"
            break
        else:
            #print(n, "is a prime number")
            prime = 'yes'       
            
            
    print(n, prime)

print("-----{}-----".format((time.time() - start_time)))
'''In terms of speed, it is average, might be one of the faster ones. However it is super simple and quick to code.
'''


# In[19]:


#Method 2
import time
start_time = time.time()
prime = ''
for n in range (0, 101):
    for i in range(2, n//2):
        if n % i == 0:
            prime = 'no'
            break
        else:
            prime = 'yes'
    else:
        if n % i == 0:
            prime = 'no'
        
        else:
            prime = 'yes'
            
    print(n, prime)
print("-----{}-----".format((time.time() - start_time)))
'''Fastest algorithm, 2nd least complex in terms of coding.
Best algorithm
'''


# In[25]:


#Method 3
import time
import math
start_time = time.time()
prime = ''
for n in range (0, 101):
    for i in range(2, math.isqrt(n)):
        if n % i == 0:
            prime = 'no'
            break
        else:
            prime = 'yes'
    else:
        if n % i == 0:
            prime = 'no'
        
        else:
            prime = 'yes'
    print(n, prime)
print("-----{}-----".format((time.time() - start_time)))
'''Complex coding without having the speed make up for it, can be faster when dealing with very large numbers
'''


# In[24]:


#Method 4
import time
import math
start_time = time.time()
prime = ''
for n in range (0, 101):
    for i in range(2, math.isqrt(n)):
        for x in range(2, i):
            if i % x == 0:
                break
            else:
                if n % i == 0:
                    prime = 'no'
                    break
                else:
                    prime = 'yes'
                    break
        else:
            continue
        break
    else:
        if n % i == 0:
            prime = 'no'
        else:
            prime = 'yes'
    print(n, prime)

print("-----{}-----".format((time.time() - start_time)))
'''Most complex out of all. 2nd slowest of the 4 methods.
'''


# In[ ]:




