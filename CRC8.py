#Basic Implementation of CRC-8 in Python

def crc8(data):
    crc = 0x00 # Initial CRC value
    poly = 0x07 # CRC-8 Polynomial -> x^8 + x^2 + x + 1

    for byte in data:
        crc ^= ord(byte) # XOR operation, similar to subtraction in polynomial division
        for _ in range(8): # Since using 8-bits
            
            if(crc & 0x80): # Checking if MSB is 1, 0x80 = 10000000 in binary
                crc = (crc << 1) ^ poly # Shifting register is similar to multiplication step
            else:
                crc <<= 1 # Just shift left if MSB is 0
                
            crc &= 0xFF # Ensure CRC remains within 8-bits        
    return crc


def add_crc8(data):
    checksum = crc8(data)
    return f"{data}|{checksum}"

def verify_crc(packet):
    try:
        msg, crc_str = packet.rsplit('|', 1)
        received = int(crc_str)

        return received == crc8(msg)
    except:
        return False