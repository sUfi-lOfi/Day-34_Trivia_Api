from tkinter import *
import requests
import random

class FlashCard:
    def __init__(self,quiz_brain):
        self.quiz_brain = quiz_brain
        # -------------------- UI Setup -------------------- #
        self.BACKGROUND_COLOR = "#B1DDC6"
        self.window = Tk()
        self.window.title("Flash Card App")
        self.window.config(bg=self.BACKGROUND_COLOR, padx=45, pady=53)

        # -------------------- Score Label -------------------- #
        self.score = 0
        self.score_label = Label(
            text=f"Score = {self.score}",
            font=("JetBrains Mono", 14),
            bg=self.BACKGROUND_COLOR
        )
        self.score_label.grid(row=0, column=1)

        # -------------------- Canvas -------------------- #
        self.canvas = Canvas(width=362, height=302, bg="#FFFFFF", highlightthickness=0)
        self.canvas_text = self.canvas.create_text(
            181, 151, text="I am Here!", font=("JetBrains Mono", 12),width = 300
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=(40, 50))

        # -------------------- Buttons -------------------- #
        self.wrong_image = PhotoImage(file="./images/wrong.png")
        self.wrong_btn = Button(
            width=100, height=100,
            image=self.wrong_image,
            border=0,
            activebackground=self.BACKGROUND_COLOR,
            highlightthickness=0,
            bg=self.BACKGROUND_COLOR,
            command=self.wrong_pressed  # Placeholder
        )
        self.wrong_btn.grid(row=2, column=0, padx=(0, 30), sticky="w")

        self.right_image = PhotoImage(file="./images/right.png")
        self.right_btn = Button(
            width=100, height=100,
            image=self.right_image,
            border=0,
            activebackground=self.BACKGROUND_COLOR,
            highlightthickness=0,
            bg=self.BACKGROUND_COLOR,
            command=self.right_pressed
        )
        self.right_btn.grid(row=2, column=1, sticky='e')
        self.update_interface()
        self.window.mainloop()
    def wrong_pressed(self):
        if self.quiz_brain.current_question["correct_answer"] == "False":
            self.score += 1
            self.score_label.config(text=f"Score : {self.score}")
        if self.quiz_brain.next_question():
            self.update_interface()
        else:
            self.end_quiz()
    def right_pressed(self):
        if self.quiz_brain.current_question["correct_answer"] == "True":
            self.score += 1
            self.score_label.config(text = f"Score : {self.score}")
        if self.quiz_brain.next_question():
            self.update_interface()
        else:
            self.end_quiz()


    def update_interface(self):
        self.canvas.itemconfig(self.canvas_text,text = f"Q{self.quiz_brain.index_of_current + 1} : {self.quiz_brain.current_question["question"]}")
    def end_quiz(self):
        self.canvas.itemconfig(self.canvas_text,text = f"Questions Ended!!\nFinal Score is {self.score}")
        self.right_btn.config(state="disabled")
        self.wrong_btn.config(state="disabled")