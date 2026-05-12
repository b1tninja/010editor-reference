# 010 Editor Manual - Arrays, Duplicates, and Optimizing

**Source:** [`manual/html/ArraysDuplicates.htm`](../html/ArraysDuplicates.htm) (SweetScape 010 Editor manual mirror).

## Page header
Arrays, Duplicates, and Optimizing

## Section headings
- **Arrays**
- **Arrays and Duplicates**
- **Optimizing Arrays of Structs**

## Summary (lead paragraphs)
An array of variables can be defined using the syntax '<data type> <variable name> [ <expression> ]'. Any of the types in the Data Types list can be used. For example:

int myArray [ 15 ] ; Note that unlike ANSI C, the size of the array can be any expression including variables, functions, or operators. For example

int myArray [ FileSize () - myInt * 0x10 + ( 17 << 5 ) ] ; The individual elements of the array can be accessed using the '[ ]' operator. For example:

for ( i = 0 ; i < 15 ; i ++ ) myArray [ i ] = i; If an array is declared with size zero a warning will be printed out and no variable will be created, but no error will be generated.

When writing a template, regular arrays can be declaring using the same syntax as scripts. However, 010 Editor has a syntax that allows arrays to be built in a special way. When declaring template variables, multiple copies of the same variable can be declared. For example:

int x; int y; int x; 010 Editor allows you to treat the multiple declarations of the variable as an array (this is called a Duplicate Array ). In this example, x[0] could be used to reference the first occurrence of x and x[1] could be used to reference the second occurrence of x . Note that referencing x always references the last element of the array. Duplicate arrays can even be defined with for or while loops. For example:

local int i; for ( i = 0 ; i < 5 ; i ++ ) int x; For another example, see the 'ZIP.bt' file that uses duplicate arrays to parse ZIP files. Duplicate arrays are also useful because of how 010 Editor deals with arrays of structs.

010 Editor contains an optimization that allows it to generate arrays of structures with millions and millions of elements. The optimization calculates the size of the first element of the array and assumes all elements of the array are the same size. This optimization will cause incorrect results if the elements can be variable size (010 Editor will display a popup warning and a warning in the Output text area if it detects this may be happening). To turn the optimization off, use the syntax ' <optimize=false> ' after the array declaration. For example:

typedef struct { int id; int length; uchar data [ length ] ; } RECORD ; RECORD record [ 5 ] <optimize = false> ; If 010 Editor displays a warning but you would still like to use the optimization, use the syntax ' <optimize=true> ' to turn off display of the warning. The ' <optimize=false> ' syntax can also be used with struct typedefs to indicate that optimization should not be used on any arrays using that structure. Unoptimized arrays can also be rewritten as duplicate arrays (see above) since the elements of duplicate arrays can have different sizes.

When defining an array with ' <optimize=false> ', older versions of 010 Editor used to show each element of the array at the same level as its parent in the Template Results . Starting in 010 Editor version 13, unoptimized arrays are displayed with a parent node that can be opened or closed to show the elements of the array, just like a regular array. To revert to the old behaviour in the Template Results see the Compiling Options page or the SetUnoptimizedArraysCollapsible function.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.