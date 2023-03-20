class QuizBrain():
    def __init__(self, Question_list):
        self.question_num=0
        self.question_list=Question_list
        self.compteur=0
        
    def still_has_question(self):
        return(self.question_num<len(self.question_list))

    def next_question(self,):
        num=self.question_num
        ok=-1
        while ok==-1:
            reponse=input("Q."+str(num)+": "+self.question_list[num].question+" True/False ???")
            ok=0
            if reponse==self.question_list[num].answer:
                self.compteur+=1
                
            elif reponse not in ["True","False"]:
                print("no an answer")
                ok=-1
            
                
        self.question_num+=1
        