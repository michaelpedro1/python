student=[
    {'id' :1, 'name' : 'alice', 'grade' :7, 'subject':'maths'},
    {'id':2, 'name' : 'bob', 'grade':8, 'subject': 'science'},
    {'id':3, 'name' : 'charlie','grade':9, 'subject':'history'},
    {'id':2, 'name' : 'bob', 'grade':8, 'subject': 'science'}
]

def get_unique_students(students_list):
    unique_entries=[]
    seen_entries=set()

    for student in students_list:
        student_tuple=tuple(student.items())


        if student_tuple not in seen_entries:
          seen_entries.add(student_tuple)
          unique_entries.append(student)
    return unique_entries

unique_student=get_unique_students(student)
for studets in  unique_student:
   print(student)      
