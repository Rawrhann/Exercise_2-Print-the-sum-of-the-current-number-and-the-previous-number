#Exercise 2: Print the sum of the current number and the previous number
#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

number = 0
for i in range(1, 11):
    sum = number + i
    print("The previous number is", number, "and the current number is", i, "and their sum is", sum)
    number = i