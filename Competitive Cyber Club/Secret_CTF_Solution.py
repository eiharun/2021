#I'm not original owner, used this program to create 
#the Badhash_Solution code and solve a practice ctf challenge.
pass_crypt =  'deA?%@JDQE%#AIJDE\x1e%#<E' #String to Decode
pass_crypt = list(pass_crypt) #Convert into a list


for x in range(0, len(pass_crypt)): #Decryption
    val = ord(pass_crypt[x]) #Converts into unicode
    val = val + 10 #Adds 10 to unicode value
    pass_crypt[x] = chr(val) #Converts into Ascii

pass_crypt = pass_crypt[::-1] #Reverses String

for x in range(0, len(pass_crypt)): #Decryption
    val = ord(pass_crypt[x]) #Converts into unicode
    val = val - 5 #Subtracts 5 to unicode value
    pass_crypt[x] = chr(val) #Converts int Ascii

str = ''
print(str.join(pass_crypt)) #Convert 'String' list back into a String
print('masoncc' + '{' + '{}'.format(str.join(pass_crypt)) + '}') #Print out full password
