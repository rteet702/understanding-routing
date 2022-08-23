from flask import Flask

new_app = Flask(__name__)

@new_app.route('/')
def base():
    return 'Hello World!'

@new_app.route('/dojo/')
def dojo():
    return 'Dojo!'

@new_app.route('/say/<word>')
def say(word):
    return f'Hi {str(word)}!'

@new_app.route('/<num>/<word>')
def repeat(num, word):
    lines = []
    for i in range(0, int(num)):
        lines.append(str(word))
    return '\n'.join(lines)

@new_app.errorhandler(404)
def page_not_found(e):
    return f'{e}'

if __name__ == '__main__':
    new_app.run(debug=True)