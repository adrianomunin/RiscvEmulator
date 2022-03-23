

class RType:
    __opcode_mask = 0b00000000000000000000000001111111
    __rd_mask = 0b00000000000000000000111110000000
    __funct3_mask = 0b00000000000000000111000000000000
    __rs1_mask = 0b00000000000111110000000000000000
    __rs2_mask = 0b00000011111000000000000000000000
    __funct7_mask = 0b11111110000000000000000000000000
    opcode = 0b000
    rd = 0b000
    rs1 = 0b000
    rs2 = 0b000
    funct3 = 0b000
    funct7 = 0b000

    def __init__(self, opcode, rd, rs1, rs2, funct3, funct7) -> None:
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.funct3 = funct3
        self.funct7 = funct7
        pass

    @staticmethod
    def parse_instruction(instruction):
        # Parseia a instrução e retorna um objeto RType
        return RType(instruction & RType.__opcode_mask, instruction & RType.__rd_mask,)


class IType:
    opcode = 0b000
    rd = 0b000
    funct3 = 0b000
    rs1 = 0b000
    imm = 0b000

    def __init__(self) -> None:
        pass


class SType:
    opcode = 0b000
    imm4_0 = 0b000
    funct3 = 0b000
    rs1 = 0b000
    rs2 = 0b000
    imm11_5 = 0b000

    def __init__(self) -> None:
        pass


ADDI = RType()
