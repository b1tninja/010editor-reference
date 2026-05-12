# 010 Editor Manual - File Properties

**Source:** [`manual/Properties.htm`](../manual/Properties.htm) (SweetScape 010 Editor manual mirror).

## Page header
File Properties

## Section headings
- **Logical Drive Properties**
- **Physical Drive Properties**
- **Process Properties**

## Summary (lead paragraphs)
The File Properties dialog displays useful information about the current file. This dialog can be accessed from the ' Edit > File Properties... ' menu option or by pressing Alt+Enter . The Properties dialog will display different information if the current file is a logical drive, physical drive, or process. See below for the information displayed.

The File Properties dialog displays the current File , Location , and Size in both hex and decimal formats. The Created , Modified , and Accessed fields display the time and date when the file was created, last changed on disk, and accessed from disk respectively. Note that on some operating systems, these dates are not always 100% accurate.

The Attributes area shows the Read Only , Hidden , Archive , and System file flags from the operating system. Note that these toggles can be clicked on to change the attributes of the file on disk.

Click the OK button to accept any file attributes changes, or the Cancel button to dismiss the File Properties dialog without making any changes.

The Drive Properties dialog display information about a logical drive (for example, 'C:' or 'D:'). The dialog lists the current File System (NTFS, FAT, CDFS, etc.) plus the Serial Number of the drive.

Each drive is divided into a number of sectors and clusters (see Editing Drives for more information). The middle section of the dialog gives the size of each sector and cluster, plus the number of free and total sectors and clusters.

The bottom section of the dialog displays the total number of bytes in the drive, the number of bytes used, and the number of free bytes. As well a graph indicates what percentage of the drive is full (yellow indicates used bytes and blue indicates unused bytes).

Click the OK button to dismiss the Drive Properties dialog.

When editing a physical drive, the properties dialog will display a different set of information about the drive than a logical drive (see above). For information on the difference between a logical and a physical drive, see Editing Drives .

A physical drive is made up of a number of sectors, tracks, and cylinders (see Editing Drives ). The middle section of the dialog lists the number of bytes per sector, track, and cylinder, as well as the total number of each on the drive (the number of tracks and cylinders is not available on all devices). The bottom part of the dialog displays the total number of bytes available on the drive. Note that information on how much of the drive is free or in use is not available for physical drives.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.