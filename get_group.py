#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[3]:


def reach_out(group,net):
    search_key=set(net.keys()) & set(group)
    for key in search_key:
        if key in net.keys():
            group+=net[key]
            del net[key]
    return {"new group":group,
           "new_net":net}

def get_group(point,net):
    group=list([point]+net[point])
    group_len=[0,1]
    while group_len[-2]!=group_len[-1]:
        temp=reach_out(group,net)
        group = temp["new_group"]
        net = temp["new_net"]
        group_len.append(len(group))
        return list(set(group))
    
def get_sub_net(nodes,net):
    sub_net = {}
    for i in nodes:
        sub_net[i] = net[i]
    return sub_net


# In[ ]:




