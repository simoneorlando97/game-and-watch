import sys 

if (len(sys.argv) <= 2):
  print("[?] Usage: " + sys.argv[0] + " flash.bin mod_flash.bin")
  sys.exit(-1)

flash_path = sys.argv[1]
mod_flash_path = sys.argv[2]

with open(flash_path, "rb") as reader:
  flash = reader.read()

with open(mod_flash_path, "rb") as reader:
  mod_flash = reader.read()

if flash != mod_flash:
      print("Diversi!")
      sys.exit()

print("Uguali!")