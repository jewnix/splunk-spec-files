# Internal Search Commands

Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/about-internal-commands)  
Splunk version: 10.2

These commands are internal, unsupported, and experimental. Use only at the direction of Splunk Support.

| Command | Description | Docs |
|---------|-------------|------|
| `collapse` | The collapse command condenses multifile results into as few files as the chunksize option allows. This command runs automatically when you use outputlookup and outputcsv commands. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/collapse) |
| `dump` | For Splunk Enterprise deployments, export search results to a set of chunk files on local disk. For information about other export methods, see Export search results in the Search Manual . | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/dump) |
| `findkeywords` | Given some integer labeling of events into groups, finds searches to generate these groups. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/findkeywords) |
| `makejson` | Creates a JSON object from the specified set of fields in the search results, and places the JSON object into a new field. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/makejson) |
| `mcatalog` | The mcatalog command performs aggregations on the values in the metric_name and dimension fields in the metric indexes. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/mcatalog) |
| `noop` | The noop command is an internal command that you can use to debug your search. It includes several arguments that you can use to troubleshoot search optimization issues. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/noop) |
| `prjob` | Use the prjob command for parallel reduce search processing of an SPL search in a distributed search environment. The prjob command analyzes the specified SPL search and attempts to reduce the search runtime by automatically placing a redistribute command in front of the first non-streaming SPL command like stats or transaction in the search. It provides the same functionality as the redistribute command, but with a simpler syntax. Similar to the redistribute command, use the prjob command to automatically speed up high cardinality searches that aggregate a large number of search results. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/prjob) |
| `redistribute` | The redistribute command implements parallel reduce search processing to shorten the search runtime of a set of supported SPL commands. Apply the redistribute command to high-cardinality dataset searches that aggregate large numbers of search results. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/redistribute) |
| `runshellscript` | For Splunk Enterprise deployments, executes scripted alerts. This command is not supported as a search command. | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/internal-commands/runshellscript) |
