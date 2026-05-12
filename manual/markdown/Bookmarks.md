# 010 Editor Manual - Using Bookmarks

**Source:** [`manual/html/Bookmarks.htm`](../html/Bookmarks.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Bookmarks

## Section headings
- **Adding Quick Bookmarks**
- **Adding Advanced Bookmarks**
- **Viewing Bookmarks**
- **Editing Bookmarks**
- **Searching for Bookmarks**
- **Removing Bookmarks**
- **Exporting and Importing Bookmarks**

## Summary (lead paragraphs)
A Bookmark is a set of bytes in a file that are marked as having special significance. There are two types of bookmarks in 010 Editor: Quick Bookmarks and Advanced Bookmarks. A Quick Bookmark just marks a position at a particular byte but an Advanced Bookmark may be given a name and may be interpreted as any of the standard data types or data types defined in a Binary Template. All bookmarks are persistent, meaning that created bookmarks will still exist after exiting and restarting 010 Editor. The bookmarks for the current file will be displayed in the Bookmarks tab (see Using the Inspector ).

Quick bookmarks provide an easy way to mark an important position or range in a file. To set a quick bookmark, move the caret to the position to mark or make a selection and then press Ctrl+F2 or click the ' Find > Toggle Bookmark ' menu option. The marked byte or selection will be displayed in a different color which is controlled by the Bookmarks color in the Theme/Color Options dialog. To move the cursor to a bookmark, press the F2 or Shift+F2 keys (see the Searching for Bookmarks section below for more information). To remove a bookmark move the caret to the bookmark you want to delete and press Ctrl+F2 or click the ' Find > Toggle Bookmark ' menu option again (see the Removing Bookmarks section below for more information).

To add an advanced bookmark, click the ' Find > Add/Edit Bookmark ' menu option, or press Ctrl+B . The ' Add Bookmark ' dialog will be displayed, which lists the attributes for the bookmark to create. To keep track of different bookmarks, a name can be assigned using the Name field, but this field is optional. Select the data type to interpret the bytes of the bookmark using the Type drop-down list. If a Binary Template has been run on the current file, the Type drop-down list will also include custom data types defined in the template (note that all bookmarks for a file using custom data types must come from the same Binary Template). If the bookmark to create is not an array, enter ' (none) ' or nothing in the Array Size field. To interpret the bookmark bytes as an array, enter the size in the Array Size field (note that a list of previously used sizes can be accessed by clicking the down arrow to the right of field).

Other options are available by clicking the Advanced Options section. If the Move Bookmark with Cursor toggle is enabled, the bookmark will move to the current cursor/caret position every time the Editor Window is clicked with the mouse or the caret is moved with the cursor keys. This feature is useful to apply structures from a Binary Template to a file when the exact file format is not known.

By default Bookmarks use the Bookmarks color in the Theme/Color Options dialog. To use a different color than the default enable the Use Custom Color toggle and choose a foreground color (text color) using the Fore color rectangle and a background color using the Back color rectangle. Clicking a color rectangle shows a drop-down list of colors and a new color for the bookmark can be chosen by clicking one of the colors in the list. Selecting None from the list means that the bookmark will not change the color. Click the More Colors... button from the drop-down list to select a different color using a standard color selection dialog.

Select which endian should be used when interpreting the data (see Introduction to Byte Ordering ) using the Little or Big toggles. By default, the endian will be the same endian as the file.

The start address and size of bookmark to be created will be listed beside the Start Address and Size labels respectively. If no bytes were selected in the file when the ' Add Bookmark ' dialog was opened, the Start Address will be the caret position in the file, and the Size will be calculated from the Type and Array Size . If a selection was made when opening the dialog, the Start Address will be the start of the selection, and the Size will be the size of the selection (note that the Array Size will be adjusted automatically to try to fit inside the selection). When defining a bookmark using a custom data type from a Binary Template, sometimes the size cannot be calculated so the size will be displayed as '???'.

Click the Add button to create the bookmark or the Cancel button to dismiss the dialog. The generated bookmarks will color the current file and be displayed in the Bookmarks tab of the Inspector. Note that when bookmarks are added to a file, that file will be displayed in the Bookmarked Files list in the Workspace (see Using the Workspace ).

A table of created bookmarks is available in the Bookmarks tab of the Inspector as shown below. Bookmarks that have not been assigned a name are marked as "(bookmark)" in the list. Clicking on a bookmark in the list selects the bytes for that bookmark in the editor.

To edit a bookmark, position the caret over a bookmark in a file, or select the bookmark from the Bookmarks tab of the Inspector as shown above. Clicking the ' Find > Add/Edit Bookmark ' menu option or pressing Ctrl+B will display the Bookmark dialog with all the values from the selected bookmark. Change any values and click Update to apply the changes or Cancel to ignore the changes.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.