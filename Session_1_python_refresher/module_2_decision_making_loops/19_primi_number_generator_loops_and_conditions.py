limit = int(input("Enter the upper limit for prime numbers: "))
# 10
print("Prime numbers up to", limit, ":")
for number in range(2, limit + 1): # number : 4
    prime = True
    if number < 2:
        prime = False
    else:
        for i in range(2, int(number/2)+1): # i = 5  # number = 15
            if number % i == 0:
                prime = False
                break
    if prime:
        print(number, end=" ")

# 2, 5, 7, 11, 13, 17

# 10 : 5 : 2