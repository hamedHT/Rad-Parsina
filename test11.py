print('&&&&&&&&&&&&')
print('*'*8)
print('5+5')


# def debugger(a, b):

# 	# adding a breakpoint()
# 	breakpoint()
# 	result = a / b
# 	return result

# print(debugger(5, 0))


for i in range(6):
	print('*'*i)
	
f = open('test2.txt','w')
b = 1
f.write(str(b))
f.write('Hello')
f.write('This is a \n')
f.write('Test!\n')
f.write('Now, this is the last line\n')
f.close()
f = open('test2.txt','r')
str = f.read()
print(str)

