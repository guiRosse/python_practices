import cls

cls.clear_screen()
def prime_checker(number):
    Flag = False
    if number == 1:
        print(f"{number} is not prime!")
        Flag = False
    elif number > 1:
        for x in range(2, number):
            if number % x == 0:
                # print(f"{number} is not prime!")
                Flag = False
                break
            else:
                # print(f"{number} is prime!")
                Flag = True
    if Flag == True:
        print(f"{number} is prime!")
    else:
        print(f"{number} is not prime!")

n = int(input("Check this number: "))
prime_checker(number=n)