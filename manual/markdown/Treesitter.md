# 010 Editor Manual - Using Syntaxes

**Source:** [`manual/html/Treesitter.htm`](../html/Treesitter.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Syntaxes

## Section headings
- **Choosing a Syntax**
- **Syntax Menu**
- **Syntax Highlighting**
- **Auto-Indent**
- **Matching Braces/Tags**
- **Show Section Lines**
- **Installing Syntaxes**
- **Writing Syntaxes**
- **Syntaxes for Large Files**

## Summary (lead paragraphs)
A syntax is a set of rules that define a language for text files such as C++, JavaScript, XML, etc. 010 Editor supports two types of syntaxes: Tree-sitter based syntaxes and Binary Template based syntaxes. Tree-sitter syntaxes parse source code into a syntax tree and can update the tree in real-time as the file is edited. Binary Template syntaxes parse one line at a time using a Binary Template . Tree-sitter syntaxes requires more memory and are slower than Binary Template syntaxes but Tree-sitter syntaxes provide much more detail in syntax highlighting and provide advanced features such as matching braces, expand selection, and identifying code sections.

The syntax for the current file can be chosen using the ' View > Syntax ' menu as discussed below , or the Syntax section of the Status Bar . Click on a Syntax name to activate that syntax. To remove a Syntax from a file, click ' View > Syntax > None (Plain) ' or click on the Syntax section of the Status Bar and select ' (none - plain) '. Note the Syntax menu and status bar section are only shown when editing text files. The Status Bar will display 'Plain' if no Syntax Highlighter is active and will display ' (Template) ' after a syntax name if that syntax is from a Binary Template.

Syntaxes are automatically assigned when a file is opened based on the file's extension. To configure which syntaxes are applied see the File Mask field in the Syntax Options dialog for Tree-sitter syntaxes, or the File Mask field in the Template Options dialog for Binary Template syntaxes. If a different syntax is chosen for a file, that syntax will be remembered the next time the file is opened and to disable remembering syntaxes see the Remember Last Syntax toggle in the Opening Files/Tabs Options dialog. To control which Syntax is applied when creating a new file see the Manage New File Types button in the Editor Options dialog. All Tree-sitter syntaxes can be turned off using the Syntax Options dialog.

Choose a syntax for the current text file by clicking ' View > Syntax ' on the main menu. Select None (Plain) to remove any syntax from the file and display the file as a plain text file. A list of recently used syntaxes is displayed at the top of this menu and click on a syntax name to switch the current file to that syntax. To list all available Tree-sitter syntaxes, select the All Syntaxes (Tree-sitter) menu option and to list all available Binary Template syntaxes, select the All Syntaxes (Templates) menu option. View all installed Tree-sitter syntaxes with the Syntax Options dialog and view all installed Template syntaxes with the Template Options dialog. To force a Tree-sitter syntax to always display at the top of the Syntax menu see the Show at Top Level toggle in the Syntax Options dialog.

Next in the Syntax menu are toggles for controlling Auto-Indent , Highlight Matching Braces/Tags and Show Section Lines . See the sections below for more information.

The ' View > Syntax > Edit Syntax File ' menu option can be used to open the .syntax010 file that is associated with the current Tree-sitter syntax. The file will be opened as a new file in the editor and see Writing Tree-sitter Syntaxes for more information. Once changes are made to the .syntax010 file, click ' View > Syntax > Refresh Syntax ' to apply the changes to all files that use that syntax. The Print Syntax Tree menu option will print out the current parse tree from a Tree-sitter syntax to the Output tab of the Output panel and see Printing Syntax Trees for more information.

Colors can be applied to a file using the current syntax. See the separate Syntax Highlighting help topic for more information.

Turn Auto-Indent on or off using ' View > Syntax > Auto-Indent '. When Auto-Indent is on and the Enter key is pressed on a line that is indented, a new line will be created and extra spaces will automatically be added to the line so that the indentation is the same as the previous line. If editing C/C++ source code or an 010 Editor Binary Template or Script and a line ends with '{' or '(', then extra spaces will be added to the line according to the indent size set with Tabs/Whitespace > Indent Size . Extra spaces will also be added when editing Python code and a line ends with ':' or if editing XML and a line ends with a new tag. If extra spaces are added to the line then pressing the Backspace key immediately afterwards will delete Indent Size spaces at a time.

When the ' View > Syntax > Highlight Matching Braces/Tag ' menu option is enabled and the caret is placed over a brace '(' or ')' in the Text Editor , that brace and the corresponding brace in the syntax will be underlined. Brace matching can be used for different types of symbols such as {}, [], () and also works with matching tags such as XML and HTML tags (for example <b> and </b>). Use ' Find > Jump to Matching Brace/Tag ' to move the caret from one brace/tag to the corresponding brace/tag. Note that matching braces/tag only works when a Tree-sitter syntax is active on the current file. To configure which braces or tags are underlined, modify the Syntax010 file for the syntax and see Writing Tree-sitter Syntaxes for more information. The background color of the braces can also be changed using the Match Brace/Tag color in the Theme/Color Options dialog.

Section Lines are dotted vertical lines displayed in the Text Editor to identify different sections of the syntax within the file. Turn off the display of the section lines using ' View > Syntax > Show Section Lines '. Section lines require a Tree-syntax to be active and see Writing Tree-sitter Syntaxes to control where the section lines are drawn.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.