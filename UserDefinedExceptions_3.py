
# coding: utf-8

# In[5]:


class NotFound(Exception):
    def __str__(self):
        self.value="Value Not Found"
        return(self.value)
try:
    x=[2,3,4,5,6]
    y=int(input("enter value to be searched:"))
    n=0
    for i in range(len(x)):
        if y==x[i]:
            print("Value Found in location:",i)
            n=0
            break
        else:
            n=1
    if n==1:   
        raise NotFound            
except NotFound:
    raise
        

