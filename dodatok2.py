from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from random import randint 
def click():
    num1 = randint(0,9)
    number.setText(str(num1))
    num2 = randint(0,9)
    number.setText(str(num2))

app = QApplication([])

main_win = QWidget()


main_win.setWindowTitle("лотерея")
main_win.resize(400,200)
main_win.move(600,400)

text = QLabel("Натисни щоб взяти участь")
text.setFon(QFont("Aria;", 20))
number1 = QLabel("?")
number1.setFont(QFont("Arial", 20))
number2 = QLabel("?")
number2.setFont(QFont("Arial", 20))
button = QPushButton("Випробувати удачу")
button = set.Font(QFont("Arial", 20))


line = QVBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(number,alignment=Qt.AlignCenter)
line.addWidget(button,alignment=Qt.AlignCenter)
main_win.setLayout(line)



button.clicked.connect(click)
main_win.show()
app.exec()