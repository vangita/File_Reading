from csv_reader import (
    students_sheteneili_sagnebit,
    average_points_by_semester,
    student_with_most_avg_points,
    hardest_subject,
    avg_points_by_semester_excel,
    ascending_student
)
from visual import bar_diagram, line_diagram


def main():
    print("Students who failed any subject:")
    print(students_sheteneili_sagnebit())

    print("\nAverage points by semester:")
    avg_points = average_points_by_semester()
    for subject, data in avg_points.items():
        print(f"\n{subject}:")
        for semester, avg in data.items():
            print(f"{semester}: {avg}")

    print("\nStudent(s) with the most average points:")
    print(student_with_most_avg_points())

    print("\nHardest subject based on average points:")
    subject, avg = hardest_subject()
    print(f"{subject}: {avg}")

    print("\nGenerating Excel file for average points by semester...")
    avg_points_by_semester_excel()
    print("Excel file generated: avg_points.xlsx")

    print("\nStudents with ascending scores across semesters:")
    good_students = ascending_student()
    for i in good_students:
        print(i)

    print("\nGenerating bar diagram for average points by semester and subject...")
    bar_diagram()
    print("Bar diagram displayed.")

    print("\nGenerating line diagram for average points by semester...")
    line_diagram()
    print("Line diagram displayed.")


if __name__ == "__main__":
    main()



