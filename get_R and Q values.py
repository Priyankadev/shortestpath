#!/usr/bin/env python
# coding: utf-8

# In[7]:


import copy
def initial_R(A,B,weight,A_B_dict):
    R={}
    net=copy.deepcopy(A_B_dict)
    for i in net.keys():
        sub_key=net[i] # last value(or connecting node ) of the dictionary
        sub_dic={}
        for j in sub_key:
            sub_dic[j]=0 #assign the sub key values key's value=0
        R[i]=sub_dic
        
    for i in range(len(A)):
        R[A[i]][B[i]]=weight[i]
    return R

def initial_Q(R):
    Q=copy.deepcopy(R)
    for i in Q.keys():
        for j in Q[i].keys():
            Q[i][j]=100
            
    return Q  
            
            
            
     


# In[ ]:





# In[ ]:





# In[ ]:




