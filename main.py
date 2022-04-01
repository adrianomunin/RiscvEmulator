import sys

from instructions import BType, IType, JType, RType, SType, UType

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

    if opcode in IType.OPCODE:
        print("IType")
        pc = IType.parse_instruction(binary_data)
        pc.print()
    elif opcode in RType.OPCODE:
        print("RType")
        pc = RType.parse_instruction(binary_data)
        pc.print()
    elif opcode in SType.OPCODE:
        print("SType")
        pc = SType.parse_instruction(binary_data)
        pc.print()
    elif opcode in BType.OPCODE:
        print("BType")
        pc = BType.parse_instruction(binary_data)
        pc.print()
    elif opcode in UType.OPCODE:
        print("UType")
        pc = UType.parse_instruction(binary_data)
        pc.print()
    elif opcode in JType.OPCODE:
        print("JType")
        pc = JType.parse_instruction(binary_data)
        pc.print()
    else:
        print("Unknown instruction", bin(
            binary_data).replace('0b', '').zfill(32))
        exit(-1)
