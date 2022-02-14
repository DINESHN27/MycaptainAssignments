#To print positive numbers in the given list
limit=int(input('Enter the number of elements in your list: '))
l=list()
print("Enter the List Elements")
for i in range(limit):
    l.append(int(input()))
print("The Given list is : ")
print(l)
print("Positive numbers in given list")
for k in l:
    if(k>=0):
        print(k,end=" ")
