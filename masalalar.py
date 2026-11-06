# n1

# def  majority_element (a:list)->int:
#     if len(a)==0:
#         return -1
#     else:
#         return max(a, key=a.count)


# print(majority_element([1,2,3,1,1,5]))

# n2

# def search_by_genre (a:str)->list:
#     cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
#     ]
#     new = []
#     for x in cinema:
#         if x["genre"]==a:
#             new.append(x)
#     print(new)

# search_by_genre(input(">>> "))

# n3

# def merge_unique_ids (a:list,b:list)->list:
#     c=a+b
#     new=[]
#     for x in c:
#         if x not in new:
#             new.append(x)
#     print(new)
        

# a = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# b = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']
# merge_unique_ids(a,b)

# n4

# def sorted_by_price (a:list)->list:
#     natija=sorted(a, key=lambda x: int(x[1]), reverse=True)
#     return natija


# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10')
# ]
# sorted_by_price(products)
# for x in sorted_by_price(products):
#     print(x)

# n5

def are_numbers_ascending (a:str)->bool:
    lst=[]
    for x in a.split():
        if x.isdigit():
            lst.append(int(x))
    
    for i in range(1,len(lst)):
        if lst[i] <= lst[i-1]:
            return False
        return True


print(are_numbers_ascending(input(">>> ")))

