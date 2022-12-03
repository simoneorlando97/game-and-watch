import sys 
from pwnlib.util.fiddling import xor 

if (len(sys.argv) <= 1):
  print("[?] Usage: " + sys.argv[0] + " ram.bin")
  sys.exit(-1)

ram_path = sys.argv[1]

with open(ram_path,"rb") as reader:
  ram = reader.read()

rom_size = 0xa000
with open("./rom_ext.bin", "wb") as writer:
  writer.write(ram[:rom_size])