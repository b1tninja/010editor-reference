# 010 Editor Manual - String Functions

**Source:** [`manual/FuncString.htm`](../manual/FuncString.htm) (SweetScape 010 Editor manual mirror).

## Page header
String Functions

## Summary (lead paragraphs)
The following is a list of string functions that can be used when writing Templates or Scripts.

double Atof( const char s[] ) Converts a string to a floating-point number. Returns zero on error.

int Atoi( const char s[] ) Converts a string to an integer. Returns zero on error.

int64 BinaryStrToInt( const char s[] ) Converts a string containing a binary number s to an integer and returns the result. For example:

return BinaryStrToInt ( "01001101" ); would return the number 77. If the string is not a valid binary string, zero is returned.

char[] ConvertString( const char src[], int srcCharSet, int destCharSet ) Given a string src that uses the character set encoding srcCharSet , the string is converted to use the character set encoding destCharSet and returned as a string. The following character set constants exist:

Custom character sets can also be specified using the ID Number specified in the Character Set Options dialog. This function should not be used with Unicode character sets (CHARSET_UNICODE). To perform conversions with Unicode strings see the StringToWString and WStringToString functions.

string DosDateToString( DOSDATE d, char format[] = "MM/dd/yyyy" ) Converts the given DOSDATE into a string and returns the results. By default the date will be in the format 'MM/dd/yyyy' but other formats can be used as described in the GetCurrentDateTime function. Click here for more information on the DOSDATE type and see the FileTimeToString function for an example of using SScanf to parse the resulting string.

string DosTimeToString( DOSTIME t, char format[] = "hh:mm:ss" ) Converts the given DOSTIME into a string and returns the results. By default the time will be in the format 'hh:mm:ss' but other formats can be used as described in the GetCurrentDateTime function. Click here for more information on the DOSTIME type and see the FileTimeToString function for an example of using SScanf to parse the resulting string.

string EnumFlagsToString( enum e ) If the variable e is an Enum Flags variable, the flags that are stored in the variable are converted to a string and returned. Multiple flags are separated by the '|' character. For example, if the enum has possible values 'ONE=0x01', 'TWO=0x02' and 'THREE=0x04', then a variable with the value 0x05 will return the string 'ONE | THREE'. The string returned by this function can be turned back into a value by using the EnumStringToFlags function.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.