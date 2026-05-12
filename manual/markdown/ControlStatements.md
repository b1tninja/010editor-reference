# 010 Editor Manual - Control Statements

**Source:** [`manual/html/ControlStatements.htm`](../html/ControlStatements.htm) (SweetScape 010 Editor manual mirror).

## Page header
Control Statements

## Section headings
- **if Statements**
- **for Statements**
- **while Statements**
- **switch statements**
- **break and continue**
- **return**

## Summary (lead paragraphs)
Statements may be grouped by '{' or '}' and may contain the regular C if statement, or the if-else statement in the form ' if ( <condition> ) then <statement> [ else <statement>]'. For example:

if ( y > x ) max = y; else { max = x; y = 0 ; } for Statements The standard C for statement can be used in any Script or Template in the form ' for ( <initialization>; <condition>; <increment> ) <statement>'. For example:

for ( int i = 0 , x = 0 ; i < 15 ; i ++ ) { x += i; } Starting in 010 Editor version 16.0, variables can be created in the <initialization> section but these variables are automatically created as local variables. Note that scoping of variables works differently than regular C such that any variables created in the for loop continue to exist even after the loop is finished. Empty for loops ' for ( ; ; )' are also supported starting in 010 Editor version 16.0.

The while and do-while statements can also be used in the form ' while ( <condition> ) <statement>' or ' do <statement> while ( <condition> )'. For example:

while ( myVar < 15 ) { x *= myVar; myVar += 2 ; } or

do { x *= myVar; myVar += 2 ; } while ( myVar < 23 ); switch statements A switch statement can be used to compare a variable with a number of values and perform different operations depending on the result. switch statements are of the form: switch ( <variable> ) { case <expression>: <statement>; [break;] . . . default : <statement>; } For example:

switch ( value ) { case 2 : result = 1 ; break ; case 4 : result = 2 ; break ; case 8 : result = 3 ; break ; case 16 : result = 4 ; break ; default : result = -1 ; } break and continue break or continue can be used in a Script or Template using the syntax ' break ;' or ' continue ;'. Use break to exit out of the current for , switch , while , or do block and transfer program control to the first statement after the block. break can also be used to break out of structs when writing Templates. Use continue to jump to the end brace of any for or while loop and continue execution of the loop.

At any point during program execution the statement ' return <expression>;' can be used to stop execution. The returned value will be displayed in the Output tab of the Output window which can be displayed by pressing Alt+3 . For example:

return 45 + 0x10 ; would display 61 in the Output area. return is also used to return a value when defining custom functions (see Functions ).

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.