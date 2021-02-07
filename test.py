from User import Examiner,Candidate

e1=Examiner("sravan",2)
print(e1)
e1.addQuestion("General Knowledge","easy")
e1.addQuestion("General Knowledge","easy")
e1.addQuestion("Python","medium")
e1.displayAllQuestions()

c1=Candidate("Surya",16)
print(c1)
c1.viewTopics()
c1.run_test()
