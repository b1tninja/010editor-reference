# 010 Editor Manual - Introduction to the Data Engine

**Source:** [`manual/DataEngine.htm`](../manual/DataEngine.htm) (SweetScape 010 Editor manual mirror).

## Page header
Introduction to the Data Engine

## Section headings
- **Features**
- **Limitations**

## Summary (lead paragraphs)
010 Editor contains a powerful data engine and this engine is used on all file and disk operations including reading data, editing, undo, redo, cut, copy, paste, inserting files, etc. As a result of using this engine, the program gains some extremely powerful functionality but also has a few limitations.

One of the post powerful features of the engine is the ability to open any hex file or drive instantly. There is no limit to the size of files that can be opened, but some file systems (including FAT) limit the file size to 2 gigabytes.

Many clipboard operations including Cut, Copy or Paste can usually (but not always) copy hex data instantly (see Using the Clipboard for more information). For example, open the largest file available on the disk, press Ctrl+A to select all, Ctrl+C to copy, Ctrl+N to create a new file, Ctrl+H to switch into hex-editing mode, and Ctrl+V to paste the data.

Other file operations, such as Insert Bytes, Insert File, Overwrite Bytes, Overwrite File, and Set File Size can operate on hex files instantly as well. For example, create a new hex file using Ctrl+N and Ctrl+H and then click ' Edit > Set File Size... '. Type '10000000000' and press Enter to create a huge file (NOTE: do not try to save this file unless enough disk space is free).

Another feature gained by using the data engine is unlimited Undo and Redo on all operations. Regardless of the size of data copied, pasted, or deleted, the operation can be undone or redone using Ctrl+Z or Ctrl+Shift+Z .

The limitations of the data engine only apply when copying or pasting large blocks of data to or from the clipboard (larger than 16KB).

The data engine uses a read-on-demand system, meaning data is not read into the editor until it is required. When Copy and Paste operate on large blocks, sometimes only pointers to the data are transferred. As a result, if a large block of memory is copied and then the file is deleted or modified by another program, the copied data may become corrupted (you will be warned when this happens). If a file is open in the editor, make sure to close the file before deleting it from disk using another program.

As stated earlier, when large blocks of data are copied to the clipboard, sometimes only pointers are copied. When the file the data is copied from is closed or modifications are saved, the actual data is then copied to the clipboard. This process is called Unlinking and may take some time if very large blocks have been copied. The Status Bar will display a progress bar while the file is being saved or closed. The ' Edit > Clipboard > Clear Clipboards ' menu option can be used to clear the clipboards, removing any large blocks from memory.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.