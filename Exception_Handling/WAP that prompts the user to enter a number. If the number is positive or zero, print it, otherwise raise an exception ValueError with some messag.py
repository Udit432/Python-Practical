try:
    n=int(input("enter the value:"))
    if n>=0:
        print(n,"no error is there")
except ValueError:
        raise ValueError()
print("value error is present")
