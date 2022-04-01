

class RType:

    OPCODE = int(0b00000000000000000000000000110011)

    def __init__(self, opcode, rd, rs1, rs2, funct3, funct7) -> None:
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.funct3 = funct3
        self.funct7 = funct7

    def print(self):
        # Imprime os dados da classe
        print("opcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("rd:", bin(self.rd).replace('0b', '').zfill(5))
        print("rs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("rs2:", bin(self.rs2).replace('0b', '').zfill(5))
        print("funct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("funct7:", bin(self.funct7).replace('0b', '').zfill(7))
        print("\n")

    @staticmethod
    def parse_instruction(instruction):
        # Parseia a instrução e retorna um objeto RType
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        funct3_mask = 0b00000000000000000111000000000000
        rs1_mask = 0b00000000000111110000000000000000
        rs2_mask = 0b00000011111000000000000000000000
        funct7_mask = 0b11111110000000000000000000000000

        return RType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     (instruction & rs1_mask) >> 15,
                     (instruction & rs2_mask) >> 20,
                     (instruction & funct3_mask) >> 12,
                     (instruction & funct7_mask) >> 25)


class IType:
    OPCODE = int(0b00000000000000000000000000010011)

    def __init__(self, opcode, rd, rs1, funct3, imm) -> None:
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.funct3 = funct3
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("opcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("rd:", bin(self.rd).replace('0b', '').zfill(5))
        print("rs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("funct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("imm:", bin(self.imm).replace('0b', '').zfill(12))
        print("\n")

    @staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        rs1_mask = 0b00000000000111110000000000000000
        imm_mask = 0b11111111110000000000000000000000
        funct3_mask = 0b00000000000000000111000000000000

        return IType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     (instruction & rs1_mask) >> 15,
                     (instruction & funct3_mask) >> 12,
                     (instruction & imm_mask) >> 20)


class SType:

    OPCODE = int(0b00000000000000000000000000100011)

    def __init__(self, opcode, funct3, rs1, rs2, imm) -> None:
        self.opcode = opcode
        self.funct3 = funct3
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("opcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("funct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("rs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("rs2:", bin(self.rs2).replace('0b', '').zfill(5))
        print("imm:", bin(self.imm).replace('0b', '').zfill(12))
        print("\n")

    @ staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        imm4_0_mask = 0b00000000000000000000111110000000
        funct3_mask = 0b00000000000000000111000000000000
        rs1_mask = 0b00000000000011111000000000000000
        rs2_mask = 0b00000001111100000000000000000000
        imm11_5_mask = 0b11111110000000000000000000000000

        return SType(instruction & opcode_mask,
                     (instruction & funct3_mask) >> 12,
                     (instruction & rs1_mask) >> 15,
                     (instruction & rs2_mask) >> 20,
                     ((instruction & imm11_5_mask) >> 20) + (instruction & imm4_0_mask))
