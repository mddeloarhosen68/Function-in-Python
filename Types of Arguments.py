def person(name = 'Anon',age = 18): #Default
    print(name)
    print(age)

person(name = 'Anon2',age = 26)   # Position and Keyword


def sum(*b):  #Or (a,*b)

    c = 0    # C = a
    for i in b:
        c = c + i
        print(c)
sum(5,6,34,78)


def person(name,**data):
    print(name)
    for i,j in data.items():  # Or   print(data)
        print(i,j)

person('Anon',age = 26, city = 'Dhaka', mob = 880199)