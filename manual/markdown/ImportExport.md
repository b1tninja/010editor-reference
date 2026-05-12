# 010 Editor Manual - Importing/Exporting Files

**Source:** [`manual/html/ImportExport.htm`](../html/ImportExport.htm) (SweetScape 010 Editor manual mirror).

## Page header
Importing/Exporting Files

## Section headings
- **Importing Files**
- **Exporting Files**
- **Importing or Exporting Data Through the Clipboard**

## Summary (lead paragraphs)
Importing and Exporting allows conversion between a binary file and a number of supported formats. When importing or exporting files, the following formats are supported:

Decimal Text - Stores a binary file as a text file where each byte is converted to a decimal number. For example, the hex byte 0xFF would be stored as the characters "255". Binary Text - Stores a binary file as a text file where each byte is converted to a binary number. For example, the binary byte 0x6F would be stored as the characters "01101111". C Code or Java Code - Converts a binary file to an array of bytes that could be included in a C/C++ or Java program. (When importing data, specify the import type as 'Source Code' and 010 Editor will automatically detect whether the data is C or Java code). Python Code - Creates python source code containing an array of bytes representing the binary data being exported. Only export is supported for this format. Intel 8, 16, or 32-Bit Hex Code - Stores a binary file in the Intel Hex format. A number of different variations of the format exist, including 8-bit, 16-bit, and 32-bit. The Intel Hex format is used in a number of different applications and is commonly used with EPROMs. Motorola S19, S28, or S37 Records - Motorola S-Record format is used for transferring binary files and is commonly used with EPROMs. Hex Editor Areas - Stores the currently selected bytes as text exactly how they are displayed in the hex editor, including addresses and both the left and right areas. For example: 0030 3031 3233 3435 3637 3839 3A3B 3C3D 3E3F 0123456789:;<=>? 0040 4041 4243 4445 4647 4849 4A4B 4C4D 4E4F @ABCDEFGHIJKLMNO 0050 5051 5253 5455 5657 5859 5A5B 5C5D 5E5F PQRSTUVWXYZ[\]^_ 0060 6061 6263 6465 6667 6869 6A6B 6C6D 6E6F `abcdefghijklmno 0070 7071 7273 7475 7677 7879 7A7B 7C7D 7E7F pqrstuvwxyz{|}~ Note that importing from this format is not supported.

Rich Text Format (RTF) - Similar to the Hex Editor Areas option above except the data is stored in Rich Text Format (also called RTF). This format is used by a number of word processors including Microsoft Word. 010 Editor includes all foreground and background coloring information with the RTF but note that some programs such as Microsoft Word do not support having background colors in RTF data. Exporting to HTML will retain both the foreground and background colors more reliably. Only export is supported for this format. Base64 - Base64 is a method of encoding binary data so that it may be transferred between different systems without losing any special characters. This format is used when transferring attachments over email and other applications on the internet. Both importing and exporting are supported for Base64 data. Uuencoding - Uuencoding is a method of encoding data similar to Base64 but with different parameters. Uuencoding is used for transferring attachments over email or newsgroups, as well as other applications. Importing and exporting are both supported for uuencoded data. Importing Files Files may be imported by clicking the ' File > Import Hex... ' menu option. Select a file to import using the displayed file dialog box. By default, all files that can be imported will be displayed and the file type will be set to ' All Supported Import Types ' but the file type can be changed to only display files of one type. Once the file is imported, it will be converted to a binary file and opened as a new file in the editor. Any of the above formats can be imported into 010 Editor except where indicated. 010 Editor contains some special functionality for importing Intel Hex or Motorola S-Records (see Opening Files for more information). The Directory Options dialog can be used to control the initial directory when the file dialog box is displayed.

When importing a file, any bytes that are skipped are set to zero value by default; however, this value can be changed using the Default Import Byte option in the Import/Export Options .

When importing Intel Hex or Motorola files, some of these files contain a blank area of zeros at the beginning of the file. 010 Editor by default skips over this blank area and sets the starting address of the imported file to the first non-zero byte. To turn off this functionality use the Import/Export Options dialog. The word OFFSET will appear in the Status Bar when a starting address is set and see Custom Starting Address for information on changing the starting address.

In some special Intel Hex or Motorola files, the addresses specified in the file indicate the position of the Word where the data exists. To convert from this Word-based addressing system to a Byte-based addressing system, enable the Words toggle in the Import/Export Options dialog for either Intel Hex or Motorola files (internally, the addresses are multiplied by two). Note that leaving this toggle enabled when the import file does not use Word-based addresses will cause undefined results.

To export the current file to one of the above formats, open the file and click the ' File > Export Hex... ' menu option. The Export Hex dialog will be displayed.

Choose a file name for the exported file in the Export File field. A file name can also be chosen by clicking the Browse button to the right of the field. The default directory for the file to export can be controlled using the Directory Options dialog. Select which type of file to export using the Export Type drop-down list. Note that changing the export type automatically modifies the extension of the file to save. The number of bytes per line in the output file can be adjusted using the Bytes Per Row field.

To view advanced options for the file to export, click the Options button. Choose the Entire File radio button to export all the bytes from the current file or if a selection is made, choose the Selection toggle button to only export the selected bytes.

The Intel Hex and Motorola S-Records formats support specifying a starting address of the data. When the Always Zero toggle is selected, the address will always be written as zero. If the Start of Range toggle is selected, the starting address of the exported bytes will be written. A custom address can also be specified by selecting the Custom toggle and entering a number in the corresponding text field.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.