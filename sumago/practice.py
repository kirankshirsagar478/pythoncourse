# for i in range(1,51):
#     print(i)

# for i in range(2,51,2):
#     print(i)

# for i in range(1,51):
#     if i%2==0:
#         print(i)

# student name and roll no input
# 4 sub marks input
# less than 35 in any one subject then fail
# total percentages display

name=input("Enter name of the student:")
rollno=int(input("Enter roll no:"))
sub1=int(input("Enter subject 1 marks:"))
sub2=int(input("Enter subject 2 marks:"))
sub3=int(input("Enter subject 3 marks:"))
sub4=int(input("Enter subject 4 marks:"))
print("Name:"+name)
print("Roll:"+str(rollno))
if sub1<35 or sub2<35 or sub3<35 or sub4:
    print("Result:Fail")
else:
    print("Result:Pass")
totalper= (sub1+sub2+sub3+sub4)/4
print("Total percentage",totalper)


