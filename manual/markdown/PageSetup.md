# 010 Editor Manual - Page Setup

**Source:** [`manual/PageSetup.htm`](../manual/PageSetup.htm) (SweetScape 010 Editor manual mirror).

## Page header
Page Setup

## Section headings
- **Print Setup**

## Summary (lead paragraphs)
The Page Setup dialog controls how the page appears when printing. Use the Page Setup dialog to set margins, headers and footers, fonts, and paper orientation for printing. Click the ' File > Page Setup... ' menu option to open the dialog.

When printing a file, most of the options from the current Edit As are used, except for the font and number of bytes per row (when printing hex data). Click the Font button to set the font to use for the printer. Use the Bytes Per Row field to control how many bytes are printed on each line of the output.

The Header and Footer fields control the text displayed in the top and bottom margins respectively. If the Show Line toggle is enabled then a horizontal line is drawn to separate the header or footer from the rest of the page. Text entered into either of the Left fields will appear left-justified and text entered into either of the Right fields will appear right-justified. Similarly, text in the Center fields will appear in the center of the page. Each field can contain a combination of regular text and special codes, indicated by a '%' symbol followed by one or two characters. Click the Insert > button to see a full list of available codes and click one of the codes from the list to enter it into the current text field. When the page is printed, the special codes will be replaced with the required information. The following is a list of available codes:

File Path (%F) - The name of the file to be printed included path. Current Page (%p) - Current page number being printed. Total Pages (%P) - Total number of pages in document. File Time - AM/PM (%t) - Last modified time for the file, displayed with am/pm indictor. File Time - 24 Hour (%T) - Last modified time for the file, displayed in 24-hour format. File Date - Short (%d) - Last modified date for the file, displayed in 'MM/DD/YY' format. File Date - Long (%D) - Last modified date for the file, displayed in 'Weekday, Month DD, YYYY' format. Current Time - AM/PM (%ct) - Current time, displayed with am/pm indictor. Current Time - 24 Hour (%cT) - Current time, displayed in 24-hour format. Current Date - Short (%cd) - Current date, displayed in 'MM/DD/YY' format. Current Date - Long (%cD) - Current date, displayed in 'Weekday, Month DD, YYYY' format.

The Margin fields indicate how much space is required from the edge of the paper to the start of the hex printout. Note that the Header and Footer are printed in the margins. Enter a value in the Top , Right , Bottom , or Left fields to control the margin size in either of those directions. If the Units radio buttons is set to inches , the fields will be displayed in number of inches. If the Units radio button is set to cm , the fields will be displayed in centimeters.

Click the Print Setup button to show the Print Setup dialog. The dialog may be used to choose the printer used when printing. Also, the size or source of the paper can be chosen. Click the Portrait radio button to print in portrait (upright) format, or the Landscape button to print in landscape (sideways) format.

Click the Print Preview button in the Page Setup dialog to close the dialog and display the Print Preview (see Print Preview ). Clicking the Print button will close the dialog and open the Print dialog (see Printing ). Press the OK button to close the dialog with the current changes made or the Cancel button to discard all changes.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.