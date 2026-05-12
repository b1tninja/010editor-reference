# 010 Editor Manual - Script Options

**Source:** [`manual/OptionsScripts.htm`](../manual/OptionsScripts.htm) (SweetScape 010 Editor manual mirror).

## Page header
Script Options

## Section headings
- **Importing and Exporting Lists of Scripts**

## Summary (lead paragraphs)
The Script Options dialog lists all Scripts that have been installed, either from the local drive or from the 010 Editor Repository . Installed Scripts are listed on the main application Scripts menu and can be set to run on startup or shutdown or when certain files are loaded. Click ' Tools > Options... ' and select Scripts from the list, or click the ' Scripts > View Installed Scripts... ' menu option to view the Script Options dialog.

A list of scripts is contained in the upper portion of the dialog displayed in the format ' Category > Script Name '. Click the Add button to add a Script from the local drive into the list (note that multiple scripts can be added at the same time using the file dialog that is displayed). Select a script and click Delete to remove the script from the list (the file is not deleted from disk). The up or down arrows can be used to change the order of the scripts in the list.

Selecting a script will show its attributes in the Script Options box. Enter a name for the script in the Name field. This name will appear on the main Scripts menu (see the Scripts Menu ) listed under the given Category . If the Category is empty the Script will be listed near the top of the Scripts menu. Turning off the Visible toggle provides an easy way to hide a script from the menu without having to delete it. Enter the script file name in the File Name field. Scripts usually have the extension '.1sc' and are very similar to C files. Click the folder button beside the field to select a script using a file dialog box or press the Edit button to close the Options dialog and view the view in the editor.

If a mask is entered in the File Mask field the script will automatically be loaded when a file is opened that matches this mask. File masks may contain the characters '*' and '?' to specify wildcards and multiple masks may be separated by commas. If a value is given in the ID Bytes field then the Script will not be loaded unless the File Mask matches the file name and the ID Bytes match the bytes at the beginning of the file (see Template Options for more information on the ID Bytes). If the selected Script has been installed from the Repository then the version number will be listed in the Status field. Clicking the Show button will hide this dialog and display information about the script in the Repository Dialog .

If the Run on Load toggle is set, the script will automatically be run when it is loaded. Note that if a template is set to load automatically for the same file, the template will be loaded and run before the script. If the Show Editor on Load toggle is set, the script will be opened for editing in the interface. Enabling the Run on Startup toggle causes the script to be run when 010 Editor is started. The script can also be run while 010 Editor is closing by enabling the Run on Shutdown toggle.

The following scripts are available by default:

Randomize - Randomizes the current selection. Allows setting a minimum and maximum byte value. SplitFile - Splits a large file into a number of smaller files (for example, file.dat could be split into file.dat.001, file.dat.002, etc). The size of each file to create can be specified when running the script. MultiplePaste - Allows data on the clipboard to be pasted multiple times. IsASCII - Reports whether the current file contains only ASCII characters. The Set Shortcut button can be used to set a shortcut key for the selected script using the Shortcut Options dialog. Click the Reset button to restore all scripts to their default values.

The Script Options dialog can export a list of scripts to a file and this list can then be imported into another copy of 010 Editor. The list of scripts can be exporting by clicking the Export List... button. Select the file to write using the standard file dialog and the exported script list will have the extension ".1sl". Lists can also be imported by clicking the Import List... button. Exporting and importing scripts works the same way as exporting or importing templates. See the Template Options dialog for more information about exporting and importing using and the Import Script List dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.