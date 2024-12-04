myset = set()
myset.add(1)
myset.add(2)
print(myset)
print(len(myset))
print(1 in myset)
print(2 in myset)
myset.remove(2)
print(2 in myset)
print(myset)
myset.remove(1)
myset = {i for i in range(5)}
print(myset)

