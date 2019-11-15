# Sample program which converts Fahrenheit to Celcius. Initial Fahrenheit number stored in RSI register.
# In this case, I've not used direct number (i.e. $5 or $9) for conversion according to formula.
# Instead, both numbers was loaded to corresponding operant registers (RAX, RCX).
#
# Dmytro Korzhevin
#
.text
.global main
main:
    movq %rsp, %rbp # for correct debugging
    movq $40, %RSI  # Initial value in RSI - 40 (0x28) Fahrenheit, which should be converted to Celcius
    subq $32, %RSI  # subtract 32 from number stored in RSI
    movq $5, %RAX   # put number 5 in RAX
    mulq %RSI       # multiply number stored in RSI on 5 (result saved in RAX)
    movq $9, %RCX   # put number 9 in RCX
    divq %RCX       # divide value in RAX on 9 which stored in RCX, result will be stored in RAX
    movq %RAX, %RSI # Move result from RAX to target RSI
