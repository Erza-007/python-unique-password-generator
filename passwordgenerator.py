import random
import string
print("password generator")
def main():
    while True:
        length=input("Enter the length:").strip()
        if not length.isdigit():
                print("please enter numeric values !")
                continue
        length=int(length)
        if length<4:
            print("minimumlength is 4!")
            continue
        break
    print("Valid length entered") 
       
    uppercase=string.ascii_uppercase
    lowercase=string.ascii_lowercase
    digits=string.digits
    special = "!@#$%^&*():><?"
    all_characters = uppercase+lowercase+digits+special
    password=[
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]
    for _ in range(length-4):
            password.append(random.choice(all_characters))
    random.shuffle(password)
    full_password = "".join(password)
    print("Generating full password\n")
    print("Your password",full_password)
if __name__ == "__main__":
    main()
