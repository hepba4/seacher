import socket
import threading
from queue import Queue
from colorama import Fore, Style

print_lock = threading.Lock()
print('''                              ███                     
                                       ░░░                      
  █████   ██████   ██████   ████████   ████  ████████    ███████
 ███░░   ███░░███ ░░░░░███ ░░███░░███ ░░███ ░░███░░███  ███░░███
░░█████ ░███ ░░░   ███████  ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ░░░░███░███  ███ ███░░███  ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ██████ ░░██████ ░░████████ ████ █████ █████ ████ █████░░███████
░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                        ███ ░███
                                                       ░░██████ 
                                                        ░░░░░░  ''')
print("Scanning")
target = input(Fore.YELLOW + "Введите IP-адрес: " + Style.RESET_ALL)
targetIP = socket.gethostbyname(target)
print(".")
n_threads = 200
input(Fore.YELLOW + f"Для продолжения нажмите ENTER  " + Style.RESET_ALL)
ports = range(1, 9999)
open_ports = []

def port_scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((targetIP, port))
        with print_lock:
            if result == 0:
                print(Fore.GREEN + f"[+] Порт {port} открыт " + Style.RESET_ALL)
                open_ports.append(port)
            else:
                print(Fore.RED + f"[-] Порт {port} закрыт " + Style.RESET_ALL)
    except:
        pass
    finally:
        sock.close()

def scan_thread():
    while True:
        port = ports_queue.get()
        port_scan(port)
        ports_queue.task_done()

ports_queue = Queue()

for t in range(n_threads):
    thread = threading.Thread(target=scan_thread)
    thread.daemon = True
    thread.start()

for port in ports:
    ports_queue.put(port)

ports_queue.join()

print(f"Открытые порты на {targetIP}:")
print(open_ports)
print(".")
