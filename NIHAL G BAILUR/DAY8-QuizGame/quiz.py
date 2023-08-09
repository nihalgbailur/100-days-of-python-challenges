import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Mars", "Earth", "Venus", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Blue Whale", "Elephant", "Giraffe", "Lion"],
                "correct_answer": "Blue Whale"
            }
        ]

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for _ in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 12), command=lambda: self.check_answer(button))
            self.option_buttons.append(button)
            button.pack()

        self.next_question()

    def next_question(self):
        if self.current_question < len(self.questions):
            question_data = self.questions[self.current_question]
            self.question_label.config(text=question_data["question"])

            options = question_data["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])

            self.current_question += 1
        else:
            self.show_score()

    def check_answer(self, selected_button):
        selected_answer = selected_button.cget("text")
        correct_answer = self.questions[self.current_question - 1]["correct_answer"]

        if selected_answer == correct_answer:
            self.score += 1

        self.next_question()

    def show_score(self):
        self.question_label.config(text=f"Your score: {self.score}/{len(self.questions)}")
        for button in self.option_buttons:
            button.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
