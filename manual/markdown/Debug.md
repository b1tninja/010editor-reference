# 010 Editor Manual - Using the Debugger

**Source:** [`manual/html/Debug.htm`](../html/Debug.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using the Debugger

## Section headings
- **Starting and Stopping the Debugger**
- **Breakpoints**
- **Stepping Through Scripts or Templates**
- **Investigating Variables**
- **Watches**
- **Quick Watch**
- **Using the Call Stack**
- **Debugging Runtime Errors**
- **Debugging Read/Write Functions**
- **Debugging On-Demand Structures**
- **Debugging Highlighting Functions**

## Summary (lead paragraphs)
The debugger allows finding and fixing issues with Scripts or Templates written for 010 Editor. Using the debugger, execution of a Script or Template can be stepped line by line and the value of each variable examined after each line. Many of the debugging operations can be controlled using the Debug Menu .

By default the debugger is always enabled in 010 Editor but can be turned on or off by clicking the ' Debug > Debugging Enabled ' menu option. If a checkmark is displayed beside the Debugging Enabled option then debugging is enabled and if an 'X' is displayed then debugging is disabled. Any time a Script or Template is run (see Running Templates and Scripts ) and debugging is enabled, the debugger automatically monitors for breakpoints . If a breakpoint is hit then the program execution pauses at the breakpoint and the debugger is started. Scripts or Templates can also be run by selecting a Script or Template in the editor and clicking the ' Debug > Start Debugging ' menu option. Note this is equivalent to using ' Scripts > Run Script ' when a Script is selected or ' Templates > Run Template ' when a Template is selected, or clicking the Run button in the top-right corner of a Template or Script editor. Debugging can only occur on one Script or Template at a time and the current Script or Template must finish before another Script or Template can begin.

Another method of starting the debugger is to select a Script or Template and then click the ' Debug > Step Into ' menu option. This option starts execution of the program but pauses at the first executable line of the program and starts the debugger. Also the debugger can be started by right-clicking on a Script or Template in the Text Editor and choosing Run to Cursor from the right-click menu. This option attempts to run the Script or Template until the selected line is reached at which point the execution is paused and the debugger is started.

When program execution is paused the current line is marked with a yellow arrow as displayed in the figure above. By default, icons for the debugger are overlaid onto the editor in the top-right corner but these buttons can be displayed in the Tool Bar instead by disabling ' View > File Bar > Show Overlaid Debug Icons ' and enabling ' View > Tool Bars > Debug '. To continue execution of the program click ' Debug > Continue ', or use ' Scripts > Continue Script or Template ' or ' Templates > Continue Script or Template ', or click the double-arrow icon in the top-right corner. The debugger can also be stepped to another line as discussed in the Stepping Through Scripts or Templates section below. Program execution can be paused by clicking the ' Debug > Pause ' menu option while a Script or Template is running or by clicking the Pause button in the Tool Bar. Pausing a Script or Template pauses the program, places the cursor at the next line to be executed and starts the debugger.

To stop a Script or Template which is running or paused click the ' Debug > Stop Script/Template ' menu option or press the keyboard shortcut Shift+Esc. Scripts or Templates can also be stopped using ' Scripts > Stop Script ' or ' Templates > Stop Template ' which only appear when a Script or Template is running. When paused or at a breakpoint, the Stop icon in the top-right corner of the editor can be clicked to stop the Script or Template. Stopping a Script or Template which is currently paused at a breakpoint resets the debugger.

A breakpoint is a line in a Script or Template the debugger will pause at when execution reaches that line. Breakpoints can be set by moving the cursor to the requested line in a Script or Template and clicking ' Debug > Toggle Breakpoint '. Click Toggle Breakpoint on a line which already contains a breakpoint to remove that breakpoint. Alternately breakpoints can be set or removed by single-clicking with the mouse in the address column on the left side of each Text Editor. In the address column a number of symbols can appear:

Hovering the mouse cursor over one of the above symbols in the Text Editor will also give information about the symbol in a hint popup. A list of all set breakpoints for the current Script or Template is available in the Breakpoints tab. The Breakpoints tab is located in a tab group with the Inspector and the '<' or '>' arrows may be used to locate the tab, or click ' Debug > View Breakpoints '.

Inside the Breakpoints tab is a list of the line numbers for each breakpoint in the file. Right-click on the Breakpoints tab and choose Add Breakpoint to set a breakpoint by line number. Select a breakpoint and choose Remove Breakpoint to delete the breakpoint from the file. Double-clicking on a breakpoint in the list will jump the mouse cursor to that line in the editor. Note that breakpoints are persistent, meaning they are saved to disk and reloaded when 010 Editor is shut down and restarted (this behaviour can be turned off using the Compiling Options dialog). To delete all breakpoints in all files use the ' Debug > Delete All Breakpoints ' menu option.

Note that breakpoints are currently not hit when 010 Editor is starting up and reloading files that were previously opened. To hit a breakpoint in a Script or Template rerun the Script or Template after 010 Editor has finished starting up. If a breakpoint is set on a line which cannot be executed (e.g. a comment) then the breakpoint will be moved to the next line that can be executed when the Script or Template is run.

Once the debugger has paused at a line in a Script or Template there are three ways to step to the next line, all of which can be access on the Debug Menu or as icons in the top-right corner of the editor:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.