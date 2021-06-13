#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
ToDoList :
1. Input multiple  hex value one time 
2. Let code can parse all the hex balue

'''


import base64
#from urllib.parse import urlparse
import binascii

def HowToUse():
	print("This is a coding / crypto Tools !!")
	print("Please choose the algorithm you want to use")
	print("Then Provide the cipher text / plain text")

def Decoder(encode_string, algo):
	if algo == 'base64': #Base64 Decode
		decodeString = base64.b64decode(encode_string)
	elif algo == 'base32': #Base32 Decode
		decodeString = base64.b32decode(encode_string)
	elif algo == 'base85': # Base85 Decode
		decodeString = base64.b85decode(encode_string)
	else:
		print('ERROR !!')
	return decodeString


def Decimal_Converter(num): # Decimal Convert
	Decimalresults = []
	Binaryresult = bin(int(num)).replace("0b", "") # Decimal to Binary
	OctalResult = oct(int(num)) # Decimal to Octal
	HexResult = hex(int(num)).replace("0x", "") # Decimal to Hex
	Decimalresults.append(Binaryresult)
	Decimalresults.append(Octalresult)
	Decimalresults.append(HexResult)
	return decimalresult


def Hex_Converter(hexdata): # Hex Converter 
	hexresult = []
	scale = 16 
	ASCIIResult = hexdata.decode("hex") # Hex to Ascii
	Binaryresult = bin(int(hexdata, scale)).zfill(8).replace("0b", "") # Hex to binary
	OctalResult = oct(int(hexdata, scale)) # hex to Octal
	DecimalResult = int(hexdata, scale) # Hec to Decimal 
	hexresult.append(ASCIIResult)
	hexresult.append(Binaryresult)
	hexresult.append(OctalResult)
	hexresult.append(DecimalResult)
	return hexresult


def Binary_Converter(binary):
	binaryresult = []
	DecimalResult = int(binary.replace('0b', '') , 2) # Bin to Decimal
	OctalResult =  oct(int(binary , 2)) # Bin to Octal
	HexResult = hex(int(binary.replace('0b', '') , 2)).replace('0x', '')
	ASCIIResult = binascii.unhexlify('%x' % int(binary , 2))
	binaryresult.append(DecimalResult)
	binaryresult.append(OctalResult)
	binaryresult.append(HexResult)
	binaryresult.append(ASCIIResult)
	return binaryresult

def String_Converter(input):
	StringResult = ''.join([hex(ord(x))[2:]for x in input])
	return StringResult


def main():
	HowToUse()
	algo = raw_input("What is the decode/decrypt Algo you want to do? ")
	if algo == "base64" or algo == "base32" or algo == "base85":
		encode_string = str(raw_input("What's the encode string ? " ))
		result = Decoder(encode_string, algo)
	elif algo == "Hex" or algo == "hex":
		hexvalue = raw_input("What's the Hex value ?")
		result = Hex_Converter(hexvalue)
	elif algo == "Bin" or algo == "bin" :
		binary = raw_input("What's the binary value ?")
		result = Binary_Converter(binary)
	elif algo == "Decimal" or algo == "decimal":
		decimal = raw_input("What's the decimal value ? ")
		result = Decimal_Converter(decimal)
	elif algo == "String" or algo == "string":
		string = raw_input("What's the string value ? ")
		result = String_Converter(string)
	print result 

if __name__ == '__main__':
	main()