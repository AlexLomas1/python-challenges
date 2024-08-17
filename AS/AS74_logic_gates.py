def nand(a,b): # Creating NAND Gate to be used in the other logic gates
    return not (a and b)

def and_gate(a,b):
    return nand(nand(a,b),nand(a,b))

def or_gate(a,b):
    return nand(nand(a,a),nand(b,b))

def nor_gate(a,b):
    return nand(nand(nand(a,a),nand(b,b)),nand(nand(a,a),nand(b,b)))

def xor_gate(a,b):
    return nand(nand(nand(a,a),b),nand(nand(b,b),a))

def not_gate(a):
    return(nand(a,a))