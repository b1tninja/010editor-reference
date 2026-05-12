# 010 Editor Manual - Base Converter

**Source:** [`manual/html/BaseConverter.htm`](../html/BaseConverter.htm) (SweetScape 010 Editor manual mirror).

## Page header
Base Converter

## Summary (lead paragraphs)
The Base Converter is an easy-to-use tool for converting between decimal, hexadecimal, octal, and binary numeric formats, plus a number of floating point and string formats. Click the ' Tools > Base Converter... ' menu option to display the Base Converter window.

Type a number into either the Decimal , Hex , Octal , or Binary field. The number will be converted into the other three formats and displayed in the corresponding fields. If an invalid number is entered, the other fields will be cleared. See the Introduction to Number Systems for more information on numeric formats.

If a number is entered into the Float or Double fields, the number will be converted from its floating point value to a binary encoding (4 bytes for a Float and 8 bytes for a Double). The binary data will be displayed as a set of 4 or 8 numbers in the Decimal , Hex , Octal , and Binary fields. Note that the endianness of the binary data can be controlled with the Little Endian and Big Endian toggles at the bottom of the dialog (see Introduction to Byte Ordering ).

If a string or character is entered in the ASCII , EBCDIC , or UNICODE fields, the string will be converted to a set of binary bytes. These bytes will be displayed as a set of numbers in the Hex , Octal , and Binary fields. Note that UNICODE strings have 2 bytes per character and the endianness of the UNICODE data can be controlled using the Little Endian and Big Endian toggles at the bottom of the dialog.

The Base Converter dialog can be left open while working in other windows in the editor and the window can be resized horizontally to enlarge or shrink the fields. Click the Close button to dismiss the dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.