#Counting the character present in the Given string

str1 = str(input("Enter the String : "))
d = dict()
l = list()
for i in str1:
    d[i] = str1.count(i)
for i in range(len(d)):
    max1 = max(d,key=d.get)
    max2 = max(d.values())
    print("{} = {}".format(max1,max2))
    d.pop(max1)











