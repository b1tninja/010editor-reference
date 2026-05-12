# 010 Editor Manual - File Dialog Options

**Source:** [`manual/OptionsFileDialogs.htm`](../manual/OptionsFileDialogs.htm) (SweetScape 010 Editor manual mirror).

## Page header
File Dialog Options

## Summary (lead paragraphs)
Use the File Dialog Options dialog to set the initial directory when opening a file dialog box. Click the ' Tools > Options... ' menu option and select ' File Dialogs ' from the list to view this dialog.

The File Dialog Directories section of the dialog controls the initial directory when various file dialogs are opened in the application (for example, when using ' File > Save As '). The Open File and Save File options control the directory when opening a file or saving a file . Note that when saving a template or script , the initial directory is controlled by the Save Template or Save Script options respectively. The Import File and Export File options control the initial directories when importing/exporting hex data. When opening templates or scripts (for example, by using ' Templates > Open Template ' or ' Scripts > Open Script '), the initial file dialog directories are controlled with the Open Template and Open Script options. Use the Open Project and Save Project options to control the directories for working with projects . There are four different options:

Last Used ??? Directory - where ??? is Open , Save , Import , Export , Template or Script . This option allows the file dialog to use a last-used directory specific to that option and the application global last-used directory is not touched. For example, by default when opening or saving templates a special last-used templates directory is used instead of the global last-used directory. Current File Location / Last Used Directory - If a file is being opened then the directory is extracted from the currently selected file. If the file is being saved, the file dialog is opened in the directory for that file if is exists. If no valid directory is found yet (for example, when saving a file that is first created), the file dialog is opened in the application global last-used directory. To ignore the current file location when saving, click the drop-down list and select Last Used Directory . Current File Location / Last Used ??? Directory - Similar to the Current File Location / Last Used Directory option, if a file being saved contains a valid directory the file dialog will be opened in that directory, or if a file is being opened and the current file contains a valid path the dialog will be opened in that directory. If the directory is not valid then the dialog will be opened in a directory as described in the Last Used ??? Directory option above. To ignore the current file location, select the Last Used ??? Directory option from the list. Clicking Reset will set all File Dialog options to their default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.