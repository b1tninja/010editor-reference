# 010 Editor Manual - Introduction to Templates and Scripts

**Source:** [`manual/IntroTempScripts.htm`](../manual/IntroTempScripts.htm) (SweetScape 010 Editor manual mirror).

## Page header
Introduction to Templates and Scripts

## Summary (lead paragraphs)
One of the most powerful features of 010 Editor is the ability to run Binary Templates and Scripts. A Binary Template allows a binary file to be understood by parsing the file into a hierarchical structure. Templates have a similar syntax to C/C++ structs but they are run as a program. Every time a variable is declared in the Template, the variable is mapped to a set of bytes in the current file. For example, the following is a simple Template:

struct FILE { struct HEADER { char type [ 4 ] ; int version; int numRecords; } header; struct RECORD { int employeeId; char name [ 40 ] ; float salary; } record [ header . numRecords ] ; } file; The variable type is mapped to the bytes 0 to 3 in the file, version is mapped to the bytes 4 to 7, and numRecords is mapped to the bytes 8 to 11. Any time a variable is accessed, its value is read from the file, and any time the variable is assigned, its value is written to the file. These structures are different from regular C since they can contain control statements such as if , for , or while . Templates are executed in a similar fashion to an interpreter, where each line is executing starting from the top of the file.

A Script file also has a similar syntax to C and can be used to edit variables defined in a Template. For example, the Script:

int i; for ( i = 0 ; i < file . header . numRecords; i ++ ) file . record [ i ]. salary *= 2.0 ; can be used to double every employee's salary using the Template. Scripts can be used with Templates, or on their own to edit files or interact with the 010 Editor program. Scripts can also be used as macros to simplify repetitive tasks.

For an example of using Templates to parse files, open a ZIP, BMP, or BMP file and look at the Template Results panel below the Hex Editor Window. For more information see:

Binary Templates are stored as text files with extension ".bt" and Scripts are stored as text files with extension ".1sc". For information on executing Scripts or Templates see:

For an introduction to writing Templates see:

Binary Templates and Scripts others have created can easily be downloaded and installed from the 010 Editor Repository. See: Introduction to the Repository To help find and fix errors with Templates and Scripts, 010 Editor includes an advanced debugger. For more information see:

Although Templates are initially compiled, they are executed similar to an interpreter. The execution starts at the first line of Template and continues line by line, obeying any control statements encountered.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.