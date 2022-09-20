from Student import  Student  # importa a classe Student que foi criada
# Com as classes pode se criar tipos de dados novos
# como nesse exemplo essa classe representa tipo de
# dados de uma aluno, com as classes podemos criar
# varios tipos de dados para representar objetos

student1 = Student("Jim", "Business",3.1, False)
student2 = Student("Eder", "Business",5.1, False)

print(student1.gpa)
print(student2.gpa)