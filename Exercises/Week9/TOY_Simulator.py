
class TOY:
#There is no error checking of the description of the TOY program given in
#the input file! See example programs TOYEuclid and TOYFibonacci
    
# The state of the X-TOY machine is given by the values of the program counter,
# PC, values of the 16 registers, R[], and the content of the 256 words in the
# memory M[].

#The input to and output of TOY program is interacive and it is achieved
# by loading into a register from M[0xFF] and storing in location M[0xFF].

    def __init__(self, fileObj, pc):
    #Yields tokens in the description of the X-TOY program in the file fileObj
        def readToken(fileobj):
            for line in fileobj:
                for token in line.split(": "):
                    yield int(token,16)
        #boot the machine by loading a program an initializing the instance
        #variables that define the state of the machine. Also, prints
        #the X-TOY program as it is read.
        self.PC = pc & 0xFF
        self.R =[0x0000] * 16
        self.M = [0x0000] * 256
        f = open(fileObj, "r")
        tokenGen = readToken(f)
        hexNumAdd = next(tokenGen, "end")
        print("Program read")
        while hexNumAdd != "end":
            print("% 4.2x:"%(hexNumAdd), end = "")
            hexNumInst = next(tokenGen, "end")
            print("% 5.4x"%(hexNumInst))
            self.M[hexNumAdd&0xFF] = hexNumInst&0xFFFF
            hexNumAdd = next(tokenGen, "end")
        print()
        return

    def dump(self): #Show state of the machine
        print("Memory dump; aka, state of the machine")
        for i in range(16):
            for j in range(0,241,16):print("% 5.4x"%(self.M[j+i]), end = "")
            print()
        print()
        print("Registers")
        for i in range(16):
            print("R[%1.1x] = %4.4x"%(i,self.R[i]))
        print()
        print("Program counter")
        print("PC = %2.2x"%(self.PC))
        print()    
        return
    
    def run(self):
        while True:
            #Fetch
            IR = self.M[self.PC]
            #To trace the next command is useful 
            #print("Program counter: ", hex(self.PC),"$", "IR", hex(IR))
            #Increment program counter
            self.PC = (self.PC + 1) & 0xFF
            #Decode instruction and execute the instruction
            op = (IR >> 12) & 0xF
            d = (IR >> 8) & 0xF
            s = (IR >> 4) & 0xF
            t = (IR >> 0) & 0xF
            addr = (IR >> 0) & 0xFF
            # to handle interactive input. Read a 4-digit hex and store in M[FF]
            if (addr == 0xFF and op == 8) or (self.R[t] == 0xFF and op == 10):
                temp = int(input("Enter a 4 digit hex number: "),16) & 0xFFFF
                self.M[0xFF] = temp
            if op == 0x0: break
            elif op == 1: self.R[d] = self.R[s] + self.R[t]
            elif op == 2: self.R[d] = self.R[s] - self.R[t]
            elif op == 3: self.R[d] = self.R[s] & self.R[t]
            elif op == 4: self.R[d] = self.R[s] ^ self.R[t]
            elif op == 5: self.R[d] = self.R[s] << self.R[t]
            elif op == 6: self.R[d] = self.R[s] >> self.R[t]
            elif op == 7: self.R[d] = addr
            elif op == 8: self.R[d] = self.M[addr]
            elif op == 9: self.M[addr] = self.R[d]
            elif op == 10: self.R[d] = self.M[self.R[t]] & 0xFFFF
            elif op == 11: self.M[self.R[t]&0xFF] = self.R[d]
            elif op == 12:
                if self.R[d] == 0: self.PC = addr
            elif op == 13: #test if R[d] > 0!!
                if (self.R[d]&0x8000 == 0) and (self.R[d]&0x7FFF != 0):self.PC = addr
            elif op == 14: self.PC = self.R[d] & 0xFF
            elif op == 15:
                self.R[d] = self.PC
                self.PC = addr
            else: print("Glup!")
            #to handle interactive output. Print content of M[FF]
            if (addr == 0xFF and op == 9) or (self.R[t] == 0xFF and op == 11):
                print("Output value: ", hex(self.M[0xFF]))
                print()
            #Make sure R[0] remains a 0 and result of
            #operations are always 16 bits -no check for overflow!
            self.R[0] = 0
            self.R[d] = self.R[d] & 0xFFFF
        return  
def main():
    inputFile = input("Name of the file describing the TOY program: ")
    pc = int(input("Enter the starting address of the TOY program in HEX: "),16)
    #Reset simulation to a read program and starting address in memory
    TOYpgm = TOY(inputFile,pc)
    
    # Output the state of the simulated machine; i.e., show memory,
    # content of registers and program counter.
    #TOYpgm.dump()
    # Simulate the program read
    TOYpgm.run()
    # Show state of the machine at the end of the simulation
    TOYpgm.dump()
    return
main()
