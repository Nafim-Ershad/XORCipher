# XOR Cipher class for encryption and decryption
class XORCipher:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        encryption = []
        for i, char in enumerate(plaintext):
            encryption.append(chr(ord(char) ^ ord(self.key[i % len(self.key)])))

        return ''.join(encryption)
    
    def decrypt(self, ciphertext):
        decryption = []
        for i, char in enumerate(ciphertext):
            decryption.append(chr(ord(char) ^ ord(self.key[i % len(self.key)])))

        return ''.join(decryption)
    