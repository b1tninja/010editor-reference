# 010 Editor Manual - Editor Options

**Source:** [`manual/OptionsEditor.htm`](../manual/OptionsEditor.htm) (SweetScape 010 Editor manual mirror).

## Page header
Editor Options

## Section headings
- **Creating Files**
- **Closing Files**
- **Scrolling**
- **Caret/Cursor**
- **Input Method Editors**

## Summary (lead paragraphs)
The Editor Options dialog is used to modify options that affect both the Hex Editor Window and the Text Editor Window . Open the Editor Options dialog by clicking ' Tools > Options... ' and selecting Editor from the list.

Manage New File Types - Clicking this button displays the Manage New File Types dialog as shown above. This dialog controls which entries appear in the ' File > New ' menu or the menu accessed by clicking the down arrow to the right of the New icon in the tool bar. The Name column controls which text appears on the menus and the Edit As column controls which Edit As is assigned to the file after it is created. A Syntax can also be assigned to the file when it is created using the Syntax column. All Tree-sitter syntaxes are listed at the top of the drop-down list and all Binary Template syntaxes are listed at the bottom followed by "(Template)". By default new files are created without word wrap turned on but to turn on word wrap double-click an entry in the Word Wrap column and select Enabled . Click the '+' icon to create a New File Type, the 'x' button to delete a New File Type, or the arrow keys to move a New File Type up or down in the list. Shortcut keys can be assigned to the different New File Types using the Shortcut Options dialog. Closing Files Hide Floating Tab Group when All Files are Closed - When all tabs are closed in the Floating Tab Group , it will automatically be hidden if this toggle is enabled. If this toggle is turned off, an empty Floating Tab Group will be displayed when all tabs are closed. The Floating Tab Group can be displayed by clicking ' View > Floating Tab Group ' on the main menu. Show Startup Page when All Files are Closed - When this toggle is enabled and all files are closed in the editor, the Startup Page will automatically be shown. If this toggle is disabled then a blank interface will be shown when all files are closed and right-click on the blank interface and select ' Startup Page ' to display the Startup Page. Scrolling Animated Scrolling - The Text Editor and Hex Editor show a short animation when using the Page Up or Page Down keys, or when jumping to a new position in a file using tools such as Find or Goto. To turn o...

Height - Specifies the height in pixels the caret extends above and below the current line. Choose Normal for no extension or + a number to extend that many pixels above and below the line. Insert Caret - Sets the shape of the caret in Insert mode (see Editing Data for more information). The first four options indicate a flashing vertical line in four possible thicknesses, ranging from thin to thick. The last two options indicate an underscore caret or a block caret. Overwrite Caret - Sets the shape of the caret in Overwrite mode (see Editing Data for more information). See the Insert Caret section above for the list of possible shapes. Show Inactive Caret - When an editor is not currently focused, the caret is drawn as a transparent line to indicate where the caret was. This line is called the Inactive Caret and can be disabled by turning the Show Inactive Caret toggle off. Input Method Editors Allow Input Method Editors (IMEs) (Linux Only) - Input Method Editors (IMEs) are special in place editors designed for entering non-ASCII characters into an editor. On some versions on Linux, IMEs can cause issues with the editor and are turned off by default. To re-enable IMEs click the Allow Input Method Editors (IMEs) toggle. The Reset button can be used to return all of the Editor Options to their default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.