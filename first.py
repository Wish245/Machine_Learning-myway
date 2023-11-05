
def deriv_w(list1,list2,w,b):
    a = 0
    for x in list1 and list2:
        a = a + (w*list1[x] + b - list2[x])*list1[x]
    d = (1/len(list1))*a
    return d

def deriv_b(list1,list2,w,b):
    a = 0
    for x in list1 and list2:
        a = a + (w*list1[x] + b - list2[x])
    d = (1/len(list1[x]))*a
    return d

