# FizzBuzz Game:
# Write a Python program that prints the numbers from 1 to 100.
# But for multiples of three, print "Fizz" instead of the number,
# and for the multiples of five, print "Buzz".
# For numbers that are multiples of both three and five, print "FizzBuzz".

fizz_count = 0
buzz_count = 0
fizzbuzz_count = 0
nums_count = 0

for i in range(1, 101): # 1,2,3
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
        fizzbuzz_count = fizzbuzz_count + 1
    elif i % 3 == 0:
        print("Fizz")
        fizz_count = fizz_count + 1
    elif i % 5 == 0:
        print("Buzz")
        buzz_count = buzz_count + 1
    else:
        print(i)
        nums_count = nums_count + 1
# 7 : LUCKY | 5  : EASY | 7 and 5 : LUCKYEASY

print(f"FIZZ Count : {fizz_count}")
print(f"BUZZ count : {buzz_count}")
print(f"FIZZBUZZ count : {fizzbuzz_count}")
print(f"NUMS count : {nums_count}")
