# 010 Editor Manual - On-Demand Structures

**Source:** [`manual/html/OnDemand.htm`](../html/OnDemand.htm) (SweetScape 010 Editor manual mirror).

## Page header
On-Demand Structures

## Section headings
- **Inline Size Functions**

## Summary (lead paragraphs)
Some 010 Editor templates that define a large number of variables may use a significant amount of system memory. To get around this issue, templates may use On-Demand Structures . With On-Demand Structures the code which defines the variables inside a struct or union is not executed until it is needed (either the structure is opened in the Template Results or a Script or Template accesses a member variable of the struct or union). In order to use on-demand structures, 010 Editor must know the size of the struct or union so that it knows where the next variable exists within the file. To enable on-demand parsing for a struct or union, use the syntax '< size= <number>|<function>|(<expression>)' after a typedef.

If the size of a struct or union is always fixed, a number can be passed to the size attribute (note that sizes are always in number of bytes). For example:

typedef struct { int header; int value1; int value2; } MyStruct <size = 12 > ; In this case, anytime a struct of type MyStruct is defined the variables header , value1 , and value2 are not defined until they are needed.

If the size of struct or union is not fixed, a custom size function can be specified. The size function takes as arguments a variable and returns an int or int64. If data needs to be read from the disk inside a size function the Read<data_type> functions must be used (see I/O Functions ). The member variables of the struct or union cannot be accessed inside the size function because they do not exist until after the size function is called. For an example of a size function, in the ZIP.bt file the ZIPFILERECORD struct could be converted to on-demand using this syntax:

typedef struct { < ... > uint frCompressedSize; uint frUncompressedSize; ushort frFileNameLength; ushort frExtraFieldLength; if ( frFileNameLength > 0 ) char frFileName [ frFileNameLength ] ; if ( frExtraFieldLength > 0 ) uchar frExtraField [ frExtraFieldLength ] ; if ( frCompressedSize > 0 ) uchar frData [ frCompressedSize ] ; } ZIPFILERECORD <size = SizeZIPFILERECORD> ; int SizeZIPFILERECORD ( ZIPFILERECORD & r ) { return 30 + // base size of the struct ReadUInt ( startof (r) + 18 ) + // size of the compressed data ReadUShort ( startof (r) + 26 ) + // size of the file name ReadUShort ( startof (r) + 28 ); // size of the extra field } Note that the size function should always return the size of a single element of the struct or union even if the struct or union is defined as part of an array. Also note that applying colors to variables within on-demand structures may not work as expected because the colors are not defined until the variables are created. Using on-demand structs combined with arguments is only supported in 010 Editor v10 or higher versions.

Starting in 010 Editor version 12.0, size functions can also be declared inline . To create an inline size function either call a function and include arguments inside brackets '(' and ')' where each argument can be any expression, or include a single expression inside brackets '(' and ')'. For example:

typedef struct { int id; string name; float salary; } EMPLOYEE <size = ( 8 + ReadStringLength ( startof ( this ) + 4 ))> ; See Attribute Functions and Inline Expressions for more information.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.