# Statistical Functions - Event Order

Category: **Statistical - Event Order**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/event-order-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `first` | `first(<value>)` | Returns the first seen value in a field. The first seen value of the field is the most recent instance of this field, based on the order in which the events are seen by the stats command. The order in which the events are seen is not necessarily chronological order. | chart, stats, timechart, eventstats, streamstats, geostats, sistats, tstats, mstats, sichart, sitimechart | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/event-order-functions#ariaid-title2) |
| `last` | `last(<value>)` | Returns the last seen value in a field. The last seen value of the field is the oldest instance of this field, based on the order in which the events are seen by the stats command. The order in which the events are seen is not necessarily chronological order. | chart, stats, timechart, eventstats, streamstats, geostats, sistats, tstats, mstats, sichart, sitimechart | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/statistical-and-charting-functions/event-order-functions#ariaid-title3) |
