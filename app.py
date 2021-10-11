# Imports
import sys
import socket

from os import system as execute, name as sysName
from time import sleep as wait

# Vars
args = sys.argv

try:
  ip = args[1]
except Exception as e:
  print('Falha nos argumentos, verifique e tente novamente.\n\nErr:\n', e)
  exit(1)

# Functions
def clear(): execute('cls' if sysName == 'nt' else 'clear')
  
def banner():
  clear()
  banner = [
    '',
    '           _____  _____       ',
    '     /\   |  __ \|  __ \      ',
    '    /  \  | |__) | |__) |   _ ',
    '   / /\ \ |  _  /|  ___/ | | |',
    '  / ____ \| | \ \| |   | |_| |',
    ' /_/    \_\_|  \_\_|    \__, |',
    '                         __/ |',
    '                        |___/ ',
    '                  By Ahosall - v1.0 ',
    '',
  ]

  for b in banner:
    print(b)

def getPorts():
  ports = []
  
  print(f'IP: {ip}\n\nAguarde um pouco ... coletando portas ...\n')
  
  for port in range(4000, 5000):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(.09)
    
    if client.connect_ex((ip, port)) == 0:
      ports.append(port)
      print(f'Open ... {port}')

  return ports

def getLocalesIPs(ports):
  banner()
  ipSplitted = ip.split('.')

  print('Ports:', str(ports))  
  for port in ports:
    print('\n=== Port', port)
    
    for newNum in range(1, 1000):
      client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      client.settimeout(.05)
      newIp = f'{ipSplitted[0]}.{ipSplitted[1]}.{ipSplitted[2]}.{newNum}'

      try:
        if client.connect_ex((newIp, port)) == 0:
          print(f'  {ipSplitted[0]}.{ipSplitted[1]}.{ipSplitted[2]}.{newNum}:{port} .... success')
      except:
        pass
  
# Main
def main():
  clear()
  banner()
  
  ports = getPorts()

  getLocalesIPs(ports)

# Init
try:
  if __name__ == '__main__':
    main()
except KeyboardInterrupt:
  print('\nSaindo...')