# 010 Editor Manual - Preprocessor

**Source:** [`manual/html/Preprocessor.htm`](../html/Preprocessor.htm) (SweetScape 010 Editor manual mirror).

## Page header
Preprocessor

## Section headings
- **Defines**
- **Built-in Constants**
- **Conditional Compilation**
- **Warnings and Errors**
- **Includes**
- **External Functions**

## Summary (lead paragraphs)
When a Script or Template is executed, a special preprocessor stage is run before the main compilation of the file begins. In the preprocessor stage, the software finds any preprocessor directives (e.g. #include, #ifdef, #define, etc.) and uses them to modify the text of the original source code. Each preprocessor directive must start with a '#' character and the '#' character must be the first non-whitespace character on a line.

Special preprocessor constants can be defined using the syntax ' #define <constant_name> [ <text_value> ]'. For example: #define PI 3.14159265 Note that a semi-colon is not required after the statement. When any occurrence of the defined constant name is encountered in the rest of the source code (except inside of a string), it will be textually replaced with the defined value of the constant. For example:

Printf ( "ToRadians=%lf\n" , 90.0 * ( PI / 180.0 ) ); When defining a constant, a value is not required after the constant name in which case a constant is still defined but it will have an empty value. The constant value can be any text string and multi-line values can be defined by placing a '\' character as the last character of a value line. For example:

#define CHECK_VALUE if( value > 5) { \ Printf( "Invalid value %d\n", value ); \ Exit(-1); } int value = 4 ; CHECK_VALUE ; value = 10 ; CHECK_VALUE ; Constants created with #define can also include other constants that have previously been created with #define . For example:

#define FILE_ICON 12 #define FOLDER_ICON (FILE_ICON+100) Any constants that are defined can be undefined later using the syntax ' #undef <constant_name>'. Note that some preprocessors support macros with #define statements but this is not currently supported in 010 Editor.

_010_WIN - defined if running the Windows version of 010 Editor. _010_MAC - defined if running the Macintosh version of 010 Editor. _010_LINUX - defined if running a Linux version of 010 Editor. _010_64BIT - defined if 010 Editor is being run in 64-bit mode. _010_SCRIPT - defined if a script is currently being run (requires 010 Editor version 16 or later). Conditional Compilation The preprocessor directives #ifdef and #ifndef can be used to compile or ignore whole sections of source code depending on if certain constants were defined with the #define directive above. The syntax for these commands is:

#ifdef | #ifndef <constant_name> (...) [ #else ] (...) #endif A common usage of this syntax is to place code such as:

#ifndef CONSTANTS_H #define CONSTANTS_H at the beginning of a header file (e.g. constants.h) and then an '#endif' statement at the end of the header file. Then, if this header file is included twice into the source code with #include (see below), the code inside the header file will only be compiled once (the second time the file is included the constant CONSTANTS_H is already defined so the #ifndef statement skips the rest of the code). Note that multiple #ifdef or #ifndef statements can be nested inside of each other, but make sure the #endif statements properly line up with the #ifdef/#ifndef statements.

The preprocessor directive #warning can be used to output a message to the Output tab of the Output Window during compilation with the syntax ' #warning "<message>"'. For example:

#ifdef NUMBITS value = value + NUMBITS ; #else #warning "NUMBITS not defined!" #endif The #error directive is similar to the #warning directive except compilation will stop once an #error directive is reached. For example:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.