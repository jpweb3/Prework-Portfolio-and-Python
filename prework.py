# Question 1
# Write a function to print “hello_USERNAME!” USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello_" + user_name +"!")

username_input = input("USERNAME: ")
hello_name(username_input)

#def hello_name(user_name):
#    print(f"hello_{user_name}!")    # f allows direct input is this better?

#username_input = input("USERNAME: ")
#hello_name(username_input)


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
  for number in range(1, 101): 
    if number % 2 != 0:
        print(number)

#first_odds()


# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    return max(a_list)

sample_list = (50, 60, 70, 71) #should this be created using []?
result = max_num_in_list(sample_list)
print(result)


# Question  4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0): 
        return True
    else:
        return False

year_input = int(input("Enter a year: "))
result = is_leap_year(year_input)
print(result)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#def is_consecutive(a_list):
# Dont quite understand how to solve this one and cannot explain answers found