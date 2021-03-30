from random import choices, shuffle

capital = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '{', '}', '|', '\\', '/', '^', '+', '=', '_', '-', ',']

def verify(plen):
    num = int(input("\nNumber of digits in the password:"))
    if num > plen: return []
    upp = int(input("\nNumber of uppercase letters in the password:"))
    if (num + upp) > plen: return []
    low = int(input("\nNumber of lowercase letters in the password:"))
    if (num + upp + low) > plen: return []
    spec = int(input("\nNumber of special characters in the password:"))
    if (num + upp + low + spec) > plen: return []
    return [num, upp, low, spec]    

plen = int(input("Enter the desired length of the password:"))

print("\nEnter the following requirements:\n")
k = verify(plen)
while len(k) == 0:
    print("\nInvalid details! Enter the details again!\n")
    k = verify(plen)

content = k
pswd = []

if content[0]!=0:
    pswd += list(choices(digits,k=content[0]))
if content[1]!=0:
    pswd += list(choices(capital,k=content[1]))   
if content[2]!=0:
    pswd += list(choices(small,k=content[2]))
if content[3]!=0:
    pswd += list(choices(symbol,k=content[3]))

shuffle(pswd)

password = ''.join(pswd)
print("\nGenerated password:"+password+"\nThank you!")
