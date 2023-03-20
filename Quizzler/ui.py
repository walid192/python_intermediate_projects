from tkinter import *
from quiz_brain import *
THEME_COLOR = "#375362"
FONT_NAME = "Courier"
SCORE=0

class Quizinterface():
    def __init__(self,quiz: QuizBrain):
        self.quiz=quiz
        self.window=Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)
        self.score_label=Label(text=f"score : 0",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        
        
        self.question_canvas=Canvas(width=300,height=250,bg="white",highlightthickness=0)
        self.question=self.question_canvas.create_text(150,125,text="here is the question",width=280,font=("arial",20,"italic"))
        self.question_canvas.grid(row=1,column=0,columnspan=2,pady=50)
        
        right_image=PhotoImage(file="Quizzler/images/true.png")
        self.true_button=Button(image=right_image,highlightthickness=0,command=self.true_pressed)
        self.true_button.grid(row=2,column=1)
        
        false_image=PhotoImage(file="Quizzler/images/false.png")
        self.false_button=Button(image=false_image,highlightthickness=0,command=self.false_pressed)
        self.false_button.grid(row=2,column=0)
        
        self.get_nextquestion()
        
        self.window.mainloop()
        
    def get_nextquestion(self):
        self.question_canvas.config(bg="white")
        
        if self.quiz.still_has_questions():
            q_text=self.quiz.next_question()
            self.question_canvas.itemconfig(self.question,text=q_text)
            self.score_label.config(text=f"score {self.quiz.score}")
        else:
            self.question_canvas.itemconfig(self.question,text="end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def true_pressed(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)
   
    def false_pressed(self):
        is_right=self.quiz.check_answer("false")
        self.give_feedback(is_right)
        
        
    def give_feedback(self,is_right):
        if is_right:
            self.question_canvas.config(bg="green")
            
        else:
            self.question_canvas.config(bg="red")
         
        self.window.after(1000,self.get_nextquestion)   
            
            
        
        