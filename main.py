from school import School
from person import Student,Teacher
from subject import subject
from classroom import Classroom

school=School('ABC','DHAKA')
eight=Classroom('Eight')
nine=Classroom('Nine')
ten=Classroom('Ten')

school.add_classrooms(eight)
school.add_classrooms(nine)
school.add_classrooms(ten)

#adding student
rahim=Student("Rahim",eight)
karim=Student("Karim",eight)
jamal=Student("jamal",nine)
kamal=Student("kamal",ten)


school.student_admission(rahim)
school.student_admission(karim)
school.student_admission(jamal)
school.student_admission(kamal)

#add teacher
Abul=Teacher("Abul khan")
bbul=Teacher("bbul khan")                                                                       
kbul=Teacher("kbul khan")

#adding subject
bangla=subject('Bangla',Abul)
english=subject('English',bbul)
math=subject('Math',kbul)

eight.add_subject(bangla)
eight.add_subject(english)
eight.add_subject(math)
nine.add_subject(english)
nine.add_subject(math)
nine.add_subject(bangla)
ten.add_subject(math)
ten.add_subject(english)
ten.add_subject(bangla)

eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()
print(school)