

class RType():

    OPCODE = [int(0b00000000000000000000000000110011)]

    def __init__(self, opcode, rd, rs1, rs2, funct3, funct7) -> None:
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.rs2 = rs2
        self.funct3 = funct3
        self.funct7 = funct7

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\trd:", bin(self.rd).replace('0b', '').zfill(5))
        print("\trs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("\trs2:", bin(self.rs2).replace('0b', '').zfill(5))
        print("\tfunct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("\tfunct7:", bin(self.funct7).replace('0b', '').zfill(7))
        print("\n")

    def __str__(self):
        # Retorna a instrução em binário
        return bin(self.opcode).replace('0b', '').zfill(7) + \
            bin(self.rd).replace('0b', '').zfill(5) + \
            bin(self.rs1).replace('0b', '').zfill(5) + \
            bin(self.rs2).replace('0b', '').zfill(5) + \
            bin(self.funct3).replace('0b', '').zfill(3) + \
            bin(self.funct7).replace('0b', '').zfill(7)

    def execute(self, riscv):
        # Executa a instrução
        if self.funct3 == 0b000 and self.funct7 == 0b0000000:  # ADD
            if riscv.DEBUG:
                print(
                    f"x{self.rd} = x{self.rs1} ({riscv.regs[f'x{self.rs1}']}) + x{self.rs2} ({riscv.regs[f'x{self.rs2}']})\n")
            riscv.regs[f'x{self.rd}'] = riscv.regs[f'x{self.rs1}'] + \
                riscv.regs[f'x{self.rs2}']
        elif self.funct3 == 0b000 and self.funct7 == 0b0100000:  # SUB
            if riscv.DEBUG:
                print(
                    f"x{self.rd} = x{self.rs1} ({riscv.regs[f'x{self.rs1}']}) - x{self.rs2} ({riscv.regs[f'x{self.rs2}']})\n")
            riscv.regs[f'x{self.rd}'] = riscv.regs[f'x{self.rs1}'] - \
                riscv.regs[f'x{self.rs2}']
        else:
            print("Fatal!! Unknown instruction", self.__str__())
            exit(-1)

    def parse_instruction(instruction):
        # Parseia a instrução e retorna um objeto RType
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        funct3_mask = 0b00000000000000000111000000000000
        rs1_mask = 0b00000000000011111000000000000000
        rs2_mask = 0b00000001111100000000000000000000
        funct7_mask = 0b11111110000000000000000000000000

        return RType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     (instruction & rs1_mask) >> 15,
                     (instruction & rs2_mask) >> 20,
                     (instruction & funct3_mask) >> 12,
                     (instruction & funct7_mask) >> 25)


class IType():
    OPCODE = [int(0b00000000000000000000000000100111),
              int(0b00000000000000000000000000000011),
              int(0b00000000000000000000000000010011)]

    def __init__(self, opcode, rd, rs1, funct3, imm) -> None:
        self.opcode = opcode
        self.rd = rd
        self.rs1 = rs1
        self.funct3 = funct3
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\trd:", bin(self.rd).replace('0b', '').zfill(5), self.rd)
        print("\trs1:", bin(self.rs1).replace('0b', '').zfill(5), self.rs1)
        print("\tfunct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("\timm:", bin(self.imm).replace('0b', '').zfill(12), self.imm)
        print("\n")

    def __str__(self):
        # Retorna a instrução em binário
        return bin(self.opcode).replace('0b', '').zfill(7) + \
            bin(self.rd).replace('0b', '').zfill(5) + \
            bin(self.rs1).replace('0b', '').zfill(5) + \
            bin(self.funct3).replace('0b', '').zfill(3) + \
            bin(self.imm).replace('0b', '').zfill(12)

    def execute(self, riscv):
        # Executa a instrução
        if self.funct3 == 0b000:  # ADDI
            riscv.regs[f'x{self.rd}'] = riscv.regs[f'x{self.rs1}'] + self.imm
        else:
            print("Fatal!! Unknown instruction", self.__str__())
            exit(-1)

    @staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        funct3_mask = 0b00000000000000000111000000000000
        rs1_mask = 0b00000000000011111000000000000000
        imm_mask = 0b11111111111100000000000000000000

        return IType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     (instruction & rs1_mask) >> 15,
                     (instruction & funct3_mask) >> 12,
                     (instruction & imm_mask) >> 20)


class SType:

    OPCODE = [int(0b00000000000000000000000000100011)]

    def __init__(self, opcode, funct3, rs1, rs2, imm) -> None:
        self.opcode = opcode
        self.funct3 = funct3
        self.rs1 = rs1
        self.rs2 = rs2
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\tfunct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("\trs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("\trs2:", bin(self.rs2).replace('0b', '').zfill(5))
        print("\timm:", bin(self.imm).replace('0b', '').zfill(12))
        print("\n")

    def execute(self, riscv):
        pass

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
                     ((instruction & imm11_5_mask) >> 21) + (instruction & imm4_0_mask) >> 7)


class BType:

    OPCODE = [int(0b00000000000000000000000001100011)]

    def __init__(self, opcode, rs1, rs2, funct3, imm) -> None:
        self.opcode = opcode
        self.rs1 = rs1
        self.rs2 = rs2
        self.funct3 = funct3
        self.imm = imm

    def execute(self, riscv):
        pass

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\trs1:", bin(self.rs1).replace('0b', '').zfill(5))
        print("\trs2:", bin(self.rs2).replace('0b', '').zfill(5))
        print("\tfunct3:", bin(self.funct3).replace('0b', '').zfill(3))
        print("\timm:", bin(self.imm).replace('0b', '').zfill(12))
        print("\n")

    @staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        imm11_mask = 0b00000000000000000000000010000000
        imm4_1_mask = 0b00000000000000000000111100000000
        funct3_mask = 0b00000000000000000111000000000000
        rs1_mask = 0b00000000000011111000000000000000
        rs2_mask = 0b00000001111100000000000000000000
        imm10_5_mask = 0b01111110000000000000000000000000
        imm12_mask = 0b10000000000000000000000000000000

        return BType(instruction & opcode_mask,
                     (instruction & rs1_mask) >> 15,
                     (instruction & rs2_mask) >> 20,
                     (instruction & funct3_mask) >> 12,
                     ((instruction & imm12_mask) >> 19) + ((instruction & imm11_mask) << 4) + ((instruction & imm10_5_mask) >> 20) + ((instruction & imm4_1_mask) >> 7))


class UType:
    OPCODE = [int(0b00000000000000000000000000110111)]

    def __init__(self, opcode, rd, imm) -> None:
        self.opcode = opcode
        self.rd = rd
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\trd:", bin(self.rd).replace('0b', '').zfill(5))
        print("\timm:", bin(self.imm).replace('0b', '').zfill(20))
        print("\n")

    def execute(self, riscv):
        pass

    @staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        imm_mask = 0b11111111111111111111000000000000

        return UType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     (instruction & imm_mask))


class JType:

    OPCODE = [int(0b00000000000000000000000001101111)]

    def __init__(self, opcode, rd, imm) -> None:
        self.opcode = opcode
        self.rd = rd
        self.imm = imm

    def print(self):
        # Imprime os dados da classe
        print("\topcode:", bin(self.opcode).replace('0b', '').zfill(7))
        print("\trd:", bin(self.rd).replace('0b', '').zfill(5))
        print("\timm:", bin(self.imm).replace('0b', '').zfill(20))
        print("\n")

    def execute(self, riscv):
        pass

    @staticmethod
    def parse_instruction(instruction):
        opcode_mask = 0b00000000000000000000000001111111
        rd_mask = 0b00000000000000000000111110000000
        imm19_12_mask = 0b00000000000011111111000000000000
        imm11_mask = 0b00000000000100000000000000000000
        imm10_1_mask = 0b01111111111000000000000000000000
        imm20_mask = 0b10000000000000000000000000000000

        return JType((instruction & opcode_mask),
                     (instruction & rd_mask) >> 7,
                     ((instruction & imm20_mask) >> 11) + (instruction & imm19_12_mask) + ((instruction & imm11_mask) >> 9) + ((instruction & imm10_1_mask) >> 20))
