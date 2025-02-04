
import random

l = []
for i in range(100):
    k = random.randint(1, 100)
    l.append(k)


def tri_selection2(l):
    n = 0
    for j in range(len(l)):
        i_min = j
        i_max = len(l)-1-j
        for i in range(j, len(l)-j):
            n += 1
            if l[i] < l[i_min]:
                i_min = i
                
            if l[i] > l[i_max]:
                i_max = i
                
        l[j], l[i_min] = l[i_min], l[j]
        l[len(l)-j-1], l[i_max] = l[i_max], l[len(l)-j-1]

    return l, n



def tri_selection1(l):
    n = 0
    for j in range(len(l)-1):
        i_min = j
        for i in range(j+1, len(l)):
            n += 1
            if l[i] < l[i_min]:
                i_min = i
            
        l[j], l[i_min] = l[i_min], l[j]
        
    return l, n

if len(l) < 6:
    print(tri_selection1(l))
else:
    print(tri_selection2(l))
