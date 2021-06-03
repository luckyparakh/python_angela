import tkinter as tk
import requests


def get_data():
    parameters = {
        'amount': 50,
        'difficulty': 'easy',
        'type': 'boolean'
    }
    req = requests.get('https://opentdb.com/api.php',params=parameters)
    req.raise_for_status()
    data = req.json()
    print(data['results'][0]['question'])
    print(data['results'][0]['correct_answer'])

get_data()