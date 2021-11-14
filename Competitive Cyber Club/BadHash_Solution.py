hash = '25144e154c3d4d3124124c1f3c25144e154c3d4d3124124c1f3c25144e591a1a4833094d201e6b4d286c04502331265e101e'
#25144e154c3d4d3124124c1f3c
#25144e154c3d4d3124124c1f3c
#25144e591a1a4833094d201e6b4d286c04502331265e101e
message = ''
state = []
hash_len=50
for i in range(0,hash_len):
	state.append(0)
def round():
	for i in range(0,hash_len):
		state[i]=(state[i]+state[(i+1)%hash_len])%128
for i in range(0,21):
	round()

def absorb(hashh):
	hash_list = list(hashh)
	hash_list_ints = []
	for m in hash_list:
		hash_list_ints.append(chr(m))
	message_len = len(hash_list_ints)
	for i in range(hash_len):
		state[i]=state[i]+hash_list_ints[i%message_len]

absorb(hash)#hash instead of message
def absorb(message):
	message_list = list(message)
	message_list_ints = []
	for m in message_list:
		message_list_ints.append(ord(m))
	message_len = len(message_list_ints)
	for i in range(hash_len):
		state[i]=state[i]+message_list_ints[i%message_len]
print(state)
hash_string = ''

for c in range(0,hash_len):
	add_str = hex(state[c])[2:]
	if len(add_str) < 2:
		add_str="0"+add_str
	print(add_str)
	#hash_string-=add_str



