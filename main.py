# This is simple XOR Cipher implementation in Python for aircraft telemetry data encryption and decryption.

import random

# Custom Module Import
from XORCipher import XORCipher
from CRC8 import add_crc8, verify_crc

# This function generates a random aircraft telemetry for XOR cipher
def generate_telemetry(num_packets=100):
    packets = []
    for i in range(num_packets):
        altitude = 10000 + random.uniform(-500, 500)
        speed = 250 + random.uniform(-30, 30)
        heading = random.uniform(0, 360)
        packets.append(f"({i}), {altitude:.2f}, {speed:.2f}, {heading:.2f}")
    return ", ".join(packets)


def add_noise(data, error_rate=0.01):
    """
    Randomly corrupt characters in the data string.
    error_rate = probability that any character flips.
    """
    data = list(data)
    for i in range(len(data)):
        if random.random() < error_rate:
            # Replace character with a random printable ASCII char
            data[i] = chr(random.randint(32, 126))
    return ''.join(data)

    
# Usage example
if __name__ == "__main__":

    # Sender Side

    key = "key123456789"
    xor = XORCipher(key)

    random_data = generate_telemetry(10)

    encrypted_data = ""

    for i in enumerate(random_data):
        encrypted_data += xor.encrypt(random_data[i[0]])

    checksum = add_crc8("".join(encrypted_data))

    # Introduce noise to simulate transmission errors
    noisy_checksum = add_noise(checksum, error_rate=0.00)
    
    # Receiver Side
    is_valid = verify_crc(noisy_checksum)

    if is_valid:
        decrypted_data = ""
        for j in enumerate(encrypted_data):
            decrypted_data += xor.decrypt(encrypted_data[j[0]])
        
        print("\nCRC8 Checksum is valid.\n")

    else:
        print("\nCRC8 Checksum is invalid. Data may be corrupted.\n")