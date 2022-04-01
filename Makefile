all: link.ld main.s
	riscv64-linux-gnu-gcc -march=rv64g -static -nostdlib -nostartfiles -T link.ld main.s
	riscv64-linux-gnu-objcopy -O binary --only-section=.text a.out prog.bin

clean:
	rm -f *.out prog.bin
