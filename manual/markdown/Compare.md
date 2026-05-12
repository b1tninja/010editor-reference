# 010 Editor Manual - Comparing Files

**Source:** [`manual/html/Compare.htm`](../html/Compare.htm) (SweetScape 010 Editor manual mirror).

## Page header
Comparing Files

## Section headings
- **Compare Dialog**
- **Comparing Blocks of Data**
- **Output Window**
- **Merging Differences**

## Summary (lead paragraphs)
The Compare Files tool allows the binary comparison of two files or two blocks of data for byte-by-byte differences. Note that this comparison is different than most text editors which only compare line-by-line. Access the Compare Files tool by clicking the ' Tools > Compare Files... ' menu option.

Enter the two files to compare in the File A and File B fields. Each field contains a drop-down list of all open files sorted alphabetically followed by a list of recent files sorted by access time. Click the browse button beside either field to use a file dialog box to select a file, or drag-and-drop a file from Windows Explorer to one of the fields. Note that if exactly two files are open in the main Tab Group in 010 Editor, the file names for those two files will be automatically entered in these fields, otherwise the current file is listed in File A and the most recent compare is listed in File B .

The Comparison tool supports two different algorithms: Binary and Byte by Byte . The Byte by Byte algorithm compares corresponding bytes between the two files (e.g. each byte at address n of file A is compared only against the byte at address n of file B) and will usually run quickly. The Binary algorithm tries to identify blocks within the files that match. This algorithm is fast when the number of differences is low between the files, but slows down if a number of differences exist (the algorithm is O(d 2 ) where d is the number of differences). Select which algorithm to use in the Comparison Type box.

Two options exist for running comparisons in the Options box. If the Match Case toggle is enabled, then ASCII strings must match exactly, otherwise strings with a mixture of upper and lowercase letters will match. If the Enable Synchronized Scrolling toggle is enabled then after the comparison, scrolling one of the files will cause the other file to scroll as well. Synchronized scrolling can be turned off using the ' Window > Synchronize Scrolling ' menu option (see the Window Menu for more information).

Other advanced options can be viewed by clicking the Advanced Options button. The display of the files after the comparison is determined by the Display Files box. If the Tile Horizontal toggle is set, the two files will be stacked one on top of the other. If the Tile Vertically toggle is selected, the files will be stacked side-by-side. The files will not be moved if the Do Not Tile toggle is selected. When tiling, the files may be moved from a Floating Tab Group to the main window and if this is done the Floating Tab Group will be hidden.

For the Binary algorithm, a limit can be put on the number of bytes the algorithm searches forward by entering a value in the Max Look-a-head field. The higher the value, the slower the algorithm may run. The Min Match Length field indicates the minimum number of consecutive bytes that must match to display a match in the final output. For higher values, random data is less likely to match, but for lower values, small matches might be ignored. The algorithm contains a heuristic that allows it to quickly accept matches of a certain size. Enter a valid in the Quick Match field to indicate the minimum number of bytes that must match for the heuristic. The lower the value, the faster the algorithm will run but the results may be less accurate. To prevent running out of memory, the compare algorithm puts a limit on the number of rows displayed in the Output Window but this limit can be changed using the Max Output Rows field.

If the Enable Synchronized Template Results Scrolling toggle is enabled then after the comparison, when the Template Results panel is scrolled in one file then it will be scrolled in the other file as well. This type of scrolling can be turned off using the ' Window > Synchronize Template Results Scrolling ' menu option and see the Window Menu for more information.

Click the Compare button to run the algorithm and display the results in the Output Window. The Cancel button will dismiss the dialog when pressed.

The binary comparison tool can also compare two blocks of data in two different files, or two blocks of data in the same file. Blocks to compare are specified in the Limit Comparison box. To compare only part of file A, click the File A toggle and enter the starting address of the block and number of bytes in the block in the Start and Size fields respectively. If the set of bytes to compare has been selected in the file, click the Get Selection icon to copy the start and size of the current selection into the proper fields. If the File A toggle is disabled, then the comparison will use the entire file A. Similarly, to limit the bytes compared in file B, enable the File B toggle and enter values in the Start and Size fields.

To compare two blocks of data in the same file, set the file name for File A and File B to be the same file name. Then specify which blocks of data to compare in the Limit Comparison box. Clicking the Compare button will cause two views of the file to be opened as could be done with the ' Window > Duplicate Window ' menu option.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.