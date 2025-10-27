import random
from XORCipher import XORCipher
from CRC8 import add_crc8, verify_crc


def generate_telemetry(num_packets=10):
    """
    Returns a LIST of telemetry packets.
    Each packet stands alone and can be individually verified.
    """
    packets = []
    for i in range(num_packets):
        altitude = 10000 + random.uniform(-500, 500)
        speed = 250 + random.uniform(-30, 30)
        heading = random.uniform(0, 360)
        packets.append(f"{altitude:.2f},{speed:.2f},{heading:.2f}")
    return packets


def add_noise(packet, error_rate=0.02):
    packet = list(packet)
    for i in range(len(packet)):
        if random.random() < error_rate:
            packet[i] = chr(random.randint(32, 126))
    return ''.join(packet)


if __name__ == "__main__":
    
    key = "key123456789"
    xor = XORCipher(key)

    # Generate a list of telemetry packets
    packets = generate_telemetry(10)

    encrypted_stream = []
    transmitted_stream = []
    received_stream = []

    # Sender: Encrypt + Add CRC per packet
    for p in packets:
        encrypted = xor.encrypt(p)
        packet_with_crc = add_crc8(encrypted)
        encrypted_stream.append(packet_with_crc)

    # Channel: Introduce noise per packet
    noisy_stream = [add_noise(pkt, error_rate=0.05) for pkt in encrypted_stream]

    # Receiver: Verify CRC + Decrypt
    for pkt in noisy_stream:
        if verify_crc(pkt):
            encrypted_data, _ = pkt.rsplit('|', 1)
            decrypted = xor.decrypt(encrypted_data)
            received_stream.append(decrypted)
        else:
            received_stream.append("CORRUPTED_PACKET")

    # Display the results
    print("\nOriginal Packets:")
    for p in packets:
        print(" ", p)

    print("\nReceived Packets:")
    for p in received_stream:
        print(" ", p)