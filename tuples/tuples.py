#TUPLES

#Question 1
list=[]
n = int(input("Enter number of elements you want in tuple\n"))
print("Enter integer elements")
for i in range(n):
    a=int(input())
    list.append(a)
tup=tuple(list)
print("Tuple is : " , tup)
rev=reversed(tup)
print("Reversed tuple is : " , tuple(rev))

#Question 2
con=[]
n = int(input("Enter the number of elements you want in tuple\n"))
print("Enter integer elements")
for i in range(n):
    a=int(input())
    con.append(a)
tupp=tuple(con)
print("The largest and smallest elements are " , max(tupp) , " and " , min(tupp) , "respectively")

