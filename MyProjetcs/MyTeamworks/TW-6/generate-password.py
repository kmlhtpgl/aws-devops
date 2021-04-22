def generatepassword():
    name = input("Please enter your full name without space: ")
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    password = ""
    namelower = name.lower()
    def split(namelower):
        return [char for char in namelower]
    #print(split(namelower))
    import random
    three_letters = random.sample(split(namelower), 3)
    #print(three_letters)
    three_digits = random.sample(digits, 4)
    #print(three_digits)
    for i in three_letters:
        password += i
    for l in three_digits:
        password += str(l)
    print(password)  

generatepassword()
