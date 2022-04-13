
import sys

from riscv import RISCV

try:
    input = sys.argv[1]

    if input is None:
        print("Failed to open file")
        exit(-1)

    riscv = RISCV()
    riscv.DEBUG = True
    riscv.start(input)

    print("Registers: (Registers with zero are hidden)")
    riscv.print_regs()
    print("\nMemory: (Memory values empty are hidden)")
    riscv.print_mem()

except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)


