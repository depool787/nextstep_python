empty_list=[]

list_fruits = ["apple","banana"]

print(list_fruits)
list_fruits[0]="mango"

print(list_fruits)

list_fruits.append("kiwi")

print(list_fruits)

list_fruits.insert(1,"guava")

print(list_fruits)

list_fruits.remove("kiwi")
print(list_fruits)


list_fruits =["apple","banana"]


for i in range( len(list_fruits)):
    print(f'{i} : {list_fruits[1]}')
    
    
list_fruits =["apple","banana"]
list_fruits.sort()
print(list_fruits)



list_fruits =["apple","banana"]
list_fruits.reverse()
print(list_fruits)

index_of_apple=list_fruits.index('banana')
print(index_of_apple)
    
    
    