# 010 Editor Manual - Using Projects and Workspaces

**Source:** [`manual/Project.htm`](../manual/Project.htm) (SweetScape 010 Editor manual mirror).

## Page header
Using Projects and Workspaces

## Section headings
- **Creating Projects and Project Options**
- **Opening and Closing Projects**
- **Viewing and Editing Projects**
- **Adding Files to Projects**
- **Project Folders and Live Folders**
- **Searching in a Project**

## Summary (lead paragraphs)
A project is list of files being worked on and the list can be organized into a tree structure with a series of folders. The files in a project can either be opened or closed in 010 Editor. A workspace file is a file containing a list of all the open files in 010 Editor including how their tabs are laid out and any extra Floating Tab windows . Projects can be created with or without an associated workspace. All files in a project are displayed in the Project node of the Workspace tab or the Project tab . Manage files in the project using the Project Menu or by right-clicking on the Project structure in the Workspace tab or Project tab . Projects are saved to disk with extension ".1pj" and workspace files are saved with extension ".1wk". The Title Bar of the application displays the name of the current project inside square brackets '[' and ']'.

A new project can be created by clicking ' Project > New Project/Workspace ' which displays the Project Options dialog:

If the Store Workspace with Project (Open Files) toggle is checked, a workspace file will be associated with the new project and all currently open files will be closed when the project is created. If the toggle is not checked then the workspace from the current application is used instead. When a project is loaded that has an associated workspace then the Workspace will show Open Files: <Project Name> but if no workspace is associated the Workspace displays just Open Files .

When the Store Paths Relative to Project File toggle is set, any paths stored on disk will be relative and if the toggle is not set the paths will be stored as absolute. For example, if the project file is "C:\Projects\Proj1.1pj" and the data file is "C:\Projects\Data\File1.dat" then the relative path is "Data\File1.dat" and the absolute path is "C:\Projects\Data\File1.dat". Use relative paths if the project file is moved with the data files.

When a project is created, the project is not saved to disk until ' Project > Save Project ' or ' Project > Save Project As ' is clicked. When a project is modified a '*' symbol is displayed after the project name in the Workspace tab or the Project tab . After a project is assigned a file name by saving, then adding or moving a file within the project will cause the project to be modified. If the Auto-Save Project toggle is set in the Project Options dialog then the project will automatically be written to disk. If Auto-Save Project is not enabled then the project must be saved manually using ' Project > Save Project '.

Project or workspace files can be opened using the ' Project > Open Project/Workspace ' or ' Project > Open Recent Projects ' menu options. The Workspace tab and Project tab contain a list of recent projects and workspaces and double-clicking on an entry will load that project or workspace file. Note that only one project can be loaded at a time. When loading a workspace file the current workspace is replaced by the workspace in the file. If loading a project and the project has an associated workspace , the current files are closed and all the files in the workspace file are loaded instead. Project and workspace files can also be opened using the command line , the ProjectOpen function, by double-clicking a project in the Windows Explorer, and by dragging and dropping a project from the Windows Explorer to 010 Editor.

Close a project using ' Project > Close Project ' or by hovering the mouse over the project name in the Workspace tab or Project tab and clicking the 'X' button as shown in the above figure. If the current project has an associated workspace then the currently open files are closed and the files from the default application workspace are loaded instead.

If a project is active when 010 Editor is closed, that project will automatically be reloaded when 010 Editor is restarted. See the Opening Files/Tabs Options dialog and the Remember Last Project option to disable this function.

Projects may be viewed using the Project section of the Workspace tab (shown above left) or the Project tab (shown above right). Both areas show the same information. When a project is loaded, the project heading indicates Project: <project_name> and when no project is loaded the heading indicates just Project . If a project is loaded that has an associated workspace, the workspace will indicate Open Files: <project_name> but if no associated workspace is found just Open Files will be listed instead. To open files in a project, double-click on a file or drag one or more files to the File Tabs .

Edit projects using the Project Menu or by right-clicking on a project node in the Workspace or Project tab. To add files to the project see the Adding Files to Projects section below. After files have been added to the project they can be rearranged or moved inside folders by clicking and dragging a file in the Workspace or the Project tab. Right-click on a file in a project and select Remove from Project or press the Delete key on the keyboard to delete the file from the project. Note this does not delete the file on disk.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.