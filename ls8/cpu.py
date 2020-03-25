"""CPU functionality."""

import sys

LDI = 0b10000010 # Load and Increment
PRN = 0b01000111 # Print
HLT = 0b00000001 # Halt
MUL = 0b10100010 # Multiply
MOD = 0b10100100 # Modulo
DIV = 0b10100011 # Divide
SUB = 0b10100001 # Subtract
ADD = 0b10100000 # Add
AND = 0b10101000 # And
NOT = 0b01101001 # Not
OR  = 0b10101010 # Or
XOR = 0b10101011 # Xor
SHL = 0b10101100 #
SHR = 0b10101101 #
INC = 0b01100101 # Increment
DEC = 0b01100110 # Decrement
CMP = 0b10100111 #


class CPU:
    """Main CPU class."""

    def __init__(self):
        self.pc = 0
        self.ram = [int] * 256
        self.reg = [0] * 8

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010,  # LDI R0,8
            0b00000000,
            0b00001000,
            0b10000010, # LDI R1,9
            0b00000001,
            0b00001001,
            0b10100010,  # MUL R0,R1
            0b00000000,
            0b00000001,
            0b01000111,  # PRN R0
            0b00000000,
            0b00000001,  # HLT

        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] = self.reg[reg_a] * self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def ram_read(self, pc):
        return self.ram[pc]

    def ram_write(self, pc, value):
        self.ram[pc] = value

    def run(self):
        running = True
        while running:
            command = self.ram[self.pc]
            if command == HLT:
                running = False

            elif command == PRN:
                print(self.reg[self.ram[self.pc+1]])
                self.pc += 2

            elif command == LDI:
                self.reg[self.ram[self.pc+1]] = self.ram[self.pc+2]
                self.pc += 3

            elif command == MUL:
                self.alu("MUL", self.ram[self.pc+1], self.ram[self.pc+2])
                self.pc += 3

            elif command == SUB:
                self.alu("SUB", self.ram[self.pc+1], self.ram[self.pc+2])
                self.pc += 3

            elif command == SUB:
                self.alu("ADD", self.ram[self.pc+1], self.ram[self.pc+2])
                self.pc += 3

