# 010 Editor Manual - Using the Mini Map

**Source:** [`manual/MiniMap.htm`](../manual/MiniMap.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Mini Map

## Section headings
- **Text Mini Map**
- **Hex Mini Map**
- **Scrolling the Mini Map**
- **Mini Map Options**
- **Highlighting Structs**
- **Visualize**

## Summary (lead paragraphs)
The Mini Map is a diagram showing the overview of a file, displayed just to the left of the vertical scroll bar in the Text Editor (shown above left) and the Hex Editor (shown above right). The Mini Map can also be viewed in the Visualize tab. Hide or show the Mini Map by clicking ' View > Mini Map > Show Mini Map ' or by placing the mouse over the left-hand side of the Mini Map until the mouse cursor turns into a left-right arrow and then clicking and dragging to the right or left. Options for the Mini Map can be accessed by right-clicking on the Mini Map or by using ' View > Mini Map > Mini Map Options... '. Note that the options and size of the Mini Map are stored in the current Edit As and changing or resizing one Mini Map will change all Mini Maps that share that Edit As. Colors for different aspects of the Mini Map can be controlled with the Theme/Color Options dialog.

The Mini Map for text files displays a zoomed out view of each line of the file. All the colors from the regular editor are shown including the selection , Syntax Highlighting , Find results, Compare results, etc. By default the Mini Map is narrow and only shows the first part of each line but the Mini Map can be widened by placing the mouse cursor over the left side of the Mini Map until the cursor turns into a left-right arrow and then clicking and dragging to the left. The zoom factor and position of the Mini Map can be controlled with the Mini Map options .

When editing hex files the Mini Map on the right side of the editor shows the bytes of the file represented as colors. Each pixel of the Mini Map corresponds to a byte in the file being edited and a number of different algorithms exist to map byte values to colors. By default the Mini Map shows 16 bytes per line but this can be adjusted using the Mini Map options . Use the options dialog to change the zoom factor or adjust which coloring algorithm is used.

The default coloring algorithm takes the color of each byte obtained from the Template results, Find results, Compare results, etc. and then modifies the color according the value of each byte. Byte values closer to 0 darken the color, bytes values closer to 255 lighten the color, and byte values of 128 leave the color the same (see above left). To see the file without lightening or darkening the color, access the options dialog and set the Contrast to 0 (see above right). The bytes of the line the cursor is on in the Hex Editor are highlighted unless a selection is made in the editor. A number of different Colorize options are also available in the options dialog.

The Mini Map automatically scrolls when the vertical scroll bar is used in the editor or when the cursor moves to a new position. Placing the mouse over the Mini Map shows a highlighted rectangle which indicates the section of the Mini Map that is currently visible in the Text Editor or Hex Editor . Clicking on this highlighted rectangle and dragging up or down scrolls the editor and Mini Map similar to how a regular scroll bar works.

Single-clicking on a line in the Mini Map which is not in the highlighted rectangle will center the editor on the clicked line. Another way exists to scroll the Mini Map by clicking on a line not in the highlighted rectangle and then holding the mouse down and moving up or down. This technique starts a special velocity scroll mode where the editor will scroll faster up as the mouse is moved up or faster down as the mouse is moved down. Velocity scrolling is useful when scrolling through large files.

Access the Mini Map Options dialog by clicking ' View > Mini Map > Mini Map Options... ' or by right-clicking on the Mini Map. When the dialog is accessed by right-clicking note that the dialog is drawn without a title bar and clicking with the mouse outside the dialog will close the dialog and accept any changes. All options for the Mini Map are stored with the current Edit As and changing an option for one file will change all files that use that Edit As.

When editing text files the above dialog is displayed. Move the Mini Map to the left side of the Text Editor or Hex Editor by clicking the Mini Map Position drop-down and selecting Left Side . The Mini Map can be hidden by clicking the Hide button and if the Mini Map is already hidden when the dialog is displayed the button will be changed to a Show button instead. Clicking the Reset button changes all Mini Map options back to their defaults. The Mini Map can also be zoomed by dragging the Zoom slider and the zoom value is the height of each line in the Mini Map.

A different options dialog with more coloring options is displayed when editing hex files. The Mini Map Position , Hide , Reset and Zoom are all identical to the text Mini Map options above. The Highlight Structs toggle is discussed below in the Highlighting Structs section. The default coloring scheme for the Mini Map takes the color of each byte from the editor and then lightens it or darkens it depending upon the byte value. Byte values closer to 0 darker the color, byte values closer to 255 lighten the color and byte values of 128 do not modify the color. The amount of darkening or lightening can be adjusted by dragging the Contrast slider and setting a value of 0 disables any lightening or darkening of the bytes (see the Hex Mini Map above for a diagram). Dragging the Brightness slider right or left lightens or darkens the whole Mini Map.

Clicking the Colorize toggle enables other coloring modes that ignore any colors from the editor such as the Template results and applies colors based on the value of each byte. Note that the Contrast slider is not used when Colorize is enabled. The following Colorize choices are currently available:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.