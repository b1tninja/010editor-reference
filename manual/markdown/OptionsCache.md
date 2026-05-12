# 010 Editor Manual - Cache Options

**Source:** [`manual/OptionsCache.htm`](../manual/OptionsCache.htm) (SweetScape 010 Editor manual mirror).

## Page header
Cache Options

## Summary (lead paragraphs)
010 Editor features a powerful data engine that enables loading huge files and cutting and pasting large blocks of memory very quickly (see Introduction to the Data Engine for more information). The Cache Options dialog controls various options of the data engine plus some options for Tree-sitter syntaxes. Open the Cache Options dialog by clicking the ' Tools > Options... ' menu option and selecting ' Cache ' from the list.

When accessing files, data that is loaded into memory is stored in a cache. The size of the cache can be specified using the Memory Limit options. Select the MB toggle and enter the cache limit in number of megabytes. Alternately, select the % of Physical Memory toggle and enter the percentage of physical memory that should be used for the cache (between 1 and 100). Note that physical memory does not include any system virtual memory (using the Windows swap file). Once too much data is loaded into the cache, data will be written to a swap file on disk and see the Directory Options dialog to control where the swap file is written.

When using a Tree-sitter syntax on a file, the syntax parses the file into a syntax tree to provide high-quality syntax highlighting. This syntax tree can require a lot of memory for large data files so the data engine uses a caching system to limit memory usage (see Syntaxes for Large Files for more information). Large files are divided into a series of blocks and the syntax tree is calculated for each block separately. Specify the size of the each block in the Tree-sitter Block Size field. The size is given in megabytes and if the current file is smaller than the block size, it is parsed as one complete syntax tree but if it is larger than the block size the syntax tree is split into multiple parts. Syntax trees for each block are kept in a cache and once too many syntax trees are loaded, the oldest trees are discarded. The size of the cache is specified using the Memory Available for Tree-sitter Cache fields. The size can either be specified in megabytes using MB , or as a percentage of total memory by using % of Physical Memory .

Clicking Reset will return all cache options to their default values.

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.