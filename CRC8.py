# Simple implementation of CRC-8 Checksum calculation and verification.

def crc8(data: str) -> int:
    crc = 0x00
    poly = 0x07
    for char in data:
        crc ^= ord(char)
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFF
    return crc


def add_crc8(packet: str) -> str:
    checksum = crc8(packet)
    return f"{packet}|{checksum}"


def verify_crc(packet: str) -> bool:
    try:
        data, crc_str = packet.rsplit('|', 1)
        received_crc = int(crc_str)
        return received_crc == crc8(data)
    except:
        return False