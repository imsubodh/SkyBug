import random
import string

while True:
    char = string.ascii_letters + string.digits + string.punctuation
    length = int(input("\nEnter the length of the Password: "))
    
    password = ''.join(random.choice(char) for _ in range(length))

    print("The Strongest Password is:")
    print("\n", password, "\n")
     
    flag = int(input("Do you want to Generate The Password again (1 for Yes, 0 for No): "))

    if flag == 0:
        break
