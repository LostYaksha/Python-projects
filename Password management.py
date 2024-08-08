from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    return key


master_pwd = input('What is your master key? ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(" ")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())



def add():
    name = input('acount name: ')
    pwd = input('type password: ')

    with open('passwords.txt', 'a') as f:
        f.write(name + " " + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input('Do you want to add password or view existing ones (view, add), press q to quit? ').lower()
    if mode == 'q':
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print('Invalid mode. ')
        continue