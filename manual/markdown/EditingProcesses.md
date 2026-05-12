# 010 Editor Manual - Editing Processes

**Source:** [`manual/html/EditingProcesses.htm`](../html/EditingProcesses.htm) (SweetScape 010 Editor manual mirror).

## Page header
Editing Processes

## Section headings
- **Open Process Dialog**
- **Editing Processes**
- **Making Process Images**
- **Viewing Process Properties**
- **Output Window**

## Summary (lead paragraphs)
010 Editor can open any currently running process as a file in the interface. The individual bytes of memory used by process can then be edited and saved back to the process. To open a process, use the Open Process dialog box which can be accessed by clicking the ' File > Open Process... ' menu option, or pressing Ctrl+Shift+O . Processes can also be opened using the Command Line .

Note: Incorrectly editing processes can lead to programs performing incorrectly or system crashes.

Choose which process to open in the Process List on the left side of the dialog. Each process has a name and an ID number associated with it. The process list can be sorted by clicking on the Process Name or Process ID headings.

When a process is selected, a number of heaps and modules are displayed for the process in the tabbed section of the dialog. A heap is simply a block of memory that has been assigned to a process. A list of all heaps for the process can be viewed by clicking on the Heaps tab in the center of the dialog. Each heap has a position in memory, indicated by the Address and Size columns. As well, each heap has a number of Flags , a State and a Type . The Flags indicate the access restrictions for the heap and may include Read, Write, WriteCopy, Execute, No access, or Unallocated. The State column may be Free (unallocated), Committed (allocated), or Reserved (allocated but not available). The Type column may be Image, Mapped, or Private.

A module is a block of memory that is associated with an executable, DLL, or other dynamically linked library. Each module may have a number of heaps contained within it. Click the Modules tab to view a list of all modules for the current process. Each module has a starting Address , a Size , and a Name which is usually the name of the executable or DLL associated with the module.

On the right-hand side of the display is a graph of all readable bytes of the process. Areas of the process that can be modified are drawn in green, and read-only areas are drawn in gray. If heaps or modules are selected in the heaps or modules list, those areas will be highlighted in the graph. A gray vertical line just to the left of the graph indicates which bytes will be opened in the editor when the Open button is clicked. Which bytes are opened is determined by the toggles in the Options box.

The Open Options box allows control of how the process is opened and is accessed by clicking the Options button. If the Open only Writeable Bytes toggle is enabled, then only the areas of the process that can be modified are opened (note that a vertical gray line just to the left of the process graph indicates which bytes will be opened). Unclick the toggle to open all readable bytes. Note that if you modify a read-only portion of the file and try to save the changes, you will receive an error. If the Open Custom Range toggle is enabled, a custom memory start address and size to open can be specified in the Start and Size combo boxes. If the tabs in the middle of the dialog are displaying heaps, then the last option will indicate Open Selected Heaps . When this option is enabled, only those heaps that are selected in the table will be opened for editing. Likewise, if the Modules tab is displayed, the last option will indicate Open Selected Modules and only the selected modules will be opened for editing. Enable the Open as Read Only toggle to open the file in read-only mode.

When a process is opened, each heap is mapped to an area of a file. See the Output Window section below for more information.

Once a process has been opened in the editor, it can be edited just like any other file (see Using the Hex Editor ). Since the size of a process is fixed, bytes cannot be inserted or deleted from the process. Once modifications have been made to the process, click the ' File > Save ' menu option to write the changes back to the process. If the process has changed, or you are attempting to modify a read-only area, you may receive an error when saving data.

After a process is loaded in 010 Editor, a byte-by-byte copy of the process can be saved to disk using the ' File > Save As... ' or ' File > Save a Copy... ' menu options (this is called a process image ). Save a portion of the process to disk by selecting bytes in the editor and clicking the ' File > Save Selection... ' menu option.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.