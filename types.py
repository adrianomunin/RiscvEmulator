
instructions_opcodes = {

}


class RType:
    opcode = 0x000
    rd = 0x000
    rs1 = 0x000
    rs2 = 0x000
    funct3 = 0x000
    funct7 = 0x000

    def __init__(self) -> None:
        pass


class IType:
    opcode = 0x000
    rd = 0x000
    funct3 = 0x000
    rs1 = 0x000
    imm = 0x000

    def __init__(self) -> None:
        pass


class SType:
    opcode = 0x000
    imm4_0 = 0x000
    funct3 = 0x000
    rs1 = 0x000
    rs2 = 0x000
    imm11_5 = 0x000

    def __init__(self) -> None:
        pass
