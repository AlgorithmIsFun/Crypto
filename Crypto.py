def encrypt_message(message):
    new_str = ''
    while message != '':
        new_str += encrypt(message[0])
        message = message[1:]
    return new_str

def encrypt(char):
    if char == ' ':
        return ' '
    num = ord(char)
    while num * 2 > 122:
        num -= 32
    return chr(num * 2)

def dencrypt_message(message):
    new_str = ''
    while message != '':
        new_str += dencrypt(message[0])
        message = message[1:]
    return new_str

def dencrypt(char):
    if char == ' ':
        return ' '
    num = ord(char)
    num = num // 2
    while num < 65:
        num += 32
    return chr(num)

if __name__ == '__main__':
    sr = encrypt_message('I am Abdullah Khan')
    print(sr)
    print(dencrypt_message(sr))
