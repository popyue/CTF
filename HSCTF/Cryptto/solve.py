encode_str = "IOWJLQMAGH"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decode = ""
for character in encode_str:
	decode+=letters[(letters.index(character)-18)%26] #encode each character
print(decode)