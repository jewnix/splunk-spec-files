# Statistical Functions - Multivalue

Category: **Statistical - Multivalue**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/multivalue-stats-and-chart-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `list` | `list(<value>)` | The list function returns a multivalue entry from the values in a field. The order of the values reflects the order of the events. | chart, stats, timechart, eventstats, streamstats, geostats, sistats, tstats, mstats, sichart, sitimechart | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/multivalue-stats-and-chart-functions#ariaid-title2) |
| `values` | `values(<values>)` | The values function returns a list of the distinct values in a field as a multivalue entry. The order of the values is lexicographical. | chart, stats, timechart, eventstats, streamstats, geostats, sistats, tstats, mstats, sichart, sitimechart | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/multivalue-stats-and-chart-functions#ariaid-title3) |
