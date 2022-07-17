from functions import *
import time
import sys

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
   logo()
   choiceVar=info()
   main(choiceVar)
  elif strAns=='n' or strAns=='no' or strAns=='q' or strAns=='quit':
    main('5')
  else:
    print('\nPlease choose any appropriate answer. (Either y or n or q)')
    repeatConv(input(f'\nDo you wanna continue? \nAnswer {Fore.LIGHTGREEN_EX}y(yes) {Fore.WHITE}or {Fore.LIGHTMAGENTA_EX}n(no) {Fore.RESET}or {Fore.LIGHTRED_EX}q(quit): {Fore.RESET}'))
def main(choice):
 if choice == '1':
   getInt=int(input("Enter a valid number: "))
   print('The number in binary format:',f"{Fore.LIGHTBLUE_EX}{int_to_bin(getInt)}")
   print('The number in hex format: ',f"{Fore.LIGHTBLUE_EX}{int_to_hex(getInt)}")
   print('The number in oct format: ', f"{Fore.LIGHTBLUE_EX}{int_to_oct(getInt)}")
   repeatConv(input(f'\nDo you wanna continue? \nAnswer {Fore.LIGHTGREEN_EX}y(yes) {Fore.WHITE}or {Fore.LIGHTMAGENTA_EX}n(no) {Fore.RESET}or {Fore.LIGHTRED_EX}q(quit): {Fore.RESET}'))
 elif choice =='2':
   getBin=input("Enter a valid binary string: ")
   print('The binary string as integer:',f"{Fore.LIGHTBLUE_EX}{bin_to_int(getBin)}")
   print('The binary string in hex:',f"{Fore.LIGHTBLUE_EX}{bin_to_hex(getBin)}")
   print('The binary string in oct:',f"{Fore.LIGHTBLUE_EX}{bin_to_oct(getBin)}")
   repeatConv(input(f'\nDo you wanna continue? \nAnswer {Fore.LIGHTGREEN_EX}y(yes) {Fore.WHITE}or {Fore.LIGHTMAGENTA_EX}n(no) {Fore.RESET}or {Fore.LIGHTRED_EX}q(quit): {Fore.RESET}'))
 elif choice=='3':
   getHex=input("Enter a valid hex string: ")
   print("The hex string as integer:",f"{Fore.LIGHTBLUE_EX}{hex_to_int(getHex)}")
   print("The hex string in binary:",f"{Fore.LIGHTBLUE_EX}{hex_to_bin(getHex)}")
   print("The hex string in oct:",f"{Fore.LIGHTBLUE_EX}{hex_to_oct(getHex)}")
   repeatConv(input(f'\nDo you wanna continue? \nAnswer {Fore.LIGHTGREEN_EX}y(yes) {Fore.WHITE}or {Fore.LIGHTMAGENTA_EX}n(no) {Fore.RESET}or {Fore.LIGHTRED_EX}q(quit): {Fore.RESET}'))
 elif choice =='4':
    getOct=input('Enter a valid oct string: ')
    print("The hex string as integer:",f"{Fore.LIGHTBLUE_EX}{oct_to_int(getOct)}")
    print("The hex string in binary:",f"{Fore.LIGHTBLUE_EX}{oct_to_bin(getOct)}")
    print("The hex string in hex:",f"{Fore.LIGHTBLUE_EX}{oct_to_hex(getOct)}")
    repeatConv(input(f'\nDo you wanna continue? \nAnswer {Fore.LIGHTGREEN_EX}y(yes) {Fore.WHITE}or {Fore.LIGHTMAGENTA_EX}n(no) {Fore.RESET}or {Fore.LIGHTRED_EX}q(quit): {Fore.RESET}'))
 elif choice=='5' or choice=='q':
   print("Thank you for using the string converter!")
   os.system('exit')
 elif choice=='':
   print("Please select any of the options!")
   logo()
   choiceVar=info()
   main(choiceVar)
 else:
  print("Invalid choice!\nPlease choose from the given options only!") 
  time.sleep(3)
  os.system('cls')
  choiceVar=info()
  main(choiceVar)
try:
  logo()
  choice=info()
  main(choice)
except KeyboardInterrupt:
  print("\nThank you for using the string converter!")
  sys.exit()
