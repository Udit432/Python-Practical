list=['my','name','is','udit','varshney']
a=open("apple.txt","w+")
for i in list:
    a.write("%s\n" %i)
f=a.close()
print(f)
b=open("apple.txt")
print(b.read())
