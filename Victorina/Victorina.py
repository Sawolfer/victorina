import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
import random

# Вопросы и ответы
questions = [
    {"question": "The supply chain only includes the delivery of finished goods to customers.", "options": ["True", "False"], "answer": "False"},
    {"question": "The upstream part of the supply chain includes distributors.", "options": ["True", "False"], "answer": "False"},
    {"question": "Good management of inventory information is important for business success.", "options": ["True", "False"], "answer": "True"},
    {"question": "Supply Chain Management (SCM) focuses only on suppliers.", "options": ["True", "False"], "answer": "False"},
    {"question": "Logistics only deals with outgoing goods.", "options": ["True", "False"], "answer": "False"},
    {"question": "Hub-and-Spoke is a method that sorts items at a central location for delivery.", "options": ["True", "False"], "answer": "True"},
    {"question": "'Reverse logistics' refers to the process of moving goods to customers.", "options": ["True", "False"], "answer": "False"},
    {"question": "Smaller companies often prefer using the term 'logistics' instead of 'supply chain management.'", "options": ["True", "False"], "answer": "True"},
    {"question": "Consolidation combines smaller shipments into larger ones.", "options": ["True", "False"], "answer": "True"},
    {"question": "Deconsolidation breaks down large shipments into smaller lots for easier delivery.", "options": ["True", "False"], "answer": "True"}
]

random.shuffle(questions)
score = 0
current_question = 0

# Функция проверки ответа
def check_answer(selected_option):
    global score, current_question
    if selected_option == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question < len(questions):
        load_question()
    else:
        messagebox.showinfo("Результат", f"Вы набрали {score} из {len(questions)} баллов!")
        root.quit()

# Функция загрузки вопроса
def load_question():
    question_label.config(text=questions[current_question]["question"])
    for i in range(2):  
        buttons[i].config(text=questions[current_question]["options"][i], command=lambda opt=questions[current_question]["options"][i]: check_answer(opt))

# Функция переключения с текста на викторину
def start_quiz():
    canvas.pack_forget()  # Скрываем Canvas (фон и текст)
    quiz_canvas.pack(fill="both", expand=True)  # Показываем фон викторины
    quiz_canvas.create_window(300, 260, window=quiz_frame, anchor="center")  # Размещаем вопросы и кнопки
    load_question()

# Создание окна
root = tk.Tk()
root.title("Викторина")
root.geometry("600x520")  
root.resizable(False, False)  

# === Экран с текстом статьи ===
canvas = tk.Canvas(root, width=600, height=520)
canvas.pack(fill="both", expand=True)

# Фоновое изображение
original_image = Image.open("sapsan-facts.jpg")
bg_photo = ImageTk.PhotoImage(original_image)
canvas.create_image(0, 0, anchor="nw", image=bg_photo)

# Читаем текст из файла
with open("article.txt", "r", encoding="utf-8") as file:
    article_text = file.read()

# Поле для текста
text_widget = tk.Text(root, wrap="word", font=("Arial", 14), height=12, width=50, bg="white", fg="#000")
text_widget.insert("1.0", article_text)
text_widget.config(state="disabled")

# Добавляем текст на canvas
canvas.create_window(300, 200, window=text_widget, width=550, height=300, anchor="center")

# Полоса прокрутки
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Добавляем скроллбар на canvas
canvas.create_window(570, 200, window=scrollbar, height=300, anchor="center")

# Кнопка "Almost read"
read_button = tk.Button(root, text="Almost read", font=("Arial", 14), command=start_quiz, bg="white")
canvas.create_window(300, 450, window=read_button, anchor="center")

# === Фон для викторины ===
quiz_canvas = tk.Canvas(root, width=600, height=520)

# Фоновое изображение для викторины
quiz_bg_image = Image.open("sapsan-facts.jpg")  # Укажите свой файл с фоном для теста
quiz_bg_photo = ImageTk.PhotoImage(quiz_bg_image)
quiz_canvas.create_image(0, 0, anchor="nw", image=quiz_bg_photo)

# === Экран с викториной ===
quiz_frame = tk.Frame(root, bg="white")

question_label = tk.Label(quiz_frame, text="", wraplength=500, font=("Arial", 18), bg="white", fg='#000')
question_label.pack(pady=20)

buttons = []
for i in range(2):  
    btn = tk.Button(quiz_frame, text="", font=("Arial", 16), width=40)
    btn.pack(pady=10)
    buttons.append(btn)

# Скрываем фон викторины до начала теста
quiz_canvas.pack_forget()

root.mainloop()