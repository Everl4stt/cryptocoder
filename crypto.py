from config import KEY, s_block, A, B, cipher

def str_xor(str1, str2) -> str:
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(str1, str2))

k1 = ''.join(f'{byte:08b}' for byte in KEY[:2])
k2 = ''.join(f'{byte:08b}' for byte in KEY[2:])
keys = {
        1: k1[2:] + k1[:2],
        2: k2[4:] + k2[:4],
        3: k1[2:] + k1[:2],
        4: k1,
        5: str_xor(k1, (k2[6:] + k2[:6])) + k2
        }

def tau_substitution(data) -> str:
    return data[16:] + data[:16]

def feistel_substitution(data, step) -> str:
    return data[16:] + str_xor(data[:16], fkeys(data[16:], step))

def p_block(data) -> str:
    for i in range(len(data)):
        num = (A * i + B) % 16
        char = data[15 - i]
        data = data[:num] + char + data[num + 1:]
    return data

def s_blocks(data) -> str:
    res_data = ''
    while len(data) > 0:
        pos = int(data[:4], 2) - 1
        res_data += s_block[pos]
        data = data[4:]
    return res_data

def fkeys(data, step) -> str:
    data = str_xor(data, keys[step])
    data = s_blocks(data)
    data = p_block(data)
    return data

def bleach(data, step) -> str:
    return str_xor(data, keys[step])

def encrypt(byte_data) -> str:
    res_data = ''
    bit_data = ''.join(f'{byte:08b}' for byte in byte_data)
    while len(bit_data) > 0:
        step = 0
        data_to_encrypt = bit_data[:32]
        bit_data = bit_data[32:]
        for char in cipher:
            if char == 't':
                data_to_encrypt = tau_substitution(data_to_encrypt)
            if char == 'f':
                step += 1
                data_to_encrypt = feistel_substitution(data_to_encrypt, step)
            if char == 'w':
                step += 1
                data_to_encrypt = bleach(data_to_encrypt, step)
        res_data += data_to_encrypt
    return res_data

def decrypt(data):
    return data[::-1]