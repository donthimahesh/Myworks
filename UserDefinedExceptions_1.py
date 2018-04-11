
# coding: utf-8

# In[19]:


class ExceedLength(Exception):
    def __str__(self):
        self.value="you have exceeded the limit"
        return(self.value)
    


# In[16]:


try:
    x=input("Enter Name:")
    if len(x)>=11:
        raise ExceedLength 
except ExceedLength as EL:
    raise EL


# In[20]:


try:
    x=input("Enter Name:")
    if len(x)>=11:
        raise ExceedLength
except ExceedLength:
    raise

