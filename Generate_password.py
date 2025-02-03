import random
import string
def generate_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    # password = ''.join(random.choice(all_characters) for _ in range(length))
    password = ''
    for i in range(length):
        password += random.choice(all_characters)

    return password

password_length = int(input("Enter the length of the password: "))
password = generate_password(password_length)
print(f"Your generated password is: {password}")
