# Write a Python program to triple all numbers of a given list of integers. Use Python map

my_file1 = (1,2,3,4,5,6,7,8,9,10)
print("Original List: ",my_file1)
result = map(lambda x : x + x + x, my_file1)
print("Triple of said list numbers: ")
print(list(result))

