attendance = {
    "1001": "Present",
    "1002": "Absent",
    "1003": "Present",
    "1004": "Present"
}


def attendance_report():
    total = len(attendance)

    present = list(attendance.values()).count("Present")

    absent = list(attendance.values()).count("Absent")

    print("\nAttendance Report")
    print("----------------------")
    print(f"Total Students : {total}")
    print(f"Present        : {present}")
    print(f"Absent         : {absent}")

    percentage = (present / total) * 100

    print(f"Attendance Rate: {percentage:.2f}%\n")


if __name__ == "__main__":
    attendance_report()