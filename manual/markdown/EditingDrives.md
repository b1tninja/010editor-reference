# 010 Editor Manual - Editing Drives

**Source:** [`manual/html/EditingDrives.htm`](../html/EditingDrives.htm) (SweetScape 010 Editor manual mirror).

## Page header
Editing Drives

## Section headings
- **Open Drive Dialog**
- **Editing Drives**
- **Making Disk Images**
- **Viewing Drive Properties**
- **Sectors, Clusters, Tracks, and Cylinders**

## Summary (lead paragraphs)
010 Editor can edit the individual bytes of hard drives, floppy drives, memory keys, flash drives, CD-ROMs, etc. To open a drive for editing, click the ' File > Open Drive... ' menu option, or press Ctrl+D to display the Open Drive dialog box. Drives can also be opened from the Command Line .

Two main types of drives can be edited in 010 Editor: Logical Drives and Physical Drives . A Logical Drive is a device or a partition that has been assigned a drive letter such as 'C:' or 'A:'. A Physical Drive corresponds to an actual device inside the computer such as a hard drive or memory key. Physical Drives may be divided into multiple Logical Drives using partitions.

When editing drives on Windows Vista and all later versions of Windows (7, 8, etc.), Windows requires that all file handles on the drive be closed before changes can be written to the drive. If writing to a Physical Drive, all file handles on the Logical Drives within the Physical Drive must first be closed (a list of Logical Drives within each Physical Drive is displayed in the Open Drive dialog below). When a drive is first opened, 010 Editor displays a warning if any file handles on the drive are open and the drive is marked as read only. To enable editing of the drive close all open files on the drive, right-click on the Editor Window and click ' Read Only ' from the pop-up menu. Note that the Windows boot drive (e.g. C:) cannot be modified unless the OS is booted from a different drive.

WARNING: Incorrectly editing a hard drive can cause severe loss of data. SweetScape Software will not be held liable for data loss as the result of incorrect editing. Edit your drives at your own risk.

In the Open Drive dialog box a list of all Logical Drives is displayed at the top of the dialog and a list of Physical Drives is displayed at the bottom of the dialog. If the drive size can be calculated, the size will be displayed to the right of each drive name. To the right of each Physical Drive name is a list of Logical Drives that are contained within that drive. Select a logical or physical drive and click the Open button to open the drive as a file in the editor. Double-clicking on a drive name in the list also opens the drive. Click the Cancel button to dismiss the dialog without opening a drive. If the Open as read-only toggle is enabled in the upper-right corner of the dialog, the drive will be opened as a read-only file.

Once a drive is opened in 010 Editor, it can be edited can like any other file (see Using the Hex Editor ). Bytes can be modified and blocks of data can be copied or pasted using the clipboard. The only limitation is because the size of drives cannot be modified, bytes cannot be inserted or deleted from a drive. Once modifications have been made to the drive, click the ' File > Save ' menu option to commit the changes to disk. On Windows Vista and all later Windows Versions (7, 8, etc.) all files on the disk must be closed before changes can be written to the drive. See the introduction to this help topic for more information.

Once a drive has been loaded in 010 Editor, use the ' File > Save As... ' or ' File > Save a Copy... ' menu option to save a byte-by-byte copy of the drive to a file (called a disk image ). A portion of the drive can be saved to disk by selecting the desired bytes and using the ' File > Save Selection... ' menu option.

To view the properties of the current logical or physical drive, click the ' Edit > Properties... ' menu option. See the File Properties help topic for more information. The properties includes information about sectors, clusters, tracks, and cylinders of the drive.

Cluster - A cluster is the smallest unit of data that a file system can allocate for a file. Each cluster has a fixed size that is always a multiple of the sector size. Older file systems (FAT16) often allocated large cluster sizes of 32K or more, meaning that even small files of 1K would take up 32K of disk space. More modern file systems (FAT32 and NTFS) allow smaller cluster sizes. A file is stored optimally on disk as a series of contiguous clusters (clusters that are in order on disk). However, a file can be split into multiple clusters on different areas of the disk and this is called fragmentation . Track - A track is a concentric ring of sectors on a platter. A read/write head can read all the data from a certain track by moving to a position and then rotating the platter. Cylinder - A cylinder is a group of tracks in all the platters that are on top of each other. By default, 010 Editor displays Sector Lines in the Hex Editor Window that indicate where sectors start and stop on the drive. For more information, see the View Menu help topic. To jump to the previous or next sector, use the Alt+Up or Alt+Down keys respectively.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.