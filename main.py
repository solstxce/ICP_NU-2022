from functions import *
import os
import time
def logo():
  os.system("cls")
  print("""
  ████████ ██                      ██        
 ██░░░░░░ ░░              ██████  ░██        
░██        ██ ██████████ ░██░░░██ ░██  █████ 
░█████████░██░░██░░██░░██░██  ░██ ░██ ██░░░██
░░░░░░░░██░██ ░██ ░██ ░██░██████  ░██░███████
       ░██░██ ░██ ░██ ░██░██░░░   ░██░██░░░░ 
 ████████ ░██ ███ ░██ ░██░██      ███░░██████
░░░░░░░░  ░░ ░░░  ░░  ░░ ░░      ░░░  ░░░░░░ 
   ██████                                              ██                 
  ██░░░░██                                            ░██                 
 ██    ░░   ██████  ███████  ██    ██  █████  ██████ ██████  █████  ██████
░██        ██░░░░██░░██░░░██░██   ░██ ██░░░██░░██░░█░░░██░  ██░░░██░░██░░█
░██       ░██   ░██ ░██  ░██░░██ ░██ ░███████ ░██ ░   ░██  ░███████ ░██ ░ 
░░██    ██░██   ░██ ░██  ░██ ░░████  ░██░░░░  ░██     ░██  ░██░░░░  ░██   
 ░░██████ ░░██████  ███  ░██  ░░██   ░░██████░███     ░░██ ░░██████░███   
  ░░░░░░   ░░░░░░  ░░░   ░░    ░░     ░░░░░░ ░░░       ░░   ░░░░░░ ░░░    

""")
def info():
  print(""" Select the type of input you wanna give:
    [1] Integer
    [2] Binary
    [3] Hex
    [4] Oct
    [q] Select this to exit the program.
     """)
  choice = input("[?]: ")
  return choice
def repeatConv(Ans):
  strAns=str(Ans)
  if strAns=='y' or strAns=='yes':
   os.system('cls')
   choiceVar=info()
   main(choiceVar)
  elif strAns=='n' or strAns=='no' or strAns=='q':
    main('5')
  else:
    print('Please choose any appropriate answer. (Either y or n)')
    repeatConv(input('Do you wanna continue? \nAnswer y(yes) or n(no) or q(quit): '))
def main(choice):
 if choice == '1':
   getInt=int(input("Enter a valid number: "))
   print('The number in binary format:',int_to_bin(getInt))
   print('The number in hex format: ',int_to_hex(getInt))
   print('The number in oct format: ', int_to_oct(getInt))
   repeatConv(input('\nDo you wanna continue? \nAnswer y(yes) or n(no) or q(quit): '))
 elif choice =='2':
   getBin=input("Enter a valid binary string: ")
   print('The binary string as integer:',bin_to_int(getBin))
   print('The binary string in hex:',bin_to_hex(getBin))
   print('The binary string in oct:',bin_to_oct(getBin))
   repeatConv(input('\nDo you wanna continue? \nAnswer y(yes) or n(no) or q(quit): '))
 elif choice=='3':
   getHex=input("Enter a valid hex string: ")
   print("The hex string as integer:",hex_to_int(getHex))
   print("The hex string in binary:",hex_to_bin(getHex))
   print("The hex string in oct:",hex_to_oct(getHex))
   repeatConv(input('\nDo you wanna continue? \nAnswer y(yes) or n(no) or q(quit): '))
 elif choice =='4':
    getOct=input('Enter a valid oct string: ')
    print("The hex string as integer:",oct_to_int(getOct))
    print("The hex string in binary:",oct_to_bin(getOct))
    print("The hex string in hex:",oct_to_hex(getOct))
    repeatConv(input('\nDo you wanna continue? \nAnswer y(yes) or n(no) or q(quit): '))
 elif choice=='5' or choice=='q':
   print("Thank you for using the string converter!")
   os.system('exit')
 elif choice=='':
   print("Please select any of the options!")
   os.system('cls')
   choiceVar=info()
   main(choiceVar)
 else:
  print("Invalid choice!\nPlease choose from the given options only!") 
  time.sleep(3)
  os.system('cls')
  choiceVar=info()
  main(choiceVar)
logo()
choice=info()
main(choice)
