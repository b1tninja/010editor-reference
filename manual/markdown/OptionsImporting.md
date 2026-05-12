# 010 Editor Manual - Import/Export Options

**Source:** [`manual/OptionsImporting.htm`](../manual/OptionsImporting.htm) (SweetScape 010 Editor manual mirror).

## Page header
Import/Export Options

## Summary (lead paragraphs)
The Import/Export Options dialog controls various options when importing or exporting files using the ' File > Import Hex... ' or ' File > Export Hex... ' menu options (see Importing/Exporting Files for more information). Open the Import/Export Options window by clicking ' Tools > Options... ' and selecting Import/Export from the list.

When importing data, some formats (such as Intel Hex or Motorola S-Records) may skip over some bytes. By default, the skipped bytes are assigned the byte value zero, but a different value can be specified by entering a number between 0 and 256 in the Default Import Byte field.

In some Intel Hex or Motorola files, the addresses are given in terms of Words instead of Bytes. 010 Editor handles these files by converting the Word-based addresses to Byte-based addresses by multiplying them by two. Click the Words toggle in the Intel Hex Address Format area or Motorola Hex Address Format area to perform the conversion on Import, or click the Bytes toggle to leave the addresses unmodified. Addresses can be converted to Word-based when exporting via the Export Options dialog (see Importing/Exporting Files ).

When importing Intel Hex or Motorola S-Record files and a blank area is found at the beginning of the file, by default the blank area is skipped and a Custom Starting Address is set for the file at the first non-blank byte. To turn off this functionality and include the blank area at the beginning of the file uncheck the Automatically set Starting Address for Intel Hex Files toggle when importing Intel Hex Files. To turn off this functionality for Motorola S-Records uncheck Automatically set Starting Address for Motorola Files .

Hex data can be exported as Hex Text using ' File > Export Hex... ' or ' Copy > Copy as > Copy as Hex Text ' (see Using the Clipboard for more information). If the Include Spaces toggle is enabled then spaces are included between each hex byte, and if Include Linefeeds is enabled then the output is divided into lines if more than 16 bytes are copied. These toggles are mirrored in the Export Hex dialog. Note the export also takes into account the Lowercase Hex toggle of the Hex Editor Options dialog.

Clicking the Reset button restores all Import/Export Options to their default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.