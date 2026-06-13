# Assignment: 2 
# 1.  Create a tuple: 
# my_tuple = (10, 20, 30, 40, 50) 
# Print: 
# ● First element  
# ● Last element  
# ● Length of the tuple  
# ● Elements from index 1 to 3  

# my_tuple = (10,20,30,40,50)

# print("first element",my_tuple[0])
# print("last element",my_tuple[-1])
# print("length of tuple",len(my_tuple))
# print(" element from index 1 to 3",my_tuple[1,4])


# 2.   Create a tuple: 
# fruits = ("apple", "banana", "mango", "orange") 
# Print: 
# ● Second fruit  
# ● Last two fruits  
# ● Total number of fruits  

# fruits = ("apple", "banana", "mango", "orange") 

# print("second fruit ",fruits[1])
# print("last two fruit ",fruits[-2])
# print("length of fruit fruit ",len(fruits))

# 3.  Create a set: 
# numbers = {10, 20, 30, 40, 50} 
# Print: 
# ● Complete set  
# ● Length of the set  
# ● Check whether 30 is present in the set  

# numbers = {10, 20, 30, 40, 50} 
# print("complete set:",numbers)
# print("length of set:",len(numbers))
# print("is 30 present?",30 in numbers)

# 4.  Create two sets: 
# set1 = {1, 2, 3, 4} 
# set2 = {3, 4, 5, 6} 
# Find: 
# ● Union  
# ● Intersection  

# set1 = {1, 2, 3, 4} 
# set2 = {3, 4, 5, 6}

# print("union:",set1.union(set2))
# print("intersection:",set1.intersection(set2))



# 5. Create a dictionary: 
# student = {"name":"Kriti", "age":20, "course":"Python"} 
# Print: 
# ● Complete dictionary  
# ● Student name  
# ● Student age 
#  Student course Create a list: 
# numbers = [12, 45, 7, 23, 56, 89, 34] 
# Write a program to find: 
# o Largest element 
# o Second largest element 
# o Smallest element 

# student = {"name":"bhupendra", "age":20, "course":"Python"} 
# print("complete directory:",student)
# print("student name:",student["name"])
# print("student age:",student["age"])
# print("student course:",student["course"])

# numbers = [12, 45, 7, 23, 56, 89, 34] 
# print("largest number:", max(numbers))

# numbers.sort()
# print("second largest element",numbers[-2])
# print("smallest element",min(numbers))


# 6. Create a list: 
# arr = [10, 20, 30, 40, 50, 60] 
# Write a function that takes the list as input and returns the list in 
# reverse order without using the reverse() method. 

# arr = [10, 20, 30, 40, 50, 60] 
# def reverse_list(lst):
#     return lst[::-1]

# print("reversed list:",reverse_list(arr) )

# 7. Create a tuple: 
# data = (5, 10, 15, 20, 25, 30, 35) 
# Write a program to: 
# ○ Count how many elements are divisible by 5 
# ○ Find the sum of all elements 
# ○ Find the average of the tuple 

# data = (5, 10, 15, 20, 25, 30, 35) 
# count=0
# for num in data:
#     if num %5 ==0:
#         count+=1

# total =sum(data)
# average=total/len(data)
# print("element divisible by 5:",count)
# print("sum:",total)
# print("average:",average)


# 8. Create a dictionary: 
# students = { 
# "Aman": 78, 
# "Riya": 92, 
# "Kriti": 88, 
# "Rahul": 95 
# } 
# Write a program to: 
# ○ Find the student with the highest marks 
# ○ Find the student with the lowest marks 
# ○ Print only the students who scored more than 85 marks

# students = {
#     "Aman": 78,
#     "Riya": 92,
#     "bhupendra": 88,
#     "Rahul": 95
# }

# highest = max(students, key=students.get)
# lowest = min(students, key=students.get)

# print("Highest Marks:", highest, students[highest])
# print("Lowest Marks:", lowest, students[lowest])

# print("Students scoring more than 85:")
# for name, marks in students.items():
#     if marks > 85:
#         print(name, marks)

# 9. Write a function: 
# count_frequency(arr) 
# that takes a list as input and prints the frequency of each element. 
# Example: 
# arr = [1, 2, 2, 3, 1, 4, 2] 
#  Output: 
#  1 -> 2 times 
# 2 -> 3 times 
# 3 -> 1 time 
# 4 -> 1 time  

# def count_frequency(arr):
#     freq = {}

#     for item in arr:
#         freq[item] = freq.get(item, 0) + 1

#     for key, value in freq.items():
#         print(key, "->", value, "times")

# arr = [1, 2, 2, 3, 1, 4, 2]
# count_frequency(arr)




 
# 10. Write a function: 
# find_duplicates(arr) 
# that takes a list as input and prints all duplicate elements present in 
# the list. 
#            Example: 
# arr = [10, 20, 30, 20, 40, 10, 50, 30] 
#             Output: 
#            Duplicate elements are: 
# 10 
# 20 
# 30

# def find_duplicates(arr):
#     seen = set()
#     duplicates = set()

#     for item in arr:
#         if item in seen:
#             duplicates.add(item)
#         else:
#             seen.add(item)

#     print("Duplicate elements are:")
#     for item in duplicates:
#         print(item)

# arr = [10, 20, 30, 20, 40, 10, 50, 30]
# find_duplicates(arr)