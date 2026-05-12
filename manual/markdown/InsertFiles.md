# 010 Editor Manual - Inserting or Overwriting Files

**Source:** [`manual/html/InsertFiles.htm`](../html/InsertFiles.htm) (SweetScape 010 Editor manual mirror).

## Page header
Inserting or Overwriting Files

## Summary (lead paragraphs)
A file can easily be inserted into another file using the Insert File or Overwrite File tools. The Insert File tool inserts the bytes from another file into the current file at the current caret position whereas the Overwrite File overwrites any bytes in the current file with another file starting at the current caret position. Access the Insert File tool by clicking the ' Edit > Insert/Overwrite > Insert File... ' menu option or pressing Ctrl+I . Access the Overwrite File using the ' Edit > Insert/Overwrite > Overwrite File... ' menu option.

Position the caret at the address to insert or overwrite the file and activate the desired tool. Select any file with the file dialog box that is shown and click the Open button. Note that files cannot be inserted into drives or processes since the file size of drives and processes is always fixed (but data can be overwritten using the Overwrite File tool).

NOTE: 010 Editor employs a read-on-demand data engine that allows even huge files to be instantly inserted or overwritten. As a result, the inserted file should not be deleted until the edits have been saved to disk (see Introduction to the Data Engine for more information).

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.