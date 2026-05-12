# 010 Editor Manual - Data Types, Typedefs, and Enums

**Source:** [`manual/DataTypes.htm`](../manual/DataTypes.htm) (SweetScape 010 Editor manual mirror).

## Page header
Data Types, Typedefs, and Enums

## Section headings
- **Typedefs**
- **Enums**
- **Enum Flags**
- **GUID**

## Summary (lead paragraphs)
Support for a number of different data types is built into 010 Editor. These data types are used when writing a Template (see Declaring Template Variables ) or when declaring variables in a Script (see Declaring Script Variables ). Commonly, a number of different names refer to the same data type (for example, ' ushort ' and ' WORD ' usually refer to a 16-bit unsigned integer). The following lists each of the data types and all of the names currently supported for that type:

8-Bit Unsigned Integer - uchar, ubyte, UCHAR, UBYTE, uint8, UINT8 16-Bit Signed Integer - short, int16, SHORT, INT16 16-Bit Unsigned Integer - ushort, uint16, USHORT, UINT16, WORD 32-Bit Signed Integer - int, int32, long, INT, INT32, LONG 32-Bit Unsigned Integer - uint, uint32, ulong, UINT, UINT32, ULONG, DWORD 64-Bit Signed Integer - int64, quad, QUAD, INT64, __int64 64-Bit Unsigned Integer - uint64, uquad, UQUAD, UINT64, QWORD, __uint64 32-Bit Floating Point Number - float, FLOAT 64-Bit Floating Point Number - double, DOUBLE 16-Bit Floating Point Number - hfloat, HFLOAT Date Types - DOSDATE, DOSTIME, FILETIME, OLETIME, time_t, time64_t (for more information on date types see Using the Inspector ) String Types - string (see Strings ), wchar_t and wstring (see Wide Strings ) Enum - See Enums below. GUID - See GUID below. Opcode - Allows incorporating the disassembler into a Template and see Disassembly in Templates for more information. Note that date types can be used in Templates, but they must be cast to an int or float before any operations can be performed on them. Default date and time formats can be set using the Inspector/Tables Options dialog. 010 Editor also has support for a special string type. Types hfloat and HFLOAT require version 5 of 010 Editor, time64_t requires version 9, GUID requires version 11, Opcode requires version 12, and types int8, INT8, uint8 and UINT8 require version 15.

Other data types can be created using the ' typedef ' keyword. The syntax for creating new types is ' typedef <data_type> <new_type_name>'. For example,

typedef unsigned int myInt ; would generate a new data type myInt for unsigned integers. Typedefs can also be used with arrays (see Arrays, Duplicates, and Optimizing ) using the syntax 'typedef <data_type> <new_type_name> [ <array_size> ]'. Note that the array size must be a constant in this case. For example, to generate a new string type with 15 characters use:

typedef char myString [ 15 ] ; myString s = "Test" ; Note that typedefs cannot be used to create multi-dimensional arrays (see Limitations ). Typedefs can also be used with structs (see Structs and Unions ).

Use the enum keyword to specify a number of constants for a variable. An enum data type can be created using the C syntax ' enum <type_name> { <constant_name> [ = expression ], ... } <variable_list>'. If no expression is given for the first constant, it is assumed to be zero. If no expression is given for any other constant, its value is assumed to be the previous constant plus one. For example,

enum MYENUM { COMP_1 , COMP_2 = 5 , COMP_3 } var1; would declare the constants COMP_1 equal to 0, COMP_2 equal to 5, and COMP_3 equal to 6. By default, enums are the same type as an integer, but the type can be changed by placing '<' type_name '>' after the enum keyword. For example,

enum < ushort > MYENUM { COMP_1 , COMP_2 = 5 , COMP_3 } var1; would declare the same variable but as an unsigned short. When an enum variable is declared and the variable is selected in the Template Results, a down arrow will appear to the right of the text field. Clicking on the down arrow displays a drop-down list of all constants defined for the enum. Selecting an item from the drop-down list, or entering a constant in the edit field and pressing Enter will assign the variable to a new value. Enums may also be used with bitfields or with enum flags .

Some enum data types represent a set of flags, where each enum constant is a bitmask that indicates whether a particular flag is enabled. Enums which represent flags should use the '<edit=flags>' special attribute after the variable or typedef. For example:

typedef enum < uint > { ITEM_EDITABLE = 0x01 , ITEM_ENABLED = 0x02 , ITEM_CLICKABLE = 0x04 } ItemFlags <edit = flags, format = hex> ; ItemFlags item1; In this example, the enum defines 3 different flags: ITEM_EDITABLE (0x01), ITEM_ENABLED (0x02) and ITEM_CLICKABLE (0x04). A value of 0x3 means that both ITEM_EDITABLE and ITEM_ENABLED are set (0x1 | 0x2 = 0x3). When using '<edit=flags>', the Template Results will show each flag separated by a '|' and clicking the drop-down arrow to the right of the value will show a list of check boxes than can be checked or unchecked to enable a particular flag.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.