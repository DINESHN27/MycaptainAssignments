#TO FIND THE EXTENSION OF THE FILE
Filename=str(input("Enter your Filename: "))
for i in range(len(Filename)):
    if Filename[i] == '.':
        Extension = Filename[i+1:len(Filename)]
if(Extension == "py"):
    print("The Extension of the file is: 'Python'")
elif(Extension == "txt"):
    print("The Extension of the file is: 'text'")
elif(Extension == "pdf"):
    print("The Extension of the file is: 'Pdf'")
elif (Extension == "c"):
    print("The Extension of the file is: 'C'")
elif(Extension == "mp4"):
    print("The Extension of the file is: 'Video'")
elif(Extension == "mp3"):
    print("The Extension of the file is: 'Audio'")
elif(Extension == "jpg"):
    print("The Extension of the file is: 'image'")
elif(Extension == "html"):
     print("The Extension of the file is: 'html'")
else:
    print("Please, Give the valid file name")










