#STRINGS

#Question 1
str=input("Enter a string\n")
print(str.upper())

#Question 2
y=input("Enter a string\n")
c=0;
for i in range(len(y)):
    if y.isdigit():
       c=1;
    else:
        c=0;
        break;
if c==1:
    print("True")
else:
    print("False")

#Question 3
stt="Hello World"
print(stt)
print(stt.replace("World","Puneet"))

