# 🛰️ Secure Telemetry Transmission Simulation
### Lightweight XOR Encryption + CRC-8 Integrity Check

This project simulates a **secure telemetry communication system** between an aircraft and a ground station.  
It demonstrates how **XOR encryption** (for confidentiality) and **CRC-8 checksum** (for integrity) can be combined to model reliable, low-resource data transmission over a noisy communication channel.

---

## ⚙️ Features

- Generates simulated aircraft telemetry packets (altitude, speed, heading)  
- Encrypts packets with a symmetric XOR cipher  
- Appends CRC-8 checksum for corruption detection  
- Simulates noisy transmission channels  
- Evaluates packet success rate across varying error probabilities  
- Visualizes the results as a graph

---

## 📁 Project Structure

```
project/
 ├── main.py             # Main simulation script
 ├── XORCipher.py        # XOR cipher implementation
 ├── CRC8.py             # CRC-8 checksum calculation
 ├── assets/Figure_1.png # Simulation result figure
 ├── REPORT.md           # Full technical report
 └── README.md           # Project overview (this file)
```

## 🚀 Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Nafim-Ershad/XORCipher.git
```
```bash
cd XORCipher
```

### 2️⃣ Run the Simulation

```bash
python main.py
```

### 3️⃣ View Results

The simulation will print noise vs. success rate values in the terminal and generate a graph

## 🧑‍💻 Author

Nafim Ershad Inan <br>
Military Institute of Science and Technology (MIST) <br>
📧 inan.nafim1089@outlook.com