# 010 Editor Manual - Converting Files

**Source:** [`manual/Convert.htm`](../manual/Convert.htm) (SweetScape 010 Editor manual mirror).

## Page header
Converting Files

## Summary (lead paragraphs)
The conversion tool supplied with 010 Editor can be used to convert bytes from one character set to another and can also transform linefeeds from one type to another. Select ' Tools > Convert ' or press Ctrl+T to open the Convert Dialog. The list of available character sets can be controlled with the Character Set Options dialog.

In the Convert dialog choose which character set to convert from using the Source Character Set drop-down list. The source character set will automatically be filled from the current Edit As or from the file's character set if ' View > Character Set > Use Default ' is turned off. Next select which character set to convert to using the Target Character Set list (by default the target character set is the same as the source). The Target Character Set lists common character sets at the top (see the Show at Top Level toggle on the Character Set Options dialog), followed by a list of recently used character sets, followed by '---' and then a list of all available character sets.

To not apply any special conversions to the linefeeds of a text file, leave the Target Linefeeds list set to ' (No Change) '. Selecting a linefeed type from the Target Linefeeds list will transform all linefeeds found in the file to the indicated type. The Convert dialog can be used to modify only the linefeeds by leaving the source and the target character set the same. See Using Edit As for more information on character sets and linefeeds.

Some text files contain a sequence of bytes at the beginning of the file to indicate which character set is used in the file and this is called a Byte-Order Mark or BOM . Byte-Order Marks are only currently used for Unicode or UTF-8 files. When the Convert dialog is opened for a Unicode or UTF-8 text file that contains a BOM, the Include Byte Order Mark (BOM) toggle will be set and the text ' (currently exists) ' will be included after the toggle. When converting a Unicode or UTF-8 file that does not contain a BOM, the Include Byte Order Mark (BOM) will be unchecked and the text ' (not present) ' will be shown. When the Target Character Set is Unicode or UTF-8, set the Include Byte Order Mark (BOM) toggle to add a BOM to the file or uncheck the toggle to remove the BOM. The toggle will be disabled when the Target Character Set is not Unicode or UTF-8. See Byte-Order Marks for more information on using BOMs with the editor.

If no bytes are selected in the file when the conversion is performed, the conversion will be applied to every byte in the file. If a selection is made the Conversion may be applied to just the selected bytes by clicking the Options button and choosing the Selection toggle (the default). Alternately, select the Entire File toggle to convert the whole file. Sometimes there is no equivalent character when converting data from one character set to another (for example when converting Unicode to ASCII). Any characters that the dialog cannot convert will be assigned the byte value listed in the Replace Invalid Characters With box (the default is the space character 0x20).

Clicking Convert will perform the conversion or clicking Cancel will close the dialog. Double-clicking on an item in the Target Character Set or Target Linefeeds list will also perform the conversion. Note that if converting a whole text file, 010 Editor may automatically change the current Edit As or may turn off the ' View > Character Set > Use Default ' toggle and set a per-file character set.

Files can also be converted to other formats using the ' File > Import Hex... ' or ' File > Export Hex... ' tools (see Importing/Exporting Files for more information).

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.