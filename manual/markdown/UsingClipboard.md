# 010 Editor Manual - Using the Clipboard

**Source:** [`manual/UsingClipboard.htm`](../manual/UsingClipboard.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Clipboard

## Section headings
- **Multiple Clipboards**
- **Clearing Clipboards**
- **Linux Selection Clipboard**
- **Exiting with Large Blocks**

## Summary (lead paragraphs)
The clipboard is a temporary scratch pad that can be used to store a block of bytes. The clipboard also makes possible moving data between applications. Most clipboard operations require that a set of bytes be selected in a file (see Selecting Bytes ). The following clipboard operations are supported:

Cut - The ' Edit > Cut ' menu option copies the selected bytes onto the clipboard and then deletes the bytes from the file. The keyboard shortcuts Ctrl+X and Shift+Del can also be used to cut data. Delete - Clicking the ' Edit > Delete ' menu option will delete the currently selected bytes from the file. The data on the clipboard will not be modified. Paste - The ' Edit > Paste ' menu option has two possible effects: When editing text data or when in Insert mode ( INS will appear in the Status Bar), the bytes on the clipboard are inserted into the file at the current cursor position. When editing hex data in Overwrite mode ( OVR will appear in the Status Bar), the bytes on the clipboard are written over the bytes in the file, starting at the cursor position. If a selection is made when a Paste operation is performed, the selection will first be deleted from the file and then the bytes will be inserted. The Insert key can be used to toggle between Insert and Overwrite mode. Note that the functionality of the Paste command can be changed in the Hex Editor Options dialog. The keyboard shortcuts Ctrl+V and Shift+Ins can also be used to paste data. Paste Special - Some applications copy data to the clipboard in a number of different formats. The ' Edit > Paste Special ' menu option is similar to the Paste menu option except that the format to paste can be chosen explicitly. See Using Paste Special for more information. Copy as Hex Text - Click the ' Edit > Copy As > Copy as Hex Text ' menu option to convert the selected bytes into text characters and copy the result onto the clipboard. For example, copying the bytes 0x2F and 0xB7 as text would result in the string "2F B7" being placed on the clipboard. Use this option to transfer binary data into a text editor or to search for a set of hex bytes in the Find tool. The format of the copied text can be adjusted using the Import/Export Options dialog. See Copying Hex Data for more information. Copy As ( export_type ) - Th...

Large blocks of memory can easily be copied to or from the clipboard (see Introduction to the Data Engine ). Use the ' Edit > Clipboard > Clear Clipboards ' menu option to remove all data from the 10 clipboards. This command is useful to prevent large blocks of data from being copied into memory when a file is saved or closed.

Unix systems have the concept of a selection clipboard where every time a selection is made in any program, the contents are automatically copied to a special clipboard. 010 Editor supports this clipboard on Linux systems and data can be pasted at the current mouse position by clicking the middle mouse button. Note that the position of the cursor does not change after data is pasted using this method. Any data selected in 010 Editor is available to be pasted in other programs using the middle-click technique. Note that the selection clipboard is independent of the regular clipboard used for copy and paste above.

Note that when the program exits, a large block of memory copied to the Windows clipboard is deleted unless the Leave Large Blocks on Clipboard on Exit toggle is set in the General Options .

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.