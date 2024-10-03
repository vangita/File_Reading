# Student Performance Analysis and Visualization

## Overview
This project analyzes student performance across multiple subjects and semesters using data from a CSV file. It provides functionality to:
- Identify students who have failed in any subject.
- Calculate average scores by semester and subject.
- Find students with the highest average points.
- Identify the hardest subject based on average scores.
- List students who have consistently improved their scores across semesters.
- Generate visualizations (bar and line diagrams) to represent student performance data.

Additionally, an Excel file is generated that contains the average scores by semester for all subjects.

## Features
- **Identify Failing Students:** Lists students who have scores below 50 in any subject.
- **Average Scores by Semester:** Calculates and displays the average score for each subject across all semesters.
- **Top Scoring Students:** Identifies students with the highest overall average score.
- **Hardest Subject:** Finds the subject with the lowest average score across all students.
- **Ascending Students:** Lists students whose scores consistently improved across semesters.
- **Generate Visualizations:** Bar and line charts are generated to visualize the performance data.
- **Excel Report:** An Excel file with the average scores by semester is generated.

## Project Structure
├── student_scores_random_names.csv\
├── csv_reader.py\
├── diagrams.py\
├── main.py\
├── avg_points.xlsx\
└── README.md

## Requirements
- `pandas`
- `matplotlib`
- `numpy`

## Results
- **Failing Students**
- **Average Points by Semester**
- **Top Scoring Students**
- **Hardest Subject**
- **Ascending Students**

## Visualizations
- Bar and line charts showing grades by subject and semester.

## License
Available under the MIT License.


