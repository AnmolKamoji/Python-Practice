numbers=[2,2,1,2,3,4,5]
uniques = []
for number in numbers:
    for number in numbers:
        if number not in uniques:
            uniques.append(number)
uniques.sort()
print(uniques)