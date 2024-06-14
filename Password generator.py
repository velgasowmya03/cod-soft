import random
import string
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    password = generate_password(length)

    print(f"Generated password: {password}")
    
if __name__ == "__main__":
    main()
