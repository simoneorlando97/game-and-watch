import sys 
from pwnlib.util.fiddling import xor 



if (len(sys.argv) <= 1):
  print("[?] Usage: " + sys.argv[0] + " file.bin")
  sys.exit(-1)

flash_path = sys.argv[1]
rom_nes_path = sys.argv[2]

with open(flash_path, "rb") as reader:
  flash = reader.read()


with open(rom_nes_path, "rb") as reader:
  rom_nes = reader.read()

# Modifico la flash fin quando non vedo una modifica 
# nella rom del gioco in ram. Calcolo l'offset in ram
# tra la modifica e l'inizio della rom. Uso questo offset 
# per trovare l'inizio della rom nella flash semplicemente 
# sommandolo a dove avevo fatto la modifica.
rom_addr_in_flash = 0x1e60
rom_size = 0xa000 #bytes
keys = xor(flash[rom_addr_in_flash:rom_addr_in_flash+rom_size],rom_nes)

with open("./keys_stream.bin","wb") as writer:
  writer.write(keys)

