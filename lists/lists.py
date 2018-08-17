#Question 1
list=[]
n=int(input("Enter how much integers you want in list\n"))
print("Enter elements")
for i in range(n):
    a=int(input())
    list.append(a)
print(list)

#Question 2
list2=['google','apple','facebook','microsoft','tesla']
list.extend(list2)
print(list)

#Question 3
list3=[1,1,2,3,4,3,4,5,3,2,3,3]
print(list3.count(3))

#Question 4
list4=[20,11,13,7,8,100,45,23]
list4.sort()
print(list4)

#Question 5
l1=[1,10,2,6,8]
print("list 1 is: ",l1)
l2=[31,24,3,5,21,32]
print("list 2 is: ",l2)
l1.sort()
l2.sort()
print("sorted list1 is: ",l1)
print("sorted list2 is: ",l2)
l1.extend(l2)
print("merged is: ",l1)
l1.sort()
print("sorted merged list is: ",l1)

#Question 6
countEve=0
countOdd=0
for i in l1:
    if(i%2==0):
        countEve+=1
    else:
        countOdd+=1
print("Odd count: " , countOdd)
print("Even count: ",countEve)
