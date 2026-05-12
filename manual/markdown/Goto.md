# 010 Editor Manual - Using Goto

**Source:** [`manual/Goto.htm`](../manual/Goto.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Goto

## Section headings
- **Goto Bar**
- **Goto Again**

## Summary (lead paragraphs)
The Goto Bar can be used to jump to any address, line, sector, or short in the current file. Access the Goto Bar by using the ' Find > Goto... ' menu option, the Tool Bar, or by pressing Ctrl+G .

When using the Goto Bar, select what type of value to jump to using the popup list to the right of the Goto label. The following 4 options are available:

Line - When Line is chosen, the Goto Bar is used to jump to a line in the file. Enter ',l' after a value to force the Goto Bar to jump to a line. A column can specified after the line number by using , or |. For example, to jump to line 5 and column 3 enter "5,3" or "5|3". Sector - Choose Sector to jump to a sector in a file or drive (see Editing Drives for more information on sectors). Enter ',s' after a value to jump to a particular sector. To jump to an offset within a sector enter the ofset after , or |. For example, to jump to sector 0x100 with offset 5 enter "0x100,5" or "0x100|5". Short - A Short is a group of two bytes within a hex file. Selecting Short from the list will jump to the chosen short. Enter ',w' after a value to force the Goto Bar to jump to a short. When entering a numeric value in the text field, choose the numeric format by choosing Decimal or Hex in the area just to the right of the text field, or by using any of the formats described in the Introduction to Number Systems section. The position to seek will be calculated using an origin. The origin can be controlled by clicking the Options button and using the Direction radio buttons:

From Current Position - Origin is the current position and plus or minus are used to move forward or backward. For example, use '+10,l' to skip forward 10 lines or '-16,b' to skip backward 16 bytes. From End of File - Origin is at the end of the file. For example, use '<16' to jump to the 16th byte from the end of the file. Press the Enter key or click the Goto icon to the right of the text field to move the caret to the new position. Usually when pressing the Enter key, the Goto Bar is automatically hidden but this can be disabled by unchecking the Hide Goto Bar after Goto toggle in the Options dialog. When this toggle is unchecked and Enter is pressed, by default the input focus moves to the editor window. To keep the input focus in the Goto Bar field, uncheck the Focus Editor after Goto toggle. Pressing the Esc key will hide the Goto Bar and a list of the recent Goto commands can be accessed by clicking the small up arrow to the right of the text field.

Once the Goto tool has been used, clicking ' Find > Goto Again ' or pressing Ctrl+Shift+G will jump to the address again. If the address was relative to the current position, the caret will be moved again in the same direction. For example, enter '+48,b' in the Goto Bar and press Enter . Then press Ctrl+Shift+G multiple times to step through the file by 48 bytes.

NOTE: The Goto Bar will be hidden automatically after a period of inactivity. To control the length of the period of inactivity before hiding see the General Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.