import requests
import sys 
import re
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PyQt5.QtWidgets import QApplication
from gui import MainWindow
from gui import LoginWindow
from gui import app
from gui import session 
# Crea l'istanza della finestra di login
login_window = LoginWindow()

# Mostra la finestra di login
login_window.show()

# Crea l'istanza della finestra principale della GUI
main_window = MainWindow()

# Esegui l'applicazione
sys.exit(app.exec_())

def main():
 

# Check if the request was successful.
 if response.status_code == 200:
    print('Login page loaded successfully.')

    # Use BeautifulSoup to parse the response HTML.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the input element with the id "identifier".
    identifier = soup.find('input', {'id': 'identifierId'})
    if identifier:
        email = input("Enter your Google email address: ")
        identifier['value'] = email

        # Submit the email form.
        next_button = soup.find('div', {'id': 'identifierNext'})
        if next_button:
            response = session.post(next_button.find('button')['jsaction'], data={'identifier': email})

            # Check if the request was successful.
            if response.status_code == 200:
                print('Email entered successfully.')

                # Find the input element with the name "password".
                password = input("Enter your Google password: ")
                password_field = soup.find('input', {'name': 'password'})
                if password_field:
                    password_field['value'] = password

                    # Submit the password form.
                    submit_button = soup.find('div', {'id': 'passwordNext'})
                    if submit_button:
                        response = session.post(submit_button.find('button')['jsaction'], data={'password': password})

                        # Check if the request was successful.
                        if response.status_code == 200:
                            print('Password entered successfully.')

                            # Send a request to Google Bard.
                            access_token = response.cookies.get('oauth_token')
                            headers = {"Authorization": f"Bearer {access_token}"}
                            request = {"text": "What is the capital of France?"}
                            response = session.post("https://bard.ai/v1/generate", headers=headers, json=request)

                            # Check if the request was successful.
                            if response.status_code == 200:
                                print('Request sent successfully.')

                                # Extract the response text.
                                response_text = response.json()['text']

                                # Generate sub-tasks for each uppercase word in the response.
                                sub_tasks = []
                                for word in re.findall(r'\b[A-Z][A-Za-z]*\b', response_text):
                                    sub_task = {'description': f'What is {word}?', 'completed': False}
                                    sub_tasks.append(sub_task)

                                # Print the sub-tasks.
                                print('Generated sub-tasks:')
                                for sub_task in sub_tasks:
                                    print(sub_task['description'])
                            else:
                                print(f'Error getting response from Bard: {response.status_code}')
                        else:
                            print(f'Error entering password: {response.status_code}')
                    else:
                        print('Submit button not found.')
                else:
                    print('Password field not found.')
            else:
                print(f'Error entering email: {response.status_code}')
        else:
            print('Next button not found.')
    else:
        print('Email field not found.')
 else:
    print(f'Error getting login page: {response.status_code}')
    
if __name__ == "_main_":
    name = "main"
    main()