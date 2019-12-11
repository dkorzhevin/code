# Program checks 2 numbers that stored in general purpose registers: RDI and RSI and identifies minimal number.  Arguments - numbers without sign. Minimal number will be saved to RAX register
#
# Dmytro Korzhevin
#

min:
	cmpq %RDI, %RSI
	ja compare
	movq %RSI, %RAX
	retq
compare:
	movq %RDI, %RAX
	retq
