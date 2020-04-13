from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return {'data': 'Hello, World! Welcome to Flask'}


@app.route('/<username>')
def show_user_profile(username):
    # show the user profile for that user
    japanese_name = j_name(username)
    return {'original name': username, 'translated name': japanese_name}

def j_name(uname):
    japanese_alphabet = {'a': 'ka', 'b': 'tu', 'c': 'mi', 'd': 'te',
                        'e': 'ku', 'f': 'lu', 'g': 'ji', 'h': 'ri',
                        'i': 'ki','j': 'zu', 'k': 'me', 'l': 'ta',
                        'm': 'rin', 'n': 'to', 'o': 'mo', 'p': 'no',
                        'q': 'ke', 'r': 'shi', 's': 'ari', 't': 'chi',
                        'u': 'do','v': 'ru', 'w': 'mei', 'x': 'na',
                        'y': 'fu', 'z': 'zi'}
    uname = uname.lower()
    translate_name = list()
    [translate_name.append(japanese_alphabet[i]) for i in uname]
    return ''.join(translate_name)


@app.route('/add/<numbers>')
def add(numbers):
    # show the user profile for that user
    numbers = split_numbers(numbers)
    return 'Add {}'.format(int(numbers[0])+int(numbers[1]))


def split_numbers(numbers):
    numbers = numbers.split(',')
    return numbers
