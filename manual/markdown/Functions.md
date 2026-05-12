# 010 Editor Manual - Functions

**Source:** [`manual/Functions.htm`](../manual/Functions.htm) (SweetScape 010 Editor manual mirror).

## Page header
Functions

## Section headings
- **Custom Functions**
- **Calling External Functions**

## Summary (lead paragraphs)
A large number of functions are built into 010 Editor. Many of the standard C functions are available, but have a uppercase first letter to differentiate them. Functions are called using the typical C syntax '<function name> ( <argument_list> )'. For example:

string str = "Apple" ; return Strlen ( str ); would return 5. Some functions can have a variable number of arguments. For example:

Printf ( "string='%s' length='%d'\n" , str, Strlen ( str ) ); would display "string='Apple' length='5'" in the Output tab of the Output Window. See Interface Functions , I/O Functions , String Functions , Math Functions , Tool Functions for a list of all functions.

Custom functions can be defined with the regular C syntax '<return type> <function name> ( <argument_list> ) { <statements> }'. The return type can be void or any of the supported data types . For example:

void OutputInt ( int d ) { Printf ( "%d\n" , d ); } OutputInt ( 5 ); Arguments are usually passed by value, but can be passed by reference using the '&' character before the argument name. Array arguments can be indicated using the characters '[]' after the argument name. Array arguments are passed by reference if possible, or by value if not. For example:

char [] GetExtension ( char filename [] , int & extLength ) { int pos = Strchr ( filename, '.' ); if ( pos == -1 ) { extLength = 0 ; return "" ; } else { extLength = Strlen ( filename ) - pos - 1 ; return SubStr ( filename, pos + 1 ); } } Prototypes can also be used on functions by replacing the statements with a semi-colon ';' after the argument list. Full recursion is supported on custom functions. Note that unlike regular C, the function 'main' is not required and execution begins from the first line of the Script or Template. Note that if a Script is run on a file after a Template has been run on that same file, the functions in the Template can be called from the Script.

Functions can also be called which reside in an external library (for example, a Windows DLL). For more information see the External (DLL) Functions help topic.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.