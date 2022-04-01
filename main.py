import sys

from instructions import IType, RType, SType

input = sys.argv[1]

if input is None:
    print("Failed to open file")
    exit(-1)

f = open(input, 'rb')
while(True):
    # read 32 bits from input and print in binary form
    data = f.read(4)
    if not data:
        break

    binary_data = int.from_bytes(data, byteorder='little')

    print("Instrução", bin(binary_data).replace('0b', '').zfill(32))

    opcode = binary_data & 0b00000000000000000000000001111111
    #print("OPCODE", bin(opcode).replace('0b', '').zfill(7))

    if opcode == IType.OPCODE:
        print("IType")
        pc = IType.parse_instruction(binary_data)
        pc.print()
    elif opcode == RType.OPCODE:
        print("RType")
        pc = RType.parse_instruction(binary_data)
        pc.print()
    elif opcode == SType.OPCODE:
        print("SType")
        pc = SType.parse_instruction(binary_data)
        pc.print()
        pass
