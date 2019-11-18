min:
	cmpq %RDI, %RSI
	ja compare
	movq %RSI, %RAX
	retq
compare:
	movq %RDI, %RAX
	retq
