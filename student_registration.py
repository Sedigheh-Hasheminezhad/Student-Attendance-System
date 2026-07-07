class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


students = []


def register_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    student = Student(student_id, name)
    students.append(student)

    print("\nStudent registered successfully.\n")


def display_students():
    print("\nRegistered Students")

    if not students:
        print("No students registered.\n")
        return

    for student in students:
        print(f"ID: {student.student_id} | Name: {student.name}")

    print()


if __name__ == "__main__":
    while True:
        print("1. Register Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            break

        else:
            print("Invalid choice.\n")