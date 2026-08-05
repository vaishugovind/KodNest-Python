# Read marks, attendance and project completion status
student_marks = int(input())
attendance_percentage = int(input())
project_status = input()

# Combine marks and attendance using 'and'
if student_marks >= 60 and attendance_percentage >= 75:
    # Nested if statement to check project completion
    if project_status == "yes":
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
