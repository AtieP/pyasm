
# cli

cli = {
	"cli": b"\xFA"
}
# dec_imm8

dec_imm8 = {
	"al": b"\xFE\xC8",
	"bl": b"\xFE\xCB",
	"cl": b"\xFE\xC9",
	"dl": b"\xFE\xCA",
	"ah": b"\xFE\xCC",
	"bh": b"\xFE\xCF",
	"ch": b"\xFE\xCD",
	"dh": b"\xFE\xCE"
}

# dec_imm16

dec_imm16 = {
	"ax": b"\x48",
	"bx": b"\x4B",
	"cx": b"\x49",
	"dx": b"\x4A",
	"sp": b"\x4C",
	"bp": b"\x4D",
	"si": b"\x4E",
	"di": b"\x4F"
}

# hlt

hlt = {
	"hlt": b"\xF4"
}

# inc_imm8

inc_imm8 = {
	"al": b"\xFE\xC0",
	"bl": b"\xFE\xC3",
	"cl": b"\xFE\xC1",
	"dl": b"\xFE\xC2",
	"ah": b"\xFE\xC4",
	"bh": b"\xFE\xC7",
	"ch": b"\xFE\xC5",
	"dh": b"\xFE\xC6"
}

# inc_imm16

inc_imm16 = {
	"ax": b"\x40",
	"bx": b"\x43",
	"cx": b"\x41",
	"dx": b"\x42",
	"sp": b"\x44",
	"bp": b"\x45",
	"si": b"\x46",
	"di": b"\x47"
} 

# int

interrupt = {
	"int_imm8": b"\xCD",
	"int3": b"\xCC",
	"into": b"\xCE"
}

# jmp

jmp = {
	"jmp": b"\xEB"
}
# mov_r8_imm8

mov_r8_imm8 = {
	"al": b"\xB0",
	"bl": b"\xB3",
	"cl": b"\xB1",
	"dl": b"\xB2",
	"ah": b"\xB4",
	"bh": b"\xB7",
	"ch": b"\xB5",
	"dh": b"\xB6"
}

# mov_r16_imm16

mov_r16_imm16 = {
	"ax": b"\xB8",
	"bx": b"\xBB",
	"cx": b"\xB9",
	"dx": b"\xBA",
	"sp": b"\xBC",
	"bp": b"\xBD",
	"si": b"\xBE",
	"di": b"\xBF"
}
