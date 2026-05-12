# 010 Editor Manual - Custom Variables

**Source:** [`manual/html/CustomVariables.htm`](../html/CustomVariables.htm) (SweetScape 010 Editor manual mirror).

## Page header
Custom Variables

## Section headings
- **Inline Read and Write Functions**
- **Read Functions for Structs**
- **Read Functions for Arrays**

## Summary (lead paragraphs)
Some binary file formats use variable types that are different from the regular Data Types . 010 Editor has a powerful syntax for letting you define custom variables in practically any format. To build a custom variable, write a custom function that converts a variable into a string . This string will be displayed in the Template Results panel as the value for the variable (this custom function is called a read function). Optionally, a write function can be written that converts a string in the Template Results panel back to the variable when the variable is edited and Enter is pressed. To assign a read and write function to a variable, use the syntax '< read= <function> [, write= <function> ] >'after a typedef. A read function takes as arguments a variable and returns a string. A write function takes as arguments a reference to a variable and a string. For example, to define a fixed point data type that uses 16 bits (the 8 high bits define the whole part and the 8 low bits define the fractional part), use:

typedef ushort FIXEDPT <read = FIXEDPTRead, write = FIXEDPTWrite> ; string FIXEDPTRead ( FIXEDPT f ) { string s; SPrintf ( s, "%lg" , f / 256.0 ); return s; } void FIXEDPTWrite ( FIXEDPT & f, string s ) { f = ( FIXEDPT )( Atof ( s ) * 256 ); } Read and write functions can also be declared inline as discussed below. In the above example, the FIXEDPT variable could be defined without a write function using '<read=FIXEDPTRead>', but the variable will be read-only in the Template Results panel. Note that the typedef must be defined before the functions in the source file. If an error can occur when a write function is called, change the return value to int and return 0 on success or -1 on failure.

If a run-time error occurs inside a read function, 010 Editor will display "(error)" in the Template Results panel and then display "(error)" every time the read function was to be called (010 Editor will not repeatedly call functions which cause run-time errors because of performance issues). Fix the error within the read function and then re-run the template to use the read function again.

Starting in 010 Editor version 12.0, read and write functions can now be declared inline which means the code for read or write can be included inside the attribute brackets '<' and '>' instead of writing a separate function. This can be done in two ways. The first is to call a function but include arguments inside brackets '(' and ')' and the arguments can be any expression. For example:

typedef ushort FIXEDPT <read = Str ( "%lg" , this / 256.0 )> ; The Str function is included starting in version 12.0 which acts like SPrintf but returns a string directly. The second way to create an inline function is to write an expression inside brackets '(' and ')'. When creating an inline write function, the expression should assign to a variable (use this to assign to the variable itself) and use the special variable value to retrieve the value of the string. For example:

typedef ushort FIXEDPT <read = Str ( "%lg" , this / 256.0 ), write = ( this = Atof ( value ) * 256.0 )> ; Inline functions can also be used with structs and arrays as discussed below.

Read functions can also be used to show information beside a struct without having to open the struct in the Template Results . When using read functions with a struct, the read function receives a reference to the struct and the '&' symbol should be used when declaring the parameter. See the following example from the 'ZIP.bt' file in the Repository :

typedef struct { //... ushort frFileNameLength; if ( frFileNameLength > 0 ) char frFileName [ frFileNameLength ] ; //... } ZIPFILERECORD <read = ReadZIPFILERECORD> ; string ReadZIPFILERECORD ( ZIPFILERECORD & file ) { if ( exists ( file . frFileName ) ) return file . frFileName; else return "" ; } When writing an inline read function for a struct, a read expression can just access one of the children of the struct. For example:

typedef struct { int id; string name; //... } Employee <read = (name)> ; Read Functions for Arrays When displaying arrays in the Template Results panel, usually no value is displayed for an array until the array is opened up. To specify a value beside the array, a custom variable can be defined. For example:

typedef float VEC3F [ 3 ] <read = Vec3FRead, write = Vec3FWrite> ; string Vec3FRead ( VEC3F v ) { string s; SPrintf ( s, "(%g %g %g)" , v [ 0 ] , v [ 1 ] , v [ 2 ] ); return s; } void Vec3FWrite ( VEC3F & v, string s ) { SScanf ( s, "(%g %g %g)" , v [ 0 ] , v [ 1 ] , v [ 2 ] ); } Note that currently, read/write functions cannot be declared simultaneously for an array of elements and for each element of the array. Starting in 010 Editor version 12.0, read and write functions can be declared inline and use this[0] , this[1] , etc. to access members of the array. For example, the above code could be declared inline as:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.