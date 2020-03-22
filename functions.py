def error(error):
	"""Displays to stdout the parameter in error and exits with return code 1."""
	print("pyasm: error: " + error)
	exit(1)

def warning(warning):
	"""Displays to stdout the warning in warning, but it doesn't terminate the program."""
	print("pyasm: warning: " + warning)


###
##
# There are functions that do the same functions as other function
# This is to make code more understandable in pyasm.py
##
###


def cli(opcode):
	"""Converts cli opcode into opcodes: Parameters:
	\nOpcode: the opcode for cli: b\"\\xFA\"
	"""
	cli_opcode = bytearray(opcode)
	return cli_opcode

def decrease(register):
	"""Converts dec instruction into opcodes. Returns the bytes. \nParameters:
	\nRegister: the opcode or opcodes for dec"""
	dec_opcodes = bytearray(register)
	return dec_opcodes

def hlt(opcode):
    """Converts hlt instruction into opcode. Returns the bytes. Parameters:
	Opcode: the opcode for hlt"""
    hlt_opcode = bytearray(opcode)
    return hlt_opcode

def increase(register):
	"""Converts inc instruction into opcodes. Returs the bytes. Parameters:
	Register: the opcode for inc"""
	inc_opcodes = bytearray(register)
	return inc_opcodes

def interrupt(opcode, address):
	"""Converts int instruction into opcodes. Returns the bytes.
	\nParameters:
	\n\nopcode: usually b\"\\xCD\"
	\naddress: the interrupt number, in hexadecimal"""
	try:
		int_address_byte = bytearray(bytes([int(address, 16)]))
		int_opcodes = bytearray(opcode + int_address_byte)
		return int_opcodes
	except ValueError:
		print("Error")
		return None

def jump(register, address):
	"""Converts the jmp instruction into opcodes. Returns the bytes."""
	try:
		# it can be a byte, two or more
		jmp_address_bytes = bytearray(bytes([int(address, 16)]))
		jmp_opcodes = bytearray(register + jmp_address_bytes)
		return jmp_opcodes
	except ValueError:
		return None

def mov(register, address):
	"""Converts the mov instruction into opcodes. Returns the bytes.
	\nParameters:\n\nregister: the opcode register you want be the address moved
	\naddress: the address that needs to be moved into the register
	\nNote: the function converts the integer into hexadecimal and then to bytes."""
	# number needs to be in hexadecimal, thats why there is a try statement
	# if something goes wrong with the hex value it returns none
	try:
		mov_address_byte = bytearray(bytes([int(address, 16)]))
		mov_opcodes = bytearray(register + mov_address_byte)
		return mov_opcodes
	except ValueError:
		print("Error")
		return None
