# 010 Editor Manual - Backup Options

**Source:** [`manual/html/OptionsBackups.htm`](../html/OptionsBackups.htm) (SweetScape 010 Editor manual mirror).

## Page header
Backup Options

## Summary (lead paragraphs)
The Backup Options controls the creation of backup files when a file is saved in the editor. Access the Backup Options by clicking ' Tools > Options... ' and selecting Backups from the list.

To enable the creation of backups, click the Backup File on Save toggle box. If the Backup toggle is set, the Backup Size Limit lists the size limit in megabytes for automatically making backup files. For example, if the size limit is 10 megabytes, then a backup will not be made when saving a file that is over 10 megabytes. The Backup Directory field lists the directory where backups will be saved. If this field is blank, the backups will be saved in the same directory where the file is located. Click the folder button beside the field to use a browse dialog to select a directory.

A number of options exist for controlling the extension of the backup file. If the No Extension Change toggle is selected, the backup file name will be the same as the original file name (this is only valid when a directory is specified in the Backup Directory field). If the Append Extension toggle is set, an extension will be added to the end of the file name when the backup is written. For example, if the original file was ' file.dat ', the backup file will be ' file.dat.bak '. To replace the file's extension with the backup extension, select the Replace Extension toggle. For example, if the original file was ' file.dat ', the backup file would be ' file.bak '. To change the backup extension, enter a new extension into the Backup Extension field (without the period).

Note that backups will not be made when saving drives or processes.

Clicking Reset will return the backup options to their original values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.