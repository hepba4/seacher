import random
import string

def generate_mullvad_key():
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    key = ''.join(random.choices(characters, k=16))
    return key

if __name__ == "__main__":

    for _ in range(100):
        print(generate_mullvad_key())
