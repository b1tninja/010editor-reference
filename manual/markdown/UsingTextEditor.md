# 010 Editor Manual - Using the Text Editor

**Source:** [`manual/html/UsingTextEditor.htm`](../html/UsingTextEditor.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Text Editor

## Section headings
- **The Caret/Cursor**
- **Editing Data**
- **Editor Keys**
- **Scrolling**
- **Mini Map**
- **Line Numbers and Ruler**
- **Word Wrap**
- **Right-Click Menu**
- **Overlaid Icons**
- **Splitting the Text Editor Window**
- **Column Mode**
- **Middle-Click Scrolling**
- **Byte-Order Marks**
- **Reloading Changes**
- **Syntax Highlighting**
- **Auto-Highlight Selection**
- **Editor Options**

## Summary (lead paragraphs)
The Text Editor Window (shown above) is the main method of viewing and editing text files in 010 Editor. Each text file that is loaded is displayed in a File Tab that shows a shortened form of the file name (the full file name can be viewed in the application title bar or in a hint popup displayed by placing the mouse cursor over the File Tab). The main area of the text editor shows the file interpreted as a series of characters (if a byte cannot be shown as a character a square symbol or cross will be displayed). On the left side of the Text Editor Window is a narrow bar which displays the current line number when the mouse is hovered over the bar. A zoomed-out view of the file is displayed as a Mini Map on the right side of the editor. A Ruler, located above the main area, displays the column offset from the start of each line and a small arrow indicates the current cursor position.

A caret (sometimes called a cursor) is flashing line in the Text Editor that indicates the current position for inserting, deleting, or editing data. Left-click with the mouse to move the caret or use the arrow keys on your keyboard (see Editor Keys below). When the editor is in Overwrite mode (see Editing Data below) the caret will be displayed as an underscore line and when the editor is in Insert mode the caret will be displayed as a vertical line. If the Text Editor Window is not active, the caret is drawn partially transparent and this is called the inactive caret. The style and shape of the caret can be controlled with the Editor Options dialog and the color of the caret and inactive caret can be controlled with the Theme/Color Options dialog.

To edit data in the editor, position the caret over the character to edit and type on the keyboard. The result of editing depends on whether the editor is in Insert or Overwrite mode. In Overwrite mode ( OVR appears in the Status Bar ) the characters typed will replace any existing characters. In Insert mode ( INS appears in the Status Bar) a new character will be inserted into the file. Note that the current Insert/Overwrite mode is stored separately for text and hex files. The current Insert/Overwrite mode can be changing using the Insert Key (see Editor Keys below) or by clicking INS/OVR in the status bar. Pressing the Delete key will delete the current character from the file.

After any edits are made a '*' character will appear in the File Tab to indicate that the file has been modified. Also, if bytes have been inserted a '*' character will appear by the file size in the Status Bar. Use the ' Edit > Undo ' and ' Edit > Redo ' menu options to undo or redo any modifications made to the file. The file can also be edited using the clipboard (see Using the Clipboard ).

The following keys can be used while editing a text file:

These keys can be customized using the Shortcut Options dialog.

When the caret is moved out of view using one of the Editor Keys above, dragging the mouse, or using a tool like Find or Goto; the editor will scroll so that the caret is visible. By default a short animation is shown but this animation can be turned off by unchecking Animated Scrolling in the Editor Options dialog. When using Find or Goto, the view will automatically try to scroll as far to the left as possible so that the target selection is still visible. To turn off this behavior see the Minimize Horizontal Scrolling toggle in the Editor Options dialog. The horizontal and vertical scroll bars or the mouse wheel can also be used to scroll the display. See the Middle-Click Scrolling section below for information on a special middle-click scrolling mode. When scrolled to the right, a vertical line is displayed in the editor and this line can be controlled with the Scroll Indicator Line color in the Theme/Color Options dialog.

At the right side of the editor is a diagram showing the lines of the file called the Mini Map. This diagram is discussed in the separate Mini Map help topic.

Line numbers are displayed by default for text files. To hide line numbers click ' View > Line Numbers > Show Line Numbers/Addresses ' or right-click on the left-most column and select Line Numbers > Show Line Numbers/Addresses . To change what is displayed in the line numbers column use the ' View > Line Numbers > Display Format ' menu. If line numbers are hidden then placing the mouse over the left-most column in the Text Editor shows the current line number in a hint popup as displayed above. Any lines that were created by word-wrap are marked with an arrow as described below. When line numbers are hidden a small triangle marker in the column indicates the last line of the file. The spacing of the line numbers can be adjusted using the Text Editor Options dialog.

A ruler is displayed at the top of the Text Editor to indicate the different columns of the file. For text files the column labels are hidden by default but can be shown by clicking ' View > Ruler > Show Labels '. The Ruler menu can also be accessed by right-clicking on the ruler. When labels are hidden and the mouse is placed over the ruler for a second, a hint popup is displayed showing the column the mouse is over (shown as Ruler: ) and the column the caret is on (shown as Current: ). Small arrows are drawn to indicate the current cursor position and the column the mouse is over and the arrows can be turned off using ' View > Ruler > Show Arrows '. Note that column 80 on the ruler is marked with a slightly thicker line.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.