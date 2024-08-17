def NAND(A,B): #Creating NAND Gate to be used in the other logic gates
    return not (A and B)

def AND_Gate(A,B):
    return NAND(NAND(A,B),NAND(A,B))

def OR_Gate(A,B):
    return NAND(NAND(A,A),NAND(B,B))

def NOR_Gate(A,B):
    return NAND(NAND(NAND(A,A),NAND(B,B)),NAND(NAND(A,A),NAND(B,B)))

def XOR_Gate(A,B):
    return NAND(NAND(NAND(A,A),B),NAND(NAND(B,B),A))

def NOT_Gate(A):
    return(NAND(A,A))