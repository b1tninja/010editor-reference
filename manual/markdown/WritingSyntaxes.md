# 010 Editor Manual - Writing Template Syntaxes

**Source:** [`manual/WritingSyntaxes.htm`](../manual/WritingSyntaxes.htm) (SweetScape 010 Editor manual mirror).

## Page header
Writing Template Syntaxes

## Summary (lead paragraphs)
A Binary Template Syntax can be written as a function inside a Binary Template starting in version 9 of 010 Editor. This means that some programming is required to create the Syntax but that they can handle a large variety of different formats. These type of syntaxes are easier to write than Tree-sitter syntaxes and are faster and require less memory, but cannot handle complex formats that Tree-sitter syntaxes can handle. New Binary Template Syntaxes can be created the same way new Binary Templates are created, for example by using the ' Templates > New Template ' menu option. To run the Binary Template use ' Templates > Run Template ' or see Running Templates . Syntaxes should also have their Category set to Syntax in order to be displayed in the Syntax popup menu of the Status Bar when they are installed.

A Binary Template which is used to perform syntax highlighting must implement the special function HighlightLineRealtime . This function is called every time a line of text is about to be displayed in the editor to apply coloring to the line. Note that this function only works on a single line but to handle multi-line syntax highlighting such as multi-line comments, see the special flags parameter of the HighlightLineRealtime function which can be used to pass the status to the next line.

Most Syntax make use of Syntax Styles which allow a single style to be used in multiple syntaxes. For example the Syntax Style "comment" is used to specify the color of comments both in C/C++ and PHP. The colors can then be changed using the Theme/Color Options dialog. See the HighlightFindStyle function to connect to styles and the HighlightApplyStyle to apply colors to text.

A number of functions have been provided to make the process of writing Syntaxes easier. A set of rule functions is provided for convenience when writing Syntax Highlighters but note that these functions are not required to be used. These functions assume that the current rule (highlighting method) is stored in the flags parameter of the HighlightLineRealtime function. Highlighting rules are provided to color single-line comments, keywords, multi-line comments, strings, tags, etc. See the functions HighlightCheckCommentRule , HighlightCheckKeywordRule , HighlightCheckMultiLineRule , HighlightCheckSingleLineRule , or HighlightCheckTagRule for more information.

In order to save time and memory, Syntaxes allow instance sharing . This means that all open files in the editor can share a single copy of a Binary Template to do syntax highlighting for a particular type. See the HighlightAllowInstanceSharing function for more information.

Syntaxes are only used for text files; however, realtime highlighting can be applied to hex files as well by implementing the HighlightBytesRealtime function. More information is found in the help topic for this function.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.