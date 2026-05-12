# 010 Editor Manual - Bitfields

**Source:** [`manual/Bitfields.htm`](../manual/Bitfields.htm) (SweetScape 010 Editor manual mirror).

## Page header
Bitfields

## Section headings
- **Padded Bitfields**
- **Unpadded Bitfields**
- **Bitfields and Enums**
- **Bitfields and Check Boxes**

## Summary (lead paragraphs)
A bitfield allows template variables to be subdivided into groups of bits. This process allows multiple variables to be packed into a single block of memory. The syntax for defining a bitfield is 'type_name <variable_name> : number_of_bits'. The type can be char, short, int, or int64 (unsigned or signed) or any of the equivalent types. If the variable name is omitted, the given number of bits will be skipped. For example,

int alpha : 5 ; int : 12 ; int beta : 15 ; would pack alpha and beta into one 32-bit value, but skip 12 bits in the middle. 010 Editor has two special bitfield modes that determine how the bits are packed into variables: padded bitfields and unpadded bitfields.

ushort a : 4 ; ushort b : 7 ; ushort c : 5 ; In little endian mode, this structure would be stored as the bits:

cccccbbb bbbbaaaa (and stored on disk as bbbbaaaa cccccbbb). In big endian mode, this structure would be stored as the bits:

aaaabbbb bbbccccc (and stored on disk as aaaabbbb bbbccccc). Whether the bits are packed left-to-right or right-to-left can be controlled by the functions BitfieldLeftToRight , and BitfieldRightToLeft .

In this mode, the program will automatically add padding bits when needed. If the size of the type being defined changes, padding will be added so the bitfield will be defined on the next variable boundary. Also, if the specified bitfield would step across the boundary of a variable, padding is added so the bitfield starts at the next variable. For example:

int apple : 10 ; int orange : 20 ; int banana : 10 ; int peach : 12 ; short grape : 4 ; The bitfields apple and orange would be packed into one 32 bit value. However, banana steps over the variable boundary, so 2 bits of padding are added so that it starts at the next 32 bit value. Banana and peach are packed into another 32-bit value, but because the size of the type changes with grape, an extra 10 bits of padding is added before grape is defined.

010 Editor includes a special unpadded bitfield mode that treats the file as one long bit stream. No padding bits are added if the variable type changes or if the bits cannot be packed into a single variable. The unpadded mode can be entered by calling the function BitfieldDisablePadding (padding can be turned back on by calling BitfieldEnablePadding ).

In unpadded bitfield mode, each variable defined reads some bits from the bitstream. For example:

BitfieldDisablePadding (); short a : 10 ; int b : 20 ; short c : 10 ; Here a reads the first 10 bits from the file, b reads the next 20 bits from the file, and so on. If the bitfields are defined as reading from right to left (this is the default for little endian data and can enabled using the function BitfieldRightToLeft ), the variables would be stored as the bits:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.