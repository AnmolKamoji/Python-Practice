numbers=[1,2,3,4,5,6]
numbers.append(20)
numbers.insert(0,10)
numbers.remove(10)
numbers.pop()
print(numbers.index(5))
print(numbers)
print(50 in numbers)
print(numbers.count(5))
numbers.sort()
numbers.reverse()
print(numbers)
numbers.append(5)
print(numbers)
uniques = []
for number in uniques:
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
print(uniques)

