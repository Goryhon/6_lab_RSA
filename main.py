import random

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    # Генерация двух простых чисел
    p = random.randint(10, 50)
    while not is_prime(p):
        p += 1

    q = random.randint(50, 100)
    while not is_prime(q):
        q += 1

    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытого ключа e
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e += 1

    # Вычисление секретного ключа d
    d = mod_inverse(e, phi)
    print(p, q, n,e,d)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

# Пример использования
public_key, private_key = generate_keypair()
message = 2155

# Шифрование
cipher_text = encrypt(public_key, message)

print(f"Зашифрованное сообщение: {cipher_text}")

# Расшифровка
decrypted_message = decrypt(private_key, cipher_text)
print(f"Расшифрованное сообщение: {decrypted_message}")