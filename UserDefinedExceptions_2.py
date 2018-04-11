
# coding: utf-8

# In[2]:


# Print A Table only till ten if range exceeds 10 it should give an error Till ten exception
class TillTen(Exception):
    def __str__(self):
        self.value="Till Ten Exception"
        return(self.value)
try:
    x=int(input("enter a number:"))
    y=int(input("enter a range:"))
    for i in range(y):
        if i<=9:
            print(x,"X",i+1,"=",x*i+1)
        else:
            raise TillTen
except TillTen:
    raise

