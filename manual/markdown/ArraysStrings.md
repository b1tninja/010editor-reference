# 010 Editor Manual - Strings

**Source:** [`manual/ArraysStrings.htm`](../manual/ArraysStrings.htm) (SweetScape 010 Editor manual mirror).

## Page header
Strings

## Section headings
- **Strings**
- **Wide Strings (Unicode Strings)**
- **Escape Sequences**
- **Reading Null-terminated Strings**

## Summary (lead paragraphs)
An array of characters is treated as a special string type. The keyword ' string ' can also be used to declare a string. The operators '=', '+', '+=', and comparison operators can be used on strings as if they were a separate data type. For example:

local char str [ 15 ] = "First" ; local string s = "Second" ; local string r1 = str + s; local string r2 = str; r2 += s; return (r1 == r2); The local keyword is not required when writing Scripts. Strings will automatically resize if assigned too many characters, and a warning will be displayed in the Output text area. All strings are assumed to be null-terminated. For a list of functions that can be used when working with strings, see String Functions .

Regular strings above assume each character can be stored in 8-bits; however this character size is not appropriate for many languages so 010 Editor also supports wide strings (also called Unicode strings) where each character is a 16-bit unsigned short. Use the special ' wstring ' type to define a wide string and each character of a wstring is assumed to be of type ' wchar_t ' (a wchar_t is equivalent to an unsigned short).

The same operators '=', '+' and '+=' are supported for wstrings as for strings and a wide string constant can be declared by placing a 'L' character before a string or character constant. For example:

local wchar_t str1 [ 15 ] = L"How now" ; local wstring str2 = "brown cow" ; local wstring str3 = str1 + L' ' + str2 + L'?' ; Extended characters can be placed in string constants using the UTF-8 character encoding. Wide strings are assumed to be null-terminated and a list of functions available for working with wide strings is available in the String Functions help topic. Wide strings can be converted to regular strings using the WStringToString or StringToWString functions, or by casting.

Special control characters can be included in strings by using an escape sequence which consists of a backspace '\' followed by one or more symbols. For example the string "\r\n" represents a DOS linefeed. To insert a regular backslash into a string use '\\'. The following escape sequences are supported:

Null-terminated strings are commonly defined in binary files. 010 Editor allows the special syntax in a template to read a null-terminated string:

string str; will both read a string until a 0 byte is encountered. Unicode strings (wide strings) can be read using:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.