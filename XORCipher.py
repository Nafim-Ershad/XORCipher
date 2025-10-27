# XOR Cipher class for encryption and decryption
class XORCipher:
    def __init__(self, key):
        self.key = key
    
    def encrypt(self, plaintext):
        encrypted = ""
        for i, c in enumerate(plaintext):
            encrypted += (chr(ord(c) ^ ord(self.key[i % len(self.key)])))
        return encrypted
    
    def decrypt(self, ciphertext):
        decrypted = ""
        for i, c in enumerate(ciphertext):
            decrypted += (chr(ord(c) ^ ord(self.key[i % len(self.key)])))
        return decrypted