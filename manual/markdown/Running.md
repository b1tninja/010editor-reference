# 010 Editor Manual - Running Templates and Scripts

**Source:** [`manual/Running.htm`](../manual/Running.htm) (SweetScape 010 Editor manual mirror).

## Page header
Running Templates and Scripts

## Section headings
- **Running Templates**
- **Running Scripts**
- **Running Templates at an Offset**

## Summary (lead paragraphs)
A number of ways exist to run a Binary Template . The easiest is simply to open a file and if 010 Editor has a Binary Template installed for that type of file the Template will be run automatically. 010 Editor comes preinstalled with Binary Templates for BMP, WAV, and ZIP files but other Templates can be installed (see Template Options or the Repository Dialog for more information). Templates can also be run by clicking on the name of a Template in the ' Templates ' menu (Templates can be installed on this menu using the Template Options dialog or the Repository Dialog ), or by using the Debug Menu .

Another method of running Binary Templates is to use the Run Template icon in the Tool Bar as shown in the above figure. Clicking on the Run Template icon shows a scrollable list of Open Templates , Installed Templates and Recent Templates . Click on a Template name in the list to execute that Template on the current file. Once a Template has been run its name appears in the Template Results panel and click the icon in the Template Results header to rerun the template or press F5. If editing a text file, the Run Template icon can be used to execute a Syntax on the current file. Previous versions of 010 Editor used a File Bar above the Hex Editor to run a Template and the old-style File Bar can still be shown by clicking ' View > File Bar > Show Old File Bar '.

At the bottom of the drop-down list are six icons which can be used for creating a new Template, opening a Template, editing the Template associated to this file, editing the list of Installed Templates, viewing the Repository Dialog , or running a Template at an offset respectively. Note that the drop-down list can be resized by clicking and dragging the handle at the bottom-right corner of the list and 010 Editor will remember the chosen size. Which Template is chosen in the list is automatically remembered when 010 Editor is restarted if the Remember Last Template toggle is set in the Opening Files/Tabs Options dialog.

A final method of running a Template is to right-click on a file in the Hex Editor and selecting Run Template... or Run Template at Offset... . Clicking Run Template... shows a dialog with the same functionality as the Run Template icon drop-down list. Run Template at Offset is discussed below in the section on offsets .

Templates are currently run in a separate thread, meaning the editor can still be used while a Template is running. Only one Template or Script can be run at a time and the current Template or Script must be stopped before another can be run. To stop a running Template click ' Templates > Stop Template ' or press Shift+Esc.

When editing a Template (the Status Bar should display Template ), a Run icon will appear in the top-right corner of the editor (see Overlaid Icons ). Clicking the down arrow to the right of the Run button displays the Run on File drop-down list. Select a file from the list to run the current Template on that file. Once a file has been selected, the hint popup for the Run button will indicate Run on File: <file_name> and clicking the Run icon or pressing F5 will rerun the current Template. If the Run icon is clicked and no file has yet been selected, the Run on File drop-down menu is displayed instead. Clicking the Open icon at the bottom of the drop-down list allows opening a file and then immediately running the current Template on that file. After the Template has been run the editor will attempt to make the target data file visible in the editor. To turn off this feature see the Compiling Options dialog. The icon to the right of the Run icon is used to open the Repository Menu .

If an error occurs while running a Template, an error message will be displayed in the Output tab of the Output Window and a dialog will ask to start the debugger . Double-clicking on an error message in the Output tab will move the cursor to the line where the error occurred. Templates can also be run using the Command Line . Once a Template has been run the Working with Template Results help topic describes how to use the results.

Similar to running Templates, Scripts can be run by clicking on a Script name in the ' Scripts ' menu (see the Script Options dialog for information on placing a Script on this menu plus a list of all available Scripts). Also, through the same dialog Scripts can be set to run when a certain file type is opened or can be set to run automatically on application startup or shutdown. See the Repository Dialog for information on installing Scripts that other people have submitted to the repository.

Alternately, Scripts can be run by clicking the Run Script icon in the Tool Bar as shown in the above figure. Selected a Script from the list of Open Scripts , Installed Scripts , or Recent Scripts to run that Script on the current file. After a Script has been selected press F7 to run the Script again.

At the bottom of the drop-down list five icons exist. These icons can be used for creating a new Script, opening a Script, editing the Script associated with this file, editing the list of Installed Scripts, or viewing the Script Repository . The drop-down list can also be resized by clicking and dragging the handle at the bottom-right corner of the list. Which Script is selected in the list is automatically remembered when 010 Editor is restarted if the Remember Last Script toggle is checked in the Opening Files/Tabs Options dialog.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.