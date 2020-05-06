import random

def passgen():
    s = 'abcdefghijkl\
        mnopqrstuvwxyz1234\
            567890ABCDEFGHIJK\
                LMNOPQRSTUVWXYZ!@#$%^&*()_-+=\
                ;/,.'

    passlen = 16
    password = "".join(random.sample(s, passlen))
    return(password)

def Add(N, A):
    f = open('doc/passwords.txt', 'a')
    f.write('\n')
    f.write(N + ":" + A)
    f.close
    print("Wrote to 'passwords.txt'")

if __name__ == "__main__":
    place = input("What is this for?> ")
    password = passgen()
    print(password)
    Add(place, password)