
#01 Even or Odd Function
def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even(10))


#02 Largest of Two Numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(10, 20))


#03 Print Numbers
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(10)


#04 Sum of Numbers
def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_n(5))


#05 Multiplication Table
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

table(5)


#06 Count Even Numbers
def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count = count + 1
    return count

print(count_even([1, 2, 3, 4, 6]))


#07 Find Maximum
def find_max(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

print(find_max([10, 25, 5, 40, 15]))


#08 FizzBuzz
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()


#09 Palindrome Checker
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))


#10 Count Vowels
def count_vowels(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count = count + 1
    return count

print(count_vowels("Hello World"))


#11 Second Largest Number
def second_largest(numbers):
    largest = numbers[0]
    second = None

    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if second == None or i > second:
                second = i

    return second

print(second_largest([10, 20, 40, 30, 50]))


#12 Guessing Game
import random

def guessing_game():
    num = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == num:
            print("Correct Guess!")
            break
        else:
            print("Wrong Guess! Try Again.")

guessing_game()


#13 Write a function grade(marks) that
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(85))
