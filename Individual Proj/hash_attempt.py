#using https://www.herevego.com/hashing-python/ as 'tutorial'

message = 'hello world'
#create hashing table


#item = chr(message)

def r_method():#Fix
    '''Remainder Method. However clashing occurs'''
    h_table = [None]*12
    for h in message:
        hash = ord(h) % len(h_table)
        h_table[hash] = ord(h) 
        return h_table

def f_method():
    '''Folding Method. Limitations Same as Remainder Method'''
    h_table = [None]*12
    msg_l = []
    #msg_int = 0
    msg_o = ''
    
    for i, h in enumerate(message):
        try:
            msg_l.append(ord(message[i]) + ord(message[i+1]))
        except:
            msg_l.append(ord(message[i]))
        msg_o += str(ord(h))
    total_h = 0
    for x in msg_l:
        total_h += x
    hsh = total_h % len(h_table)
    h_table[hsh] = msg_o
    return h_table

print(r_method())
print(f_method())