import pandas as pd

df  = pd.read_csv("student_scores_random_names.csv")

def students_sheteneili_sagnebit():
    res = (df[(df["Math"] < 50) | (df["Physics"] < 50) | (df["Chemistry"] < 50) |
                 (df["Biology"] < 50) | (df["English"] < 50)]).drop_duplicates(subset=["Student"])
    return res['Student']


def average_points_by_semester():
    result_dct={}
    subjects = ["Math", "Physics", "Chemistry","Biology", "English"]
    for subject in subjects:
        dct = {}
        for i in range(1, 9):
            avg = float((df[df["Semester"] == f"Semester {i}"][subject].mean()))
            dct[f"Semester {i}"] = round(avg, 2)
        result_dct[subject] = dct
    return result_dct


def student_with_most_avg_points():
    st = df.groupby("Student").agg({
        'Math': ['sum', 'count'],
        'Physics': ['sum', 'count'],
        'Chemistry': ['sum', 'count'],
        'Biology': ['sum', 'count'],
        'English': ['sum', 'count']
    })
    st["avg"] = st.xs("sum", axis=1, level=1).sum(axis=1) / st.xs("count", axis=1, level=1).sum(axis=1)
    students = st[st["avg"]==st["avg"].max()].index.tolist()
    return students

def hardest_subject():
    avg_points =df.mean(numeric_only=True)
    return avg_points.idxmin(), round(float(avg_points.min()),2)

def avg_points_by_semester_excel():
    data = average_points_by_semester()
    exc = pd.DataFrame(data)

    return exc.to_excel("avg_points.xlsx")

def ascending_student():
    stud = df.groupby(["Student","Semester"]).mean(numeric_only=True)
    stud["avg"] = stud.mean(axis=1)
    students = []
    for student, each in stud.groupby("Student"):
        avg_values = each["avg"].values
        if all(avg_values[i] <= avg_values[i + 1] for i in range(len(avg_values) - 1)):
            students.append(student)
    return students








