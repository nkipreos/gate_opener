import serial
import commons
import time

def main():
  global ser, card_array
  card_array = []
  ser = serial.Serial(
    port='/dev/tty.usbserial-210',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout=0)

  ser.write(commons.start_read())
  ser.write(commons.close_relay())
  ser.flush()
  print("Setup complete")

  try:
    print("Waiting for start byte")
    while True:
      start_byte = ser.read().hex()
      if(bytes(start_byte, 'utf-8') == commons.start_routine()[0]):
        print("Start byte received")
        second_byte = ser.read().hex()
        if(bytes(second_byte, 'utf-8') == commons.start_routine()[1]):
          len_l = ser.read().hex()
          leng = int(bytes(len_l + ser.read().hex(), 'utf-8'), 16)
          for i in range(leng):
            print('x' + ser.read().hex(), end='')
          time.sleep(3)
          print("\n")
  except Exception as e:
    ser.close()
    f = open("error.txt", "a")
    f.write(str(e))
    f.close()

def compare_start_routine():
  for i in range(6):
    current_byte = ser.read().hex()
    if(bytes(current_byte, 'utf-8') != commons.start_routine()[i + 1]):
      return False
  return True

def compare_serial():
  for i in range(7):
    current_byte = ser.read().hex()
    if(bytes(current_byte, 'utf-8') != commons.device_serial()[i]):
      return False
  return True

def read_cards():
  num_cards = int(ser.read().hex(), 16)
  cards = []
  for i in range(num_cards):
    id_length = int(ser.read().hex(), 16)
    card_id = ''
    for j in range(id_length):
      card_id += ser.read().hex()
    cards.append(card_id)
  return cards

def include_in_card_list(card):
  with open('cards.txt', 'a') as f:
    if card not in card_array:
      card_array.append(card)
      f.write(card[0:-4] + '\n')

if __name__ == "__main__":
  main()