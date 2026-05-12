# 010 Editor Manual - General Options

**Source:** [`manual/OptionsGeneral.htm`](../manual/OptionsGeneral.htm) (SweetScape 010 Editor manual mirror).

## Page header
General Options

## Section headings
- **Startup**
- **Clipboard**
- **Updates**
- **History**
- **Auto-Hide**
- **Application Scale Factor**
- **Importing and Exporting Settings**
- **Reset Settings**

## Summary (lead paragraphs)
The General Options dialog contains options for the whole application. Access this dialog by clicking the ' Tools > Options... ' menu option and selecting General from the list. This dialog can also be used to import, export, or reset options for the entire application.

Allow Only One Instance of 010 Editor - If this flag is set, only one copy of 010 Editor is allowed to run at a time. If new files are opened from the Windows Explorer or elsewhere, they are loaded into the already-running program. Hide Splash Screen on Startup - If enabled, this toggle will prevent the splash screen from displaying while 010 Editor is starting up. This option is only available if you have purchased a license of 010 Editor and entered your license information in the Licensing dialog. Add 010 Editor to Windows Explorer right-click menu - If this toggle is enabled, an entry that says 010 Editor will be added to the Windows Explorer popup menu when you right-click on a file. Clicking the 010 Editor option will cause the file to be opened in 010 Editor. Clipboard Leave Large Blocks on Clipboard on Exit - When this toggle is set and the clipboard contains a large block of data on exit (over 4 megabytes), 010 Editor will copy this block onto the system clipboard. When not set, large blocks are discarded and will be unavailable to other programs after 010 Editor exits. Note that small blocks (under 4 megabytes) are automatically copied. 010 Editor supports copying large blocks (gigabytes in some cases) that the Windows clipboard cannot handle (the limit is about 16 megabytes on some systems). Therefore some blocks may not copy onto the clipboard properly if too much data is copied. Auto Convert to Text when Copying Hex Bytes - If this toggle is enabled and Copy is used while the caret is in the Hex Area of the Hex Editor , the bytes will be converted to text before the data is copied to the clipboard, similar to Copy as Hex Text . If the caret is in the Character Area of the Hex Editor then the bytes are copied without converting to text. This option also works if the caret is in an area that is displaying either Binary or Decimal data. If data is copied from a Hex Area and pasted into another Hex Area the original bytes will be pasted. The default for ...

Paste on Middle-Click (Linux Only) - Linux systems allow pasting from the selection clipboard by clicking the middle-button on a mouse. To disable middle-clicking to paste, turn off this toggle. If the toggle is off then middle-clicking activates the middle-click scrolling mode. Updates Check For Updates/News Every - If this toggle is enabled 010 Editor will download any news, including notification of new releases, from our website and display it on the Startup Page. Enter the number of days between downloads in the Days field and note that new updates are not installed automatically. See the Startup Page for more information. Show Popup when New Version is Available - When this toggle is enabled and 010 Editor discovers a new version is available while checking for updates, a popup window will be displayed. If the Check for Updates toggle is turned off a popup will not be displayed. Updates can also be checked manually by clicking the ' Help > Check for Updates ' menu option on the main menu. History History List Size - Specifies the number of items to appear in the recent file history list. This affects the number of items on the ' File > Open Recent ' list and the number of Recent Files in the Workspace (see Using the Workspace for more information). Auto-Hide Auto-Hide Bar Time - Some tools in 010 Editor are displayed as a bar at the bottom of the editor including the Find Bar , Replace Bar , Goto Bar , Select Bar , etc. When any of these bars are not used for a period of time, they will be automatically hidden. Enter the number of seconds of inactivity in the Auto-Hide Bar Time field before a bar is hidden. If the toggle to the left of Auto-Hide Bar Time is disabled, the auto-hide time will be ignored and bars will never be automatically hidden. Application Scale Factor Use Custom Scaling - When this toggle is set then a scaling factor is applied to the whole application. Use the drop-down lists to the right of the toggle to select a scale factor. For examp...

Three options exist for resetting settings in the General Options dialog. Click the Reset button and then select Reset 'General' Options to return all of the General Options to their default values. Clicking Reset All Options is equivalent to pressing the Reset button on each page of the entire Options dialog. Clicking Reset Application resets all settings, history lists, window layout and tabs but requires the application to restart to take effect. To be able to return to the original settings, click the Export button to export settings before clicking Reset Application .

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.