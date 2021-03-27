def convertMillis(millis):
     seconds=(millis/1000)%60
     minutes=(millis/(1000*60))%60
     hours=(millis/(1000*60*60))
     return seconds, minutes, hours

def main():
    print("###  This program converts milliseconds into hours, minutes, and seconds ###")
    print('To exit the program, please type "exit"')
    while True:
        millis=input("Enter time in milliseconds:  ")
        if millis.casefold() == "exit":
            print("Exiting the program, Good bye")
            break
        try: 
            if int(millis) >= 1:
                con_sec, con_min, con_hour = convertMillis(int(millis))
                split_sec = str(con_sec).split('.')
                int_sec = int(split_sec[0])
                split_min = str(con_min).split('.')
                int_min = int(split_min[0])
                split_hour = str(con_hour).split('.')
                int_hour = int(split_hour[0])
                if int(millis) < 1000:
                    print(f"just {millis} milliseconds")
                elif int(millis) >= 1000 and int(millis) < 60000:
                    print(f"{int_sec} second/s")
                elif int(millis) >= 60000 and int(millis) < 3600000:
                    print(f"{int_min} minute/s {int_sec} second/s")
                else:
                    print(f"{int_hour} hour/s {int_min} minute/s {int_sec} second/s")  
                    
                    
            else:
                print("Millisecond can`t be negative or zero, please enter again")
        except ValueError: 
            print("Not valid input!!!please enter again")
main()