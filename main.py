import os
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

except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)


