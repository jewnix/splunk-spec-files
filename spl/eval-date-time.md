# Evaluation Functions - Date and Time

Category: **Evaluation - Date and Time**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `now` | `now()` | This function takes no arguments and returns the time that the search was started when run as an ad-hoc search. If used with a scheduled search, returns the time that the search was scheduled to run, which might not be the time that the scheduled search actual runs. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions#ariaid-title2) |
| `relative_time` | `relative_time(<time>,<specifier>)` | This function takes a UNIX time as the first argument and a relative time specifier as the second argument and returns the UNIX time value of <specifier> applied to <time>. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions#ariaid-title3) |
| `strftime` | `strftime(<time>,<format>)` | This function takes a UNIX time value as the first argument and renders the time as a string using the format specified. The UNIX time must be in seconds. Use the first 10 digits of a UNIX time to use the time in seconds. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions#ariaid-title4) |
| `strptime` | `strptime(<str>,<format>)` | This function takes a time represented by a string and parses the time into a UNIX timestamp format. You use date and time variables to specify the format that matches string. For a complete list and descriptions of the variables, see Date and time format variables . | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions#ariaid-title5) |
| `time` | `time()` | This function returns the wall-clock time, in the UNIX time format, with microsecond resolution. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/date-and-time-functions#ariaid-title6) |
