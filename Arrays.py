import array as arr

arr_num = arr.array('i', [1, 2, 3, 3, 3, 4, 5, 6])
print("Original array:", (arr_num))

print("The number of times 3 occured in the array is:")
print((arr_num.count(3)))

arr_num.reverse()
print("The array reversed:")
print(arr_num)