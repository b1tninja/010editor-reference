# 010 Editor Manual - External (DLL) Functions

**Source:** [`manual/html/ScriptDLL.htm`](../html/ScriptDLL.htm) (SweetScape 010 Editor manual mirror).

## Page header
External (DLL) Functions

## Section headings
- **Linking to Functions**
- **Writing External Functions**
- **Passing Parameters to External Functions**
- **Returning Values from External Functions**
- **Granting Permission to Templates for using DLLs**

## Summary (lead paragraphs)
A Script or Template can execute a function that is located inside an external dynamic linked library. Supported libraries include DLLs on Windows (*.dll), Shared Objects on Linux (*.so), and DYLIB libraries on macOS (*.dylib). Note that the 32-bit version of 010 Editor must be used when calling functions in a 32-bit library and the 64-bit version of 010 Editor but be used when calling functions in an 64-bit library.

In a Script or Template, to declare a function that exists inside an external DLL enclose the function prototypes inside a ' #link "<filename>" ' statement and an ' #endlink ' statement. For example:

#link "TestDLL.dll" int MyDLLFunc1 ( int a, int b ); int MyDLLFunc2 (); #endlink The declared functions should not have a body (i.e. only a semicolon should be placed after the function prototype). Any other code can be placed inside a #link, #endlink section but limiting the code in this section to function prototypes is recommended. When a library file name is specified with a #link statement, 010 Editor looks for the library in a number of different directories in the same order that is used for Includes . Library file names can be given with no extension, in which case they will automatically be given the extension .dll on Windows, .so on Linux, or .dylib on macOS. If the library could not be found or the function could not be found inside the library then an error is generated and execution of the Script or Template is stopped. When using #link in a Template, the Template will require permission from the user to access the DLL as discussed below.

When creating a dynamic link library using C++, note that extern "C" should be used before the function definition to prevent name mangling. Also certain Window compilers may require __declspec(dllexport) before a function to allow that function to be called by external programs. For example to define a simple function in a C++ file the following could be used:

#define DECL_EXPORT extern "C" __declspec(dllexport) DECL_EXPORT int MyDLLTotalFunc ( int count, int * values ) { int i, total = 0 ; for ( i = 0 ; i < count; i ++ ) total += values [ i ] ; return total; } Functions written using 32-bit compilers must use the cdecl calling convention for parameter passing to work properly. Functions written using 64-bit compilers must use the Microsoft x64 calling conversion on Windows or the System V AMD64 ABI calling convention on Linux and macOS.

The following data types can be passed to external functions:

Note that passing structs is currently not supported with external DLLs although this may be supported for certain compilers in the future. As an example, the following code could be used in a Binary Template to call the C++ function defined above:

#link "TotalDLL.dll" int MyDLLTotalFunc ( int count, int values [] ); #endlink local int data [ 3 ] = { 30 , 45 , 2 }; local int total = MyDLLTotalFunc ( 3 , data ); Printf ( "Total = %d\n" , total ); Returning Values from External Functions The following data types can be returned from external functions:

When attempting to use the #link statement inside a Binary Template the following message is displayed:

The Allow button must be clicked to let the Template continue execution otherwise the Template will be stopped with an error. The permissions for executing functions inside DLLs can also be granted or revoked using the Permission Options dialog. Any permissions allowed or denied will be remembered the next time the Template is run.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.