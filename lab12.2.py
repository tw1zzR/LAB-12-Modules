import random, string


def Encryption(text):
    ecrypt = ""
    for i in range(len(text)):
        ecrypt += text[i] + random.choice(string.ascii_letters)
    return  ecrypt

def Decryption(text):
    ecrypt = ""
    b = 1
    for i in range(len(text)):
        if b < 1:
            b += 1
            continue
        ecrypt += text[i]
        b = 0
    return ecrypt

encrypted_text = Encryption("ЦЕЙ ТЕКСТ БУДЕ ЗАШИФРОВАНО")
decrypted_text = Decryption(encrypted_text)

print(encrypted_text)
print(decrypted_text)



