L = [6, 7, 8, 9, 1, 2, 3, 4, 5]
count = 0


for i in L:
    count += 1


avg = count/len(L)

print("Average = ", avg)
print("The count is ", count)

L.sort()

print("The biggest number in the set is: ", L[0])
print("The smallest number in the set is: ", L[-1])


