num_str = input("Enter a number: ")
num = int(num_str)
temp = num
sum = 0
length = len(num_str)

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** length)
    temp = temp // 10

if num == sum:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")

    