# 010 Editor Manual - Opening Files/Tabs Options

**Source:** [`manual/OptionsOpening.htm`](../manual/OptionsOpening.htm) (SweetScape 010 Editor manual mirror).

## Page header
Opening Files/Tabs Options

## Section headings
- **Opening Files**
- **Remember**
- **Tabs for Files**

## Summary (lead paragraphs)
Use the Opening Files/Tabs Options dialog to control options when a file is first opened , including which Edit As is assigned to the file and which File Tab the file uses. Access the Opening Files/Tabs Options dialog by clicking ' Tools > Options... ' and selecting Opening Files from the list.

When a file is opened in 010 Editor, the file is assigned an Edit As based on the masks in the Edit As Options dialog. If no mask matches the file name, 010 Editor can automatically try to detect the correct Edit As (select Auto-Detect Edit As ) or 010 Editor can assign a specific Edit As (select Use Edit As and choose the Edit As from the drop-down list).

If a file is opened but it is already loaded in the editor, a popup dialog will give the choice whether to view the file in the editor or to create a duplicate of the file as using ' Windows > Duplicate Window '. In the File is Already Open drop-down list, if Ask to Duplicate is selected then the popup dialog is displayed. If View File is selected then the file will be shown and no dialog will be displayed and if Duplicate is selected then the file will be duplicated and no dialog will be displayed. In the popup dialog, if Always use this option is selected then either View File or Duplicate will be become the current choice.

When using the command line to open a file but the given file does not exist, a popup dialog asks whether to create the file or ignore the request. If the File Does Not Exist from Command Line drop-down list is set to Ask to Create File then the popup dialog is displayed. If Create File is chosen then the file is automatically created and no dialog is shown. If Show Error is chosen then an error message is displayed instead. In the popup dialog, if Always use this option is checked then either Create File or Show Error will be selected.

When opening a Windows shortcut .LNK file, 010 Editor can either automatically open the target file specified in the LNK file, or the LNK file itself. If Ask to Open Target or LNK is chosen then a dialog pops up each time an LNK file is opening asking to either open the Target or the LNK. If Open Target is chosen then the target is extracted from the LNK file and opened, and if Open LNK is chosen then the original LNK file is opened and no dialog is displayed. The displayed popup dialog has a toggle Always use this option which can be checked to remember the chosen option and the chosen option can also be changed through this Option dialog page. Note that not all LNK file formats are supported and a warning message is displayed in the status bar if an unsupported LNK is opened.

If Force Read Only when Opening Files is enabled then all files that are opened in the editor are marked as read only. Turn off read only using ' Edit > Read Only ' or by right-clicking on an editor and choosing Read Only .

When the Remember Last Used Edit As toggle is set, 010 Editor will remember the last used Edit As , Endian, Character Set and Word Wrap setting for a file last time it was closed and will restore those settings when the file is opened again. If the Remember Last Cursor Position toggle is enabled then the last cursor position and scroll bar position will be restored to their previous values when 010 Editor is closed and reopened. The selection for a file will also be restored if Remember Last Selection is checked. If Remember Last Project is enabled and 010 Editor was closed when a project was active, the same project will be reloaded when 010 Editor is restarted.

If Remember Last Script or Remember Last Template is checked then the last Script or Template that was chosen for a file using one of the drop-down lists is restored when a workspace is opened. Note that the remembered Script or Template is not automatically run but the connection is set up so that ' Scripts > Run Script ', ' Templates > Run Template ', F5 or F7 will run the proper file. If the Syntax for the current file has been changed, that Syntax will automatically be assigned to the file when it is opened again if Remember Last Syntax is checked.

If the Show Tabs in Title Bar toggle is enabled, then all File Tabs are displayed in the Title Bar of the application. When the toggle is turned off, all File Tabs are displayed in a row above each editor, similar to older versions of 010 Editor.

By default, when a Script or Template or Syntax File is loaded in 010 Editor, it is displayed in a Floating Tab Group and all other files are loaded in the main interface. To control where Scripts or Templates are loaded use the Open Scripts and Template in drop-down list: Main Interface means use the main application window, Floating Tab Group means use a floating window and Current Tab Group means to use whichever Tab Group the currently selected file is in. Similarly, use the Open Syntax Files in drop-down list to control where Syntax Files (with extension .syntax010) are loaded. Use the Open Files in drop-down list to control where all other files are loaded using the same options.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.