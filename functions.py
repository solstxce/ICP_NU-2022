def bin_to_int(number):
    sum=0
    numStr=str(number)
    for q in range(0,len(numStr)):
        noDigits=len(numStr)
        reqPower=noDigits-q-1
        sum=(sum)+int(numStr[q])*2**int(reqPower)
    return sum
def hex_to_int(number):
    sum=0
    numStr=str(number)
    for q in range(len(numStr)):
        noDigits=len(numStr)
        reqPower=noDigits-q-1
        sum=sum+int(numStr[q])*16**int(reqPower)
    return sum
def int_to_bin(number):
    #int to binary
    b=[]
    while(number>0):
        d=number%2
        b.append(str(d))
        number=number//2
    b.reverse()
    sum=''.join(b)
    return sum 
def int_to_hex(number):
    remGen=[]
    sum=0
    temp=number
    while temp!=0:
        rem=int(temp%16)
        temp=int(temp//16)
        if rem>=10:
            rem=rem%10
            alpList='abcdefghi'
            rem=alpList[rem]
            remGen.append(str(rem))
        else:
            remGen.append(str(rem))
    sum=''.join(remGen[::-1])
    return sum
def bin_to_hex(number):
    mainNum=bin_to_int(number)
    sum=int_to_hex(mainNum)
    return sum
def oct_to_int(number):
    number=int(number)
    temp=number
    i=0
    j=0
    sum=0
    while temp!=0:
        rem= temp%10
        if rem>7:
            j=j+1
            if j>0:
                print("invalid number")
                break
        elif rem<8:
            sum+=rem*8**i
            i+=1
            temp=int(temp/10)
    if j>0:
        print("invalid number")
    else:
        return sum
def int_to_oct(number):#first we input a number
    temp=number #we store our integer in a variable counter as n is constant
    i=1 # i stands for the place value
    sum=0 # final octal number
    while temp!=0: #the calculation will continue untill the quotient becomes zero
        rem=int(temp%8) # we find out the remainder in integer
        sum=sum+i*rem   # sum is counter for the octal number
        i=i*10  # i is multiplied by 10 to get the next place value
        temp=temp//8 # this gives the next value of quotient
    return sum
def bin_to_oct(number):
    mainNum=bin_to_int(number)
    sum=int_to_oct(mainNum)
    return sum
def oct_to_bin(number):
    mainNum=oct_to_int(number)
    sum=int_to_bin(mainNum)
    return sum
def oct_to_hex(number):
    mainNum=oct_to_int(number)
    sum=int_to_hex(mainNum)
    return sum
def hex_to_bin(number):
    mainNum=hex_to_int(number)
    sum=int_to_bin(mainNum)
    return sum
def hex_to_oct(number):
    mainNum=hex_to_int(number)
    sum=int_to_oct(mainNum)
    return sum
