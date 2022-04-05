import secrets
import string

def get_random_password_string(length):
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(pass_chars) for x in range(length))
    return password
