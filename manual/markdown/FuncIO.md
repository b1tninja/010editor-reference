# 010 Editor Manual - I/O Functions

**Source:** [`manual/FuncIO.htm`](../manual/FuncIO.htm) (SweetScape 010 Editor manual mirror).

## Page header
I/O Functions

## Summary (lead paragraphs)
The following is a list of input/output functions that can be used when writing Templates or Scripts.

void BigEndian() Indicates that all subsequent reads and writes from the file should use big-endian byte order. This function can be used in a Template to specify the byte order of variables. See LittleEndian to set little-endian byte order.

void BitfieldDisablePadding() void BitfieldEnablePadding() These functions control how multiple bitfields are packed into a set of bits. See Bitfields more information on bitfields. Padding is enabled by default.

int BitfieldGetAutoCheckBox() This function returns true if all Bitfields that are defined with only 1 bit are automatically assigned a check box Variable Editor in the Template Results . Use BitfieldSetAutoCheckBox to turn on or off this functionality. The default value is true.

int BitfieldGetCurrentShift() Returns the number of bits that have been read so far when defining template variables using bitfields . This value, along with the FTell function, indicate the current bit read position in a file. Zero is returned if no bitfields have been defined. Note that this function returns the same value whether bitfields are being read in left-to-right or right-to-left format (see Bitfields for more information). The current bit read position is calculated differently when using padded bitfields versus unpadded bitfields . When using the padded bitfields (the default), the bit read position cumulates but will reset when the data type changes. For example:

local int shift; int a : 5 ; shift = BitfieldGetCurrentShift (); // value of 5 int b : 12 ; shift = BitfieldGetCurrentShift (); // value of 17 short c : 2 ; shift = BitfieldGetCurrentShift (); // value of 2 When using unpadded bitfields the position does not reset when the data type changes but the position is always in the range 0..7. For example:

local int shift; BitfieldDisablePadding (); short a : 3 ; shift = BitfieldGetCurrentShift (); // value of 3 short b : 7 ; shift = BitfieldGetCurrentShift (); // value of 2 (10 mod 8) Requires 010 Editor v15.0 or higher. void BitfieldLeftToRight() void BitfieldRightToLeft() These functions control how bitfields are packed into a variable. See Bitfields for an introduction to using bitfields. The packing is different depending on if the Template is in big or little endian mode and the packing may change after calling the LittleEndian or BigEndian functions. In little endian mode the default is right-to-left and in big endian mode the default is left-to-right.

void BitfieldSetAutoCheckBox( int enabled ) If enabled is true, all Bitfields that are defined with a single bit are automatically assigned a check box Variable Editor in the Template Results . Note the check box is applied when the variable is first created. The current enabled state can be queried with the BitfieldGetAutoCheckBox function and the default value is true.

double ConvertBytesToDouble( uchar byteArray[] ) float ConvertBytesToFloat( uchar byteArray[] ) hfloat ConvertBytesToHFloat( uchar byteArray[] ) These functions take as input an array of hex bytes byteArray and returns either the double, float, or hfloat that is represented by those bytes. The byteArray parameter must contain at least 8 bytes for the ConvertBytesToDouble function, 4 bytes for the ConvertBytesToFloat function, or 2 bytes for the ConvertBytesToHFloat function. The conversion is performed using the endian for the current file, which can be controlled using the BigEndian or LittleEndian functions. See the ConvertDataToBytes function to convert a double, float, or hfloat to a set of bytes.

int ConvertDataToBytes( data_type value, uchar byteArray[] ) Given a variable value that can be of any of the main data types (e.g. float, short, int, etc.), this function converts the variable to a set of bytes as it would be written to a file and stores the results in the byteArray variable. The return value is the number of bytes written to the array. Note that byteArray must be large enough to hold the bytes from the conversion. The endian used for the conversion is taken from the current file endian, which can be set using the BigEndian or LittleEndian functions.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.