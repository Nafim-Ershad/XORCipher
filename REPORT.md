# Secure Telemetry Transmission Simulation using XOR Encryption and CRC-8 Integrity Check

**Author:** Nafim Ershad Inan  
**Date:** October, 2025  

---

## Abstract

This project simulates secure telemetry communication between an aircraft and a ground station. The system employs a **lightweight XOR-based cipher** to ensure data confidentiality and a **CRC-8 checksum** to detect corruption during transmission. A random noise model introduces character-level errors to emulate a noisy communication channel. 

---

## Background and Motivation

Telemetry links in UAVs and small satellites operate in **noisy, bandwidth-limited, and power-constrained** environments. Implementing full-scale encryption or complex error correction is often infeasible on low-end embedded processors.  

This study demonstrates how simple yet effective mechanisms—**XOR encryption for confidentiality** and **CRC-8 for integrity**—can be combined to form a lightweight secure telemetry protocol.

---

## Methodology

### 1. Data Generation
The system generates random aircraft telemetry packets:
```text
<altitude (m)>, <speed (m/s)>, <heading (deg)>
```
Each packet is approximately 21 characters long.
Example: 
```text
10052.75,268.11,142.37
```

### 2. Encryption (XOR Cipher)
A class has be created for the encryption and decryption of the packets. The encryption is done by the following:

```python
encrypted = xor.encrypt(packet)
```
This provides lightweight symmetric encryption suitable for resource-limited systems.

### 3. Integrity Check (CRC-8)
After encryption, a CRC-8 checksum is computed and appended:
```python
packet_crc = add_crc8(encrypted)
```
CRC-8 uses the polynomial:

$x^8 + x^2 + x + 1$ (0x07)

which is a standard, hardware-friendly choice for 8-bit integrity checks.

### 4. Noise Simulation
Channel noise is modeled by randomly replacing characters in the packet with printable ASCII characters at a configurable error rates:

```python
noisy = add_noise(pkt, error_rate)
```
This simulates transmission corruption caused by interference or bit flips.

### 5. Verification and Decryption
**On the receiver side:**<br>
CRC-8 is verified using `verify_crc(packet)`. If valid, the encrypted payload is decrypted using the same XOR key.
If invalid, the packet is flagged as corrupted.

## Experimental Setup
| Parameter      | Description                     | Value     |
| -------------- | ------------------------------- | --------- |
| Trials         | Packets per simulation run      | 200       |
| Noise range    | Error probability per character | 0.0 – 1.0 |
| Packet length  | 21                              | —         |
| Encryption key | `"key123456789"`                | —         |
| CRC polynomial | `x⁸ + x² + x + 1` (0x07)        | —         |

Each packet was independently encrypted, transmitted through a noisy channel, and verified at the receiver. The simulation was repeated for various and random noise probabilities to determine the packet success rate (fraction of correctly received packets).

## Result
