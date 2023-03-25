"""
3/25/2023
CBC-Cypher Block Chaining
"""

cipher_table = {
    '0b00': '0b01',
    '0b01': '0b10',
    '0b10': '0b11',
    '0b11': '0b00'
}
decipher_table = {
    '0b00': '0b11',
    '0b01': '0b00',
    '0b10': '0b01',
    '0b11': '0b10'
}

message = ["0b00", "0b01", "0b10", "0b11"]


def CBC_CipherMessage(message, IV="0b10"):
    output = []
    for m in message:
        xor = '0b{:02b}'.format(int(m, 2) ^ int(IV, 2))
        IV = cipher_table.get(xor)
        output.append(IV)
    return output


def CBC_DecipherMessage(message, IV="0b10"):
    output = []
    for m in message:
        temp = m
        m = decipher_table.get(m)
        xor = '0b{:02b}'.format(int(m, 2) ^ int(IV, 2))
        IV = temp
        output.append(xor)
    return output


print(CBC_CipherMessage(message))
print(CBC_DecipherMessage(CBC_CipherMessage(message)))
