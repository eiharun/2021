hash = '25144e154c3d4d3124124c1f3c25144e154c3d4d3124124c1f3c25144e591a1a4833094d201e6b4d286c04502331265e101e'
hash_list = list(hash)

state = []
hash_len=50
for i in range(0,hash_len):
	state.append(0)

def round():
	for i in range(0,hash_len):
		state[i]=(state[i]+state[(i+1)%hash_len])%128

def deabsorb(hash_list):
	#message_list = list(message)
	hashnew = []
	for m in hash_list:
		hashnew.append(chr(m))
	hashnew_len = len(hashnew)
	for i in range(hash_len):
		state[i]=state[i]+hashnew[i%hashnew_len]

def solver(hash):
    deabsorb(hash_list)
    round()
    


for c in range(0,hash_len):
    add_str = chr(state[c])

solver(hash)