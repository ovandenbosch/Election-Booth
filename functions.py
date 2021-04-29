from __future__ import print_function, unicode_literals


from pprint import pprint

from PyInquirer import prompt, Separator


def admin():
    options = [
    {
        'type': 'list',
        'name': 'choice',
        'message': 'What do you want to do?',
        'choices': [
            'Save Data',
            'Load Data',
            'Display votes',
            'Alter votes',
            'Return to voting'
        ]
    }]

    choice = (prompt(options)['choice'])

    

    
    

admin()