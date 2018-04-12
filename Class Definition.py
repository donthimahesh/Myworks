
# coding: utf-8

# In[14]:


class tmp:
    a=10
    b=20
    c=[1,3,4,5,10,50,16,82]
    def add(x,y):
        print("Sum of two numbers:",x+y)
    def table(x):
        for i in range(10):
            print(x,"*",i+1,"=",x*(i+1))
    def searching(x,y):
        z=0
        for i in y:
            if(x==i):
                print(z)
            z=z+1


# In[15]:


print(tmp.a)
print(tmp.b)
tmp.add(tmp.a,tmp.b)
tmp.table(tmp.b)
tmp.searching(tmp.a,tmp.c)

