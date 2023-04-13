RUS = 'йцукенгшщзхъ фывапролджэё ячсмитьбю'
ENG = 'qwertyuiop asdfghjkl zxcvbnm'
ENG_MAC = 'qwertzuiop asdfghjkl yxcvbnm'


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    password = password.strip()
    a = 0
    b = 0
    c = 0
    if len(password) < 9:
        raise LengthError
    for i in password:
        if i.isdigit():
            c = 1
        elif i.islower():
            a = 1
        elif i.isupper():
            b = 1
        if not a:
            raise LetterError
        if not b:
            raise LetterError
        if not c:
            raise DigitError
        for i in range(0, len(password)):
            if len(password) - i < 3:
                break
            if any([True for j in [RUS, ENG, ENG_MAC] if password[i:i + 3].lower() in j]):
                raise SequenceError
    return 'ok'

try:
    print(check_password("G7FgTU0bwТuio"))
except Exception as error:
    print(error.__class__.__name__)