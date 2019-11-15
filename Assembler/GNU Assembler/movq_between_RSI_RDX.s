# Swap values between RSI and RDX using general purpose registers:
# RAX, RBX, RCX, RDX, RBP, RDI, RSI, R8 - R15
# Stack usage prohibited.
#
# Assembly options: $SOURCE$ -o $PROGRAM.OBJ$ --64 -a=$LSTOUTPUT$
# Linking options: $PROGRAM.OBJ$ $MACRO.OBJ$ -g -o $PROGRAM$ -m64 -fno-pie -no-pie
#
# Dmytro Korzhevin
#
.text
.global main
main:
    movq %rsp, %rbp #for correct debugging
    movq %RSI, %RAX
    movq %RDX, %RBX
    movq %RAX, %RDX
    movq %RBX, %RSI
    