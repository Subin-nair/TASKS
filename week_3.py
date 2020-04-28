print('hello world!')

#to include single qoutes or double quotes in the string add backslash before it
print('Brian\'s mother: He\'s not the Messiah. He\'s a very naughty boy!')
 
print(1 + 1)

# print new line
print("Hello\nWorld!")

#getting input
#input("Enter something please: ")

#adding the string
print("First string" + ", " + "second string")

print("2" + "2")
print('2' + "2")

print("spam" * 5)

#type conversion. convert the types example integer and float
print(int("25"))
print(float("25"))

this_is_a_normal_name = 7
print(this_is_a_normal_name)

"""xy = 256
del xy
print(xy)"""

#length of a string
a = "Hello"
print(len(a))


#removes spaces in the beginning and end
a = "                          Hello, World!                         "
print(a.strip()) # returns "Hello, World!"


#check string
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)
y = "z" not in txt
print(y)

a = "Hello"
b = "World"
c = a + b
print(c)

#add space in between
c = a + " " + b
print(c)

age = "36"
txt = "My name is John, I am " + age
print(txt)

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

qty = 2
number = 35
price = 25
x = "I need {} pencils with number {} for {} dollars"
print(x.format(qty,number,price))

#new and return
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 


txt = "     banana     "
x = txt.strip()
print("of all fruits",x,"is my favorite")
print("whats","up")
# comma and plus symbol in the print determines the space between the string (not sure)

#lowercase and casefold
txt = "Hello my FRIENDSnnknknnkJKHJHUTUHJKJJ  mmmmmHHIJKJK"
x = txt.lower()
print(x)
x = txt.casefold()
print(x)

a = 25
b = 23
if a == b:
    print("a is equal to be")
elif b == b-a:
    print("yoho")
else:
    print("abstract")

i = 20
while i>2:
    print(i)
    i -= 1

""" MULTIPLES OF 5 TILL 50"""

i = 1
while i < 50:
    if(i%5==0):
        print(i)
    i=i+1

for x in range(1,50):
  if(x%5==0):
   print(x)

for x in range(0,50,5):
    if(x>0):
     print(x)