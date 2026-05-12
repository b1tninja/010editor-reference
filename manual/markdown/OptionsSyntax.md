# 010 Editor Manual - Syntax Options

**Source:** [`manual/OptionsSyntax.htm`](../manual/OptionsSyntax.htm) (SweetScape 010 Editor manual mirror).

## Page header
Syntax Options

## Summary (lead paragraphs)
The Syntax Options dialog lists all Tree-sitter Syntaxes that are installed and see Using Syntaxes for more information about syntaxes. To access this dialog click the ' Tools > Options... ' menu option and select Syntax from the list. Assign a Tree-sitter Syntax to a file using the ' View > Syntax ' menu or by clicking the Syntax section of the Status Bar .

A list of all Tree-sitter syntaxes as at the top of the dialog and use the Up and Down arrows to reorder the list. Clicking Delete removes the syntax from the list but does not delete all of the associated files from disk. Clicking Add... opens a standard file dialog box that can be used to select a .syntax010 file to add to the list. Note that a dynamic link library is also required when adding a Tree-sitter Syntax and see Writing Tree-sitter Syntaxes for more information on created Tree-sitter Syntaxes.

When a Syntax is selected in the list, its information is displayed in the Syntax Options section. The name of the syntax in the Name field is displayed in the ' View > Syntax ' menu and the Syntax section of the Status Bar. When the Visible toggle is unchecked, the syntax will not be displayed in the ' View > Syntax ' or the Status Bar. The Syntax File field gives the file name of the .syntax010 file used to configure syntax highlighting, matching braces/tags, etc. Click the Open icon to select a new file or click the Edit... to open the .syntax010 file in the editor and close the Syntax Options dialog. The file name of the dynamic link library is shown in the DLL File field and this file is required for the syntax to work. Click the Open icon to select a new DLL file.

The File Mask and ID Regex fields control which files are automatically assigned this syntax when they are opened. The File Mask uses wildcard characters to match the name of a file being opened and can use '*' to indicate zero or more matches, or '?' to indicate exactly one match. Use the comma to separate multiple masks. For example, "*.bt,*.1sc" would match files with the extension ".bt" or ".1sc". If a regular expression is listed in the ID Regex field then that regular expression must match the first line of the file being opened before the syntax is assigned.

Tree-sitter Syntaxes support injections where one syntax may exist inside another syntax (for example, JavaScript or CSS code may exist inside an HTML file). If the current syntax can be injected into other syntaxes, enter a name in the Injection Name field. This injection name is used when writing a .syntax010 file and see Editing Injections for more information.

When a file is opened in the editor, it is assigned an Edit As by checking each Mask of each Edit As in the Edit As Options dialog. If no Edit As matches but the file is assigned the current syntax, then the Edit As from the Default Edit As field is applied to the file. Use the drop-down list to select a different Edit As.

The ' View > Syntax ' menu shows a list of recently used Tree-sitter Syntaxes at the top of the menu. To force the current syntax to always be displayed in the recently used list, enable the Show at Top Level toggle. Turn off the use of all Tree-sitter Syntaxes by enabling the Disabled All Tree-sitter Syntaxes toggle. When this toggle is on, only Binary Template based syntaxes will be used.

Clicking the Reset button will return the list of syntaxes to the original list when 010 Editor was installed and will reset all fields to their original values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.