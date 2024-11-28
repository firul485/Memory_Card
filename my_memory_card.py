from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QLabel, QPushButton, 
    QGroupBox, QRadioButton
)



app = QApplication([])

bt_answer = QPushButton('Ответить')
question = QLabel('Самый сложный вопрос в мире')

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
q1 = Question(
    'Государственный язык португалии',
'Португальский',
    'Англиский', 'Испанский', 'Французкий'
)
questions_list.append(q1)

questions_list = []
questions_list.append(Question(
    'Государственный язык португалии',
    'Португальский',
    'Англиский', 'Испанский', 'Французкий'))

RadioGroupBox = QGroupBox('Варинты ответов')

q_1 = QRadioButton('Вариант 1')
q_2 = QRadioButton('Вариант 2')
q_3 = QRadioButton('Вариант 3')
q_4 = QRadioButton('Вариант 4')

layuot_ans1 = QHBoxLayout()
layuot_ans2 = QVBoxLayout()
layuot_ans3 = QVBoxLayout()
layuot_ans2.addWidget(q_1)
layuot_ans2.addWidget(q_2)
layuot_ans3.addWidget(q_3)
layuot_ans3.addWidget(q_4)

layuot_ans1.addLayout(layuot_ans2)
layuot_ans2.addLayout(layuot_ans3)
RadioGroupBox.setLayout(layuot_ans1)

layuot_line1 = QHBoxLayout()
layuot_line2 = QHBoxLayout()
layuot_line3 = QHBoxLayout()

layuot_line1.addWidget(question, alignment =(Qt.AlignHCenter | Qt.AlignVCenter))
layuot_line2.addWidget(RadioGroupBox)
layuot_line3.addStretch(1)
layuot_line3.addWidget(bt_answer, stretch=2)
layuot_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layuot_line1, stretch=2)
layout_card.addLayout(layuot_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layuot_line3, stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

answer = [q_1, q_2, q_3, q_4]

def ask(q1:Question):
    shufle 

main_win = QWidget()
main_win.setLayout(layout_card)
main_win.setWindowTitle('Memory card')
main_win.show()
app.exec()
