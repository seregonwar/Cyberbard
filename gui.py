from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import subprocess
import tkinter as tk
import threading

subprocess.Popen(['python', 'Cyberbard.py'])
class LoginWindow(QtWidgets.QDialog):
    self.login_window = LoginWindow()
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")

        # Creazione dei widget
        self.email_label = QtWidgets.QLabel("Email:")
        self.email_input = QtWidgets.QLineEdit()
        self.password_label = QtWidgets.QLabel("Password:")
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton("Login")

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout) 

        # Eventi
        self.login_button.clicked.connect(self.login)

    def login(self):
     email = self.email_lineEdit.text()
    password = self.password_lineEdit.text()
    if email != "" and password != "":
        
        # Login con Google
        driver = webdriver.Chrome()
        driver.get("https://accounts.google.com/signin/v2/identifier?passive=1209600&continue=https%3A%2F%2Fbard.google.com%2F&followup=https%3A%2F%2Fbard.google.com%2F&flowName=GlifWebSignIn&flowEntry=ServiceLogin&rd=https%3A%2F%2Fbard.google.com%2F")
        email_field = driver.find_element_by_name("identifier")
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)
        time.sleep(1)
        password_field = driver.find_element_by_name("password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        
        # Dopo aver effettuato l'accesso con successo
        self.logged_in = True

        # Chiudi il driver
        driver.quit()

        self.chat_tabWidget.setCurrentWidget(self.chat_page)
    else:
        self.show_warning_message("Inserisci la tua email e password")

class ChatWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chat")

        # Creazione dei widget
        self.message_history = QtWidgets.QTextEdit()
        self.message_input = QtWidgets.QLineEdit()
        self.send_button = QtWidgets.QPushButton("Send")

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.message_history)
        layout.addWidget(self.message_input)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        # Eventi
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.message_input.text()

        # Invio del messaggio al destinatario
        # ...

        # Aggiornamento della cronologia dei messaggi
        self.message_history.append(f"> {message}")
        self.message_input.clear()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Creazione delle finestre
        self.login_window = LoginWindow()
        self.chat_window = ChatWindow()

        # Aggiunta delle finestre alla finestra principale
        self.setCentralWidget(self.chat_window)
        self.addDockWidget(QtCore.Qt.LeftDockWidgetArea, self.login_window)

        # Proprietà della finestra principale
        self.setWindowTitle("Cyberbard")

if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()