# 010 Editor Manual - Writing Tree-sitter Syntaxes

**Source:** [`manual/html/WritingTreesitter.htm`](../html/WritingTreesitter.htm) (SweetScape 010 Editor manual mirror).

## Page header
Writing Tree-sitter Syntaxes

## Section headings
- **Installing a New Tree-sitter Syntax**
- **Syntax Trees**
- **Editing a Syntax010 File**
- **S-Expressions**
- **Editing Syntax Highlighting**
- **Editing Matching Braces/Tag**
- **Editing Section Lines/Folds**
- **Editing Injections**
- **Printing Syntax Trees**

## Summary (lead paragraphs)
A Tree-sitter Syntax requires two things: a dynamic link library containing a Tree-sitter parser (.dll on Windows, .so on Linux, or .dylib on macOS), and a Syntax010 file. A Syntax010 file is a text file with extension .syntax010 that controls how symbols are mapped to syntax styles for syntax highlighting, how brace-matching is done, and how section lines are calculated. Installing a new Tree-sitter syntax involves compiling the dynamic link library and creating the Syntax010 file. To modify how syntax highlighting, brace-matching, or section lines are calculated just involves editing the Syntax010 file and see Editing a Syntax010 File below.

A variety of Tree-sitter syntaxes are available on the internet and a good place to find syntaxes is to search on GitHub for tree-sitter-??? where ??? is the syntax name. If a syntax is found, download and extract the source code package. Creating the dynamic link library requires compiling just the files "src/parser.c" and optionally "src/scanner.c" or "src/scanner.cc". For example, to compile using gcc use:

gcc -o tree-sitter-???.so -shared src/parser.c src/scanner.c -I./src If the parser.c file does not exist, install the Tree-sitter command line interface (tree-sitter-cli) and run:

tree-sitter generate in the directory where the package was extracted. To create an entirely new Tree-sitter syntax involves writing a 'grammar.js' file which describes the rules for the syntax. See the site:

https://tree-sitter.github.io/ for more information. If installing a new syntax copy the file "queries/highlights.scm" to the file "???.syntax010". Next use the Syntax Options dialog and click the Add... button to add the "???.syntax010" file to 010 Editor.

When creating syntax files, it is important to understand that the Tree-sitter dynamic link libraries parse source code into a syntax tree. For example, for the C code:

void main () { return 5 ; } This code is parsed into the syntax tree:

( function_definition type : ( primitive_type ) declarator : ( function_declarator declarator : ( identifier ) parameters : ( parameter_list "(" ")" )) body : ( compound_statement "{" ( return_statement "return" ( number_literal ) ";" ) "}" )) Syntax trees contain symbol names (e.g. function_definition or identifier), and strings (e.g. "{" or "return"). Field names as shown above in green are followed by a colon. Field names are conceptually named edges in a node graph and can be ignored in many syntax files. To view the syntax tree created for a section of source code see Printing Syntax Trees .

Open the Syntax010 file for the current syntax by clicking the ' View > Syntax > Edit Syntax File ' menu option. To create a new Syntax010 file just create a new text file and save it with the extension ".syntax010". The Syntax010 file can be edited as a regular text file and once changes are made, click ' View > Syntax > Refresh Syntax ' or click the icon in the top-right corner of the editor to apply the syntax changes to all open files that use that syntax. Syntax010 files are very similar to the "queries/highlights.scm" file that is included with many Tree-sitter packages but adds some extensions. Separate sections for brace matching, injections and code folding can all be included in a Syntax010 file using the '#section' keyword as described below. Syntax010 files use ';' to indicate comments and contain a series of S-expressions .

A Syntax010 file consists of a series of S-expressions. The simplest S-expression contains a single symbol in brackets or a string, followed by '@' and a capture group name. For example:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.