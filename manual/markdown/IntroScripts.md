# 010 Editor Manual - Writing Scripts

**Source:** [`manual/IntroScripts.htm`](../manual/IntroScripts.htm) (SweetScape 010 Editor manual mirror).

## Page header
Writing Scripts

## Summary (lead paragraphs)
010 Editor has a powerful scripting engine that allows many tasks to be automated. Script files have the extension '.1sc' and are very similar in syntax to C. All scripts are executed similar to how an interpreter would run the file, starting at the first line of the program and progressing downwards (there is no need to write a 'main' function as in ANSI C). Scripts can be used to perform editing operations on files, manipulate files on disk, or even perform complex operations like file comparisons, checksums, and find in files. To open or run a script see the Scripts Menu or Running Templates and Scripts . A repository of scripts can be accessed by clicking the ' Scripts > Script Repository ' menu option (see the Repository Dialog ). Scripts can be configured to run on startup, shutdown, or when files are opened, and scripts can also be added to the ' Scripts ' menu (see Script Options ).

View the following topics for more information on the syntax used when writing Scripts:

A large number of functions are available when writing Scripts. The available functions are described in:

Binary Templates have a syntax similar to scripts, but allow a file to be parsed into a number of variables. Scripts can be used to modify the variables that are defined in Templates. See Writing Templates for an introduction to using Templates.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.