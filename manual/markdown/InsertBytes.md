# 010 Editor Manual - Inserting or Overwriting Bytes

**Source:** [`manual/html/InsertBytes.htm`](../html/InsertBytes.htm) (SweetScape 010 Editor manual mirror).

## Page header
Inserting or Overwriting Bytes

## Summary (lead paragraphs)
Two tools are included with 010 Editor that make inserting or overwriting blocks of bytes easy (for example, if you want to insert a row of eighty '*' characters these tools make this operation simple).

Click the ' Edit > Insert/Overwrite > Insert Bytes... ' menu option to access the Insert Bytes tool. The current caret address will be displayed in the Start Address field. Enter the number of bytes to insert in the Size field. The address and size can be displayed in decimal or hex formats by clicking on the Decimal or Hex radio buttons. Usually the range of bytes to insert is specified using the Size field but the range can also be specified using an End Address by clicking the Options button and enabling the Specify Range using Start Address + End Address toggle (note that the range does not include the byte at the end address).

The value of the bytes to be inserted can be controlled in the Byte Value box by entering a value in the Char , Hex or Decimal fields. Note that the value is automatically converted between the different formats as a number is entered in either field (the Char field will be left blank if there is no printable character that corresponds to the byte value). Click the OK button to insert the bytes, or the Cancel button to close the dialog without making changes. Note that bytes cannot be inserted into a drive or a process.

Click the ' Edit > Insert/Overwrite > Overwrite Bytes... ' menu option to access the Overwrite Bytes tool. If any bytes are selected in the editor, the starting address of the selection will be displayed in the Start Address field and the number of bytes selected will be displayed in the Size field; otherwise, the current caret position will be listed in the Start Address field and the last number of filled bytes will be listed in the Size field. The range of bytes to overwrite can also be specified by using a start address and end address (see the Insert Bytes dialog above for more information). A Byte Value can be entered as when using the Insert Bytes tool. Click OK to set all the bytes specified by the Range to the given Byte Value . The Cancel button will close the dialog with no changes.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.