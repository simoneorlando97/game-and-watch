import sys 

rom_path = sys.argv[1]

with open(rom_path, "rb") as reader:
  rom = reader.read()

with open("./pad_rom.bin", "wb") as writer:
  writer.write(rom)
  writer.write(b"\x00" * (40960 - len(rom)))