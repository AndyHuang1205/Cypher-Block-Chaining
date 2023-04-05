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


def toBinary(message):
    binaryList = []
    for c in message:
        string = "{:08b}".format(ord(c))
        for i in range(0, len(string), 2):
            binaryList.append("0b" + string[i:i + 2])
    return binaryList


def toString(messageList):
    string = ""
    message = ""
    for m in messageList:
        message += m[2:]

    start = 0
    end = 8
    while end < len(message) + 1:
        string += chr(int(message[start:end], 2))
        start += 8
        end += 8
    return string


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


print("CBC-Cypher Block Chaining")
userInput = input("Enter plaintext: ")
plainTextBinary = toBinary(userInput)

cipherMessage = CBC_CipherMessage(plainTextBinary)
print(f"The plaintext in binary in a list is {plainTextBinary}")
print("The ciphertexts are: {}".format(cipherMessage))
print("The deciphered text in binary are: {}".format(CBC_DecipherMessage(cipherMessage)))
print("The deciphered text is: " + toString(CBC_DecipherMessage(cipherMessage)))
