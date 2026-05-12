# 010 Editor Manual - Selecting Bytes

**Source:** [`manual/SelectingBytes.htm`](../manual/SelectingBytes.htm) (SweetScape 010 Editor manual mirror).

## Page header
Selecting Bytes

## Section headings
- **Marking a Selection**

## Summary (lead paragraphs)
Before using any of the clipboard operations such as Cut, Copy, or Paste, a selection must be made on the file (see Using the Clipboard ). Selections can be made with either the mouse, the keyboard, or through the Select bar.

To select bytes with the mouse, click a file with the left mouse button and drag the mouse over the file. To select bytes with the keyboard, hold down the Shift key and move the caret with any of the cursor movement keys (see Using the Text Editor or Using the Hex Editor for a list of keys). The bytes that are selected will be displayed with a blue background. The number of bytes selected and the start address of the selection are displayed in the Status Bar along the bottom of the application.

Double-click the mouse and drag on a text file to select by words instead of characters. Triple-click the mouse to select a single line of text or triple-click and drag to select multiple lines of text.

All bytes in the file can be selected at once using the ' Select > Select All ' menu option. To move the caret to the start of the selection, right-click on the Editor Window and choose ' Selection > Goto Selection Start ' from the right-click menu. Similarly, to move the caret to the end of the selection select ' Selection > Goto Selection End ' from the right-click menu.

Bytes can also be selected with the Select bar (see Selecting a Range ). The start address and number of bytes of the selection can be viewed at any time by opening the Select bar.

If text in the editor already has coloring applied, for example through Syntax Highlighting or a Binary Template , then the selection colors are blended with the existing colors so that the existing colors are partially visible. The amount of blending and the color of the selected bytes can be controlled with the Theme/Color Options dialog.

An alternate way of setting the selection involves right-clicking on a byte in an editor and then choosing either the ' Selection > Mark Selection Start ' or ' Selection > Mark Selection End ' menu options from the right-click menu. Alternately, Mark Selection Start and Mark Selection End are available on the Select main menu. When Mark Selection Start or Mark Selection End is clicked while no selection has been made, 010 Editor will remember the selection mark for the current file (note that there is no visual indication where the selection marks are). If both the start and end of the selection have been marked, 010 Editor will select those bytes. If a selection is currently active and then either Mark Selection Start or Mark Selection End is clicked, the selection will be expanded or contracted so that the start or end lies at the correct position. This is a useful way to either enlarge or shrink a selection on a file.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.