def int_to_hex(number):
    convHex=hex(number)
    return convHex
def int_to_oct(number):
    convOct=oct(number)
    return convOct
def int_to_bin(number):
    convBin=format(number,"b")
    return convBin
def hex_to_int(number):
    int_str=str(number)
    #Here we are converting number to string because, the int() function throws an error: int() can't convert non-string with explicit base.
    convIntHex=int(int_str,16)
    return convIntHex
def hex_to_bin(number):
    int_str=str(number)
    #Here 0 before ':' means starting from 0 and 08 means to a string with 8 digits and zeroes padded b means in binary representation. Format changes the string according to the instructions given.
    convBinHex="{0:08b}".format(int(int_str, 16))
    return convBinHex
def hex_to_oct(number):
    int_str=str(number)
    convOctHex=oct(int(int_str, 16))
    return convOctHex
def bin_to_int(number):
    int_str=str(number)
    convIntBin=int(int_str,2)
    return convIntBin
def bin_to_hex(number):
    int_str=str(number)
    num=int(int_str,2)
    convHexBin=hex(num)
    return convHexBin
def bin_to_oct(number):
    int_str=str(number)
    num=int(int_str,2)
    convOctBin=oct(num)
    return convOctBin
