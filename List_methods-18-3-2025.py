# Task:-
# 1)Implement the program to print true when the first and last element in the list was even, else print false.

# num = [2,5,4,3,8,9,7,6,2,1,8,5,4]
# if num[0] and num[len(num)-1] %2 == 0:
#     print("true")
# else:
#     print("False")


# 2) implement the program to create a function which performs the count method. Without using any methods.
num = [1,1,1,2,5,3,3,5,6,8,7,9,10,45,11,1,1,2,7]
element = 2
def count_method(num,element):
    count = 0
    for i in range(0,len(num)):
        if num[i]==element:
            count+1
        return count
print(count_method(num,element))

# 3) write a program to print the prime numbers in the new list from the existing list.
# num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# new_list=[]
# for i in range(0,len(num)):
#     if num[i]%2 ==0:
#         new_list.append(i)
# print(new_list)