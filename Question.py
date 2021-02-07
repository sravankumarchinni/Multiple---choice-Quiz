class Question:
    
    prompt=[]
    options=[]
    answers=[]
    topic_name=[]
    difficulty_level=[]

    def __init__(self,prompt=[],options=[],answer=[],topic_name=[],difficulty_level=[]):
        self.prompt=prompt
        self.options=options
        self.answer=answer
        self.topic_name=topic_name
        self.difficulty_level=difficulty_level
        
    
    def _addQuestion(self,topic_name,difficulty_level):

        statement=input("Enter question statement: ")
        self.prompt.append(statement)
        Question.prompt.append(statement)
        self.topic_name.append(topic_name)
        Question.topic_name.append(topic_name)
        self.difficulty_level.append(difficulty_level)
        Question.difficulty_level.append(difficulty_level)

        l1=[]
        for i in range(4):
            l1.append(input("Enter option no. "+str((i+1))+": "))
        self.options.append(l1)
        Question.options.append(l1)

        ans=input("Which is the correct option (1/2/3/4) ? ")
        self.answer.append(int(ans))
        Question.answers.append(int(ans))
        
        
    def _displayAllQuestions(self):
        
        print("Total number of questions are: ",len(self.prompt))
        print("\n")
        for i in range(len(self.prompt)):
            print("Ques. "+str(i+1)+self.prompt[i])
            for j in range(len(self.options[i])):
                print(str(j+1)+")"+str(self.options[i][j]))
            print("\n\n")
            
            
    def viewTopics(self):
        a=set(Question.topic_name)
        print(a)


    @classmethod
    def run_test(cls):

        score=0

        for statement in range(len(cls.prompt)):
            
            print("Topic: "+cls.topic_name[statement])
            print(cls.prompt[statement])
            
            for i in range(len(cls.options[statement])):
                print(str(i+1)+")"+str(cls.options[statement][i]))
                
            print("Question level: ",cls.difficulty_level[statement])
            
            answer=int(input("Enter option number as answer: "))
            print("\n")

            if answer==cls.answers[statement]:
                score+=1
        print("\n")
        print("You got",str(score),"/",str(len(cls.prompt)),"correct.")

        