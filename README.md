# pyasm
An assembler made using Python. It exports to binary.

# How to use it
Download Python 3. Then, to run the file, use `python pyasm.py [output file]`. Done!

# Valid instructions
`mov r8, imm8`  
`mov r16, imm16`  
`cli`  
`hlt`  
`int3`  
`into`  
`int xx`  
`db byte`  
`jmp <label>`  
`fill <byte> <times>`  
`fillu <byte> <bytes until the file is>`  
`inc r8`  
`inc r16`  
`dec r8`  
`dec r16`   

**Note that all numbers are in hexadecimal, except for fill and fillu.**  
**Example of a label: `label:`**

# Valid preprocessor directives
`#incbin "binary file"`

# I want to help to the development!
Open an issue or send a pull request.
