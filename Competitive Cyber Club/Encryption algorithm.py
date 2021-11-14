import random
import binascii

message = 'hello world mr beast'
#input('Input Message to be encrypted: ')

def msg_to_bin(msg):
    l=[]
    b=[]
    for x in msg:
        l.append(ord(x))
    for x in l:
        b.append(str(bin(x)[2:]))
    bs = ''.join(b)
    return bs

def text_from_bits(bits):
    bits = "0" + bits[2:]
    msg = ""
    while bits != "":
        i = chr(int(bits[:8], 2))
        msg = msg + i
        bits = bits[8:]
    return msg

mks = msg_to_bin(message)
mkr = random.randrange(len(mks)//2, len(mks)*2)
mki = int(mks) + mkr
mkb = bin(mki)

key = text_from_bits(str(mkb))
print(key, '\n', mkr)