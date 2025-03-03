import socket
import concurrent.futures
import pyfiglet
from colorama import Fore, Style

def display_startup_screen():
    ascii_banner = pyfiglet.figlet_format("KRscan", font="standard")
    print(Fore.BLUE + ascii_banner + Style.RESET_ALL)
    print(Fore.YELLOW + "Made by kryp10n" + Style.RESET_ALL)

def scan_port(target, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target, port))
            if result == 0:
                return port, "OPEN"
    except:
        pass
    return port, "CLOSED"

def scan_ports(target, ports, timeout):
    open_ports = []
    closed_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target, p, timeout), ports)
        for port, status in results:
            if status == "OPEN":
                open_ports.append(port)
            else:
                closed_ports.append(port)
    return open_ports, closed_ports

def get_ports():
    print(Fore.YELLOW + "\nSelect scan mode:" + Style.RESET_ALL)
    print("1. Default")
    print("2. Slow")
    print("3. Fast")
    print("4. Custom")
    mode = input("Choose: ")
    
    if mode == "1":
        return range(1, 1025)
    elif mode == "2":
        return range(1, 65536)
    elif mode == "3":
        return [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 3389, 5900, 8080]
    else:
        print(Fore.RED + "Invalid mode!" + Style.RESET_ALL)
        exit()

def get_timeout():
    print(Fore.YELLOW + "\nSelect scan speed:" + Style.RESET_ALL)
    print("1. Default")
    print("2. Slow")
    print("3. Fast")
    print("4. Custom")
    choice = input("Choose: ")
    
    if choice == "1":
        return 0.5
    elif choice == "2":
        return 1.0
    elif choice == "3":
        return 0.3
    elif choice == "4":
        try:
            custom_timeout = float(input("Enter custom timeout (seconds): "))
            return max(0.1, custom_timeout)
        except ValueError:
            print(Fore.RED + "Invalid input! Using default timeout." + Style.RESET_ALL)
            return 0.5
    else:
        print(Fore.RED + "Invalid choice! Using default timeout." + Style.RESET_ALL)
        return 0.5

def main():
    display_startup_screen()
    timeout = get_timeout()
    ports = get_ports()
    target = input(Fore.YELLOW + "\nEnter target IP/Domain: " + Style.RESET_ALL)
    
    print(Fore.CYAN + f"\nScanning {target}..." + Style.RESET_ALL)
    open_ports, closed_ports = scan_ports(target, ports, timeout)
    
    if open_ports:
        print(Fore.GREEN + f"\nOpen Ports: {', '.join(map(str, open_ports))}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "\nNo open ports found." + Style.RESET_ALL)
    
    if closed_ports:
        print(Fore.YELLOW + f"\nClosed Ports: {', '.join(map(str, closed_ports[:10]))}..." + Style.RESET_ALL)
    
if __name__ == "__main__":
    main()

