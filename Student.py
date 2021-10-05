#print(average_grade(student))

def average_grade_all_students(student_list):
  total = 0
  count = 0
  for student in student_list:
    total += sum(student["grades"])
    count += len(student["grades"])

  return total/count

print(average_grade_all_students(students))