from scapy.all import Ether, IP, UDP, sendp

# Визначте розмір пакету в байтах
packet_size_bytes = 125000  # Розмір пакету в байтах (1 байт = 8 біт)

# Визначте швидкість передачі в бітах за секунду (85 Мбіт)
transmission_speed_bps = 85000000  # 85 Мбіт = 85,000,000 біт

# Визначте інтервал між відправкою пакетів (у секундах)
packet_send_interval = packet_size_bytes * 8 / transmission_speed_bps

# Функція для створення та відправки пакету
def send_packet():
    # Створіть UDP-пакет з визначеним розміром
    packet = Ether() / IP() / UDP(Raw(b'\x00' * packet_size_bytes))

    # Відправте пакет
    sendp(packet, iface="your_network_interface")

# Відправляйте пакети з вказаним інтервалом
while True:
    send_packet()
    time.sleep(packet_send_interval)
