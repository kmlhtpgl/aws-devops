def generatepassword():
    name = input("Please enter your full name without space: ")
    password = ""
    import random
    three_letters = random.sample(name, 3)
    four_digits = random.sample(range(10), 4)
    for i in three_letters:
        password += i
    for l in four_digits:
        password += str(l)
    print(password.lower())  

generatepassword()
