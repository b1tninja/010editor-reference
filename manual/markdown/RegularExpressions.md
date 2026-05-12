# 010 Editor Manual - Using Regular Expressions

**Source:** [`manual/html/RegularExpressions.htm`](../html/RegularExpressions.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Regular Expressions

## Section headings
- **Matching Characters**
- **Character Classes**
- **Anchors**
- **Repetition**
- **Alternation**
- **Matching Hex Bytes**
- **Multi-Line Regular Expressions**
- **Replacements**
- **Capture Groups**
- **Functions**

## Summary (lead paragraphs)
Regular Expressions are a powerful syntax for finding string patterns within a file. Many different flavors of regular expressions exist and 010 Editor uses a syntax similar to Ruby/Perl as implemented by the Oniguruma regular expression library. To search for a regular expression, click the Options button in the Find Bar and enable the Search with Regular Expressions toggle (see the image below). Regular expressions can be used when performing a Find , Replace , Find In Files , or Replace In Files operation. Note that the letter 'R' will appear beside the word Options when regular expressions are enabled. The full syntax of regular expressions are beyond the scope of this document but the following contains an introduction to the major features of regular expressions. Warning: Some regular expressions can be very complex and using certain regular expressions containing lots of repetition operators can cause searches to be performed very slowly.

Regular expressions look just like regular Find strings. For example, to find a string such as 'Green' just use the regular expression:

Green Regular expressions use a number of special control characters to control how the searches are done and the special characters are: ".[]^$()/\*{}?+|". To search for any of these control characters include an extra '\' character before the control character. For example, to search for the string "5+6" use the regular expression: 5\+6 A number of special codes can be used to match characters:

For example, to search for all phone numbers in the form 555-5555 use the regular expression:

\d\d\d-\d\d\d\d By default, the '.' operator does not match linefeeds but to search across multiple lines see the Multi-Line Regular Expressions section. Note that the case-sensitivity of regular expressions is controlled by the Match Case toggle in the Find Bar Options.

A Character Class or Character Set provides a way to give a number of different options that a single character can match. Character Classes are denoted with '[' and ']' brackets where each character inside the brackets can match. For example, the regular expression:

defen[cs]e will match both the words 'defence' and 'defense'. Inside of a character class, only the characters "]\-^" are considered control characters. The '-' character can be used to indicate a range of characters. For example the character class:

[0-9a-fA-F] will match any of the hexadecimal characters. Using the '^' character at the beginning of a character class indicates a negated character class, meaning the regular expression will match any characters that are not in the character class. For example, the character class:

[^abc] will match any characters that are not a, b, or c.

All matching so far has worked by matching a particular character. Regular expressions also support anchors which work by matching a position within a file. The following anchors are supported:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.