try:
    a=5
    b=0
    print(a/b)
except ZeroDivisionError:
    print("error")
except NameError:
    print("name error")
else:
    print("else")
finally:
    print("finally")
print("End of code")