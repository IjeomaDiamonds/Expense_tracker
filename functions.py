def my_func():
    print("this is my first function")

#my_func()
def check_prime(num):
    number = int(num)
    condition = 0
    count = 2
    iteration = 0

    while iteration <= number /2:
        if number % count == 0:
            condition = 1
            break
        iteration += 1
    if condition == 0:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')

#check_prime(25)
#check_prime(26)
#check_prime(27)
#check_prime(28)
def add_num(*num):
    final_num =0
    for num in num:
        final_num += num
    return final_num

#print(add_num(1,2,3,4,5,6,7,8,9,10))
