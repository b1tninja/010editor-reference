# 010 Editor Manual - Introduction to Byte Ordering

**Source:** [`manual/html/ByteOrdering.htm`](../html/ByteOrdering.htm) (SweetScape 010 Editor manual mirror).

## Page header
Introduction to Byte Ordering

## Summary (lead paragraphs)
Data on a computer is usually divided into sets of 8 bits, called a byte (see Introduction to Number Systems ). A byte can store 256 different values but to store larger numbers, a set of bytes must be grouped together. The term ' Endian ' refers to how these bytes are grouped together.

Big Endian - In big-endian systems (for example, Motorola machines), bytes are stored with the most significant byte first. In the same example, the hex bytes '2f 75 05' would represent the number 0x2f7505 (3110149) in decimal. Which endian is used to convert bytes to numbers is very important and every file in 010 Editor has an endian setting. LIT will appear in the Status Bar when the current file is in little-endian mode, and BIG will appear in big-endian mode. Most tools and the Inspector use this endian setting. To change the default endian used for files, use the ' View > Endian ' menu or click LIT or BIG in the status bar. 010 Editor can be configured to automatically set the endian based on the file extension (see Using Edit As ).

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.