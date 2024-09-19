
def stop_read():
  packet = bytearray()
  packet.append(0x53)
  packet.append(0x57)
  packet.append(0x00)
  packet.append(0x03)
  packet.append(0xFF)
  packet.append(0x40)
  packet.append(0x14)
  return packet

def start_read():
  packet = bytearray()
  packet.append(0x53)
  packet.append(0x57)
  packet.append(0x00)
  packet.append(0x03)
  packet.append(0xFF)
  packet.append(0x41)
  packet.append(0x13)
  return packet

def release_relay():
  packet = bytearray()
  packet.append(0x53)
  packet.append(0x57)
  packet.append(0x00)
  packet.append(0x03)
  packet.append(0xFF)
  packet.append(0x86)
  packet.append(0xCE)
  return packet

def close_relay():
  packet = bytearray()
  packet.append(0x53)
  packet.append(0x57)
  packet.append(0x00)
  packet.append(0x03)
  packet.append(0xFF)
  packet.append(0x85)
  packet.append(0xCF)
  return packet

def start_routine():
  return [b'43', b'54']

def device_serial():
  return [b'c3', b'83', b'24', b'04', b'24', b'55', b'd6']

def calculate_checksum(data):
  checksum = 0
  for byte in data:
    checksum += byte
  checksum = (~checksum + 1) & 0xFF
  return checksum