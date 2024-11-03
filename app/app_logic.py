from random import randint, randrange
import os
def navigate_to(controller, page_name):
    controller.show_frame(page_name)


def check_prime_number(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_number():
    while True:
        number = randint(500, 1000)
        if check_prime_number(number):
            return number



def greatest_common_factor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_public_key(phiNumber):
    e = randrange(2, phiNumber)
    while greatest_common_factor(e, phiNumber) != 1:
        e = randrange(2, phiNumber)
    return e

def generate_private_key(e, phiNumber):
    k = 0
    while True:
        d = (1 + k * phiNumber) / e
        if d.is_integer():
            return int(d)
        k += 1

def convert_key_to_base64(key):
    return str(key).encode("utf-8").hex()

def convert_base64_to_key(base64_key):
    print(base64_key)
    key =  str(bytes.fromhex(base64_key).decode("utf-8"))
    print(key)
    return key


def encrypt_message(message, public_key):
    public_key = public_key.strip().replace("(", "").replace(")", "").replace(" ", "")
    e, n = map(int, public_key.split(","))
    message_bytes = message.encode('utf-8')
    encrypted_message = [pow(byte, e, n) for byte in message_bytes]
    return encrypted_message


def decrypt_message(encrypted_message, private_key):
    private_key = private_key.strip().replace("(", "").replace(")", "").replace(" ", "")
    d, n = map(int, private_key.split(","))

    encrypted_bytes = list(map(int, encrypted_message.split()))

    decrypted_bytes = [pow(byte, d, n) for byte in encrypted_bytes]
    return bytes(decrypted_bytes).decode('utf-8')

def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
        if not os.path.exists(directory):
            raise Exception(f"Không thể tạo thư mục {directory}.")

def write_to_file(file_path, data):
    ensure_directory_exists(file_path)
    print(file_path)
    with open(file_path, 'w') as file:
        file.write(data)
    with open(file_path, 'r') as file:
        print(file.read(), "dataa")

def read_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()