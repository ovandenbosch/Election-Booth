from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json



questions = [
    {
        'type': 'password',
        'message': 'Enter your password',
        'name': 'password'
    }
]

answers = prompt(questions)
print(answers)