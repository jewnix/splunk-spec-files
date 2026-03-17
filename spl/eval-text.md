# Evaluation Functions - Text

Category: **Evaluation - Text**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `len` | `len(<str>)` | This function returns a count of the UTF-8 code points in a string. While the character length and number of code points are identical for some strings in English, the count is not the same for all strings, including strings in other languages. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title2) |
| `lower` | `lower(<str>)` | This function takes one string argument and returns the string in lowercase. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title3) |
| `ltrim` | `ltrim(<str>,<trim_chars>)` | This function removes characters from the left side of a string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title4) |
| `replace` | `replace(<str>,<regex>,<replacement>)` | This function substitutes the replacement string for every occurrence of the regular expression in the string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title5) |
| `rtrim` | `rtrim(<str>,<trim_chars>)` | This function removes the trim characters from the right side of the string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title6) |
| `spath` | `spath(<value>,<path>)` | Use this function to extract information from the structured data formats XML and JSON. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title7) |
| `substr` | `substr(<str>,<start>,<length>)` | This function returns a substring of a string, beginning at the start index. The length of the substring specifies the number of character to return. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title8) |
| `trim` | `trim(<str>,<trim_chars>)` | This function removes the trim characters from both sides of the string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title9) |
| `upper` | `upper(<str>)` | This function returns a string in uppercase. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title10) |
| `urldecode` | `urldecode(<url>)` | This function takes one URL string argument X and returns the unescaped or decoded URL string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/text-functions#ariaid-title11) |
