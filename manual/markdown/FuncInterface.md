# 010 Editor Manual - Interface Functions

**Source:** [`manual/html/FuncInterface.htm`](../html/FuncInterface.htm) (SweetScape 010 Editor manual mirror).

## Page header
Interface Functions

## Summary (lead paragraphs)
The following is a list of functions for communicating with the 010 Editor program when writing a Template or Script.

void AddBookmark( int64 pos, string name, string typename, int64 arraySize=-1, int forecolor=cNone, int backcolor=0xffffc4, int moveWithCursor=false ) Creates a bookmark in the file on which the current Script or Template is being executed (not the actual Script or Template). See Using Bookmarks for information on bookmarks and see Running Templates and Scripts for information on controlling on which file a Script or Template is run.

pos indicates the local address where the bookmark will be generated and name gives the name of the bookmark (this name can be empty). typename is a string giving the type of the bookmark to generate and this must be one of the built-in types or a user-defined type. If the type is user-defined and the AddBookmark function is run from a Template, that type must be defined in the current Template. If the type is user-defined and the AddBookmark function is run from a Script, that type must be defined in a Template that has already been run on the file (not in the current Script). Specify an array of variables using the arraySize argument or set arraySize to -1 to just generate a single variable. The text color of the bookmark can be indicated using the forecolor argument and the background color can be specified with the backcolor argument. If the moveWithCursor argument is true, the bookmark will reposition itself to the cursor as the cursor moves around the file.

For example, after loading a ZIP file in 010 Editor (which will cause the 'ZIP.bt' Template to be run on the file), create a new Script and run the following command on the file:

AddBookmark ( GetCursorPos (), "endmarker" , "ZIPENDLOCATOR" , -1 , cRed ); Here the type "ZIPENDLOCATOR" type is defined in the 'ZIP.bt' file, not in the Script. The functions GetNumBookmarks , GetBookmarkPos and GetBookmarkName can be used to query existing bookmarks and the RemoveBookmark function can be used to erase bookmarks.

int64 AddressFileToLocal( int64 fileAddress ) Given fileAddress , an address of a byte in a file, this function converts the address into local coordinates and returns the result. The local coordinate system is a method of referencing bytes in a file where 0 is the first byte and FileSize ()-1 is the last byte. Usually the file and local coordinate systems are the same unless editing a process or a file with a custom starting address . To convert from a local coordinate to a file coordinate use the AddressLocalToFile function. This function is equivalent to ProcessHeapToLocalAddress when editing a process.

int64 AddressLocalToFile( int64 localAddress ) Almost all functions in scripts and templates use the local coordinate system, where 0 is the first byte in the file and FileSize ()-1 is the last byte. This differs from the file coordinate system which uses the addresses as displayed in the Hex Editor . Given a localAddress , this function converts the address of the byte from local coordinates to file coordinates and returns the result. See AddressFileToLocal for the inverse operation and for more information. This function is equivalent to ProcessLocalToHeapAddress when editing a process.

void Assert( int value, const char msg[] = "" ) Stops execution of the script or template if the value is equal to zero. If execution is stopped, the text message msg will be displayed in the Output tab of the Output Window (note that this is an optional argument). Because conditional statements evaluate to 1 or 0 in C/C++, comparisons can be used in asserts. For example:

Assert ( numRecords > 10 , "numRecords should be more than 10." ); Requires 010 Editor v3.1 or higher. void ClearClipboard() Removes any data that is on the currently active clipboard. See the SetClipboardIndex function to control which clipboard is active.

void CopyBytesToClipboard( uchar buffer[], int size, int charset=CHARSET_ANSI, int bigendian=false ) Copies size bytes from the array buffer and places them on the currently active clipboard. If the data being copied represents a string, use the charset parameter to indicate which character set the string uses (see the ConvertString function for a list of character sets). If copying Unicode data the bigendian parameter indicates if the data is in big or little endian format, otherwise this parameter is ignored. See the SetClipboardIndex function to control which clipboard is currently active.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.