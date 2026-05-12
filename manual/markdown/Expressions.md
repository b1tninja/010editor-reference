# 010 Editor Manual - Expressions

**Source:** [`manual/Expressions.htm`](../manual/Expressions.htm) (SweetScape 010 Editor manual mirror).

## Page header
Expressions

## Section headings
- **Boolean Operators**
- **Numbers**

## Summary (lead paragraphs)
Expressions in Scripts or Templates can contain any of the standard C operators:

Note that the >> operator can give different results depending if the operand is signed or unsigned. When unsigned the left-most bit will always be zero (logical shift) and when signed the left-most bit is copied from the operand (arithmetic shift). Brackets '(' or ')' can be used to group expressions. For example:

(45 + 123) * (456 ^ 16) is a valid expression. The following comparison operators can be used: < (less than) > (greater than) <= (less than or equal) >= (greater than or equal) == (equal) != (not equal) ! (not) For example,

(45 > 32) would return the value 1. Any of the assignment operators +=, -=, *=, /=, &=, ^=, %=, |=, <<=, or >>= can also be used. A number of addition Special Keywords including sizeof can be used in expressions.

The following boolean operators can be used in expressions:

For example, to perform an operation if A and B are true or if C is not true, use:

if( (A && B) || !C ) ... Brackets can be used to indicate which order the operations should be performed.

Numbers may be entered in a number of different formats (see Introduction to Number Systems ):

Hexadecimal - 0xff, 25h, 0EFh Octal - 013 (with a zero before any numbers) Binary - 0b011 The 'u' character can be used after a number to indicate an unsigned value (e.g. '12u'), or 'L' can be used to indicate an 8-byte int64 value (e.g. '-1L'). Floating-point numbers may contain 'e' for an exponent (e.g. 1e10). A floating-point number is automatically assumed to be an 8-byte double unless an 'f' character is located after the name (e.g. 2.0f), in which case the number is assumed to be a 4-byte float.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.