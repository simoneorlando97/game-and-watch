import sys 
from pwnlib.util.fiddling import xor 

if (len(sys.argv) <= 3):
  print("[?] Usage: " + sys.argv[0] + " flash.bin rom.bin keys.bin")
  sys.exit(-1)

flash_path = sys.argv[1]
rom_nes_path = sys.argv[2]
keys_path = sys.argv[3]

with open(flash_path, "rb") as reader:
  flash = reader.read()

with open(rom_nes_path, "rb") as reader:
  rom_nes = reader.read()

with open(keys_path, "rb") as reader:
  keys = reader.read()

xorred_rom = xor(rom_nes, keys)

rom_addr_in_flash = 0x1e60
rom_size = 0xa000
with open("./modified_flash.bin", "wb") as writer:
  writer.write(flash[0:rom_addr_in_flash])
  writer.write(xorred_rom)
  writer.write(flash[rom_addr_in_flash + rom_size:])


