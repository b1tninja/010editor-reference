# 010 Editor Manual - Updating and Merging Files

**Source:** [`manual/html/RepositoryMerge.htm`](../html/RepositoryMerge.htm) (SweetScape 010 Editor manual mirror).

## Page header
Updating and Merging Files

## Section headings
- **Merging and Conflicts**

## Summary (lead paragraphs)
When the Repository has been updated (see Updating the Repository ) and a new version of an already installed Template or Script has been found, the special icon appears beside the file in the Templates or Script list of the Repository Dialog . Also, if the Template or Script is open in the editor then the icon appears in the top-right corner of the editor. To install the new version either click the Update button in the Repository Dialog or the Update from Repository menu option in the Repository Menu . The Repository Dialog can display a list of all available versions of a file in the Repository and indicates which version is currently installed.

If the local Template or Script has not been modified then installing the update only involves downloading and coping the new file over the old file; however, if the local Template or Script has been modified then a dialog is displayed which gives the option to either Merge or Overwrite the file. Clicking Overwrite discards all the local changes and copies in the new file. Clicking Merge attempts to insert all the changes from the Repository into the current working file using a 3-way merge algorithm.

Often merges can be done with no issues; however, problems can occur when a change from the Repository occurs in the same place that a local edit has been made and this is called a conflict . For example if the new version in the Repository added the line:

struct HDRINFO hdr; to the end of the file but the local Template was already modified to add the line:

struct DATARECORD data; to the end of the file. This is a conflict and 010 Editor places both lines into the merged Template marked with the '<<<<<<<', '========', and '>>>>>>>' tags. For example:

<<<<<<< struct HDRINFO hdr; ======= struct DATARECORD data; >>>>>>> When a conflict occurs the icon appears in the top-right corner of a Template or Script editor. To resolve the conflict the user must edit the file and remove the '<<<<<<<', '========', and '>>>>>>>' tags. Then either delete the first option, delete the second option, or keep both options in some combination. Once the tags have been deleted, saving the file will automatically remove the icon. Before the merge takes place the local Template or Script is copied to a file with the extension .premerge and this file can be copied back if problems occur during the merge.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.