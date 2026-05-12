# 010 Editor Manual - Calculator

**Source:** [`manual/html/Calculator.htm`](../html/Calculator.htm) (SweetScape 010 Editor manual mirror).

## Page header
Calculator

## Section headings
- **Expressions**
- **Variables**
- **Functions**

## Summary (lead paragraphs)
The Calculator provided with 010 Editor is a full expression calculator using a syntax similar to C. The calculator can be loaded by clicking the ' Tools > Calculator... ' menu option or pressing F8 .

Enter values into the calculator by clicking the buttons at the bottom of the calculator or by typing on the keyboard. Note that many common letters, numbers, and symbols can be entered by clicking the calculator buttons but some of the advanced features of the calculator are accessible only by typing commands on the keyboard.

Click the Backspace button to delete the character to the left of the current caret position or press the Clear button to delete all information in the calculator. Clicking the Copy button copies the last result to the Windows clipboard and clicking the Run or ' = ' button will evaluate the current expression and display the result in the calculator window.

For evaluating simple expressions, enter an expression in the calculator with no semi-colon (';') at the end of the line. Note that when entering hexadecimal numbers, place an 'h' after the number (for example '2Fh'). Because the calculator uses C-syntax, make sure to place a '0' before any hexadecimal numbers that begin with a letter (for example, you must use '0FFh' instead of just 'FFh'). Click the Run button or press F8 again to display the results in the calculator. For example: 1000h + 512 * 123 will display the result '67072 [10600h]'. If a semi-colon is included at the end of the line, the expression is treated as a C program and to display results the return keyword must be used. For example:

return 0x1000 + 512 * 123 ; All standard C operators are supported including +, -, *, /, ~, ^, &, %, |, <<, >>, ?:, brackets, etc. Decimal, hex, octal, and binary number formats are supported. For example:

( 312 + 013 ) * ( 0x1000 | 0b10 ) Note that multiplication is slightly different than seen in scripts and templates since integers are automatically cast to 64-bit integers before a multiply is done. See Writing Scripts and Expressions for more information on expressions.

Variables can also be declared and used in the calculator using C syntax. For example:

int x = 0x4210 + 512 ; int y = (x << 16 ) + x; return y; A variable declared in the calculator will be displayed in the Variables tab of the Inspector. Strings and arrays are also supported. See Data Types for a full list of supported data types.

010 Editor includes a number of functions for math operations, editing files, editing strings, and interacting with the interface. Most functions are similar to their C counterparts but have a capital first letter. The Printf function is supported and can be used for displaying text in the Output tab of the Output panel. For example:

Printf ( "Integer result = %d, String result = '%s'\n" , 0x24 << 3 , "Test" ); See Interface Functions , I/O Functions , String Functions , Math Functions , or Tool Functions for a full list of functions.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.