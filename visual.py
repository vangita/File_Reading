import matplotlib.pyplot as plt
import numpy as np
from csv_reader import average_points_by_semester, df

def bar_diagram():
    data = average_points_by_semester()

    subjects = data.keys()
    semesters = list(next(iter(data.values())).keys())
    values = {subject: [data[subject][sem] for sem in semesters] for subject in subjects}

    bar_width = 0.1
    index = np.arange(len(semesters))

    plt.figure(figsize=(10, 6))
    for i, subject in enumerate(subjects):
        plt.bar(index + i * bar_width, values[subject], bar_width, label=subject)

    plt.xlabel("Semesters")
    plt.ylabel("Grades")
    plt.title("Grades by Subject and Semester")
    plt.xticks(index + bar_width, semesters)
    plt.legend(title="Subjects")
    plt.show()
bar_diagram()
def line_diagram():
    stud = df.groupby("Semester").agg({
        'Math': ['sum', 'count'],
        'Physics': ['sum', 'count'],
        'Chemistry': ['sum', 'count'],
        'Biology': ['sum', 'count'],
        'English': ['sum', 'count']
    })

    stud['avg'] = stud.xs('sum', axis=1, level=1).sum(axis=1) / stud.xs('count', axis=1, level=1).sum(axis=1)
    plt.figure(figsize=(10, 6))
    plt.plot(stud["avg"].index, stud["avg"], label="average score")
    plt.title("Average points by semester")
    plt.xlabel("Semester")
    plt.ylabel("Average Score")
    plt.legend()
    plt.show()

line_diagram()


