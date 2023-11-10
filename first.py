import numpy as np

def deriv_w(list1,list2,w,b):
    a = 0
    for x in range(len(list1)):
        tmp_a = a + (w*list1[x] + b - list2[x])*list1[x]
        a = tmp_a
    d = (1/len(list1))*a
    return d

def deriv_b(list1,list2,w,b):
    a = 0
    for x in range(len(list1)):
        tmp_a = a + (w*list1[x] + b - list2[x])
        a = tmp_a
    d = (1/len(list1))*a
    return d

def main():
    w = 10.0
    b = 10.0
    alpha = 0.1
    beta = 25.5
    list1 = np.array([0.0,0.5,1.0,1.5,2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3.0,3.5,4.0,4.5,5.0])
    list2 = np.array([0.0,0.0,0.0,0.0,0.0,2.0,5.0,14.0,24.0,69.0,87.0,139.0,171.0,255.0,328.0,746.0,1157.0,1504.0,1958.0])
    tmp_b=0
    tmp_w=0
    while tmp_w != w and tmp_b != b:
        tmp_w = w - alpha* deriv_w(list1,list2,w,b)
        tmp_b = b - alpha* deriv_b(list1,list2,w,b)
        w = tmp_w
        b = tmp_b
    y = w*beta + b
    print(w)
    print(b)
    print(y)
    return 0

main()
