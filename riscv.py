
from ctypes import Union

from instructions import BType, IType, JType, RType, SType, UType


class RISCV:
    _XLEN = 32
    DEBUG = False

    def __init__(self) -> None:
        self.memory = [0b0] * (2**12)  # 4096 bytes
        # 32 registradores
        self.regs = {
            'x0': 0b0,
            'x1': 0b0,
            'x2': 0b0,
            'x3': 0b0,
            'x4': 0b0,
            'x5': 0b0,
            'x6': 0b0,
            'x7': 0b0,
            'x8': 0b0,
            'x9': 0b0,
            'x10': 0b0,
            'x11': 0b0,
            'x12': 0b0,
            'x13': 0b0,
            'x14': 0b0,
            'x15': 0b0,
            'x16': 0b0,
            'x17': 0b0,
            'x18': 0b0,
            'x19': 0b0,
            'x20': 0b0,
            'x21': 0b0,
            'x22': 0b0,
            'x23': 0b0,
            'x24': 0b0,
            'x25': 0b0,
            'x26': 0b0,
            'x27': 0b0,
            'x28': 0b0,
            'x29': 0b0,
            'x30': 0b0,
            'x31': 0b0,
            'pc': -1,  # current instruction
        }

    # Inicia um programa
    def start(self, filename):
        with open(filename, 'rb') as f:
            while True:
                # Le 32 bits
                data = f.read(4)
                if not data:
                    break
                # Transforma em inteiro
                binary_data = int.from_bytes(data, byteorder='little')
                # Caso pc seja -1, o programa começa no endereço 0
                if self.regs['pc'] == -1:
                    self.regs['pc'] = 0
                    mem_last = 0
                    # Salva a instrução na memória
                    self.memory[self.regs['pc']] = binary_data
                else:
                    self.memory[mem_last+1] = (binary_data)
                mem_last += 1

                if self.DEBUG:
                    print(f"Instrução carregada na memoria: mem[{mem_last}] ", bin(
                        binary_data).replace('0b', '').zfill(32))
        if(self.regs['pc'] != -1):
            self._run()

    # Executa o programa que está na memória
    def _run(self):

        # Enquanto houver instruções na memória
        while self.regs['pc'] < len(self.memory):
            # Le a instrução
            instruction = self.memory[self.regs['pc']]
            if instruction == 0:
                self.regs['pc'] += 1
                continue
            # Decodifica a instrução
            decoded = self._decode(instruction)
            # Executa a instrução
            self._execute(decoded)

    # Executa a instrução

    def _execute(self, instruction):
        # Executa a instrução
        instruction.execute(self)
        # Incrementa o PC
        self.regs['pc'] += 1

    # Decodifica a instrução
    def _decode(self, instruction):
        # Extrai o opcode para saber qual o tipo da instrução
        opcode = instruction & 0b00000000000000000000000001111111
        if self.DEBUG:
            print("Decodificando instrução")

        if opcode in IType.OPCODE:
            pc = IType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução I-Type")
                pc.print()
        elif opcode in RType.OPCODE:
            pc = RType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução R-Type")
                pc.print()
        elif opcode in SType.OPCODE:
            pc = SType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução S-Type")
                pc.print()
        elif opcode in BType.OPCODE:
            pc = BType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução B-Type")
                pc.print()
        elif opcode in UType.OPCODE:
            pc = UType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução U-Type")
                pc.print()
        elif opcode in JType.OPCODE:
            pc = JType.parse_instruction(instruction)
            if self.DEBUG:
                print("\n\tInstrução J-Type")
                pc.print()
        else:
            print("Fatal!! Unknown instruction", bin(
                instruction).replace('0b', '').zfill(32))
            exit(-1)
        return pc

    # Exibe o conteudo da memoria
    def print_mem(self):
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                continue
            print(
                f"{i} -> {bin(self.memory[i]).replace('0b', '').zfill(32)} == {self.memory[i]}")

    # Exibe todos os registradores
    def print_regs(self):
        for reg in self.regs:
            if self.regs[reg] == 0:
                continue
            print(
                f"{reg} -> {bin(self.regs[reg]).replace('0b', '').zfill(self._XLEN-1)} == {self.regs[reg]}")
