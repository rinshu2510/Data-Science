# n=12
# name = 'Rinshu'
# print(f"Name is {name.upper()} and no is {n}")
# print("name is {} and no is {}".format(name,n))

# x='refactor'
# print(x[-1:-4:-1])

#List comprehension

# list = [num*2 for num in range(10)]
# print(list)

#map()
def even(num):
    return num*2

l = [1, 2, 3, 4, 5, 6 ,7 , 8, 9, 10]

# result = list(map(even,l))

#lamda
result = list(map(lambda x:x*x,l))
print(result)

#filter

# fil = list(filter(lambda x : x%2==0,l))
# print(fil)
#
# fil = list(filter(lambda x : x%2==0,l))[1]
# print(fil)

print(list(filter(lambda x : x%2==0,l))[1])

