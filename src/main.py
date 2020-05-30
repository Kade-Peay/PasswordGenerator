import secrets, string

def passgen():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(16))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break

    return password

def Add(N, A):
    f = open('C:/Users/kadep/Password_Generator/doc/passwords.txt', 'a')
    f.write('\n')
    f.write(N + ":" + A)
    f.close
    print("Wrote to 'passwords.txt'")

if __name__ == "__main__":
    place = input("What is this for?> ")
    password = passgen()
    print(str(password))
    Add(place, str(password))