# n1

def  majority_element (a:list)->int:
    if len(a)==0:
        return -1
    else:
        return max(a, key=a.count)


print(majority_element([1,2,3,1,1,5]))