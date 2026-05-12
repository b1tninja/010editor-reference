# 010 Editor Manual - Using the Repository Dialog

**Source:** [`manual/RepositoryDialog.htm`](../manual/RepositoryDialog.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Repository Dialog

## Section headings
- **Templates Tab**
- **Scripts Tab**
- **Status Tab**
- **History Tab**

## Summary (lead paragraphs)
The Repository Dialog is the main way to install and uninstall Templates or Scripts in the Repository . Access the Repository Dialog by clicking either ' Templates > Template Repository ' or ' Scripts > Script Repository ' on the main menu. Once the dialog is displayed, click the Templates or Scripts tabs at the bottom of the screen to toggle between the repositories.

The Templates tab displays all Binary Templates in the repository in a list along the left side of the dialog. The icon next to a Template name indicates that Template is currently installed. By default all Templates are displayed sorted by Category . To display only installed Templates click the Show drop-down list and select Installed or select Uninstalled to show those templates that have not been installed. Selecting Update from the list shows only those templates that have updates available to install. To display all Templates sorted by file name but without categories click the Sort By drop-down list and select Alphabetic from the list. Selecting Newest from the Sort By menu shows the most recently modified Templates at the top of the list.

At the top-right of the dialog is a search field marked with the icon . To search for a value within the Repository click this field and type the value. Only those Templates that contain the value, either in the file name, description or file mask, will be displayed in the list of Templates. To cancel the search either delete the find value or click the X icon beside the search field.

Once a Template is selected from the list the information for that Template is displayed in the main part of the dialog. Click the Install button or right-click on the Template name in the list of Templates and choose Install to install the Template. When a Template is installed it is either downloaded from the online repository or copied from the local repository storage (see Updating the Repository ), and then copied into the Template Repository Directory as set in the Directory Options dialog. When a Template is installed a record is added to the list of installed Templates as stored in the Template Options dialog and the Template will appear on the main application Templates menu listed under its category.

To uninstall a Template that has been installed either click the Uninstall button, right-click on the Template name in the list of Templates and choose Uninstall , or delete the Template from the list of installed Templates in the Template Options dialog. When a Template is uninstalled using this dialog the installed file is automatically deleted from the Template Repository Directory unless the Template has been modified, in which case a dialog is displayed giving the option to either Delete or Keep the Template file.

Click the small down arrow to the right of the Uninstall button to access the Repository Menu . This menu has many of the same options as the Repository Menu located in a Script or Template editor. Click the Edit File menu option to close the Repository dialog and load the installed Template in the editor. Clicking the View Installed Information option closes the dialog and displays the information for this Template in the Template Options dialog. The other menu options on this menu are discussed in the Repository Menu help topic.

At the bottom of the dialog is the Available Versions table which lists all versions of the Template that exist in the Repository. Scroll to the right to view the comments for each version. Some Templates may require a newer version of 010 Editor to be installed as listed in the Requires Version column. Clicking the View button beside each version loads that version in the editor as a read-only file with the version included in the file name (for example, version 2.3 of ZIP.bt would be loaded as 'ZIP.v2.3.bt'). The file is not installed. To install a specific version click the down arrow to the right of the View button and choose Install from the popup menu. If modifications have been made to a file then installing a version will display a dialog box which asks to either Overwrite the modified file or Keep the modified file. Each version can be compared with the currently installed version by clicking the down arrow to the right of View and select Diff from the menu. To compare a version with the previous (older) version in the table select Diff with Previous from the menu.

If a Template is not installed the Ask to install this template when opening files toggle is displayed under the Available Versions table. If this toggle is enabled and a data file is opened in 010 Editor that matches the File Mask field (and the ID Bytes field if non-empty), then a dialog is displayed asking to install this Template (see Installing Files on Open from the Repository ). If this toggle is not checked then the dialog box will not be displayed.

The Scripts tab shows all 010 Editor Scripts that can be installed from the Repository. The functionality of this tab is identical to the Templates tab as described above except that the Ask to install this template when opening files toggle is not shown and 010 Editor will not ask to install Scripts when opening files in the main editor.

The current status of the repository is listed in the Status tab of the Repository dialog. The Updates area contains information about when the Repository was last updated and is discussed in the help topic Updating the Repository . The Installing and Terms areas are identical to the options available in the Repository Options and are discussed in that help topic.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.