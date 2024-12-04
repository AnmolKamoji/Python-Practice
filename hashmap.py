mymap = {}
mymap["Alice"] = 88
mymap["Bob"] = 78
print(mymap)
mymap["Alice"]=80
print(mymap)
print("Alice" in mymap)
mymap.pop("Alice")
print(mymap)