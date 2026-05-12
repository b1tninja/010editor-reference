# 010 Editor Manual - Using the Inspector

**Source:** [`manual/Inspector.htm`](../manual/Inspector.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Inspector

## Section headings
- **Inspector Tab**
- **Variables Tab**
- **Visualize Tab**
- **Bookmarks Tab**
- **Functions Tab**

## Summary (lead paragraphs)
The Inspector is a powerful tool for examining and editing binary data as a number of different data types. Grouped with the Inspector are seven other tabs: Variables , Visualize , Bookmarks , Functions , Watch , Call Stack and Breakpoints . The Variables tab shows a list of created variables after running a Binary Template or a Script. The variables are also displayed in the Template Results panel but the Variables tab is an alternate location that can be undocked. The Visualize tab is an alternate place to view the Mini Map . The Bookmarks tab displays a list of all created Bookmarks for the current file (see Using Bookmarks ) and the Functions tab shows a list of all built-in functions that can be used in Scripts or Templates. Show or hide the tabs by using the ' View > Inspector Windows ' menu. The Watch , Call Stack and Breakpoints tabs are discussed in the Using the Debugger help topic.

Some options for the different tabs are accessed by right-clicking with the mouse on the window. The Copy menu and the Column Display Format menu are discussed in the Using Tables topic. Use the Column Display Format menu to change the format the Value column uses to display data by choosing Hex , Decimal , Octal , or Binary . Click the Export CSV menu option to write the current table to a CSV file. A CSV file (which stands for Comma Separated Value) is a text file where each cell is written separated by commas and CSV files are written in UTF-8 format.

When viewing the tabs ( Inspector , Variables , Bookmarks , etc.) note that the small left and right arrows beside the tabs may need to be clicked to view all the tabs. The following sections discuss each tab:

When the Inspector tab is selected a list of data types will be displayed in a table . When a file is opened, the binary data starting at the caret is converted to each of the different data types and displayed in the table. As the caret is moved around the file, the Inspector will change to display the converted data. If a selection is made in the current file, the data is converted starting at the beginning of the selection. The following formats are supported in the Inspector:

Signed Byte - 8-bit number between -128 and 127 Unsigned Byte - 8-bit number between 0 and 255 Signed Short - 16-bit number between -32768 and 32767 Unsigned Short - 16-bit number between 0 and 65535 Signed Int - 32-bit number between -2147483648 and 2147483647 Unsigned Int - 32-bit number between 0 and 4294967295 Signed Int64 - 64-bit number -9223372036854775808 and 9223372036854775807 Unsigned Int64 - 64-bit number between 0 and 18446744073709551615 Float - 32-bit floating-point number between 1.175494351e-38 and 3.402823466e38 Double - 64-bit floating-point number between 2.2250738585072014e-308 and 1.7976931348623158e+308 Half Float - 16-bit floating-point number between 5.960464e-08 and 65504 String - Displays a null-terminated ASCII character string (limit of 256 characters). If a string is edited and characters are inserted or deleted, when in Insert mode, bytes will be inserted or deleted from the file but when in Overwrite mode, null bytes will be written to the file so that the file size does not change. Unicode - Displays a null-terminated Unicode character string (limit of 128 characters). Strings are edited in a similar manner to the String data type. --> DOSDATE - 16-bit value representing the date in DOS using the format 'MM/dd/yyyy' (note that M means month, d means day, and y means year). The date format can be controlled in the Inspector/Tables Options dialog. DOSTIME - 16-bit value representing the time in DOS using the format 'hh:mm:ss' (note that h means hour, m means minute, and s means second). The time format can be controlled in the Inspector/Tables Options dialog. FILETIME - 64-bit value representing date and time in Windows using the format 'MM/dd/yyyy hh:mm:ss'. FILETIME is a 64-bit integer representing the number of 100-nanosecond intervals since 01/01/1601 12:00 AM. The date format can be controlled in the Inspector/Tables Options dialog. OLETIME - 64-bit value representing date and time in OLE and Delphi using the format 'MM/dd/yyyy...

If the value displayed in the Value column is a valid positive decimal or hexadecimal number, right-clicking on the Inspector will show two additional menu options: ' Goto Address XXX ' and ' Goto Sector XXX ' where XXX is the number. Clicking Goto Address will jump to that byte position in the file. Clicking Goto Sector will multiple the number by the size of a sector and jump to that position. The size of a sector is usually 512 but will be automatically calculated for drives and can also be adjusted by clicking ' View > Division Lines > Set Sector Size ' when editing a hex file.

The different data types in Inspector may be reordered or deleted or your own custom data formats may be added. To customize the Inspector tab, right-click on the table and click the ' Customize... ' menu option or see the Inspector/Tables Options dialog.

The Variables tab displays variables that were generated by running a Script or a Binary Template (see Introduction to Templates and Scripts for more information). Usually the variables generated by a template are edited in the Template Results panel (see Working with Template Results ) but this tab provides an alternate place to view and edit variables that can be undocked. The functionality of this tab is the same as the Template Results panel and is discussed in the Working with Template Results help topic.

The Visualize tab allows viewing the bytes of a file as colors and provides the same information as the Mini Map . For text files each line is scaled down to a smaller size so that a larger part of the file is visible at one time. For hex files each byte of the file is mapped to a color and the number of bytes per line in the Visualize tab can be different than the number of bytes per line in the editor. Access the options for the tab by right-clicking on the diagram. See the Using the Mini Map help topic for more information about the different drawing options.

The Bookmarks tab displays a list of all bookmarks for the current file (see Using Bookmarks ). Bookmarks are displayed and edited similar to the Template Results panel mentioned above. The Name column displays the name from the Add/Edit Bookmark dialog. The Value column shows the bytes of the bookmark interpreted according to the data type. The Start and Size columns display the position of the bookmark, and the Color column shows the Foreground (Text) and Background colors from the dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.