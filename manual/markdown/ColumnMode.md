# 010 Editor Manual - Using Column Mode

**Source:** [`manual/ColumnMode.htm`](../manual/ColumnMode.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Column Mode

## Section headings
- **Columns Selections and the Clipboard**
- **Typing with Column Selections**
- **Hex Editor and Column Mode**

## Summary (lead paragraphs)
Column Mode is a special editing mode when using the Text Editor or Hex Editor where columns of data are selected instead of a contiguous set of bytes (see the image above for an example). To enter Column Mode click the ' View > Linefeeds > Column Mode ' menu option, type Alt+C , or click the Column Mode icon in the Toolbar. Column selections can also be made without entering Column Mode by holding down the Ctrl key while dragging the mouse.

Once a column selection is made in the Text Editor , use the regular clipboard operations to manipulate the data. For example, Ctrl+C will copy the column selection to the clipboard and the Delete key will delete the column selection. When a column selection has been copied to the clipboard and Paste is used, the data is pasted as columns even if the editor is not in Column Mode (this is useful so that Ctrl plus dragging can be used to make a column selection and the selection can be copied and pasted all without entering Column Mode). Pasting a column selection has a few different possibilities:

Note that when pasting and a column selection has been made, the column selection will be deleted before the paste occurs.

010 Editor has a special Column Insert Line which can be created by clicking and dragging straight down when in Column Mode or when the Ctrl key is held down. The Column Insert Line is displayed as a vertical blue line as shown in the figure below left. When a Column Insert Line exists and a key is typed on the keyboard, that key will be inserted onto each line at the same time. The following figure shows an example of typing the characters '{' and ' ' when a Column Selection Line is made:

This technique also works when regular column selections are made and keys are typed on the keyboard, except in this case the typed keys are written over the column selection until the cursor reaches the right side of the column selection. Typing additional keys when the cursor is at the right side of the column selection will insert that key on each line. For example, the following image shows making a column selection and then typing the characters 'DECL' on the keyboard (note the position of the cursor on the right-hand image):

Column mode also works with the Hex Editor except all selections are made by byte as shown above. Note that deleting a column selection in the Hex Editor can cause columns to be unsynchronized. Pasting works similar to the Text Editor Column Mode except that if a column selection exists while pasting, the selection will not be deleted before the paste occurs. Typing on a Column Selection works the same way as indicated above and typing 0's is a quick way to blank out a column selection.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.