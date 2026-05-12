# 010 Editor Manual - Structs and Unions

**Source:** [`manual/Structs.htm`](../manual/Structs.htm) (SweetScape 010 Editor manual mirror).

## Page header
Structs and Unions

## Section headings
- **Unions**
- **Structs with Arguments**
- **Recursive Structs**
- **Local Structs**

## Summary (lead paragraphs)
The C keyword ' struct ' can be used in a Template to define a hierarchical data structure when parsing a file. Structures can be defined using C/C++ syntax. For example:

struct myStruct { int a; int b; int c; }; See Declaring Template Variables for information on declaring the variables within a struct. Structs can also be declared in Scripts but require the local keyword to be used. Note the semi-colon after the struct definition is required. This syntax would actually generate a new type myStruct , but would not declare any variables until an instance of type myStruct is declared:

myStruct s; After this declaration, the Template Results would have an entry 'myStruct s' with an arrow beside it. Clicking the arrow would open the struct and display the variables a , b , and c beneath.

Instances of structures can be declared at the same time the structure is defined. For example:

struct myStruct { int a; int b; int c; } s1, s2; would generate two instances of myStruct. s1 would cover the first 12 bytes of the file (4 bytes for each of the 3 integers) and s2 would cover the next 12 bytes of the file.

These structs are more powerful than typical C structs since they may contain control statements such as if , for , or while . For example:

struct myIfStruct { int a; if ( a > 5 ) int b; else int c; } s; In this example, when s is declared only two variables are generated: a , and one of b or c . Remember that templates are executed as an interpreter would, evaluating each line before stepping to the next. The value of a is read directly from the current file.

Structures can be nested and array of structures can also be declared. For example:

struct { int width; struct COLOR { uchar r, g, b; } colors [ width ] ; } line1; Note that forward-declared structs are supported and structs can even be nested recursively. Typedefs can be used with structs as an alternate way to define a structure. For example:

typedef struct { ushort id; int size; } myData ; Unions A union can be declared using the same syntax as structs except that the keyword ' union ' is used instead of ' struct '. In a union, all the variables start at the same position and the size of the union is just large enough to contain the largest variable. For example, for the union:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.