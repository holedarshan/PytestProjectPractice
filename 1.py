def is_prime(num):

    if num >= 2 :
        for i in range(2,(num//2)+1 ):
            if num % i == 0:
                print(f"{num} is  not prime number")
                break

        else:
            print(f"{num} is  prime number")

    else:
        print(f"{num} is  not prime number")


is_prime(11)

