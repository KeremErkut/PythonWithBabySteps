notes = [90, 75, 60, 64]
print(type(notes))

list = ["a", 15.5, 90, -4, notes]
print(len(list)) # -> 5

print(list[4]) 

wholeList = [notes, list]

del wholeList #List can be deleted using 'del'.

print(notes[:2])
print(notes[2:])
print(notes[0:2])
print(list[4][0])

list.append("kerem")

list.remove("kerem")

list.insert(0,"kerem")

list.insert(len(list),"99")

list.pop(0)

list.count("kerem")

listBackup = list.copy()

list.extend(["a","b",10])

list.index("a")

list.reverse()

list.sort() #This methot will not work because the list contains different data types.

list.clear() 