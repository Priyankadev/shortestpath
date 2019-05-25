#!/usr/bin/env python
# coding: utf-8

# In[11]:


import csv
def get_dict(data):
    A_0=data["node"].values.tolist()
    B_0=data["connected"].values.tolist()
    weight=data["weight"].values.tolist()
    # create a data frame and assign column name to that 
    A=A_0+B_0
    B=B_0+A_0
    weight=weight+weight
    
    A=list(map(lambda x:int(x),A)) #store the data into list
    B=list(map(lambda x:int(x),B))
    
    A_key=sorted(set(A)) #sort the nodes using dictionary ,so that we can get the sorted list of nodes
    A_B_dict={} #create a blank dictinary to for key value pair
    
    for i in range(len(A_key)): #iterate the values as per the list length
        A_B_dict[A_key[i]]=[] #store the sorted nodes as key and leave the values blank
        
    for i in range(len(A)):
        if B[i] not in A_B_dict[A[i]]: #check whether current node and connected node should not be same
            A_B_dict[A[i]].append(B[i]) #add values of B(connected nodes ) to the dictionary
        
    mydict=A_B_dict
    with open("connection_weight.csv",'w') as csv_file: #create a csv file to store the nodes an connected nodes
        writer=csv.writer(csv_file)
        for key,val in mydict.items():
            writer.writerow([key,val]) #take the dictionary values to the csv file
    csv_file.close()
            
    return{"A":A,
           "B":B,
           "weight": weight,
           "A_B_dict":A_B_dict}
        
        












# In[ ]:





# In[ ]:




