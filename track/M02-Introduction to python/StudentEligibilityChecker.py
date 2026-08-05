
# Check the academic requirements
Marks=int(input("Enter marks :"))
Attendence=int(input("Enter Attendence :"))
project =input("do you have project (yes/no):").strip()
if (Marks >=60) and (Attendence >=75):
    if project == "yes" :
       print("Eligible\n")
    else:
        print("Not Eligible\n")
else :
    print("Not Eligible\n")
