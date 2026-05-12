# 010 Editor Manual - Using the Portable Version

**Source:** [`manual/html/Portable.htm`](../html/Portable.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Portable Version

## Section headings
- **Directory Structure**
- **Licensing Issues**
- **Uninstalling**

## Summary (lead paragraphs)
010 Editor is available as a portable version meaning the 010 Editor directory can be placed onto a USB key and moved between different computers without having to run an installer on each computer. Currently the portable version is only available on Windows and must be installed using a separate installer found on: https://www.sweetscape.com/download/010editor/ When the portable version of 010 Editor is being run the title of the application is '010 Editor Portable' and the version will include 'Portable' in the ' Help > About ' dialog. Note that with the portable version of 010 Editor no desktop icon will be created and the '010 Editor' entry will not be added to the Windows Explorer right-click menu.

When 010 Editor Portable is installed the following directory structure will be found on disk:

This directory structure can be moved to different locations or different computers. Start the application by running the '010EditorPortable.exe' program (this is equivalent to running the '010Editor.exe' program in the 'AppData' directory). All Scripts and Templates installed from the Script or Template Repository are automatically installed into the '010 Scripts' and '010 Templates' directories. Any other custom Scripts or Templates should be installed into these directories if they are going to be used on different systems. The directory options for the portable version can be controlled by clicking ' Tools > Options... ' and selecting ' Directories ' from the list:

By default all directories are specified offset from ($BASEDIR) which is the directory which contains '010 Scripts', '010 Templates', 'AppData' and '010EditorPortable.exe', or ($PROGDIR) which is location of the '010Editor.exe' executable file. Note that ($BASEDIR) does not exist on non-portable versions of 010 Editor. If a large amount of room is needed for a swap or temporary file these directories could be changed to a location on the local hard-drive.

The portable version of 010 Editor uses the same license as the regular version of 010 Editor and a special license is not required to run the portable version; however, the license information for the regular version of 010 Editor is stored in the Windows registry but the license information for the portable version is stored in the 'AppData\Config' directory. If the portable version is run with no license installed but a license exists in the Windows registry, you will be asked to copy the license to the portable version if you are the owner of the license. If the license is changed in either the portable or standard version of 010 Editor the license will not automatically be copied over and must be entered using the Licensing dialog. Uninstalling Note that there is also no uninstaller for the portable version of 010 Editor and to uninstall simply delete the directory structure that was created.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.