# 010 Editor Manual - Using Find

**Source:** [`manual/Find.htm`](../manual/Find.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Find

## Section headings
- **Find Bar**
- **Find Options**
- **Output Window**
- **Find Next/Find Previous**
- **Type Specifiers**
- **Finding Variables**
- **Add Highlighter**
- **Clearing Find History**

## Summary (lead paragraphs)
The Find Bar can be used to find a string, a set of hex bytes, or a number of different data types within a file. The Find Bar can be accessed from the ' Find > Find... ' menu option, the Tool Bar, or by pressing Ctrl+F .

When performing a search, the Find Bar will be displayed at the bottom of the editor. Different data types may be searched by clicking the type name to the right of the Find label and choosing from the popup list. The following types are supported:

Hex Bytes (h) - searches for a set of hex bytes (for example: 'FF 00 CB'). ASCII String (a) - searches for an ASCII+ANSI string. Unicode String (u) EBCDIC String (e) Signed Byte (i8) Unsigned Byte (ui8) Signed Short (i16) Unsigned Short (ui16) Signed Int (i32) Unsigned Int (ui32) Signed Quad (i64) Unsigned Quad (ui64) Float (f) Double (lf) Variable Name (n) - see Finding Variables below Variable Value (v) - see Finding Variables below The value in brackets is the type specifier and can be used as a quick way to search for different data types (see the Type Specifiers section below). Enter a string, value, or hex bytes to search for in the text field and the field will automatically be converted to hexadecimal bytes and displayed to the right of the Options button. Note that when converting numbers or Unicode strings, the endian of the current file is used (see Introduction to Byte Ordering ). Note also that the text field can be resized by dragging the resize handle to the right of the Options button.

Typing in the Find Bar will automatically try to find the next occurrence but this can be turned off by unchecking the Incremental Search toggle in the Advanced Options below. Clicking the icon will find the next occurrence of the value in the current file or clicking the icon will find the previous occurrence. Clicking the All button will find all instances of the target value in the file and display the results in the Output Window (see below). Pressing the Enter key in the text field has three different possible outcomes depending upon which options are set in the Options dialog: If the Find All Occurrences toggle is set, pressing Enter will perform a Find All operation but if it is not set, pressing Enter will either find the next occurrence of the find value if the Down toggle is selected, or find the previous occurrence if the Up toggle is selected. If no occurrences of the find value could be found, the find text field will be displayed in an orange color. Press the Esc key to hide the Find Bar and return to editing the file. Long searches are threaded and can be stopped by clicking the Stop button than appears in the Find Bar.

Different options for the dialog can be displayed by clicking the Options button. When the Find All Occurrences toggle is set, pressing the Enter key in the text field will find all occurrences of the target value. When this toggle is not set, pressing the Enter key will either search for the next or previous occurrence of the target value depending upon if the Down or Up toggle is set in the Direction box.

By default all find operations search the entire file but it is possible to limit finding to one part of the file by using the Range box. To limit the find, first select some bytes in the file and then click the Options button and then the Lock to Selection button. The Lock to Selection button will be disabled if no selection exists. After this button is clicked, all subsequent find operations will be limited to the selection and the limited area will be highlighted brown in the editor (see Theme/Color Options to change the color). To return to searching the whole file, click the Unlock Selection button or the icon.

When searching for strings, two options are available: If the Match Case toggle is enabled, the target string will only match if the bytes match exactly. When the toggle is disabled, characters that are not the same case will match. If the Match Whole Word toggle is set, the target string will not match partial words. When Match Case is enabled, the Options button will contain the 'C' character in brackets and when the Match Whole Word toggle is enabled, the Options button will contain the 'W' character in brackets.

To search for regular expressions enable the Search with Regular Expressions toggle and see the separate Regular Expressions help topic. When regular expression searching is turned on the Options button will contain the 'R' character in brackets. When searching for strings or hex bytes, enable the Search with Wildcards toggle to allow the characters '*' and '?' to be used as wildcards in the text field. The '?' wildcard must match exactly one byte, and the '*' wildcard can match zero up to a certain maximum number of bytes. For example, the value 'adv*e?' would match both the strings 'advantages' and 'advised'. When searching for Hex Bytes using wildcards, '??' indicates one hex byte to find. The maximum number of bytes for a match can be specified using the Advanced Options section as described below. When the Search with Wildcards toggle is turned on, the special syntax '\*' and '\?' can be used to literally search for the characters '*' (ASCII code 0x2A) or '?' (ASCII code 0x3F).

When searching for floats or doubles, the Float Find Tolerance field will be displayed. This field can be used to search for numbers that are very close to other numbers. Because of numerical precision, sometimes floating-point numbers are stored as 2.00000001 instead of 2. Enter a tolerance value in the Float Find Tolerance field. Numbers that are within the tolerance above or below the target value will match.

If the Allow Multiple Find Ranges toggle is enabled, 010 Editor can store the search results from a number of different queries and can optionally color each query by a different color in the Editor Window. When this toggle is enabled, each query that is performed will add another section of results to the Find tab of the Output Window (see Output Window below for more information). Also, the coloring of the file can be controlled with the Advanced Options section as discussed below.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.