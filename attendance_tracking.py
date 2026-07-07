attendance = {}

def mark_attendance():
student_id = input("Student ID: ")

status = input("Present or Absent (P/A): ").upper()

if status == "P":
attendance[student_id] = "Present"

else:
attendance[student_id] = "Absent"

print("Attendance recorded.\n")

def show_attendance():
print("\nAttendance List")

if not attendance:
print("No attendance records.\n")
return

for student_id, status in attendance.items():
print(f"{student_id} : {status}")

print()

if name == "main":
while True:

print("1. Mark Attendance")
print("2. Show Attendance")
print("3. Exit")

choice = input("Choose: ")

if choice == "1":
mark_attendance()

elif choice == "2":
show_attendance()

elif choice == "3":
break

else:
print("Invalid choice.\n")