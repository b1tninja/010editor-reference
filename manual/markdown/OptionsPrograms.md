# 010 Editor Manual - Program Options

**Source:** [`manual/OptionsPrograms.htm`](../manual/OptionsPrograms.htm) (SweetScape 010 Editor manual mirror).

## Page header
Program Options

## Summary (lead paragraphs)
The Program Options dialog allows adding custom programs on the Tools menu (see the Tools Menu for more information). Click the ' Tools > Options... ' menu option and select Programs from the list to view this dialog.

The upper area of the dialog contains a list of all custom programs available. Click the New button to add a new program to the list, or select an item and click Delete to remove a program from the list. The up and down arrows will change the order of items in the list.

After selecting a program from the list, the program's details will be shown in the Program Options box. The Name field indicates the caption that will appear on the Tools menu and may contains an '&' to indicate the default character. The Program field should contain the file name of the program to be run. Click the folder button beside the Program field to use a file dialog box to select a file. The arguments for the program can be specified in the Arguments field. The following special codes can be used in the argument list and will automatically be replaced by the correct values:

Cursor Position (%c) - Gives the address of the cursor in the file. Selection Start (%s) - If a selection exists, gives the address of the first byte of the selection. Selection Size (%z) - If a selection exists, gives the size of the selection. Note that all positions and sizes are specified in decimal format but can be specified in hex format by enabling the Hex Addresses toggle. Clicking the Insert button provides an easy way to insert different codes into the argument list. A working directory can be specified for the program by entering a directory into the Working Dir field. Click the folder button beside the field to use a directory browser to select the directory. Note that any environment variables can be included in the fields by using the '$' symbol (for example: '($WINDIR)' ). The special symbol ($PROGDIR) can be used to indicate the path where 010 Editor exists.

By default, the following custom programs are installed:

Windows Notepad... - Runs the standard Windows Notepad program with the currently loaded file. Click the Reset button to restore all Program Options to the default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.