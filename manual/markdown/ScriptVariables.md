# 010 Editor Manual - Declaring Script Variables

**Source:** [`manual/ScriptVariables.htm`](../manual/ScriptVariables.htm) (SweetScape 010 Editor manual mirror).

## Page header
Declaring Script Variables

## Section headings
- **Constants**

## Summary (lead paragraphs)
A variable can be declared using the syntax '<data type> <variable name>;' Use an '=' to assign a value to the variable. Multiple variables can also be declared using the ',' operator. For example:

int x; float a = 3.5f ; unsigned int myVar1, myVar2; Currently only the characters a..z, A..Z, 0..9 and underscore '_' are allowed in variable names and the variable name must start with a letter or underscore. For a complete list of types allowed, see Data Types . Any variables declared in a Script will be displayed in the Variables tab of the Inspector . Arrays of variables can also be declared (see Arrays, Duplicates, and Optimizing ). Declaring variables is the main way of building Templates (see Declaring Template Variables for more information).

Constants can be declared using the keyword ' const ' before a variable declaration. For example:

const int TAG_EOF = 0x3545 ; This syntax is generally better for defining constants than using the ' #define ' preprocessor directive. A number of constants are built into 010 Editor, including true , false , TRUE , FALSE , M_PI , and PI . See Interface Functions for a list of other constants used for coloring or Tool Functions for a list of constants used when calling tool functions.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.