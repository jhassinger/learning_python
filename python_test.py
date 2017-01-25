
# coding: utf-8

# In[1]:

print('hello world')


# In[2]:

a = 3 + 2
print(a)


# In[3]:

help(print)


# # Make Markdown block

# In[9]:

import numpy as np

#100 evenly-spaced numbers from 0 to 2*pi
start = 0
end = 2 * np.pi
num_val = 100
x = np.linspace(start, end, num_val)

#calculate sine and cosine
y = np.sin(x)
z = np.cos(x)

print(y)


# In[13]:

#import matplotlib
import matplotlib.pyplot as plt

#plot sin
plt.plot(x, y, label='sin')
#plot cosine
plt.plot(x, z, ':', label='cos')

#legend
plt.legend()

#save
plt.savefig('./sincos.png')
plt.savefig('./sincos.pdf')

#show our plot
plt.show()


# In[ ]:



