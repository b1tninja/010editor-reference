# 010 Editor Manual - Using Find Strings

**Source:** [`manual/FindStrings.htm`](../manual/FindStrings.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Find Strings

## Section headings
- **Output Window**

## Summary (lead paragraphs)
The Find Strings dialog can be used to discover the location of strings within a binary file. Access the Find Strings dialog using the ' Find > Find Strings... ' menu option and note that this tool is generally not useful for text files because a text file consists entirely of a set of strings.< /P> Use the Find Strings dialog by specifying the minimum number of characters for each string in the Minimum String Length field. Choose whether to search for ASCII strings, Unicode strings, or both ASCII and Unicode strings using the String Type field. By default, the search will take place over the whole file ( Entire File will be selected in the Range group), but the search can be limited to an area of the file by making a selection before opening the Find Strings dialog and then choosing the Selection toggle. Click the Find button to search through the file and list all strings that were found and see the Output Window below. Clicking Cancel or pressing the Esc key will dismiss the dialog without performing a search.

Other options are available for the Find Strings dialog by clicking the Advanced Options section. If the Require Null After String toggle is set, only those strings that have a null (zero) character immediately following the string will be listed in the Output Window. The Matching Characters box can be used to customize exactly which characters are considered when searching for strings. Characters are divided into a number of different groups which can be enabled or disabled by clicking the toggles. For example, if Letters A..Z is selected then all letters (including uppercase and lowercase) will be considered part of a string. A list of custom characters can be specified in the Custom field and the sequence ".." can be used to indicate a range of characters. For example, to search just for letters or the characters $, & and @, disable all toggles except the Custom toggle and enter "A..Za..z$&@" in the Custom field.

After the search is performed, all strings that were found will be displayed in the Find tab of the Output Window. The top line lists how many strings were found and clicking on a string name will highlight that string in the editor. The figure above shows an example of finding strings in the 'notepad.exe' file. A graph of where the strings were found in the file is located to the left of the list of strings. Different formats for the Address column can be chosen by right-clicking on a cell in the column and selecting Column Display Format from the popup menu. Right-click the table and select ' Clear ' to clear all the results or press the Esc key to hide the Output Window.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.