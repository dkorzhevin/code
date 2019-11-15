# Add data in RSI to existing data in RDX and move result from RDX to RSI. 
# In this particular case, not needed, but general purpose registers can be used: 
# RAX, RBX, RCX, RDX, RBP, RDI, RSI, R8 - R15. Stack usage prohibited.
#
# Dmytro Korzhevin
#
.text
.global main
main:
    addq %RSI, %RDX
    movq %RDX, %RSI
