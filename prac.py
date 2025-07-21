list = []
print("Blank list : ")
print(list)

list.append(2)
list.append(5)
print(f"After appending 2 and 5 is : {list}")

list.insert(2,10)
list.insert(3,15)
print(f"After inserting at 2nd and 3rd position: {list}")

list.extend([5,"hello"])
print(f"After extending with 5 and hello : {list}")

list.extend((1,2,3,4))
print(f"After extending list with tuple : {list}") # still the list is same not separate tuple inside it

list3 = [12,"I am list 3",list,["Hello, how are you!"],'hi','oops','work please'] # The multidimmensional list : [12, 'I am list 3', [2, 5, 10, 15, 5, 'hello', 1, 2, 3, 4], ['Hello, how are you!']]
print(f"The multidimmensional list : {list3}")

print(list3[0])
print(list3[3:])
print(list3[:3])
print(list3[-1:])
print(list3[-1:-6])
print(list3[:-1])
print(list3[::-1])

list3.remove(12)
print(f"After removing 12 from list 3 : {list3}")

list3.pop()
print(f"Popping last element from the list 3 : {list3}")

list3.pop(3)
print(f"After popping 3rd element from the list 3 : {list3}")

print(f"slicing from 1 to 3 : {list3[0:2]}")
print(f"Slicing from negative side : {list3[:-1]}")
print(f"Slicing from end : {list3[-3:-1]}")

dictionary = {'Name':'Geeks',1:'Hello',4:'world',3:2}
print(dictionary)
print(f"Dictionary with specific element index : {dictionary['Name']}")

valid_list = [("Name", "Geeks"), (1, "Hello"), (4, "world"), (3, 2)]
Dict = dict(valid_list)
print(Dict)  # Output: {'Name': 'Geeks', 1: 'Hello', 4: 'world', 3: 2}

print(dictionary.get('Name'))

nestedDictionary = {1:{'Name':'Geeks'},2:'hello'}
print(nestedDictionary[1]['Name'])

valid_list.pop()
print(f"Popping last element : {valid_list}")

dictionary = {'Name': 'Geeks', 1: 'Hello', 4: 'world', 3: 2}
dictionary.popitem()  # Removes the last inserted key-value pair
print(dictionary)

odd_square = [x**2 for x in range(1,11) if x % 2 == 1]
print(odd_square)

words = ["hello","world","obvious","play",'cricket',"song"]
firstCharacter = [x[0] for x in words]
print(firstCharacter)

uppercaseString = [x.upper() for x in words]
print(uppercaseString)

pairs = [(x,y) for x in range(1,3) for y in range(4,6)]
print(pairs)

matrix = [[1,2,3],[4,6,7],[9,0,1]]
flattendList = [num for row in matrix for num in row]
print(flattendList)
