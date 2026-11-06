# n1

# def  majority_element (a:list)->int:
#     if len(a)==0:
#         return -1
#     else:
#         return max(a, key=a.count)


# print(majority_element([1,2,3,1,1,5]))

# n2

def search_by_genre (a:str)->list:
    cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
    ]
    new = []
    for x in cinema:
        if x["genre"]==a:
            new.append(x)
    print(new)

search_by_genre(input(">>> "))