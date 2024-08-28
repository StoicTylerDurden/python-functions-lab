# integer_set = {1, 2, 3, 4, 5}
# print(integer_set)
# another_int_set = set([11, 5, 6, 7, 8, 9, 5])
# print(another_int_set)
# chips = ['potato', 'computer', 'fish and', 5, 6]

# chips_set = set(chips)
# chips_set.add("Tomato")
# print(chips_set)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # we want 'n * n' for each 'n' in nums 
# for n in nums:
#     squares.append(n * n)

# print(squares)
# # prints [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



# squares = [<expression> for n in listName]

squares = [n*n for n in nums]
print(squares)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_squares = []

# # we want 'n * n' for each 'n' in nums  if 'n * n' is even
# for n in nums:
#     square = n * n 
#     if square % 2 == 0:
#         even_squares.append(square)

# even_squares = [<expression> for loop if <condition>]

even_squares = [n * n for n in nums if (n*n)%2 ==0]
print(even_squares)
# prints: [4, 16, 36, 64, 100]

