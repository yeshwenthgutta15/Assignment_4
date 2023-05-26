# Write a Python program to square the elements of a list using map() function

def square_mine_no(n):
    return n*n
lst_no = (4,8,7,9)
print("Original List: ",lst_no)
result = map(square_mine_no, lst_no)
print("Square the elements of said list using map: ")
print(list(result))
