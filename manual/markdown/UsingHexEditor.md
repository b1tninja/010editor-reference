# 010 Editor Manual - Using the Hex Editor

**Source:** [`manual/html/UsingHexEditor.htm`](../html/UsingHexEditor.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Hex Editor

## Section headings
- **The Caret/Cursor**
- **Editing Data**
- **Editor Keys**
- **Mini Map**
- **Right-Click Menu**
- **Swapping Bytes**
- **Splitting the Hex Editor Window**
- **Custom Starting Address**
- **Template Results**
- **Column Mode**
- **Middle-Click Scrolling**
- **Reloading Changes**
- **Copying Hex Data**
- **Editor Options**

## Summary (lead paragraphs)
The Hex Editor Window (shown above) is the main method of viewing and editing binary files in 010 Editor (to edit text files see Using the Text Editor ). A Hex Editor Window is displayed for each binary file that is loaded in the editor. Each file is displayed in a File Tab that displays a shortened form of the file name but the full file name can be viewed in the application title bar or in a hint popup displayed by placing the mouse cursor over the File Tab. The Hex Editor Window is divided into a left and a right area. By default, the left area displays the bytes of the file as a series of hexadecimal bytes and the right area displays the bytes as a series of characters (if a byte cannot be shown as a character a '.' will be displayed). At the far right of the editor by the scroll bar, the Mini Map displays the bytes of the file interpreted as a set of colors. To the left of the Hex Editor Window is a list of addresses. Each address indicates the file position of the first byte on the line. At the top of the window a Ruler indicates the byte offsets from the address on that line. The editor can be changed to display data in a number of different formats and to modify how the Hex Editor Window displays data see Using Edit As .

A caret (also called a cursor) is displayed in the Hex Editor Window as a flashing line and the caret indicates the current position for inserting, deleting, or editing data. Move the caret with the mouse by clicking anywhere in the main display with the left mouse button. Alternately, the arrow keys can be used to move the caret (see Editor Keys below). When the editor is in Overwrite mode (see Editing Data below) the caret will be displayed as an underscore line and when the editor is in Insert mode the caret will be displayed as a vertical line. When the caret is in the left or right areas, the byte the caret is currently over will be highlighted gray in the other area. Switch between areas by pressing the Tab key. If the Hex Editor Window is not focused, the caret is drawn partially transparent and this is called the inactive caret. Use the Editor Options dialog to control the style and shape of the caret and use the Theme/Color Options dialog to set the color of the caret and inactive caret.

To edit data in the editor, position the caret over the byte to edit. When the caret is in the left area (hexadecimal data) enter a valid hexadecimal digit (0 to 9 or A to F) to edit the data. When the caret is in the right area (character data) enter any character to edit the data.

The result of editing depends on whether the editor is in Insert or Overwrite mode. In Overwrite mode ( OVR appears in the Status Bar) the characters typed will replace any existing characters. In Insert mode ( INS appears in the Status Bar) a new byte will be inserted in the file (NOTE: when editing hexadecimal data, a byte is inserted only when the caret is over the first digit in the hexadecimal byte). The current Insert/Overwrite mode is stored separately for text and hex files and the current mode can be changing using the Insert Key (see Editor Keys below) or by clicking INS/OVR in the status bar. Pressing the Delete key will delete the current byte from the file.

When any edits are made to the file, a '*' character will appear in the title bar to indicate that the file has been modified. If bytes have been inserted, a '*' character will appear by the file size in the Status Bar. The ' Edit > Undo ' and ' Edit > Redo ' menu options can be used to undo or redo any changes made to the file. The file can also be edited using the clipboard (see Using the Clipboard for more information).

The following keys are available when editing the file:

The editor keys can be customized using the Shortcut Options dialog.

A diagram is displayed on the right side of the editor which shows the bytes of the file mapped to colors. This diagram is discussed in the separate Mini Map help topic.

A menu of editing options can be accessed by right-clicking on the Hex Editor Window. This menu is sub-set of the Edit Menu (see the Edit Menu for an explanation of each menu option). The Right-Click menu can also be used to set the current selection and see Selecting Bytes for more information. Templates can be run as regular or at an offset by clicking Run Template... or Run Template at Offset... and see Running Templates and Scripts for more information. Once Find or Compare has been performed on a file, the menu options Clear Find Results or Clear Compare Results appear and can be used to clear the Output tables. The Right-Click Menu can be customized by right-clicking the editor and selecting the Customize... menu option (see the Menu Options dialog for more information). Right-click on the address column to see a menu to control addresses or right-click on the ruler to see a menu to control the ruler and layout of each line.

010 Editor has the ability to visually swap bytes of data in the Hex Editor without modifying the underlying data (for example, compare the image above with the image at the top of this page). Data can be swapped in groups of 2 bytes, 4 bytes, 8 bytes, etc. and the number of bytes is controlled using the ' View > Group By ' menu. To swap data, choose a byte grouping in the ' View > Group By ' other than Byte and then enable the ' View > Group By > Swap Little-Endian Bytes by Group ' option. Note that swapping is only performed when the current file is in Little Endian mode and when swapping is enabled ' LIT<> ' will appear in the status bar. When bytes are swapped in the Hex Editor, the selection behaves differently because 010 Editor only supports selecting a contiguous range of bytes. Therefore, the selection may sometimes appear disjointed because of which bytes are selected. Hold down the Ctrl key when selecting using the keyboard to ensure that a full group is selected. To swap the bytes in the actual data file, see the Hex Operations dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.