# 010 Editor Manual - Disassembly in Templates

**Source:** [`manual/DisassemblerTemplates.htm`](../manual/DisassemblerTemplates.htm) (SweetScape 010 Editor manual mirror).

## Page header
Disassembly in Templates

## Section headings
- **Opcodes**
- **Arrays of Opcodes**
- **Viewing the Disassembler Results**
- **Disassembly in Scripts**

## Summary (lead paragraphs)
The disassembler can be used to convert hex bytes to assembly language. See the separate Disassembler help topic for an introduction.

Disassembly can be performed in Templates starting in version 12 by using the special Opcode data type that disassembles a single CPU instruction. The architecture for an Opcode must be declared either using the DisasmSetMode function or using the special attribute < disasm=<constant>|<function>|(<expression>) >. For example, to disassemble in X86 32-bit mode use the code:

DisasmSetMode ( DISASM_X86_32 ); Opcode opx86; or

Opcode opx86 <disasm = DISASM_X86_32 > ; See the DisasmSetMode function for a full list of architecture constants and options. Note that if any options are specified using '|' then the expression must be enclosed in brackets '(' ')'. For example:

Opcode oparm <disasm = ( DISASM_ARM_32 | DISASM_OPTION_ARM_THUMB )> ; The generated Opcode will contain a variable number of bytes, depending upon the type of opcode read from the file. Use the regular startof or sizeof operators to query the position or size of an opcode.

An array of opcodes can be generated using a duplicate array as described in the Arrays, Duplicates, and Optimizing help topic. For example, to disassemble an entire file for X86 64-bit use:

DisasmSetMode ( DISASM_X86_64 ); while ( ! FEof () ) Opcode opx86; The above code can be slow for large files so 010 Editor has a special optimization for arrays of Opcodes. To use this optimization, create an array of opcodes using '[' and ']' but the size inside the brackets is the number of bytes instead of the number of opcodes. For example, an entire file could be disassembled with:

DisasmSetMode ( DISASM_X86_64 ); Opcode opx86 [ FileSize () ] ; After creating the array, use the DisasmNumOps function to retrieve the actual number of opcodes created. For example, to disassemble an entire file for ARM and then print out the results to the Output panel use:

Opcode ops [ FileSize () ] <disasm = DISASM_ARM_32 > ; local int i, count = DisasmNumOps ( ops ); for ( i = 0 ; i < count; i ++ ) Printf ( "%d (%d %d)= '%s'\n" , i, startof (ops [ i ] ), sizeof (ops [ i ] ), DisasmOpString ( ops [ i ] ) ); Note the DisasmOpString function can be used to convert an Opcode into a string representation.

When a Template is run that has an Opcode variable declared, the disassembly is shown in the Value column of the Template Results as shown above. The Start column shows the starting address of each opcode and the Size column shows the size of each opcode. See Working with Template Results for more information.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.