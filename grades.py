import csv

def calculate_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'

def read_data(filename):
    students = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            marks = list(map(int, [row['Math'], row['Science'], row['English']]))
            total = sum(marks)
            avg = round(total / len(marks), 2)
            grade = calculate_grade(avg)
            students.append({
                'Name': name,
                'Total': total,
                'Average': avg,
                'Grade': grade
            })
    return students

def show_report(students):
    print("\nStudent Performance Report\n")
    print("{:<10} {:<10} {:<10} {:<6}".format("Name", "Total", "Average", "Grade"))
    for student in students:
        print("{:<10} {:<10} {:<10} {:<6}".format(
            student['Name'], student['Total'], student['Average'], student['Grade']
        ))

    top_student = max(students, key=lambda x: x['Average'])
    print(f"\n🏆 Top Scorer: {top_student['Name']} with Average {top_student['Average']}")

def main():
    filename = "students.csv"
    students = read_data(filename)
    show_report(students)

if __name__ == "__main__":
    main()
