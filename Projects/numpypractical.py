# Concept : Analyze exam scores for multiple students using NumPy arrays.   
# Generate random Marks for 20 students across 5 subjects.
import numpy as np
# Step 1: Data Set Creation
marks_data = np.random.randint(0, 101, size=(20, 5))
print("\nMarks Data:\n", marks_data)
# Step 2: Total Marks of Each Student
total_marks = np.sum(marks_data, axis=1)
print("\nTotal Marks per Student:", total_marks)
# Step 3: Average Marks per Subject
average_subject_marks = np.mean(marks_data, axis=0)
print("\nAverage Marks per Subject:", average_subject_marks)
# Step 4: Increase Marks by 5%
increased_marks = marks_data * 1.05
print("\nMarks After 5% Increase:\n", increased_marks)
# Step 5: Data Manipulation
first_ten_students = marks_data[:10, :]
print("\nMarks Data for First Ten Students:\n", first_ten_students)
# Step 6: Students with Total Marks > 400
high_achievers = total_marks > 400
print("\nHigh Achievers (Total Marks > 400):", np.where(high_achievers)[0])
# Step 7: Statistical Analysis
mean_marks = np.mean(marks_data)
median_marks = np.median(marks_data)
std_dev_marks = np.std(marks_data)
print("\nOverall Mean Marks:", mean_marks)
print("Overall Median Marks:", median_marks)
print("Overall Standard Deviation of Marks:", std_dev_marks)
# Step 8: Identify Student with Highest Marks in a Subject
max_subject_marks = np.max(marks_data, axis=0)
print("\nHighest Marks in Each Subject:", max_subject_marks)
best_student_subject = np.argmax(max_subject_marks)
print("Student with Highest Marks in a Subject: Student", best_student_subject)
