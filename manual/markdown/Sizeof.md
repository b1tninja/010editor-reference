# 010 Editor Manual - Special Keywords

**Source:** [`manual/html/Sizeof.htm`](../html/Sizeof.htm) (SweetScape 010 Editor manual mirror).

## Page header
Special Keywords

## Section headings
- **sizeof**
- **startof**
- **exists**
- **function_exists**
- **this**
- **parentof**

## Summary (lead paragraphs)
sizeof ( double ) would return 8. The sizeof operator can also compute the size of simple structs or unions (see Structs and Unions ). A simple struct is one that does not contain if statements or other statements that may change its size when declared. Attempting to compute the size of a non-simple struct or union will generate an error.

The special keyword startof can be used on a variable that has been declared in a Template to calculate the starting address of the bytes the variable is mapped to in the file. The address is returned in local coordinates . For example, after opening a BMP file, use the following command in a script to position the cursor/caret at the beginning of the first line of bitmap data:

SetCursorPos ( startof ( lines [ 0 ] ) ); exists The special exists operator can be used to determine if a variable has been declared. The operator will return 1 if the given variable exists, or 0 if it does not. For example, after opening a ZIP file, the following command in a script will output all file names:

int i; string s; while ( exists ( file [ i ] ) ) { s = file [ i ]. frFileName; Printf ( "%s\n" , s ); i ++ ; } function_exists The function_exists operator can be used to test if a particular function is defined either as a user-defined function or a built-in function (see Functions for more information). The operator returns 1 if the function exists or 0 if it does not. For example:

if ( function_exists (CopyStringToClipboard) ) { ... } Requires 010 Editor v3.1 or higher. this The this keyword can be used to access the variable representing the current structure being defined (see Structs and Unions ). For example:

void PrintHeader ( struct HEADER & h ) { Printf ( "ID1 = %d\n" , h . id1 ); Printf ( "ID2 = %d\n" , h . id2 ); } struct HEADER { int id1; int id2; PrintHeader ( this ); } h1; If no current structure is currently being defined, this is NULL.

The parentof keyword can be used to access the struct or union that contains a given variable. For example:

void PrintHeader ( struct HEADER & h ) { Printf ( "ID1 = %d\n" , h . id1 ); Printf ( "ID2 = %d\n" , h . id2 ); } struct HEADER { int id1; int id2; struct SUBITEM { int data1; int data2; PrintHeader ( parentof ( this ) ); } item1; PrintHeader ( parentof (item1) ); } h1; If the given variable is not inside a struct or union an error will be generated.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.