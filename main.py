
#xor the chunks of the following binary number into an 8-bit hash

b1 = [1,1,1,1,0,0,0,0]
b2 = [0,1,0,1,0,1,0,1]
b3 = [0,1,0,1,1,0,0,1]


#XOR if A is 1 and B is 0 return 1, if a is 0 and b is 1 return 1
xor = lambda  a, b: 1 if ((a == 1 & b == 0)||(a == 0 & b == 1)) else 0

#map takes list + applies function
map(xor, b1, b2)

#b2 = result of b1 and b2 XOR
b2 = map(xor, b1, b2)

print(list, b2)

b3= map(xor, b2, b3)

print(list, b3)