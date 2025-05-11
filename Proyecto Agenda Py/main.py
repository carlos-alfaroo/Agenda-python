import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QDateEdit
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QDate

import Date as D
import Person as P

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda")
        self.setGeometry(700, 300, 375, 667)

        self.initUI()


    def initUI(self):
        # hey button
        self.heyButton = QPushButton("Heyy", self)
        self.heyButton.setGeometry(280, 100, 70, 30)
        self.heyButton.clicked.connect(self.on_click)
        self.heyButton.setObjectName("HeyButton")
        

        # header
        self.header = QLabel("this is your new Agenda", self)
        self.header.setFont(QFont("Arial", 17))
        self.header.setGeometry(0, 0, 375, 65)
        self.header.setStyleSheet("Background-color: hsl(338, 71%, 25%)")
        self.header.setAlignment(Qt.AlignCenter)

        # Label for Photo
        #self.label1 = QLabel(self)
        #self.label1.setGeometry(20, 100, 250,100)
        
        #self.photo = QPixmap("st.jpg")
        #self.label1.setPixmap(self.photo)
        #self.label1.setScaledContents(True)
        #self.label1.setAlignment(Qt.AlignCenter)

        # Text box  
        self.textBox = QLineEdit(self)
        self.textBox.setGeometry(20, 220, 250, 30)
        self.textBox.setPlaceholderText("Schedule something")

        # Text box button
        self.textBoxButton = QPushButton("Add", self)
        self.textBoxButton.setGeometry(280, 220, 70, 30)
        self.textBoxButton.clicked.connect(self.on_textBoxButton)

        # Label for list
        self.boxList = QTextEdit(self)
        self.boxList.setGeometry(20, 270, 330, 350)
        self.boxList.setReadOnly(True)
        self.boxList.setStyleSheet("""Background-color: hsl(338, 71%, 25%);
                                    color: white;
                                    font-size: 14px;
                                    Border-radius: 13%;
                                   padding: 10px;
                                    """)
        
        # Date picker
        self.datePicker = QDateEdit(self)
        self.datePicker.setGeometry(20, 180, 150, 30)
        self.datePicker.setDate(QDate.currentDate())
        self.datePicker.setCalendarPopup(True)





        # CSS
        self.setStyleSheet("""
            QPushButton{
                Border-radius: 13%;
                Background-color: hsl(344, 74%, 37%);
                Border: 14px, solid;
                Color: white;
            }
            QPushButton:hover{
                Border-radius: 13%;
                Background-color: hsl(349, 50%, 62%);
                Border: 14px, solid;
                Color: black;
            }
            QPushButton#HeyButton{
                Background-color: white;           
                color: black;    
            }
        """)
    
    def on_textBoxButton(self):
        text = self.textBox.text()
        if text:    #asegura que el texto no este vacio
            qdate = self.datePicker.date()
            customDate = D.Date(day = qdate.day(), month = qdate.month(), year = qdate.year())
            dateStr = customDate.toString()
            currentText = self.boxList.toPlainText()
            newText = currentText + f"\n• {dateStr} - {text}" if  currentText else f"• {dateStr} - {text}"
            self.boxList.setPlainText(newText)
            self.textBox.clear()
            self.textBoxButton.setText("Add")
        
        
       #45 print(text) # en vez de imprimirlo en terminal, en el GUI



    def on_click(self):
        self.heyButton.setText("Clicked")
        print("Heeeeey!!!!")

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())






