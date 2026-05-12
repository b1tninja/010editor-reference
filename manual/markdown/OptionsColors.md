# 010 Editor Manual - Theme/Color Options

**Source:** [`manual/OptionsColors.htm`](../manual/OptionsColors.htm) (SweetScape 010 Editor manual mirror).

## Page header
Theme/Color Options

## Section headings
- **Application Colors**
- **Title Bar**
- **Menu/Right Click Menu**
- **Dialogs**
- **Tool Bar Colors**
- **Status Bar Colors**
- **Startup Page Colors**
- **File Tab Colors**
- **Dock Window Tab Colors**
- **Dock Window Colors**
- **Table Colors**
- **Graph Colors**
- **App Bar Colors**
- **Editor Colors**
- **Hex Editor Colors**
- **Scroll Bars**
- **Mini Map**
- **Find**
- **Compare**
- **Template Styles**
- **Syntax Styles**

## Summary (lead paragraphs)
010 Editor contains a number of themes which are a set of colors for all the various user interface elements in the program. Some themes have dark backgrounds, called dark themes, and some themes have light backgrounds, called light themes. The Theme/Colors Options dialog allows choosing a theme and a theme can also be chosen in the Welcome dialog displayed when 010 Editor is run for the first time or with the ' View > Theme ' menu. Open the Theme/Color Options dialog by clicking ' Tools > Options... ' and selecting Theme/Colors from the list. Styles for all the Syntax Highlighting rules are also controlled by this dialog. New themes can be created and the individual colors in the themes can be customized. The following themes are available:

Starry Sky - A dark theme similar to Sunset Sky except uses purple as the default keyword style. Bright Sky - The standard light theme with a white background. Morning Sky - Another light theme similar to Bright Sky but uses different colors for syntax highlighting (red and green). A number of themes from older versions of 010 Editor are available for users who prefer the older styles:

Blue Sky - A light theme with a white background and blue tabs. Rain Cloud - Identical to Blue Sky except the tabs are displayed as gray. Day & Night - Uses a light theme for the editor and a dark theme for the application background. Midnight - Similar to Evening Sky except the background is black. Classic - A theme used in old versions of 010 Editor. If a theme has been imported using the Import... button at the bottom of the dialog then a new theme named Custom will also be available in the list followed by the file name of the theme in brackets. Clicking the Export... button will save the current theme to a file including any modified colors.

Some user interface elements are drawn using a native style, meaning the operating system draws those elements using its standard drawing procedures (for example the macOS menu bar and the macOS status bar are always drawn by the operating system). 010 Editor overrides some of this drawing with its own user interface styles but the native style can be turned on for some elements by clicking the Options button and turning on native drawing for either the Dialogs, Menu Bar, Menus, Tool Bars, Tool Buttons, Dock Headers (the title above each dock window), File Tabs, the Dock Window tabs, Table Headers, Scroll Bars or Group Boxes. By default, tabs, headers, menus, buttons, and scroll bars are drawn with rounded corners but this can be disabled by unchecking the Rounded Tabs , Rounded Headers , Rounded Menus , Rounded Buttons , or Rounded Scroll Bars options. Uncheck the Use Taller Tabs option to use more compact File Bar tabs. Also when switching themes when individual colors have been modified by the user, 010 Editor will ask whether to Reset the modified colors or to Keep the modified colors. If the Reset Colors when Switching Themes option is set to Ask then a dialog is displayed asking for the user choice but if the choice has already been set the Reset Colors when Switching Themes option will be set to Yes or No .

The Colors table allows customizing individual colors in each theme. Click the color box in the Fore column to set the foreground (text) color of the item or click the color box in the Back column to set the background color of the item. If a color has been modified the color name is drawn in Bold and a Reset button appears in the Reset column. Clicking the Reset button returns just that color to its original value. Some colors may be set to None , which means that the foreground or background color will be inherited from what is drawn behind the element (or in some cases setting to None means the default operating system color will be used instead). Some colors may also include a percentage which represents the Opacity: a value of 0% means full transparent and a value of 100% means fully opaque. When an Opacity is chosen between 0% and 100% then the color is blended with the background color.

Click on a color box to open up the Color Selector Box. Select a color from the box, or click the More Colors... button to open the standard Color Selector Dialog. When using the Color Selector Dialog, select a color from either the color boxes on the left or the color area on the right and click the OK button. Clicking the Add to Custom Colors button adds the current color to the list of 16 colors on the bottom left and this list is also displayed at the bottom of the color selector. If the color has an Opacity then a slider at the bottom of the dialog can be dragged to adjust the Opacity percentage. The Cancel button will close the dialog without selecting a color.

The following lists each of the color options and what they control. Note that when each color is changed the results usually are updated in the application immediately, making it easier to see how color changes will affect the application.

Dock Header - Sets the color of the header of the top of each Dock Window . Dock headers can be drawn using the system (native) style by using the Options drop-down menu. Dock Header Highlighted - When the mouse hovers over a Dock Window header, the header is changed to this color. Title Bar Title Bar - Controls the background color of the Title Bar and the color of the text within the bar. Icons - Sets the foreground and background color of icons in the Title Bar such as the close and minimize buttons. Note the background color is not used on some platforms. Icon Hover - The background color of some icons when the mouse is placed over the icon. Close Hover - The background color of the Close button when the mouse is placed over the icon. Disabled Text - Sets the text color of any text that is displayed in the Title Bar when it is disabled. Menu/Right Click Menu Menu/Right Click Menu (Windows only) - Sets the text and background color of a popup menu that is shown by clicking the Menu Bar at the top of the application or by right-clicking on the editor. If Native Dialogs is turned on in the Options drop-down list then the system default colors are used for this and the following colors. Menu Item Disabled - The text color of a disabled item in the menu. Menu Item Highlighted - Controls the text and background colors of a menu item when the mouse hovers over the menu item. Menu Separator - The color of a horizontal separator line in the menu. Menu Outline - Sets the color of the outline box around the popup menu. Menu Checked - The color of a rectangle drawn behind a checkmark or icon when it is checked in the menu. Menu Bar - Controls the color of the Menu Bar at the top of the application window. A color of None means the default operating system colors are used. If Native Menu Bar is checked in the Options drop-down list the system default colors are used for this color and the following colors. Menu Bar Selected - When the contents of a Menu Bar item are being...

Use the Syntax Style section to control the color scheme for all of the Syntax Highlighting rules. The use of styles allows multiple Syntax Highlighting rules to share a single color scheme (see Syntax Highlighting for more information). For example, both commenting in C++ and PHP share the 'comment' style. Changing the 'comment' style affects the colors of all rules that use that style. All styles that begin 'tag' are used in tag-based (e.g. XML, HTML) languages and all other styles are typically used in programming languages. Syntax Styles can be assigned a different color depending on if they are being used for a dark theme or a light theme.

Syntax style names are multi-level, meaning then may have multiple periods '.' in their names. If a syntax style is not found then the last period and identifier are removed and the style is searched again. For example, if the "type.builtin" style does not exist then the "type" style would be used instead. When a Syntax Style is selected in the list a special group of icons appears at the top-right corner of the dialog:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.