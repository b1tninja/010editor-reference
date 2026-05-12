# 010 Editor Manual - Using Find in Files

**Source:** [`manual/FindInFiles.htm`](../manual/FindInFiles.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Find in Files

## Section headings
- **Find in Files Bar**
- **Output Window**

## Summary (lead paragraphs)
The Find in Files Bar is used to search for a set of bytes across multiple files. Open the Find in Files Bar by using the ' Find > Find in Files... ' menu option, the Tool Bar, or by pressing Ctrl+Shift+F .

When searching for a set of bytes across files, the Find in Files Bar is displayed at the bottom of the editor. The top portion of the bar, the Find Bar, is used to specify what bytes to search for and is identical to the normal Find Bar (see Using Find for more information).

The in Files area is used to indicate which files should be searched. To search a directory enter a directory in the text field to the right of the in Files label or choose a directory by clicking the browse button to the right of the field. To search only files that are currently open in the interface, click the arrow icon on the right side of the text field and select All Open Files from the popup list. To search only files in the current project select Current Project from the list. Enter a file name mask in the File Types field using the characters '*' and '?' to indicate wildcards. Multiple file masks can be entered in the field by separating them by commas or semi-colons (for example: "*.exe,*.dll"). If the Include Subdirectories toggle is enabled in the Options section, then the subdirectories of the specified directory are recursively searched as well.

Other options for the search can be set by clicking the Options button. Consult the Using Find help topic for information on the Match Case , Match Whole Words , Search with Regular Expressions and Search with Wildcards toggles. When a Find in Files operation is performed the results are displayed in the Output Window. By default, only those files that contain 1 or more occurrence of the find value are listed; however, all files that were searched can be listed in the Output Window by enabling the List All Files toggle.

The Advanced Options are the same as the Find Bar except for the addition of the Follow Symbolic Links toggle. When this toggle is enabled and the Include Subdirectories toggle is checked then any symbolic links that point to directories will be searched as well. When the Follow Symbolic Links toggle is disabled then any symbolic links that point to directories are ignored.

Click the Find in Files button to start the Find in Files search and note that for long searches a Stop button will appear in the Find in Files bar. Click the Stop button to halt the search. Note also that the text fields in the in Files section can be resized by dragging the resize handle to the right of the Browse button or to the right of the File Types field.

When some occurrences of the search string are located in a file, the results are displayed in the Find in Files tab of the Output Window. For each file which contains a match of the search string, a dark gray header line will be displayed in the Output Window indicating the name of the file and the number of occurrences found. All search occurrences for the file will be listed below the dark gray header, one per row of the table. Click the arrow buttons beside the header or double-click on the header to hide or show all search results for that file. Alternately, all headers can be closed by right-clicking on the table and selecting the ' Shrink All ' menu option, or all headers can be opened by right-clicking and selecting the ' Expand All ' menu option. Each search result lists the File , Address , and Value and where the search occurrence was found (note that the Size column can be shown by right-clicking on the table and choosing ' Show Size Column ').

Along the left side of the dialog is a graph indicating where the search occurrences were found. The graph will display information for the file the currently selected search occurrence is in. The selected search occurrence will be highlighted as a dark blue line and the other occurrences will be displayed as blue lines. The number below the graph indicates the total number of occurrences that were found in all files. The display format for each column can be set to hexadecimal or decimal by right-clicking on the Output Window and selecting ' Column Display Format '. Press the Enter key while a find occurrence is highlighted to load that file and move the caret to the address of the occurrence. Pressing Ctrl+Enter will perform a similar operation as pressing Enter , but the application focus will remain on the Output Window. The search results can be exported or imported from the table in CSV format by right-clicking on the results and choosing either Export CSV or Import from the right-click menu. Right-click the table and select ' Clear ' to clear all find in files results, or press the Esc key to hide the Output Window.

NOTE: The Find in Files Bar will be hidden automatically after a period of inactivity. To control the length of the period of inactivity before hiding see the General Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.