# 010 Editor Manual - Tool Functions

**Source:** [`manual/html/FuncTools.htm`](../html/FuncTools.htm) (SweetScape 010 Editor manual mirror).

## Page header
Tool Functions

## Summary (lead paragraphs)
The following is a list of functions that allow running many of the tools in the Tools Menu or Find Menu, as well as functions for working with drives and processes.

int64 Checksum( int algorithm, int64 start=0, int64 size=0, int64 crcPolynomial=-1, int64 crcInitValue=-1 ) Runs a simple checksum on a file and returns the result as a int64. The algorithm can be one of the following constants:

If start and size are zero, the algorithm is run on the whole file. If they are not zero then the algorithm is run on size bytes starting at local address start . See the ChecksumAlgBytes and ChecksumAlgStr functions to run more complex algorithms. crcPolynomial and crcInitValue can be used to set a custom polynomial and initial value for the CRC functions. A value of -1 for these parameters uses the default values as described in the Check Sum/Hash Algorithms topic. A negative number is returned on error.

int ChecksumAlgArrayStr( int algorithm, char result[], uchar *buffer, int64 size, char ignore[]="", int64 crcPolynomial=-1, int64 crcInitValue=-1 ) Similar to the ChecksumAlgStr function except that the checksum is run on data stored in an array instead of in a file. The data for the checksum should be passed in the buffer array and the size parameter lists the number of bytes in the array. The result from the checksum will be stored in the result string and the number of characters in the string will be returned, or -1 if an error occurred. See the ChecksumAlgStr function for a list of available algorithms.

int ChecksumAlgArrayBytes( int algorithm, uchar result[], uchar *buffer, int64 size, char ignore[]="", int64 crcPolynomial=-1, int64 crcInitValue=-1 ) Similar to the ChecksumAlgStr function except that the checksum is run on data in an array instead of in a file and the results are stored in an array of bytes instead of a string. The data for the checksum should be passed in the buffer array and the size parameter lists the number of bytes in the array. The result of the checksum operation will be stored as a set of hex bytes in the parameter result . The function will return the number of bytes placed in the result array or -1 if an error occurred. See the ChecksumAlgStr function for a list of available algorithms.

int ChecksumAlgStr( int algorithm, char result[], int64 start=0, int64 size=0, char ignore[]="", int64 crcPolynomial=-1, int64 crcInitValue=-1 ) Similar to the Checksum algorithm except the following algorithm constants are supported:

The result argument specifies a string which will hold the result of the checksum. The return value indicates the number of characters in the string, or is negative if an error occurred. Any ranges to ignore can be specified in string format with the ignore argument (see Check Sum/Hash Algorithms ). The crcPolynomial and crcInitValue parameters are used to set a custom polynomial and initial value for the CRC algorithms. Specifying -1 for these parameters uses the default values as indicated in the Check Sum/Hash Algorithms help topic. See the Checksum function above for an explanation of the different checksum constants.

int ChecksumAlgBytes( int algorithm, uchar result[], int64 start=0, int64 size=0, char ignore[]="", int64 crcPolynomial=-1, int64 crcInitValue=-1 ) This function is identical to the ChecksumAlgStr function except that the checksum is returned as a byte array in the result argument. The return value is the number of bytes returned in the array.

TCompareResults Compare( int type, int fileNumA, int fileNumB, int64 startA=0, int64 sizeA=0, int64 startB=0, int64 sizeB=0, int matchcase=true, int64 maxlookahead=10000, int64 minmatchlength=8, int64 quickmatch=512 ) Runs a comparison between two files or between two blocks of data. The type argument indicates the type of comparison that should be run and can be either:

fileNumA and fileNumB indicate the numbers of the file to compare (see GetFileNum ). The file numbers may be the same to compare two blocks in the same file. The startA , sizeA , startB , and sizeB arguments indicate the size of the blocks to compare in the two files. If the start and size are both zero, the whole file is used. If matchcase is false, then letters of mixed upper and lower cases will match. See Comparing Files for details on the maxlookahead , minmatchlength and quickmatch arguments. The return value is TCompareResults structure with contains a count variable indicating the number of resulting ranges, and an array of record . Each record contains the variables type , startA , sizeA , startB , and sizeB to indicate the range. The type variable will be one of:

## Notes
Machine-generated for navigation; figures, tables, and full `<pre>` examples remain in the `.htm`.