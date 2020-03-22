import opcodes
import functions

import sys
import os.path

# check for arguments
if len(sys.argv) < 2:
	functions.error("You need to specify an output file\nUsage: pyasm.py [output file]")
elif len(sys.argv) > 2:
	functions.error("You need to specify only an output file\nUsage: pyasm.py [output file]")
else:
	pass

output_file = open(sys.argv[1], "wb")

print("Welcome to Pyasm!")
print("Press enter to exit, and remember, use 4 digits when moving to immediant register!")

## segment and offset
segment = 0000
offset = 0000

## dictionary to save labels
labels = {}

## flags
is_label = False


try:
	while True:

		asm_input = input(str(segment) + ":" + str(offset) + " ")

		# check if key is enter
		if asm_input == "":
			print("Program terminated successfully.")
			exit(0)
		asm_input_tokenized = asm_input.split(" ")

		# set flag to None to avoid bugs
		is_label = False

		# checks if it is a label the input
		for i in asm_input:
			if i == ":":
				label_without_colon = asm_input.replace(":", "")
				labels[label_without_colon] = offset
				is_label = True	# set is_label flag 
				break
			else:
				pass

		# if its a label, the for loop above sets is_label variable to 1
		if is_label == True:
			continue
		
		# cli -> clear interrupt flag
		elif asm_input_tokenized[0].lower() == "cli" and len(asm_input_tokenized) == 1:
			result = functions.cli(opcodes.cli["cli"])
			offset+=1
			output_file.write(result)

		# db -> declare byte
		elif asm_input_tokenized[0].lower() == "db":
			# the for loop is to make raw all the bytes after DB
			try:
				for i in range(0, len(asm_input_tokenized) - 1):
					j = i + 1
					result = bytearray(bytes([int(asm_input_tokenized[j], 16)]))
					output_file.write(result)
					offset+=1		# increase offset

			except ValueError:
				print("Error")

		# incbin -> include binary file
		elif asm_input_tokenized[0].lower() == "#incbin" and len(asm_input_tokenized) == 2:
			if not os.path.exists(str(asm_input_tokenized[1])):
				print("Error")
			elif os.path.isdir(str(asm_input_tokenized[1])):
				print("Error")
			else:
					input_file = open(str(asm_input_tokenized[1]), "rb")
					input_file_content = input_file.read()
					output_file.write(input_file_content)

					input_file_len = bytearray(bytes(input_file_content))
					input_file_len = len(input_file_len)

					for i in range(0, input_file_len):
						offset += 1

					input_file.close()


		# fill -> fill with x y times		
		elif asm_input_tokenized[0].lower() == "fill" and len(asm_input_tokenized) == 3:

			try:

				value = int(asm_input_tokenized[1])
				times = int(asm_input_tokenized[2])


				for i in range(0, times):
					offset+=1		# increase offset
					result = bytearray(bytes([value]))
					offset+=1
					output_file.write(result)

			except ValueError:
				print("Error")

		# fillu -> fill with x until the file is y bytes long
		elif asm_input_tokenized[0].lower() == "fillu" and len(asm_input_tokenized) == 3:

			try:

				value = int(asm_input_tokenized[1])
				until = int(asm_input_tokenized[2])                                                           

				for i in range(0, until):
					if offset == until:
						break
					result = bytearray(bytes([value]))
					offset+=1
					output_file.write(result)

			except ValueError:
				print("Error")



		# START CHECKING DECREASE
		#

		# START CHECKING FOR 8 BIT REGISTERS

		elif asm_input_tokenized[0].lower() == "dec" and len(asm_input_tokenized) == 2:

			## START CHECKING FOR 8 BIT REGISTERS
			##

			if asm_input_tokenized[1].lower() == "al":
				result = functions.decrease(opcodes.dec_imm8["al"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bl":
				result = functions.decrease(opcodes.dec_imm8["bl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "cl":
				result = functions.decrease(opcodes.dec_imm8["cl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dl":
				result = functions.decrease(opcodes.dec_imm8["dl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ah":
				result = functions.decrease(opcodes.dec_imm8["ah"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bh":
				result = functions.decrease(opcodes.dec_imm8["bh"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ch":
				result = functions.decrease(opcodes.dec_imm8["ch"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dh":
				result = functions.decrease(opcodes.dec_imm8["dh"])
				offset+=2
				output_file.write(result)

			##
			## END CHECKING FOR 8 BIT REGISTERS

			## START CHECKING FOR 16 BIT REGISTERS
			##

			elif asm_input_tokenized[1].lower() == "ax":
				result = functions.decrease(opcodes.dec_imm16["ax"])
				# Opcode for decreasing 16 bit register is one byte
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bx":
				result = functions.decrease(opcodes.dec_imm16["bx"])
				offset+=1
				output_file.write(result)
				
			elif asm_input_tokenized[1].lower() == "cx":
				result = functions.decrease(opcodes.dec_imm16["cx"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dx":
				result = functions.decrease(opcodes.dec_imm16["dx"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "sp":
				result = functions.decrease(opcodes.dec_imm16["sp"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bp":
				result = functions.decrease(opcodes.dec_imm16["bp"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "si":
				result = functions.decrease(opcodes.dec_imm16["si"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "di":
				result = functions.decrease(opcodes.dec_imm16["di"])
				offset+=1
				output_file.write(result)

			else:
				print("Error")

		# 
		# END CHECKING DECREASE

		# START CHECKING HLT

		elif asm_input_tokenized[0].lower() == "hlt" and len(asm_input_tokenized) == 1:

			result = functions.hlt(opcodes.hlt["hlt"])
			offset+=1
			output_file.write(result)



		# START CHECKING INCREASE
		#

		
		elif asm_input_tokenized[0].lower() == "inc" and len(asm_input_tokenized) == 2:

			## START CHECKING FOR 8 BIT REGISTERS
			##

			if asm_input_tokenized[1].lower() == "al":
				result = functions.increase(opcodes.inc_imm8["al"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bl":
				result = functions.increase(opcodes.inc_imm8["bl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "cl":
				result = functions.increase(opcodes.inc_imm8["cl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dl":
				result = functions.increase(opcodes.inc_imm8["dl"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ah":
				result = functions.increase(opcodes.inc_imm8["ah"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bh":
				result = functions.increase(opcodes.inc_imm8["bh"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ch":
				result = functions.increase(opcodes.inc_imm8["ch"])
				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dh":
				result = functions.increase(opcodes.inc_imm8["dh"])
				offset+=2
				output_file.write(result)

			##
			## END CHECKING FOR 8 BIT REGISTERS

			## START CHECKING FOR 16 BIT REGISTERS
			##

				# note that the opcode for inc r16 is one byte

			elif asm_input_tokenized[1].lower() == "ax":
				result = functions.increase(opcodes.inc_imm16["ax"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bx":
				result = functions.increase(opcodes.inc_imm16["bx"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "cx":
				result = functions.increase(opcodes.inc_imm16["cx"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dx":
				result = functions.increase(opcodes.inc_imm16["dx"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "sp":
				result = functions.increase(opcodes.inc_imm16["sp"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bp":
				result = functions.increase(opcodes.inc_imm16["bp"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "si":
				result = functions.increase(opcodes.inc_imm16["si"])
				offset+=1
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "di":
				result = functions.increase(opcodes.inc_imm16["di"])
				offset+=1
				output_file.write(result)

			else:
				print("Error")

		#
		# END CHECKING INCREASE



		# START CHECKING INTERRUPTS
		#

		elif asm_input_tokenized[0].lower() == "int" and len(asm_input_tokenized) == 2:

			# try statement if the value given is incorrect

			try:
				result = functions.interrupt(opcodes.interrupt["int_imm8"], asm_input_tokenized[1])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			except ValueError:
					print("Error")

		elif asm_input_tokenized[0].lower() == "int3" and len(asm_input_tokenized) == 3:
			result = bytearray(opcodes.interrupt["int3"])
			offset+=1
			output_file.write(result)

		elif asm_input_tokenized[0].lower() == "into":
			result = bytearray(opcodes.interrupt["into"])
			offset+=1
			output_file.write(result)

		#
		# END CHECKING INTERRUPTS

			
		# START CHECKING FOR MOV
		# 

		elif asm_input_tokenized[0].lower() == "mov":

			##  START CHECKING FOR IMMEDIATE ADDRESSES
			##

			### START CHECKING 8BIT IMMEDIATE ADDRESSES
			###


			if asm_input_tokenized[1].lower() == "al," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["al"], asm_input_tokenized[2])
				# if given as address an invalid number the function returns None
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bl," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["bl"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "cl," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["cl"], asm_input_tokenized[2])
				if result == None:
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dl," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["dl"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ah," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["ah"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bh," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["bh"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "ch," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["ch"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dh," and len(asm_input_tokenized) == 3:
				result = functions.mov(opcodes.mov_r8_imm8["dh"], asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=2
				output_file.write(result)

			###
			### END CHECKING 8BIT IMMEDIATE ADDRESSES

			### STARTING CHECKING 16BIT IMMEDIATE ADDRESSES

			elif asm_input_tokenized[1].lower() == "ax," and len(asm_input_tokenized) == 4:
				# ax and all 16 bit registers = lower part and higher part, so we do functions.mov() twice
				result = functions.mov(opcodes.mov_r16_imm16["ax"], asm_input_tokenized[3])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bx," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["bx"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "cx," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["cx"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "dx," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["dx"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "sp," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["sp"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "bp," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["bp"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "si," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["si"], asm_input_tokenized[2])
				if result == None: 
					continue

				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)

			elif asm_input_tokenized[1].lower() == "di," and len(asm_input_tokenized) == 4:
				result = functions.mov(opcodes.mov_r16_imm16["di"], asm_input_tokenized[2])
				if result == None: 
					continue
				
				result = functions.mov(result, asm_input_tokenized[2])
				if result == None: 
					continue

				offset+=3
				output_file.write(result)


			else:
				print("Error")

			###
			### END CHECKING 16BIT IMMEDIATE ADDRESSES

			##
			## END CHECKING FOR IMMEDIATE ADDRESSES
			
		#
		# END CHECKING MOV

		else:
			print("Error")

except EOFError:
	output_file.close()
	exit(0)
