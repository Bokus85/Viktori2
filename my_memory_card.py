#создай приложение для запоминания информации
from random import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QMessageBox, QRadioButton, QButtonGroup

app = QApplication([])
main_win =  QWidget()


RadioGroupBox = QGroupBox('Варианты ответов')
gfd = QGroupBox('Результаты:')
u1 = QLabel('Самый сложный вопрос в мире!')
u2 = QPushButton('Следующий вопрос.')
u3 = QLabel('Правильно\Неправильно')
u4 = QLabel('Правильный ответ')

question = QLabel('Как звали главного героя Far Cry 3')
btn_answer1 = QRadioButton('Джейсон Броди')
btn_answer2 = QRadioButton('Дейзи Ли')
btn_answer3 = QRadioButton('Грант Броди')
btn_answer4 = QRadioButton('Вас Монтенегро')

hgh = QPushButton('Ответить')

layout_main1 = QHBoxLayout()
layout_main2 = QVBoxLayout()
layout_main3 = QVBoxLayout()

layout_main2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layout_main2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layout_main3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layout_main3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layout_main1.addLayout(layout_main2)
layout_main1.addLayout(layout_main3)
RadioGroupBox.setLayout(layout_main1)


f4 = QVBoxLayout()
f4.addWidget(u3)
f4.addWidget(u4)
gfd.setLayout(f4)





f5 = QVBoxLayout()

f5.addWidget(question)
f5.addWidget(RadioGroupBox)
f5.addWidget(gfd)
f5.addWidget(hgh)
main_win.setLayout(f5)


RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)


gfd.hide()


answer = [btn_answer1,btn_answer2,btn_answer3,btn_answer4]


def next_question():
    main_win.total += 1
    print ("Всего вопросов:", main_win.total)
    kap_question = randint(0, len(tar_list)-1)
    if kap_question >= len(tar_list):
        kap_question = 0 
    d = tar_list [kap_question]
    ask(d)
    

def show_result():
    hgh.setText('Следующий вопрос.')
    RadioGroupBox.hide()
    gfd.show()


def show_question():
    gfd.hide()
    RadioGroupBox.show()
    hgh.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(False)



class Das():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


def ask(q):
    shuffle(answer) 
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    question.setText(q.question)
    u4.setText(q.right_answer)
    show_question()

def show_correct(res):
    u3.setText(res)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print("Правильных ответов",main_win.score)
        print()
    else:
        if answer[1].isChecked()  or  answer[2].isChecked  or  answer[3].isChecked():
            print("Правильных ответов",main_win.score)
            show_correct('НЕправильно!')


tar_list = []
q = Das('Сколько стоит Bugatti Veyron?', '153 млн.350 тыс.' , '110млн.' , '89млн.' , '167млн.')
q1 = Das('Как дела?','Нормально','Плохо',"-__-","аналогично")
q2 = Das('Что делаешь?','Ничего','Программирую','ем','Играю')
q3 = Das("Сколько времени ты играешь?","сутки","1час","2-3часа","30min")
q4 = Das("Какую платформу любишь?","Консоли или ПК","Браузерные","Клиентские","На телефоне")
q5 = Das("В любой игре круто когда:","Когда управляешь мышкой и клавиатурой","Бестплатно","Паркуришь","Стреляешь")
q6 = Das("Вышла новая игра, твои действия","Сразу куплю","Ждать версию для ПК или Консоли","Скачаю пиратку","Мечтать о ней")
q7 = Das("Ешь за компьютером?","нет, грязные руки","Конечно","иногда","когда скачивается игра или фильм")

tar_list.append(q1)
tar_list.append(q2)
tar_list.append(q3)
tar_list.append(q4)
tar_list.append(q5)
tar_list.append(q6)
tar_list.append(q7)
tar_list.append(q)

    
main_win.kap_question = -1


def click_OK():
    if hgh.text() == 'Ответить':
        check_answer()
    else:
        next_question()


main_win.setWindowTitle("Memo Card")




hgh.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_question()
main_win.show()
app.exec_()
