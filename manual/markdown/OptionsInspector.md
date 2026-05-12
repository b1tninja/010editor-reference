# 010 Editor Manual - Inspector/Tables Options

**Source:** [`manual/OptionsInspector.htm`](../manual/OptionsInspector.htm) (SweetScape 010 Editor manual mirror).

## Page header
Inspector/Tables Options

## Section headings
- **Hex Display Format**
- **Date/Time Format**

## Summary (lead paragraphs)
Use the Inspector/Tables Options dialog to control how the Inspector operates and how data is displayed in some tables such as the Template Results . View the Inspector/Tables Options window using ' Tools > Options... ' and selecting Inspector/Tables from the list or by right-clicking on the Inspector and choosing Customize... .

The Inspector tab allows interpreting binary data in a file in a number of different formats. If the Use Built-in Auto Inspector toggle is enabled then the normal list of data types will appear in the Inspector; however, to modify which data types are displayed enable the Use Custom Template option. The custom Inspector usually uses the file ' Inspector.bt ' which comes included with the 010 Editor Repository (if this file does not exist it will be installed when clicking OK or Edit ). A different Inspector template can be chosen by clicking the Browse button to the right of the text file and selecting a template. Clicking the Edit button will close the Options dialog and open the Template for editing.

When editing the ' Inspector.bt ' file, each variable is defined to start at the current cursor/caret position or at the start of the current selection, if a selection exists. Variables are defined this way by including the statement 'FSeek( pos );' before each variable definition. The different data types of the Inspector may be modifying by reordering or deleting the lines in the ' Inspector.bt ' file. Additionally, other data types including structs or unions may be added using any of the regular techniques for writing templates (see Introduction to Templates and Scripts ) but ensure the statement 'FSeek( pos );' exists before each variable. Even custom data types can be added to the Inspector file using Custom Variables . Every time the caret position is moved in a file, the ' Inspector.bt ' file will be rerun to move the variables to their new position.

Use the Hex Display Format drop-down list to choose whether hex numbers in tables are displayed with 'h' appended (choose FFh), with '0x' prepended (choose 0xFF), or with no prefix or suffix (choose FF). This setting affects the Inspector , the Template Results , as well as a variety of other places in the application such as the Compare Results , Process Tab and the Status Bar .

To control the formats used for date and time variable types in the Inspector use the Date/Time Format area. These formats are also used in the Template Results panel. Specify the default date format in the Default Date Format field and the default time format in the Default Time Field . A few common formats can be chosen by clicking the down arrow to the right of each field. The following characters can be used when writing formats:

The chosen date and time formats can be accessed in Scripts and Templates using the GetDefaultDateFormat , GetDefaultDateTimeFormat and GetDefaultTimeFormat functions. Click the Reset button to restore the Inspector/Tables Options to their default values. If the ' Inspector.bt ' file has been modified, when the Reset button is clicked you will be asked if you wish to delete all modifications and return to the original ' Inspector.bt ' file.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.