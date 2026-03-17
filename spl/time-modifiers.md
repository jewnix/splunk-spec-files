# Time Modifiers

Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers)  
Splunk version: 10.2

## List of time modifiers

| Modifier | Syntax | Description | Docs |
|---|---|---|---|
| earliest | earliest=[+\|-] <time_integer><time_unit>@<time_unit> | Specify the earliest _time for the time range of your search. Use earliest=1 to specify the UNIX epoch time 1, which is UTC January 1, 1970 at 12:00:01 AM. Use earliest=0 to specify the earliest event in your data. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| _index_earliest | _index_earliest=[+\|-] <time_integer><time_unit>@<time_unit> | Specify the earliest _indextime for the time range of your search. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| _index_latest | _index_latest=[+\|-] <time_integer><time_unit>@<time_unit> | Specify the latest _indextime for the time range of your search. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| latest | latest=[+\|-] <time_integer><time_unit>@<time_unit> | Specify the latest time for the _time range of your search. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| now | now() or now | Refers to the current time. If set to earliest, now() is the start of the search. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| time | time() | In real-time searches, time() is the current machine time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |

## Define the time amount

| Time unit | Valid unit abbreviations | Docs |
|---|---|---|
| subseconds | microseconds (us), milliseconds (ms), centiseconds (cs), or deciseconds (ds) | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| second | s, sec, secs, second, seconds | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| minute | m, min, mins, minute, minutes | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| hour | h, hr, hrs, hour, hours | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| day | d, day, days | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| week | w, week, weeks | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| month | mon, month, months | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| quarter | q, qtr, qtrs, quarter, quarters | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| year | y, yr, yrs, year, years | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |

## Other time modifiers

| Modifier | Syntax | Description | Docs |
|---|---|---|---|
| daysago | daysago=<int> | Search events within the last integer number of days. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| enddaysago | enddaysago=<int> | Set an end time for an integer number of days before Now. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| endhoursago | endhoursago=<int> | Set an end time for an integer number of hours before Now. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| endminutesago | endminutesago=<int> | Set an end time for an integer number of minutes before Now. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| endmonthsago | endmonthsago=<int> | Set an end time for an integer number of months before Now. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| endtime | endtime=<string> | Search for events before the specified time (exclusive of the specified time). Use timeformat to specify how the timestamp is formatted. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| endtimeu | endtimeu=<int> | Search for events before the specific UNIX time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| hoursago | hoursago=<int> | Search events within the last integer number of hours. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| minutesago | minutesago=<int> | Search events within the last integer number of minutes. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| monthsago | monthsago=<int> | Search events within the last integer number of months. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| searchtimespandays | searchtimespandays=<int> | Search within a specified range of days, expressed as an integer. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| searchtimespanhours | searchtimespanhours=<int> | Search within a specified range of hours, expressed as an integer. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| searchtimespanminutes | searchtimespanminutes=<int> | Search within a specified range of minutes, expressed as an integer. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| searchtimespanmonths | searchtimespanmonths=<int> | Search within a specified range of months, expressed as an integer. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| startdaysago | startdaysago=<int> | Search the specified number of days before the present time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| starthoursago | starthoursago=<int> | Search the specified number of hours before the present time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| startminutesago | startminutesago=<int> | Search the specified number of minutes before the present time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| startmonthsago | startmonthsago=<int> | Search the specified number of months before the present time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| starttime | starttime=<timestamp> | Search from the specified date and time to the present, inclusive of the specified time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| starttimeu | starttimeu=<int> | Search for events starting from the specific UNIX time. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
| timeformat | timeformat=<string> | Set the timeformat for the starttime and endtime modifiers. By default: timeformat=%m/%d/%Y:%H:%M:%S | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) |
