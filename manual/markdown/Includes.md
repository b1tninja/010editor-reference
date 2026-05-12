# 010 Editor Manual - Includes

**Source:** [`manual/html/Includes.htm`](../html/Includes.htm) (SweetScape 010 Editor manual mirror).

## Page header
Includes

## Summary (lead paragraphs)
Additional source code files can be inserted into the current script or template using the syntax '#include "filename"'. For example:

#include "Vector.bt" Note that a semi-colon is not required after the statement. The angle brackets '<' and '>' can be used around the file name instead of quotes (as in regular C), but the semantics are the same. The indicated file will be inserted into the script or template and the code will be executed as if it were one long file.

When a file is included, it will be searched for in the following directories in the following order:

File Directory - The directory where the file that contains the include statement currently resides. Template Directory - The default Template directory specified using the Directory Options . Script Directory - The default Script directory specified using the Directory Options . Template Repository Directory - The directory where Templates from the Repository are installed (see Directory Options ). Script Repository Directory - The directory where Scripts from the Repository are installed (see Directory Options ). Additional Include Directories - Any additional directories specified using the Compiling Options dialog. Include files can be nested as in regular C. Use ".." to search the parent directory or use "\" or "/" to search sub-directories. For example:

#include "src/common.bt" #include "../defs/userdefs.bt" Note that either "\" or "/" can be used and 010 Editor will automatically change the slash to the proper slash for the current platform when searching for files. During execution, if an error occurs inside an include file, you will be asked if you want to load the include file in the interface.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.