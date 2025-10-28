import random
import matplotlib.pyplot as plt
import numpy as np

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


def add_noise(packet, error_rate=0.001):
    packet = list(packet)
    for i in range(len(packet)):
        if random.random() < error_rate:
            packet[i] = chr(random.randint(32, 126))
    return ''.join(packet)

def simulate(error_rate, trials):

    """
    Runs the secure telemetry pipeline for many packets
    and returns packet success rate as a fraction 0.0–1.0.
    """
    key = "key123456789"
    xor = XORCipher(key)

    packets = generate_telemetry(trials)
    success_count = 0

    for p in packets:
        # Encrypt Data
        encrypted = xor.encrypt(p)
        # Add CRC-8
        pkt = add_crc8(encrypted)

        # Noise
        noisy = add_noise(pkt, error_rate)

        # Verify + decrypt if valid
        if verify_crc(noisy):
            success_count += 1
    return success_count / trials

if __name__ == "__main__":
    trials = 200
    noise_levels = np.linspace(0.0, 1.0, 30)   # evenly spaced noise rates (0% → 100%)
    repetitions = 10                           # run each noise level multiple times for averaging

    mean_success = []
    std_success = []

    for n in noise_levels:
        # Generate mean success rate
        rates = [simulate(n, trials) for _ in range(repetitions)]
        mean_success.append(np.mean(rates))
        std_success.append(np.std(rates))
        print(f"Noise={n:.2f} → Mean Success={np.mean(rates):.3f}")

    # === PLOT RESULTS ===
    plt.figure()
    plt.plot(noise_levels, std_success, marker='o')
    plt.xlabel("Noise (error probability)")
    plt.ylabel("Packet Success Rate")
    plt.title("Effect of Noise on Secure Telemetry Transmission")
    plt.grid(True)
    plt.show()