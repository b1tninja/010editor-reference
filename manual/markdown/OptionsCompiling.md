# 010 Editor Manual - Compiling Options

**Source:** [`manual/html/OptionsCompiling.htm`](../html/OptionsCompiling.htm) (SweetScape 010 Editor manual mirror).

## Page header
Compiling Options

## Summary (lead paragraphs)
The Compiling Options dialog is used to control some options for running scripts and templates. For more information about compiling see Running Templates and Scripts . The Compiling Options dialog can be accessed by clicking the ' Tools > Options... ' menu item and selecting ' Compiling '.

The Compile Options group controls warnings and how scripts and templates are run. If the Show Warnings toggle is enabled, any warnings generated during compilation will be displayed in the Output tab of the Output Window or in a popup window. Click the Configure button to control exactly which warnings are displayed as in the figure below. Any warnings that begin with Popup: generate a popup window and the other warnings are displayed in the Output Window. If the toggle is disabled no warnings will be displayed. Warnings can also be turned off for individual variables by using the syntax <warn=false> when defining the variable.

If the Auto Show Output Panel for Scripts toggle is enabled and a script calls the Printf function to display data, the Output tab of the Output Window will automatically be displayed. If this toggle is disabled, the Output Window will not automatically be shown but can be accessed by the ' View > Output ' menu option. Similarly the Auto Show Output Panel for Templates controls whether the Output Window is automatically shown when Printf is called in a template. If Show Target File after Running Script/Template is enabled and a Script or Template is run on a file, the editor will try to show the target file's tab. The file's tab will not be displayed if it is in the same Tab Group as the Script or Template being run. By default, unoptimized arrays have a parent node in the Template Results that can be opened or closed like a regular array. This parent node can be hidden by unchecking Unoptimized Arrays are Collapsible and see Optimizing Arrays of Structs for more information.

The next options are for the debugger . If the Breakpoints are Persistent toggle is on then any breakpoints will automatically be saved to disk and reloaded when 010 Editor is shut down and restarted. When the debugger is paused at a line in a Script or Template then placing the mouse cursor over the name of a variable in the Text Editor will attempt to display the value of the variable in a hint popup. If the Show Variable Hints when Debugging toggle is turned off then no hints are displayed. When a runtime error occurs while executing a Script or Template, a message box will popup asking to start the debugger if the Ask to start the debugger option is chosen. If the Start the debugger option is chosen then the cursor is placed at the line where the error occurred and the debugger is started. If Do not start debugging is chosen then the Script or Template is stopped as usual. The last two options can also be selected by choosing the Always use this action toggle in the message box asking to start the debugger. Note the debugger will not be started if debugging is turned off using ' Debug > Debugging Enabled '.

Which File Tabs are used to edit Scripts or Templates is now controlled in the Opening Files page of the Options dialog.

The Includes field contains a list of all directories to be searched when a file is included using the #include command in a template or script (see the Includes help topic for more information). Enter all directories to be searched separated by spaces in the Includes field. If a directory contains spaces, place double quotes around the directory in the field. Clicking the Browse button with the '+' symbol will allow adding a directory to the list using a standard directory select dialog. To control the directories where Scripts or Templates are stored see the Directory Options dialog. Click the Reset button to reset all options to their original values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.