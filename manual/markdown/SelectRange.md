# 010 Editor Manual - Selecting a Range

**Source:** [`manual/html/SelectRange.htm`](../html/SelectRange.htm) (SweetScape 010 Editor manual mirror).

## Page header
Selecting a Range

## Summary (lead paragraphs)
The Select Bar can be used to select a set of continuous bytes in a file by specifying a starting address and a number of bytes, or a start address and an end address. To open the Select Bar, click the ' Select > Select Range... ' menu option or press Ctrl+Shift+A . If the Select Bar is opened when a selection is already made, the bar will display the start address and size (or end address) of the current selection. Note that when the Select Bar is displayed and the selection changes in a file, the Select bar will update to display the current selection.

By default, the Select Bar specifies selections using a Start and a Size field. The Start field of the bar displays the address of the first byte of the selection. If no selection is made, the address will be the current caret position. The Size field displays the number of selected bytes. If no bytes are currently selected, this field shows the last number of bytes selected with this bar. Choose the numeric format for the fields by clicking either Hex or Decimal to the right of the size field, or use any of the formats described in the Introduction to Number Systems section. Press the Enter key to make a selection or the Esc key to hide the bar.

Alternately, selections can be controlled using a Start address and an End address. To enable this mode, click the Options button and enable the Specify Range using Start Address + End Address toggle. Enter the address of the end of the selection in the End field (note that the Size field disappears). For example, entering a Start address of 1000 and an End address of 1005 would select 5 bytes (the byte at the end address is not selected). When a selection is made, the start address and size of the selection are displayed in the status bar. See the Status Bar help topic for more information.

NOTE: The Select Bar will be hidden automatically after a period of inactivity. To control the length of the period of inactivity before hiding see the General Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.