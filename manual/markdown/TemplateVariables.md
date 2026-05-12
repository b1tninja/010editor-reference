# 010 Editor Manual - Declaring Template Variables

**Source:** [`manual/TemplateVariables.htm`](../manual/TemplateVariables.htm) (SweetScape 010 Editor manual mirror).

## Page header
Declaring Template Variables

## Section headings
- **Special Attributes**
- **Attribute Functions and Inline Expressions**
- **Display Format**
- **Colors**
- **Template Styles**
- **Endian**
- **Comments**
- **Names**
- **Positioning Variables**
- **Local Coordinates and File Coordinates**
- **Open Status of Variables**
- **Hidden Variables**
- **Local Variables**
- **Variable Editors**
- **Warnings**

## Summary (lead paragraphs)
Declaring variables in templates is performed similar to ANSI C and Scripts , but with an important difference: every time a variable is declared in the Template, that variable is mapped to a set of bytes in a file. For example, running the template:

char header [ 4 ] ; int numRecords; Would create the character array header , which is mapped to the first 4 bytes of the current file, and the integer numRecords , which is mapped to the next 4 bytes of the file. Both variables will be displayed in the Template Results panel and can be used for editing the file. See Data Types for a list of allowed types. Variables can also be edited using Scripts (see Editing Variables with Scripts ). Variables which behave as regular C variables can be declared using the local keyword as discussed below. The main way of grouping Template variables together is to declare structs or unions and see the Structs and Unions help topic for more information.

One or more special attributes can be specified after a variable inside '<' and '>' brackets. The following attributes are supported:

< format =hex|decimal|decimalhex|octal|binary, fgcolor =<color>|<function>|(<expression>), bgcolor =<color>|<function>|(<expression>), style =<style_name>, comment ="<string>"|<function>|(<expression>), name ="<string>"|<function>|(<expression>), open =true|false|suppress, hidden =true|false|<function>|(<expression>), read =<function>|(<expression>), write =<function>|(<expression>), size =<number>|<function>|(<expression>), edit =check|color|flags|none, pos =<number>|<function>|(<expression>), localpos =<number>|<function>|(<expression>), optimize =true|false, disasm =<constant>|<function>|(<expression>), warn =true|false > Special Attributes that can use <function> or (<expression>) statements are discussed in the Attribute Functions and Inline Expressions section and note (<expression>) is only available in 010 Editor version 12.0 or higher and <function> had extra limitations before version 12.0. Version 14.0 or higher is required for styles. Version 16.0 or higher is required for edit , pos , localpos or warn . All attributes are discussed below except for the read and write attributes (used to create Custom Variables ), the size attribute (used to create On-Demand Structures ), the optimize attribute (used with Optimized Arrays ) and the disasm attribute (used for Disassembly in Templates ).

Some special attributes as listed above can specify a custom function or expression. One method to do this is to specify just the function name in the attribute. For example:

typedef byte MySize <comment = SizeCommentFunc> ; Then the function should be defined in the Template after the typedef or variable is defined. The first argument for the function is a reference to the variable defined with '&'. Only the write function takes a second argument which is a string. The return type depends upon the type of attribute being defined and the following is an example of a comment function that returns a string:

string SizeCommentFunc ( MySize & s ) { if ( s < 0 ) return "Negative sizes not allowed." ; else return "" ; } Starting in 010 Editor version 12.0, inline functions can be written, meaning the code can be specified directly inside the '<' and '>' brackets without having to write a separate function. There are two ways to do this. First, a function can be called for the attribute and arguments can be passed to the function using '(' and ')' but the arguments can be any expression. For example:

typedef float Vec3f [ 3 ] <read = Str ( "<%g %g %g>" , this [ 0 ] , this [ 1 ] , this [ 2 ] )> ; Vec3f v1; The keyword this is used to access the current variable inside the expression and note that this[0] , this[1] , etc. can be used if the variable is an array. The second way to write an inline function is to write an expression enclosed inside brackets '(' and ')'. For example to specify a red background color if an int64 is negative use:

int64 c1 <bgcolor = ( this < 0 ? cRed : cNone )> ; More examples are available in the Inline Read and Write Functions section.

By default, all variables declared will be displayed in the Template Results panel in decimal format. To switch between hexadecimal, decimal, octal, or binary display formats, see the functions DisplayFormatDecimal , DisplayFormatHex , DisplayFormatDecimalHex , DisplayFormatBinary , and DisplayFormatOctal .

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.