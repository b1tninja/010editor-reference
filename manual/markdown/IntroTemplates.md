# 010 Editor Manual - Writing Templates

**Source:** [`manual/html/IntroTemplates.htm`](../html/IntroTemplates.htm) (SweetScape 010 Editor manual mirror).

## Page header
Writing Templates

## Summary (lead paragraphs)
Binary Templates, one of the most powerful features of 010 Editor, allow virtually any binary file to be parsed into a series of variables. Templates allow binary files to be understood and edited in a much easier fashion than typical hex editors. Each Template is stored as a text file with the extension ".bt" and can be edited directly in 010 Editor (see the Templates Menu ). Templates are executed as an interpreter would run, starting from the first line in the file and progressing downwards. When a Template is executed the file is parsed into a number of variables and the variables are displayed in the Template Results panel (see Template Results for more information). Templates can be configured to automatically load and execute each time a file is opened (see Template Options ). For an example of how Templates work open any ZIP, BMP, or WAV file on your computer and see the Repository Dialog for information on installing Templates from the Repository.

The syntax of Binary Templates is similar to that of scripts . The following topics describe the syntax specifically used when writing Binary Templates:

A large number of functions are available when writing Templates. The following topics list all available functions:

Scripts can be used to modify variables defined in a Template. See Writing Scripts for more information on Scripts and Editing Variables with Scripts for information on using Scripts and Templates together.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.