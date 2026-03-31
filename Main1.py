SetA = {1, 2, "A", 28, "C", "G", 0}
Set1 = {2, "C", 28, "N", 6, "F" }
SetQ = {2, "C", "G", 6, "H", 3}

result = SetA.union(Set1, SetQ)
list1 = list(result)
print(list1)

result2 = SetA.intersection(Set1, SetQ)
list2 = list(result2)
print(list2)