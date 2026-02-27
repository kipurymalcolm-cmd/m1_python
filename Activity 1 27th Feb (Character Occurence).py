string=input("Please Enter Word: ")
char=input("Please Enter Character: ")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count=count+1
    i=i+1
print("The character",char,"has been repeated",count,"times")

    