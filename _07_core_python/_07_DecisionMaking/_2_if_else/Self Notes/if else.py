workingdays = int(input("no. of working days"))
absence = int(input("no. of absent days"))
if workingdays <= 0:
    print("invalid data")
else:
    attendence_percentage = ((workingdays-absence)/workingdays)*100
    print("attendence_percentage",attendence_percentage)
    if attendence_percentage > 75:
        print("student allows to exams")
    else:
        print("not allowed")
