# 010 Editor Manual - Introduction to Number Systems

**Source:** [`manual/NumberSystems.htm`](../manual/NumberSystems.htm) (SweetScape 010 Editor manual mirror).

## Page header
Introduction to Number Systems

## Section headings
- **Bits and Bytes**
- **Entering Numbers in Text Fields**

## Summary (lead paragraphs)
When editing raw hex data, 010 Editor uses a variety of different number systems including decimal, hexadecimal, octal, and binary. Each number system has a different ' base ' that is used to convert from a set of digits to a numeric value. For example, the digits '246' can be converted to a number using base 10 by 2*10 2 + 4*10 + 6 = 246. In general, if the n digits of a number A are numbered where A 0 is the right-most digit, A 1 is the digit to the left and so on, then the value of a number of base B is calculated:

A n-1 *B^ n-1 + A n-2 *B^ n-2 + ... + A 1 *B + A 0

The following is a list of the 4 number systems used:

Hexadecimal - Numbers are represented as base 16. All the decimal digits are used, plus the letters 'A', 'B', 'C', 'D', 'E', and 'F' are used to represent the numbers 10 through 15. For example, in hexadecimal 3d7 = 3*16 2 + 13*16 1 + 7 = 983. This system is commonly referred to as Hex . Octal - Numbers are represented as base 8. Only the digits '0' through '7' are used ('8' or '9' is not allowed). For example, the number 2740 = 2*8 3 + 7*8 2 + 4*8 1 + 0 = 1504. Binary - Numbers are represented as base 2. Only the digits '0' or '1' can be used. For example, the number 10110 = 1*2 4 + 0*2 3 + 1*2 2 + 1*2 1 + 0 = 22. Bits and Bytes A digit of a binary number is also called a ' bit '. When 8 bits are grouped together, the result is called a ' byte '. Since a byte has 8 binary digits, it can represent any value from 0 up to 255 inclusive. Every file stored on a disk is stored as a set of bytes. Note that when 4 bits are grouped together (base 2), this can also be represented as a single hexadecimal digit (base 16). For example, binary 0101 = '5' hexadecimal, or binary 1111 = 'F' hexadecimal.

010 Editor is designed specifically for editing the individual bytes of a file. When a file is opened for editing, a Hex Editor Window shows the representation of each byte as a hexadecimal number and as a character (see Introduction to Editing for more information).

Almost anywhere a number is entered in 010 Editor (in most text fields, the Inspector, etc.), the program supports input in a number of different formats. Usually, the format of the number is assumed to be decimal (some fields have a Decimal and Hex toggle beside them - clicking the Hex toggle will set the default to be hex). However, the other formats can be entered with a special syntax:

Octal - Enter ',o' after the number. For example, '377,o' is an octal number. Binary - Enter ',b' after the number. For example, '0101,b' is a binary number. Decimal - Enter ',d' after the number. For example, '123,d' is a decimal number. Characters - Characters can be entered by placing single quotes around the character. For example, 'A' would be converted to the number 65. Most standard C escape sequences are also supported using '\'. For example, '\n' would be converted to the number 10. See Introduction to Byte Ordering for information on how to group bytes together to make numbers larger than 255.

The number formats supported in Scripts and Templates are slightly different. See Introduction to Templates and Scripts for more information.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.