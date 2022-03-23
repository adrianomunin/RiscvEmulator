import instructions

instructions_opcodes = {
    'ADDI': instructions.ADDI,
}


def extract_r_type(data):
    # Extrai os dados de um instrução do tipo R
    return instructions.RType.parse_instruction(data)
