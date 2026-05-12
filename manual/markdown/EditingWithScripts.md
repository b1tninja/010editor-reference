# 010 Editor Manual - Editing Variables with Scripts

**Source:** [`manual/html/EditingWithScripts.htm`](../html/EditingWithScripts.htm) (SweetScape 010 Editor manual mirror).

## Page header
Editing Variables with Scripts

## Summary (lead paragraphs)
Templates are meant only to parse a binary file and cannot modify the data file they are run on (however, Templates can be allowed to read from or write to other files using Permissions ). To edit the variables defined from the template, use either the Template Results panel or a script. When a variable is declared in a Template, it is mapped to a set of bytes in the file. Reading the variable causes bytes in the file to be read and assigning to the variable causes the bytes of the file to be modified.

Scripts have access to any of the variables declared in the Template and can use '.' to access data in structures. For example, using the template:

struct myStruct { int a; int b; int c; } s1, s2; a script could be written to swap the a variables:

int temp; temp = s1 . a; s1 . a = s2 . a; s2 . a = temp; Note that there is no special syntax to use; a Script can automatically access any Template variable if the Script is run after the Template is run. For a list of other special keywords that can be used while editing Template variables with a Script see Special Keywords . Using a combination of Templates and Scripts provides a powerful method of editing binary files.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.