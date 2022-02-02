
passwd = input('Input Password: ')
passwd = list(passwd)

for x in range(0, len(passwd)):
    uni = ord(passwd[x])
    uni += len(passwd)
    passwd[x] = chr(uni)

passwd_1 = []
passwd_2 = []

for x in range(0, len(passwd)):
    if x < len(passwd)//2:
        passwd_1.append(passwd[x])
    if x >= len(passwd)//2:
        passwd_2.append(passwd[x])

passwd_1 = passwd_1[::-1]
passwd_2 = passwd_2[::-1]

for x in range(0, len(passwd_1)):
    uni = ord(passwd_1[x])
    uni -= len(passwd_2)%(2)
    passwd_1[x] = chr(uni)

for x in range(0, len(passwd_2)):
    uni = ord(passwd_2[x])
    uni -= len(passwd_1)%(2)

    passwd_2[x] = chr(uni)

passwd = passwd_1 + passwd_2

for x in range(0, len(passwd)):
    uni = ord(passwd[x])
    uni += 10
    uni //= 2
    passwd[x] = chr(uni)

pass_str = ''
passwd = pass_str.join(passwd)
print(passwd)
