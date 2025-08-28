marks = int(input("Enter the marks between (1-100): "))
attendance = int(input("Enter the attendance (%): "))

if attendance < 50:
    print("Not eligible for exam due to attendance < 50")
    exit()
elif attendance < 75:
    print("Warning. Low attendance")
else:
    print("No Warning")

if marks >= 90:
    print("Grade = A")
elif marks >= 80:
    print("Grade = B")
elif marks >= 70:
    print("Grade = C")
elif marks >= 60:
    print("Grade = D")
else:
    print("Fail")
