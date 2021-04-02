numbers = input("Please enter 5 numbers(leave space between the numbers): ")
list1 = numbers.split()
#print(list1)
biggest = 0
for i in list1:
    if int(i) > biggest:
        biggest = int(i)


print(biggest)