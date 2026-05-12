# 010 Editor Manual - Command Line Parameters

**Source:** [`manual/html/CommandLine.htm`](../html/CommandLine.htm) (SweetScape 010 Editor manual mirror).

## Page header
Command Line Parameters

## Section headings
- **Opening Files**
- **Opening Drives**
- **Opening Processes**
- **Importing Files**
- **Position the Caret**
- **Making Selections**
- **Opening Scripts or Templates**
- **Saving and Closing Files**
- **Replacing Strings or Bytes**
- **Comparing Files**
- **Running 010 Editor in Batch Files**
- **Running 010 Editor without a User Interface**
- **Opening Projects and Workspaces**
- **Setting the Starting Address**
- **Safe Mode**
- **Resetting the Application**
- **Reinstalling the Application**
- **Exiting the Application**
- **Wayland Support**
- **Other Command Line Parameters**

## Summary (lead paragraphs)
A set of files to load can be specified on the command line when starting 010 Editor. Each file to load should be separated by a space. For example, to load two files use:

010editor file1.dat file2.dat Multiple files can be loaded on the command line by using the wildcards '*' and '?'. For example:

010editor *.bin file???.dat By default, when 010 Editor is installed it is placed in the system path. This means that 010 Editor can be run from any command line by entering '010editor' (no directory needs to be specified). This command line syntax can be used to load files even if 010 Editor is already running. To not place 010 Editor in the path, disable the ' Add 010 Editor to the system path ' toggle in the install program.

Drives can be opened from the command line by using the -drive: command, followed by either a drive label or a drive number. If a drive label is specified, a logical drive is opened and if a drive number is specified, a physical drive is specified (see Editing Drives for more information). For example:

010editor -drive:C -drive:1 would open logical drive C: and physical drive 1.

Processes can be opened using the -process: command, followed by either a process identification number or a name of a process. For more information on working with processes, see the Editing Processes help topic. For example, to open two processes from the command line use:

010editor -process:cmd.exe -process:1074 Importing Files To import any of the available file formats, use the -import: command, followed by the file to load. Any of the accepted import or export types are accepted and the type used will be based from the file extension (see Importing/Exporting Files for more information). For example, to import a C file use:

010editor -import:array.c The wildcard characters '*' and '?' can also be used to import multiple files at the same time.

The caret can automatically be positioned within a file using the -line: or -goto: commands. Specify -line: followed by a number to jump to that line within the file. For example:

010editor file1.txt -line:100 To jump to a specific address within a file use the -goto: command followed by a number and the number may be in any of the supported numeric formats. For example:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.