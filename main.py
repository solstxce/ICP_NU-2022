from functions import *
import os
def info():
  print(""" Select the type of input you wanna give:
    [1] Integer
    [2] Binary
    [3] Hex
    [4] Oct
    [5] Select this to exit the program.
     """)
  choice = int(input("[?]: "))
  return choice
choice=info()
if choice == 1:
  getInt=int(input("Enter a valid number: "))
  print('The number in binary format:',int_to_bin(getInt))
  print('The number in hex format: ',int_to_hex(getInt))
  print('The number in oct format: ', int_to_oct(getInt))
elif choice ==2:
  getBin=input("Enter a valid binary string: ")
  print('The binary string as integer:',bin_to_int(getBin))
  print('The binary string in hex:',bin_to_hex(getBin))
  print('The binary string in oct:',bin_to_oct(getBin))
elif choice==3:
  getHex=input("Enter a valid hex string: ")
  print("The hex string as integer:",hex_to_int(getHex))
  print("The hex string in binary:",hex_to_bin(getHex))
  print("The hex string in oct:",hex_to_oct(getHex))
elif choice==5:
  print("Thank you for using the string converter!")
  os.system('exit')
else:
      #This part is not yet done!
      print("Invalid choice!\nPlease choose from the above options only!")
      os.system('cls')
      info()
