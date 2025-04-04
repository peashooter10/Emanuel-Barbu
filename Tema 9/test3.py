import string
char_sets = [
    string.ascii_lowercase,
    string.ascii_lowercase,
    string.ascii_lowercase,
    string.ascii_uppercase,
    string.digits,
    "!#@$"
]
password_to_break = "pasA3!"
def generate_password(index=0, current_password="",broken = False):
    if current_password == password_to_break:
        raise Exception(f"Password is broken {current_password}")
    if index == len(char_sets):
        return
    for char in char_sets[index]:
        generate_password(index + 1, current_password + char,broken)
try:
    generate_password()
except Exception as e:
    print(e)