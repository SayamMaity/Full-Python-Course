#code with harry code

sub1 = int(input ("Enter first subject marks\n"))
sub2 = int(input ("Enter second subject marks\n"))
sub3 = int(input ("Enter third subject marks\n"))
if(sub1<=35 or sub2<=35 or sub3<=35):
    print("You are fail because you have less than 35% in one of the subjects")
elif (((sub1+sub2+sub3)/3)<40):
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations1 You have passed the exam with marks",((sub1+sub2+sub3)/3))


# # my code

# marks_1=int(input("enter marks_1 "))
# marks_2=int(input("enter marks_2 "))
# marks_3=int(input("enter marks_3 "))
# total=(marks_1+marks_2+marks_3)/3
# print(total)
# if(marks_1>=35 and marks_2>=35 and marks_3>=35 and total>=40):
#     print("pass")
# else:
#     print("fail")