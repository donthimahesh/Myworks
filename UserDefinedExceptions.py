
# coding: utf-8

# In[11]:


class ExceedLength(Exception):
    def __init__(self):
        self.value="you have exceeded the limit"
    def __str__(self):
        return(self.value)


# In[12]:


try:
    x=input("Enter Name:")
    if len(x)>=11:
        raise ExceedLength 
except ExceedLength as EL:
    raise EL


# In[13]:


try:
    x=input("Enter Name:")
    if len(x)>=11:
        raise ExceedLength
except ExceedLength:
    raise

