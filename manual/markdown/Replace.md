# 010 Editor Manual - Using Replace

**Source:** [`manual/html/Replace.htm`](../html/Replace.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Replace

## Section headings
- **Replace Bar**
- **Replace Next/Replace Previous**

## Summary (lead paragraphs)
The Replace Bar is used to search and replace a set of bytes within a file. Access the Replace Bar from the ' Find > Replace... ' menu option, the Tool Bar, or by pressing Ctrl+R .

Specify the data to find in the Find Bar at the bottom of the editor. The functionality of this bar is documented in the Using Find help topic. Enter the value to replace in the Replace text field and choose the data type to replace with the popup list to the right of the Replace label (see Using Find for more information). The replace value will be converted to a set of hex bytes and displayed to the right of the Replace All button.

Click the Find buttons or to scan through the file without making any replacements. Clicking the Replace buttons or has two possible effects: If no occurrence of the Find value has been found yet, these buttons function just like the Find buttons and search for either the next or the previous occurrence of the Find value and set the selection to the result. If, however, a Find occurrence has been found (as indicated by the selection), clicking either of these buttons will replace the current selection with the Replace value and then search for another occurrence of the Find value. Pressing the Enter key while in the Replace text field will replace the value and find either the next or the previous occurrence depending upon if the Down or Up toggle is set in the Options dialog. Clicking the Replace All button automatically replaces all occurrences of the target value in the file.

All options when performing a Replace operation are identical to the Find Bar except for the Show All Replacements toggle and the Pad With Zeros toggle. When the Show All Replacements toggle is set and a Replace All operation is done, all the replacements will be shown in the Output Window (see Using Find for more information). When the Pad With Zeros toggle is enabled, a set of zero bytes will be appended to the replaced hex bytes until the length is the same as the find hex bytes. This feature is useful to replace a string with a shorter string without changing the file length. The Range box is similar in functionality to the Range box of the Find Bar. The Advanced Options are also documented in the Using Find help topic.

When replacing a large number of values (more than the Limit Find Occurrences setting in the Advanced Options ) and Show All Replacements is turned on, the text "Too many to display" will appear at the bottom of the Replace results. Note that all the replacements will be done but not all the replacements will be listed in the Replace results.

After a replacement has been performed, clicking the ' Find > Replace Next ' menu option or the ' Find > Replace Previous ' menu option will perform the replacement again. These commands, along with the ' Find > Find Next ' and ' Find > Find Previous ' menu options can be used to step through a file making replacements even when the Replace Bar is hidden.

NOTE: The Replace Bar will be hidden automatically after a period of inactivity. To control the length of the period of inactivity before hiding see the General Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.