from tkinter import *
# Константа
CANVAS_SIZE = 700

# список вопросов и ответов к ним
q_a = {
    '2+2': 4,
    '5+7': 12,
    '9+2': 11, 
    '8+11': 19,
    '6+7': 13,
}
root = Tk()
canvas = Canvas(root, height=CANVAS_SIZE, width=CANVAS_SIZE, bg='gray94', borderwidth=3)
canvas.pack()

class Start_page():
    '''
    Это титульная страница, используемая для предоставления пользователю выбор между учеником и учителем
    '''
    def __init__(self):
        canvas.create_text(360, 150, text='Ты учитель или ученик?', fill='black', font='Arial 25')
        self.button_teacher = Button(canvas, padx=17.5, pady=30, width=15, height=5, text='Учитель', bg='maroon2', bd=0, font='Arial 9', activebackground='maroon1', command=self.teacher_button)
        self.button_student = Button(canvas, width=15, height=5, padx=20, pady=30, text='Ученик', bg='spring green', bd=0, font='Arial 9', activebackground='lawn green', command=self.student_button)
        self.button_teacher.place(x=385, y=300)
        self.button_student.place(x=185, y=300)

    def teacher_button(self):
        '''
        Этя функция "удаляет" титульную страницу, и запускает страницу учителя
        '''
        self.button_teacher.destroy()
        self.button_student.destroy()
        canvas.delete(0, ALL)
        Teacher_page()

    def student_button(self):
        '''
        Эта функция "удаляет" титульную страницу, и запускает страницу ученика
        '''
        self.button_teacher.destroy()
        self.button_student.destroy()
        canvas.delete(0, ALL)
        Student_page()

class Student_page():
    '''
    Это страница ученика, где пользователь должен отвечать на примеры по умолчанию, а также примеры, добавленные в режиме учителя
    ''' 
    def __init__(self):
        canvas.create_text(360, 100, text='Реши пример:', fill='black', font='Arial 25')
        self.entry_field = Entry(canvas, width=40, borderwidth=3)
        self.send_answer = Button(canvas, width=7, height=4, text='Отправить', command=self.send_answer, bg='lightblue', font='Arial 6')
        self.exit =  Button(canvas, bg='tomato', text='В главное меню', font='Arial 6', command=self.go_to_menu)

        self.entry_field.place(x=235, y=200)
        self.send_answer.place(x=333, y=240)
        self.exit.place(x=318, y=680)
        self.mark_q = len(q_a) - 1
        self.true_answers = 0
        self.questions = list(q_a.keys())
        self.answers = list(q_a.values())
        self.start_math()
    def start_math(self):
        '''
        Эта функция выводит на экран решаемый пример
        '''
        if self.mark_q == -1:
            self.end()
        try:
            self.text_math.destroy()
        except:
            pass
        printed_text = f'{self.questions[self.mark_q]}'
        self.text_math = Label(canvas, text=f'{printed_text}', fg='black', font='Arial 15')
        self.text_math.place(x=335, y=150)
        self.mark_q -= 1
        if self.mark_q == -2:
            self.text_math.destroy()
    def send_answer(self):
        '''
        Эта функция запоминает ввод пользователя, и запускает проверку правильности ответа, а также смену примера
        '''
        self.user_answer = self.entry_field.get()
        self.entry_field.delete(0, END)
        self.start_math()
        self.check_true()
    def check_true(self):
        '''
        Эта функция проверяет ответ, и если он правильный, зачисляет +1 к правильным ответам
        '''
        try:
            if int(self.user_answer) == int(self.answers[self.mark_q + 2]):
                self.true_answers += 1

        except:
            pass
    def go_to_menu(self):
        '''
        Эта функция "удаляет" страницу ученика - выход из режима ученика на титульную страницу
        '''
        self.text_math.destroy()
        self.entry_field.destroy()
        self.send_answer.destroy()
        self.exit.destroy()
        canvas.delete(0, ALL)
        Start_page()
    
    def end(self):
        self.entry_field.destroy()
        self.send_answer.destroy()
        self.text_math.destroy()
        self.true_answers += 1
        canvas.delete(0, ALL)
        canvas.create_text(355, 340, text=f'Правильных ответов: {self.true_answers}', font='Arial 25')

class Teacher_page():
    '''
    Это страница учителя, где пользователь может добавлять примеры к списку по умолчанию, для решения их в режиме ученика
    '''
    def __init__(self):
        canvas.create_text(360,150, text='Хотите добавить пример?', fill='black', font='Arial 25')
        self.btn_yes = Button(canvas, width=15, height=5, padx=20, pady=30, text='Да', bg='spring green', bd=0, font='Arial 9', activebackground='lawn green', command=self.btn_yes)
        self.btn_not = Button(canvas, width=15, height=5, padx=20, pady=30, text='Нет', bg='red', bd=0, font='Arial 9', activebackground='maroon3', command=self.btn_not)
        self.btn_yes.place(x=185, y=300)
        self.btn_not.place(x=385, y=300)

    def btn_yes(self):
        '''
        Эта функция выполняет роль отказа от перехода в режим учителя - возвращает пользователя на титульную страницу
        '''
        self.btn_yes.destroy()
        self.btn_not.destroy()
        canvas.delete(0, ALL)
        self.question_page()

    def btn_not(self):
        '''
        Эта функция выполняет роль соглашения перехода в режим учителя - переходит на страницу добавления примеров
        '''
        self.btn_yes.destroy()
        self.btn_not.destroy()
        canvas.delete(0, ALL)
        Start_page()

    def question_page(self):
        '''
        Это страница для добавления примеров, выполняет роль отрисовки интерфейса
        '''
        canvas.create_text(360, 100, text='Напишите свой пример', fill='black', font='Arial 25')
        canvas.create_text(485, 125, text='без ответа', fill='gray', font='Arial 12')
        self.entry_field = Entry(canvas, width=40, borderwidth=3)
        self.entry_field.place(x=235, y=200)
        self.send_question = Button(canvas, width=7, height=4, text='Отправить', bg='lightblue', font='Arial 6', command=self.send_question)
        self.exit =  Button(canvas, bg='tomato', text='В главное меню', font='Arial 6', command=self.go_to_menu)
        self.exit.place(x=316, y=680)
        self.send_question.place(x=330, y=240)

    def go_to_menu(self):
        '''
        Эта функция "удаляет" страницу учителя, выход из режима на титульную страницу
        '''
        self.entry_field.destroy()
        self.send_question.destroy()
        self.exit.destroy()
        try:
            self.text_error.destroy()
        except:
            pass
        canvas.delete(0, ALL)
        Start_page()

    def send_question(self):
        '''
        Эта функция проверяет наличие примера в списке по умолчанию
        '''
        self.exam = self.entry_field.get()
        self.entry_field.delete(0, END)
        try:
            for q in q_a:
                if self.exam == q:
                    self.text_error = Label(canvas, text='Данный пример уже имеется', fg='red', font='Arial 10')
                    self.text_error.place(x=275, y=140)
                if self.exam not in q_a:
                    self.change_dict()
        except:
            pass

    def change_dict(self):
        '''
        Эта функция изменяет список примеров - добавляет пример, написанный в режима учителя
        '''
        q_a[self.exam] = eval(f'{self.exam}')
# Тестинг
start = Start_page()

root.mainloop()