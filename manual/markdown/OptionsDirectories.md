# 010 Editor Manual - Directory Options

**Source:** [`manual/OptionsDirectories.htm`](../manual/OptionsDirectories.htm) (SweetScape 010 Editor manual mirror).

## Page header
Directory Options

## Summary (lead paragraphs)
The Directory Options dialog controls the location of various directories used in 010 Editor. To open the Directory Options dialog click the ' Tools > Options... ' menu option and select ' Directories ' from the list.

010 Editor stores file data in a cache in memory which can be controlled using the Cache Options dialog. Once too much data is loaded into the cache, data will be written to a swap file on disk. Enter the directory where the swap file should be stored in the Swap Directory field. Click the folder button to use a dialog to select the swap directory from a list. 010 Editor occasionally uses temporary files. Enter the directory where these files should be stored in the Temp Directory field or click the folder button to select a directory with a dialog box.

The Script Directory field lists the default location where local scripts are assumed to exist on disk (this is used for the ($SCRIPTDIR) variable in the Script Options ). Similarly, the Template Directory field lists the default directory where local templates are stored (this is equivalent to the ($TEMPLATEDIR) variable in the Template Options ).

The Script Repository Directory and Template Repository Directory fields control where Scripts and Templates are placed when they are installed from the Repository (see Using the Repository Dialog ). These directories can be accessed using the constants ($SCRIPT_REPOS_DIR) or ($TEMPLATE_REPOS_DIR) in the Script Options or Template Options dialogs.

The Syntax Directory and Syntax DLL Directory fields control the location of Tree-sitter syntaxes . Syntax010 files are located in the directory indicated by Syntax Directory and the Tree-sitter dynamic link library files are located in the Syntax DLL Directory (.dll on Windows, .so on Linux, or .dylib on macOS). Note that some Syntax010 file may not be created until the syntax is first run. The constants ($SYNTAX_DIR) and ($SYNTAX_DLL_DIR) can be used to access these directories in the Syntax Options dialog.

Note that if the Script Directory , Template Directory , Script Repository Directory , Template Repository Directory , Syntax Directory or Syntax DLL Directory fields are modified, you must physically move the script or template or syntax files to the new location otherwise you may get a 'file not found' error when attempting to run a file.

If using the Portable version of 010 Editor all directories will begin with the ($BASEDIR) constant, which is the root directory where the portable version was installed. See Using the Portable Version for more information on the directory structure with the portable version.

Clicking Reset will return all directory options to the default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.