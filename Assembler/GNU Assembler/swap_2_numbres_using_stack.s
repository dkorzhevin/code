# We need to swap 2 numbers, stored in RSI and RDX between them. All other general purpose registers
# should be restored to original values, in case they will be used.
# Next general purpose registers could be used:  RAX, RBX, RCX, RDX, RBP, RDI, RSI, R8 - R15
# Stack should be used in this case, but should be restored to original state.
# XOR/XCHG should not be used. I.e. XCHG %RSI, %RDX not allowed in this case.
#
# Dmytro Korzhevin
#
.text
.global main
main:
    pushq %RSI # put RSI contents in stack
    pushq %RDX # put RDX contents in stack
    popq %RSI  # move RDX value stored in stack as most recent to register RSI. RSP will be reduced by 8
    popq %RDX  # move RSI value from stack to RDX. Reduce RSP by 8 and stack will be restored to original state
    
