# 010 Editor Manual - Hex Editor Options

**Source:** [`manual/OptionsHexEditor.htm`](../manual/OptionsHexEditor.htm) (SweetScape 010 Editor manual mirror).

## Page header
Hex Editor Options

## Section headings
- **Hex Display**
- **Insert**
- **Delete**
- **Highlighting**
- **Addresses**
- **Separator**
- **Template Variables**
- **Resize**

## Summary (lead paragraphs)
The Hex Editor Options dialog controls options when using the Hex Editor Window (see Using the Hex Editor for more information). Open the Hex Editor Options window by clicking ' Tools > Options... ' and choosing Hex Editor from the list.

Insert Always Insert Blocks - By default, when a block is pasted into the current editor using ' Edit > Paste ' or Ctrl+V , two results are possible: The block will be inserted when in Insert mode, or written over the current bytes when in Overwrite mode (see Using the Clipboard for details). When this toggle is enabled, the block will always be inserted, regardless of the current mode. Select Block After Paste - When this toggle is enabled and a block is pasted using ' Edit > Paste ' or Ctrl+V , the inserted bytes will be selected. If the toggle is disabled, no bytes will be selected. Warn on Insert - Every time that data is inserted into a file (either using ' Edit > Paste ' or typing in the editor while in Insert mode), the Status Bar will show a warning message in orange that bytes were inserted. If this toggle is turned off, just a regular message will be displayed in the Status Bar. Delete Allow Delete in Overwrite Mode - When this toggle is turned on and the Delete key is pressed while the hex editor is in Overwrite mode, the current selection will be deleted from the file. If no selection is made, the byte the caret is on will be deleted. When this toggle is disabled no deletions will be allowed in Overwrite mode and switch to Insert mode to delete bytes. Highlighting Highlight Current Byte - There are two possible areas in the Hex Editor Window: the left area, and the right area. When the caret is in one area, the current byte in the other area will be highlighted gray by default. If the toggle is turned off, the byte will no longer be highlighted. Highlight Modified Bytes - As changes are made to a file, the text in the Hex Editor will change to orange to indicate where modifications were made. By turning this toggle off, modified bytes will be displayed the same as unmodified bytes. Highlight Current Line - The line the caret is on in the Hex Editor Window is highlighted a yellow color on light themes and a dark blue color on dark themes. To turn off t...

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.