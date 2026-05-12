# 010 Editor Manual - Opening Files

**Source:** [`manual/OpeningFiles.htm`](../manual/OpeningFiles.htm) (SweetScape 010 Editor manual mirror).

## Page header
Opening Files

## Summary (lead paragraphs)
010 Editor contains a number of methods for opening files. Clicking the ' File > Open File... ' menu option, or pressing Ctrl+O opens a file dialog box. After selecting a file and clicking the Open button, the file will be displayed as either a Text Editor Window or a Hex Editor Window in the main display. See Using the Text Editor or Using the Hex Editor for information on editing the file. When opening a file, if the Open as read-only toggle is selected in the dialog, the file will be opened in read-only mode. To control which directory is used when the Open File dialog is shown see the Directory Options dialog.

The editor stores a list of files that have been recently opened. This list can be accessed from the ' File > Open Recent ' menu option, from the Workspace (see Using the Workspace ), or from the Startup Page (see the Using the Startup Page ). Click a file from the Open Recent menu to load it into memory. The number of files in the list can be controlled from the General Options dialog.

Another way of opening files is to use the standard Windows Explorer program. When 010 Editor was installed, enabling the ' Add 010 Editor to explorer right-click menu ' toggle in the install program will allow files to be opened from the Explorer. Right click on a file and select the ' 010 Editor ' option. Another method of opening files is to drag-and-drop a file from the Windows Explorer onto a running 010 Editor program. If dragging and dropping an Intel Hex or Motorola S-Record file, the file will automatically be imported (this functionality can be turned off using the Import/Export Options dialog). Files can also be associated with 010 Editor, meaning that double-clicking a file in the Windows Explorer will open the file in 010 Editor. Intel Hex files or Motorola S-Record files can be automatically associated with 010 Editor by selecting the ' Associate Intel Hex files with 010 Editor ' or ' Associate Motorola S-Records with 010 Editor ' toggle in the install program. For more information on Intel Hex or Motorola S-Record files, see Importing/Exporting Files .

The Workspace also contains a simplified browser that can be used to open files. Files can be loaded from the Favorite Files list or the Bookmarked Files list in the Workspace. Files can be opened when starting 010 Editor from the command line and see Command Line Parameters for more information. 010 Editor can also be used to edit hard drives and processes. See the Editing Drives or Editing Processes help topics for more information.

After a file is opened, how it is displayed in the editor depends upon which Edit As is assigned to the file. See the Using Edit As help topic for more information. Various options to control how files are opened are available in the Opening Files/Tabs Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.