a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" dell empty symbols
#--------------------------------------------------------------
a = "Hello, World!"
print(a.replace("o", "J")) #change o on J. output "HellJ, WJrld!"
#--------------------------------------------------------------
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 





age = 36
txt = "My name is John,\n and I am {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


'''
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace	
\f	Form Feed	
\ooo	Octal value	
\xhh	Hex value
'''