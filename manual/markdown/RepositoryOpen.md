# 010 Editor Manual - Installing Files on Open from the Repository

**Source:** [`manual/RepositoryOpen.htm`](../manual/RepositoryOpen.htm) (SweetScape 010 Editor manual mirror).

## Page header
Installing Files on Open from the Repository

## Summary (lead paragraphs)
When any file is opened in 010 Editor, 010 Editor checks the file name and the ID bytes at the beginning of the file to see if any Templates exist in the Repository that can parse data in the file. If a Template is found and no Template is already installed to parse the data file (see the Template Options dialog for a list of installed Templates) then the following dialog is displayed:

Clicking the Install button will automatically install and run the displayed Template on the current data file. Sometimes multiple Templates exist in the Repository which can parse the same file. In this case all the Templates will be displayed in the above dialog and select the Template to install by clicking on it before pressing the Install button. Alternately, double-clicking on a Template will install and run that file.

Note that some Templates exist in the repository with the File Mask '*' meaning files of this type do not have a specific file extension (an example of this is Linux or macOS executable files). 010 Editor will not automatically display this dialog for Templates that use the '*' mask and these type of Templates must be installed directly using the Repository Dialog .

Clicking the Ignore button will close the dialog without installing the Template and the dialog will not be displayed again asking to install this Template. In the Repository Dialog the toggle Ask to install this template when opening files is displayed at the bottom of each Template page. When the Ignore button is clicked this toggle is unchecked for that Template. To no longer ignore a template when opening files, recheck the Ask to install this template when opening files box. If multiple Templates are displayed in the above dialog box the Ignore button instead displays Ignore All and clicking Ignore All will ignore all Templates in the list.

Click the Ask me Later button to close the dialog without installing any Templates but this dialog will be displayed again the next time a data file is opened that this Template can parse. See the Template Options dialog for more information on the meaning of the File Mask and ID Bytes fields. Other Templates can be installed or uninstalled using the Repository Dialog .

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.