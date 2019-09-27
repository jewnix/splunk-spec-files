#   Version 7.2.1
#
# This file contains possible attribute/value pairs for saved search entries in
# savedsearches.conf.  You can configure saved searches by creating your own
# savedsearches.conf.
#
# There is a default savedsearches.conf in $SPLUNK_HOME/etc/system/default. To
# set custom configurations, place a savedsearches.conf in
# $SPLUNK_HOME/etc/system/local/.  For examples, see
# savedsearches.conf.example. You must restart Splunk to enable configurations.
#
# To learn more about configuration files (including precedence) please see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#  * You can also define global settings outside of any stanza, at the top of
#    the file.
#  * Each conf file should have at most one default stanza. If there are
#    multiple default stanzas, attributes are combined. In the case of multiple
#    definitions of the same attribute, the last definition in the file wins.
#  * If an attribute is defined at both the global level and in a specific
#    stanza, the value in the specific stanza takes precedence.

#*******
# The possible attribute/value pairs for savedsearches.conf are:
#*******

[<stanza name>]
* Create a unique stanza name for each saved search.
* Follow the stanza name with any number of the following attribute/value
  pairs.
* If you do not specify an attribute, Splunk uses the default.

disabled = [0|1]
* Disable your search by setting to 1.
* A disabled search cannot run until it is enabled.
* This setting is typically used to keep a scheduled search from running on
  its schedule without deleting the search definition.
* Defaults to 0.

search = <string>
* Actual search terms of the saved search.
* For example, search = index::sampledata http NOT 500.
* Your search can include macro searches for substitution.
* To learn more about creating a macro search, search the documentation for
  "macro search."
* Multi-line search strings currently have some limitations.  For example use
  with the search command '|savedseach' does not currently work with multi-line
  search strings.
* Defaults to empty string.

dispatchAs = [user|owner]
* When the saved search is dispatched via the "saved/searches/{name}/dispatch"
  endpoint, this setting controls, what user that search is dispatched as.
* This setting is only meaningful for shared saved searches.
* When dispatched as user it will be executed as if the requesting user owned
  the search.
* When dispatched as owner it will be executed as if the owner of the search
  dispatched it no matter what user requested it.
* If the 'force_saved_search_dispatch_as_user' attribute, in the limits.conf
  file, is set to true then the dispatchAs attribute is reset to 'user' while
  the saved search is dispatching.
* Defaults to owner.


#*******
# Scheduling options
#*******

enableSched = [0|1]
* Set this to 1 to run your search on a schedule.
* Defaults to 0.

cron_schedule = <cron string>
* The cron schedule used to execute this search.
* For example: */5 * * * *  causes the search to execute every 5 minutes.
* Cron lets you use standard cron notation to define your scheduled search
  interval.
  In particular, cron can accept this type of notation: 00,20,40 * * * *, which
  runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a
  cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43.
* Splunk recommends that you schedule your searches so that they are staggered
  over time. This reduces system load. Running all of them every 20 minutes
  (*/20) means they would all launch at hh:00 (20, 40) and might slow your
  system every 20 minutes.
* Splunk's cron implementation does not currently support names of months/days.
* Defaults to empty string.

schedule = <cron-style string>
* This field is DEPRECATED as of 4.0.
* For more information, see the pre-4.0 spec file.
* Use cron_schedule to define your scheduled search interval.

allow_skew = <percentage>|<duration-specifier>
* Allows the search scheduler to randomly distribute scheduled searches more
  evenly over their periods.
* When set to non-zero for searches with the following cron_schedule values,
  the search scheduler randomly "skews" the second, minute, and hour that the
  search actually runs on:
    * * * * *     Every minute.
    */M * * * *   Every M minutes (M > 0).
    0 * * * *     Every hour.
    0 */H * * *   Every H hours (H > 0).
    0 0 * * *     Every day (at midnight).
* When set to non-zero for a search that has any other cron_schedule setting,
  the search scheduler can only randomly "skew" the second that the search runs
  on.
* The amount of skew for a specific search remains constant between edits of
  the search.
* An integer value followed by '%' (percent) specifies the maximum amount of
  time to skew as a percentage of the scheduled search period.
* Otherwise, use <int><unit> to specify a maximum duration.  Relevant units
  are: m, min, minute, mins, minutes, h, hr, hour, hrs, hours, d, day, days.
  (The <unit> may be omitted only when <int> is 0.)
* Examples:
    100% (for an every-5-minute search) = 5 minutes maximum
    50% (for an every-minute search) = 30 seconds maximum
    5m = 5 minutes maximum
    1h = 1 hour maximum
* A value of 0 disallows skew.
* Default is 0.

max_concurrent = <unsigned int>
* The maximum number of concurrent instances of this search the scheduler is
  allowed to run.
* Defaults to 1.

realtime_schedule = [0|1]
* Controls the way the scheduler computes the next execution time of a
  scheduled search.
* If this value is set to 1, the scheduler bases its determination of the next
  scheduled search execution time on the current time.
* If this value is set to 0, the scheduler bases its determination of the next
  scheduled search on the last search execution time. This is called continuous
  scheduling.
  * If set to 1, the scheduler might skip some execution periods to make sure
    that the scheduler is executing the searches running over the most recent
    time range.
  * If set to 0, the scheduler never skips scheduled execution periods.
  * However, the execution
    of the saved search might fall behind depending on the scheduler's load.
    Use continuous scheduling whenever you enable the summary index option.
* The scheduler tries to execute searches that have realtime_schedule set to 1
  before it executes searches that have continuous scheduling
  (realtime_schedule = 0).
* Defaults to 1

schedule_priority = default | higher | highest
* Raises scheduling priority of a search:
  + "default": No scheduling priority increase.
  + "higher": Scheduling priority is higher than other searches of the same
    scheduling tier. While there are four tiers of priority for scheduled
    searches, only the following are affected by this property:
    1. Real-Time-Scheduled (realtime_schedule=1).
    2. Continuous-Scheduled (realtime_schedule=0).
  + "highest": Scheduling priority is higher than other searches regardless of
    scheduling tier. However, real-time-scheduled searches with priority =
    highest always have priority over continuous scheduled searches with
    priority = highest.
  + Hence, the high-to-low order (where RTSS = real-time-scheduled search,
    CSS = continuous-scheduled search, d = default, h = higher, H = highest)
    is: RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d)
* The scheduler honors a non-default priority only when the search owner has
  the 'edit_search_schedule_priority' capability.
* Defaults to "default".
* A non-default priority is mutually exclusive with a non-zero 'schedule_window'
  (see below).  If a user specifies both for a scheduled search, the scheduler
  honors the priority only.
* However, if a user specifies both settings for a search, but the search owner
  does not have the 'edit_search_scheduler_priority' capability, then the
  scheduler ignores the priority setting and honors the 'schedule_window'.
* WARNING: Having too many searches with a non-default priority will impede the
  ability of the scheduler to minimize search starvation.  Use this setting
  only for mission-critical searches.

schedule_window = <unsigned int> | auto
* When schedule_window is non-zero, it indicates to the scheduler that the
  search does not require a precise start time. This gives the scheduler
  greater flexibility when it prioritizes searches.
* When schedule_window is set to an integer greater than 0, it specifies the
  "window" of time (in minutes) a search may start within.
  + The schedule_window must be shorter than the period of the search.
  + Schedule windows are not recommended for searches that run every minute.
* When set to 0, there is no schedule window. The scheduler starts the search
  as close to its scheduled time as possible.
* When set to "auto," the scheduler calculates the schedule_window value
  automatically.
  + For more information about this calculation, see the search scheduler
    documentation.
* Defaults to 0 for searches that are owned by users with the
  edit_search_schedule_window capability. For such searches, this value can be
  changed.
* Defaults to "auto" for searches that are owned by users that do not have the
  edit_search_window capability. For such searches, this setting cannot be
  changed.
* A non-zero schedule_window is mutually exclusive with a non-default
  schedule_priority (see schedule_priority for details).

#*******
# Workload management options
#*******

workload_pool = <name of workload pool>
* Sets the name of the workload pool to be used by this search.
* There are multiple workload pools defined in workload_pools.conf.
  Each workload pool has different resource limits associated with it,
  for example, CPU, Memory, etc.
* The search process of this search will be launched into the
  workload_pool specified above.
* The workload_pool used should be defined in workload_pools.conf.
* If workload management is enabled and a explicit workload_pool is not specified,
  the default_pool defined in workload_pools.conf will be used.

#*******
# Notification options
#*******

counttype = number of events | number of hosts | number of sources | custom | always
* Set the type of count for alerting.
* Used with relation and quantity (below).
* NOTE: If you specify "always," do not set relation or quantity (below).
* Defaults to always.

relation = greater than | less than | equal to | not equal to | drops by | rises by
* Specifies how to compare against counttype.
* Defaults to empty string.

quantity = <integer>
* Specifies a value for the counttype and relation, to determine the condition
  under which an alert is triggered by a saved search.
* You can think of it as a sentence constructed like this: <counttype> <relation> <quantity>.
* For example, "number of events [is] greater than 10" sends an alert when the
  count of events is larger than by 10.
* For example, "number of events drops by 10%" sends an alert when the count of
  events drops by 10%.
* Defaults to an empty string.

alert_condition = <search string>
* Contains a conditional search that is evaluated against the results of the
  saved search.  Alerts are triggered if the specified search yields a
  non-empty search result list.
* Defaults to an empty string.


#*******
# generic action settings.
# For a comprehensive list of actions and their arguments, refer to
# alert_actions.conf.
#*******

action.<action_name> = 0 | 1
* Indicates whether the action is enabled or disabled for a particular saved
  search.
* The action_name can be: email | populate_lookup | script | summary_index
* For more about your defined alert actions see alert_actions.conf.
* Defaults to an empty string.

action.<action_name>.<parameter> = <value>
* Overrides an action's parameter (defined in alert_actions.conf) with a new
  <value> for this saved search only.
* Defaults to an empty string.


#******
# Settings for email action
#******

action.email = 0 | 1
* Enables or disables the email action.
* Defaults to 0.

action.email.to = <email list>
* REQUIRED. This setting is not defined in alert_actions.conf.
* Set a comma-delimited list of recipient email addresses.
* Defaults to empty string.

* When configured in Splunk Web, the following email settings
  are written to this conf file only if their values differ
  from settings in alert_actions.conf.

action.email.from = <email address>
* Set an email address to use as the sender's address.
* Defaults to splunk@<LOCALHOST> (or whatever is set in alert_actions.conf).

action.email.subject = <string>
* Set the subject of the email delivered to recipients.
* Defaults to SplunkAlert-<savedsearchname> (or whatever is set
  in alert_actions.conf).

action.email.mailserver = <string>
* Set the address of the MTA server to be used to send the emails.
* Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf).

action.email.maxresults = <integer>
* Set the maximum number of results to be emailed.
* Any alert-level results threshold greater than this number will be capped at
  this level.
* This value affects all methods of result inclusion by email alert: inline,
  CSV and PDF.
* Note that this setting is affected globally by "maxresults" in the [email]
  stanza of alert_actions.conf.
* Defaults to 10000

action.email.include.results_link = [1|0]
* Specify whether to include a link to search results in the
  alert notification email.
* Defaults to 1 (or whatever is set in alert_actions.conf).

action.email.include.search = [1|0]
* Specify whether to include the query whose results triggered the email.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.include.trigger = [1|0]
* Specify whether to include the alert trigger condition.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.include.trigger_time = [1|0]
* Specify whether to include the alert trigger time.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.include.view_link = [1|0]
* Specify whether to include saved search title and a link for editing
  the saved search.
* Defaults to 1 (or whatever is set in alert_actions.conf).

action.email.inline = [1|0]
* Specify whether to include search results in the body of the
  alert notification email.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.sendcsv = [1|0]
* Specify whether to send results as a CSV file.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.sendpdf = [1|0]
* Specify whether to send results as a PDF file.
* Defaults to 0 (or whatever is set in alert_actions.conf).

action.email.sendresults = [1|0]
* Specify whether to include search results in the
  alert notification email.
* Defaults to 0 (or whatever is set in alert_actions.conf).


#******
# Settings for script action
#******

action.script = 0 | 1
* Enables or disables the script action.
* 1 to enable, 0 to disable.
* Defaults to 0

action.script.filename = <script filename>
* The filename, with no path, of the shell script to execute.
* The script should be located in: $SPLUNK_HOME/bin/scripts/
* For system shell scripts on Unix, or .bat or .cmd on windows, there
  are no further requirements.
* For other types of scripts, the first line should begin with a #!
  marker, followed by a path to the interpreter that will run the
  script.
  * Example: #!C:\Python27\python.exe
* Defaults to empty string.

#******
# Settings for lookup action
#******

action.lookup = 0 | 1
* Enables or disables the lookup action.
* 1 to enable, 0 to disable.
* Defaults to 0

action.lookup.filename = <lookup filename>
* Provide the name of the CSV lookup file to write search results to. Do not provide a filepath.
* Lookup actions can only be applied to CSV lookups.

action.lookup.append = 0 | 1
* Specify whether to append results to the lookup file defined for the action.lookup.filename attribute.
* Defaults to 0.

#*******
# Settings for summary index action
#*******

action.summary_index = 0 | 1
* Enables or disables the summary index action.
* Defaults to 0.

action.summary_index._name = <index>
* Specifies the name of the summary index where the results of the scheduled
  search are saved.
* Defaults to summary.

action.summary_index.inline = <bool>
* Determines whether to execute the summary indexing action as part of the
  scheduled search.
* NOTE: This option is considered only if the summary index action is enabled
  and is always executed (in other words, if counttype = always).
* Defaults to true.

action.summary_index.<field> = <string>
* Specifies a field/value pair to add to every event that gets summary indexed
  by this search.
* You can define multiple field/value pairs for a single summary index search.


#*******
# Settings for lookup table population parameters
#*******

action.populate_lookup = 0 | 1
* Enables or disables the lookup population action.
* Defaults to 0.

action.populate_lookup.dest = <string>
* Can be one of the following two options:
  * A lookup name from transforms.conf. The lookup name cannot be associated with KV store.
  * A path to a lookup .csv file that Splunk should copy the search results to,
    relative to $SPLUNK_HOME.
    * NOTE: This path must point to a .csv file in either of the following
            directories:
      * etc/system/lookups/
      * etc/apps/<app-name>/lookups
      * NOTE: the destination directories of the above files must already exist
* Defaults to empty string.

run_on_startup = true | false
* Toggles whether this search runs when Splunk starts or any edit that changes
  search related args happen (which includes: search and dispatch.* args).
* If set to true the search is ran as soon as possible during startup or after
  edit otherwise the search is ran at the next scheduled time.
* We recommend that you set run_on_startup to true for scheduled searches that
  populate lookup tables or generate artifacts used by dashboards.
* Defaults to false.

run_n_times = <unsigned int>
* Runs this search exactly the given number of times, then never again (until
  Splunk is restarted).
* Defaults to 0 (infinite).


#*******
# dispatch search options
#*******

dispatch.ttl = <integer>[p]
* Indicates the time to live (in seconds) for the artifacts of the scheduled
  search, if no actions are triggered.
* If the integer is followed by the letter 'p' Splunk interprets the ttl as a
  multiple of the scheduled search's execution period (e.g. if the search is
  scheduled to run hourly and ttl is set to 2p the ttl of the artifacts will be
  set to 2 hours).
* If an action is triggered Splunk changes the ttl to that action's ttl. If
  multiple actions are triggered, Splunk applies the largest action ttl to the
  artifacts. To set the action's ttl, refer to alert_actions.conf.spec.
* For more info on search's ttl please see limits.conf.spec [search] ttl
* Defaults to 2p (that is, 2 x the period of the scheduled search).

dispatch.buckets  = <integer>
* The maximum number of timeline buckets.
* Defaults to 0.

dispatch.max_count = <integer>
* The maximum number of results before finalizing the search.
* Defaults to 500000.

dispatch.max_time = <integer>
* Indicates the maximum amount of time (in seconds) before finalizing the
  search.
* Defaults to 0.

dispatch.lookups = 1| 0
* Enables or disables lookups for this search.
* Defaults to 1.

dispatch.earliest_time = <time-str>
* Specifies the earliest time for this search. Can be a relative or absolute
  time.
* If this value is an absolute time, use the dispatch.time_format to format the
  value.
* Defaults to empty string.

dispatch.latest_time = <time-str>
* Specifies the latest time for this saved search. Can be a relative or
  absolute time.
* If this value is an absolute time, use the dispatch.time_format to format the
  value.
* Defaults to empty string.

dispatch.index_earliest= <time-str>
* Specifies the earliest index time for this search. Can be a relative or
  absolute time.
* If this value is an absolute time, use the dispatch.time_format to format the
  value.
* Defaults to empty string.

dispatch.index_latest= <time-str>
* Specifies the latest index time for this saved search. Can be a relative or
  absolute time.
* If this value is an absolute time, use the dispatch.time_format to format the
  value.
* Defaults to empty string.

dispatch.time_format = <time format str>
* Defines the time format that Splunk uses to specify the earliest and latest
  time.
* Defaults to %FT%T.%Q%:z

dispatch.spawn_process = 1 | 0
* Specifies whether Splunk spawns a new search process when this saved search
  is executed.
* Default is 1.

dispatch.auto_cancel = <int>
* If specified, the job automatically cancels after this many seconds of
  inactivity. (0 means never auto-cancel)
* Default is 0.

dispatch.auto_pause = <int>
* If specified, the search job pauses after this many seconds of inactivity. (0
  means never auto-pause.)
* To restart a paused search job, specify unpause as an action to POST
  search/jobs/{search_id}/control.
* auto_pause only goes into effect once. Unpausing after auto_pause does not
  put auto_pause into effect again.
* Default is 0.

dispatch.reduce_freq = <int>
* Specifies how frequently Splunk should run the MapReduce reduce phase on
  accumulated map values.
* Defaults to 10.

dispatch.rt_backfill = <bool>
* Specifies whether to do real-time window backfilling for scheduled real time
  searches
* Defaults to false.

dispatch.indexedRealtime = <bool>
* Specifies whether to use indexed-realtime mode when doing realtime searches.
* Overrides the setting in the limits.conf file for the indexed_realtime_use_by_default
  attribute in the [realtime] stanza.
* This setting applies to each job.
* See the [realtime] stanza in the limits.conf.spec file for more information.
* Defaults to the value in the limits.conf file.

dispatch.indexedRealtimeOffset = <int>
* Controls the number of seconds to wait for disk flushes to finish.
* Overrides the setting in the limits.conf file for the indexed_realtime_disk_sync_delay
  attribute in the [realtime] stanza.
* This setting applies to each job.
* See the [realtime] stanza in the limits.conf.spec file for more information.
* Defaults to the value in the limits.conf file.

dispatch.indexedRealtimeMinSpan = <int>
* Minimum seconds to wait between component index searches.
* Overrides the setting in the limits.conf file for the indexed_realtime_default_span
  attribute in the [realtime] stanza.
* This setting applies to each job.
* See the [realtime] stanza in the limits.conf.spec file for more information.
* Defaults to the value in the limits.conf file.

dispatch.rt_maximum_span = <int>
* The max seconds allowed to search data which falls behind realtime.
* Use this setting to set a limit, after which events are not longer considered for the result set.  
  The search catches back up to the specified delay from realtime and uses the default span.
* Overrides the setting in the limits.conf file for the indexed_realtime_maximum_span
  attribute in the [realtime] stanza.
* This setting applies to each job.
* See the [realtime] stanza in the limits.conf.spec file for more information.
* Defaults to the value in the limits.conf file.

dispatch.sample_ratio = <int>
* The integer value used to calculate the sample ratio. The formula is 1 / <int>.
* The sample ratio specifies the likelihood of any event being included in the sample.
* For example, if sample_ratio = 500 each event has a 1/500 chance of being included in the sample result set.
* Defaults to 1.

restart_on_searchpeer_add = 1 | 0
* Specifies whether to restart a real-time search managed by the scheduler when
  a search peer becomes available for this saved search.
* NOTE: The peer can be a newly added peer or a peer that has been down and has
        become available.
* Defaults to 1.


#*******
# auto summarization options
#*******
auto_summarize  = <bool>
* Whether the scheduler should ensure that the data for this search is
  automatically summarized
* Defaults to false.

auto_summarize.command = <string>
* A search template to be used to construct the auto summarization for this
  search.
* DO NOT change unless you know what you're doing

auto_summarize.timespan = <time-specifier> (, <time-specifier>)*
* Comma delimited list of time ranges that each summarized chunk should span.
  This comprises the list of available granularity levels for which summaries
  would be available. For example a timechart over the last month whose
  granularity is at the day level should set this to 1d. If you are going to need
  the same data summarized at the hour level because you need to have weekly
  charts then use: 1h;1d

auto_summarize.cron_schedule = <cron-string>
* Cron schedule to be used to probe/generate the summaries for this search

auto_summarize.dispatch.<arg-name> = <string>
* Any dispatch.* options that need to be overridden when running the summary
  search.

auto_summarize.suspend_period      = <time-specifier>
* Amount of time to suspend summarization of this search if the summarization
  is deemed unhelpful
* Defaults to 24h

auto_summarize.max_summary_size     = <unsigned int>
* The minimum summary size when to start testing it's helpfulness
* Defaults to 52428800 (5MB)

auto_summarize.max_summary_ratio    = <positive float>
* The maximum ratio of summary_size/bucket_size when to stop summarization and
  deem it unhelpful for a bucket
* NOTE: the test is only performed if the summary size is larger
  than auto_summarize.max_summary_size
* Defaults to: 0.1

auto_summarize.max_disabled_buckets = <unsigned int>
* The maximum number of buckets with the suspended summarization before the
  summarization search is completely stopped and the summarization of the
  search is suspended for auto_summarize.suspend_period
* Defaults to: 2

auto_summarize.max_time = <unsigned int>
* The maximum amount of time that the summary search is allowed to run. Note
  that this is an approximate time and the summarize search will be stopped at
  clean bucket boundaries.
* Defaults to: 3600

auto_summarize.hash = <string>
auto_summarize.normalized_hash = <string>
* These are auto generated settings.

auto_summarize.max_concurrent = <unsigned int>
* The maximum number of concurrent instances of this auto summarizing search,
  that the scheduler is allowed to run.
* Defaults to: 1

#*******
# alert suppression/severity/expiration/tracking/viewing settings
#*******

alert.suppress = 0 | 1
* Specifies whether alert suppression is enabled for this scheduled search.
* Defaults to 0.

alert.suppress.period = <time-specifier>
* Sets the suppression period. Use [number][time-unit] to specify a time.
* For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour etc
* Honored if and only if alert.suppress = 1
* Defaults to empty string.

alert.suppress.fields = <comma-delimited-field-list>
* List of fields to use when suppressing per-result alerts. This field *must*
  be specified if the digest mode is disabled and suppression is enabled.
* Defaults to empty string.

alert.severity = <int>
* Sets the alert severity level.
* Valid values are: 1-debug, 2-info, 3-warn, 4-error, 5-severe, 6-fatal
* Defaults to 3.

alert.expires = <time-specifier>
* Sets the period of time to show the alert in the dashboard. Use [number][time-unit]
  to specify a time.
* For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour etc
* Defaults to 24h.
* This property is valid until splunkd restarts. Restart clears the listing of
  triggered alerts.

alert.digest_mode = true | false
* Specifies whether Splunk applies the alert actions to the entire result set
  or on each individual result.
* Defaults to true.

alert.track = true | false | auto
* Specifies whether to track the actions triggered by this scheduled search.
* auto  - determine whether to track or not based on the tracking setting of
  each action, do not track scheduled searches that always trigger actions.
* true  - force alert tracking.
* false - disable alert tracking for this search.
* Defaults to auto.

alert.display_view = <string>
* Name of the UI view where the emailed link for per result alerts should point to.
* If not specified, the value of request.ui_dispatch_app will be used, if that
  is missing then "search" will be used
* Defaults to empty string

alert.managedBy = <string>
* Specifies the feature/component that created the alert.
* Defaults to empty string.


#*******
# UI-specific settings
#*******

displayview =<string>
* Defines the default UI view name (not label) in which to load the results.
* Accessibility is subject to the user having sufficient permissions.
* Defaults to empty string.

vsid = <string>
* Defines the viewstate id associated with the UI view listed in 'displayview'.
* Must match up to a stanza in viewstates.conf.
* Defaults to empty string.

is_visible = true | false
* Specifies whether this saved search should be listed in the visible saved
  search list within apps.
* Saved searches are still visible when accessing the "Searches, reports,
  and alerts" page in Splunk Web.
* Defaults to true.

description = <string>
* Human-readable description of this saved search.
* Defaults to empty string.

request.ui_dispatch_app  = <string>
* Specifies a field used by Splunk UI to denote the app this search should be
  dispatched in.
* Defaults to empty string.

request.ui_dispatch_view = <string>
* Specifies a field used by Splunk UI to denote the view this search should be
  displayed in.
* Defaults to empty string.

#******
# Display Formatting Options
#******

# General options
display.general.enablePreview = 0 | 1
display.general.type = [events|statistics|visualizations]
display.general.timeRangePicker.show = 0 | 1
display.general.migratedFromViewState = 0 | 1
display.general.locale = <string>

# Event options
display.events.fields = [<string>(, <string>)*]
display.events.type = [raw|list|table]
display.events.rowNumbers = 0 | 1
display.events.maxLines = <int>
display.events.raw.drilldown = [inner|outer|full|none]
display.events.list.drilldown = [inner|outer|full|none]
display.events.list.wrap = 0 | 1
display.events.table.drilldown = 0 | 1
display.events.table.wrap = 0 | 1

# Statistics options
display.statistics.rowNumbers = 0 | 1
display.statistics.wrap = 0 | 1
display.statistics.overlay = [none|heatmap|highlow]
display.statistics.drilldown = [row|cell|none]
display.statistics.totalsRow = 0 | 1
display.statistics.percentagesRow = 0 | 1
display.statistics.show = 0 | 1

# Visualization options
display.visualizations.trellis.enabled = 0 | 1
display.visualizations.trellis.scales.shared = 0 | 1
display.visualizations.trellis.size = [small|medium|large]
display.visualizations.trellis.splitBy = <string>
display.visualizations.show = 0 | 1
display.visualizations.type = [charting|singlevalue|mapping|custom]
display.visualizations.chartHeight = <int>
display.visualizations.charting.chart = [line|area|column|bar|pie|scatter|bubble|radialGauge|fillerGauge|markerGauge]
display.visualizations.charting.chart.stackMode = [default|stacked|stacked100]
display.visualizations.charting.chart.nullValueMode = [gaps|zero|connect]
display.visualizations.charting.chart.overlayFields = <string>
display.visualizations.charting.drilldown = [all|none]
display.visualizations.charting.chart.style = [minimal|shiny]
display.visualizations.charting.layout.splitSeries = 0 | 1
display.visualizations.charting.layout.splitSeries.allowIndependentYRanges = 0 | 1
display.visualizations.charting.legend.mode = [standard|seriesCompare]
display.visualizations.charting.legend.placement = [right|bottom|top|left|none]
display.visualizations.charting.legend.labelStyle.overflowMode = [ellipsisEnd|ellipsisMiddle|ellipsisStart]
display.visualizations.charting.axisTitleX.text = <string>
display.visualizations.charting.axisTitleY.text = <string>
display.visualizations.charting.axisTitleY2.text = <string>
display.visualizations.charting.axisTitleX.visibility = [visible|collapsed]
display.visualizations.charting.axisTitleY.visibility = [visible|collapsed]
display.visualizations.charting.axisTitleY2.visibility = [visible|collapsed]
display.visualizations.charting.axisX.scale = linear|log
display.visualizations.charting.axisY.scale = linear|log
display.visualizations.charting.axisY2.scale = linear|log|inherit
display.visualizations.charting.axisX.abbreviation = none|auto
display.visualizations.charting.axisY.abbreviation = none|auto
display.visualizations.charting.axisY2.abbreviation = none|auto
display.visualizations.charting.axisLabelsX.majorLabelStyle.overflowMode = [ellipsisMiddle|ellipsisNone]
display.visualizations.charting.axisLabelsX.majorLabelStyle.rotation = [-90|-45|0|45|90]
display.visualizations.charting.axisLabelsX.majorUnit = <float> | auto
display.visualizations.charting.axisLabelsY.majorUnit = <float> | auto
display.visualizations.charting.axisLabelsY2.majorUnit = <float> | auto
display.visualizations.charting.axisX.minimumNumber = <float> | auto
display.visualizations.charting.axisY.minimumNumber = <float> | auto
display.visualizations.charting.axisY2.minimumNumber = <float> | auto
display.visualizations.charting.axisX.maximumNumber = <float> | auto
display.visualizations.charting.axisY.maximumNumber = <float> | auto
display.visualizations.charting.axisY2.maximumNumber = <float> | auto
display.visualizations.charting.axisY2.enabled = 0 | 1
display.visualizations.charting.chart.sliceCollapsingThreshold = <float>
display.visualizations.charting.chart.showDataLabels = [all|none|minmax]
display.visualizations.charting.gaugeColors = [<hex>(, <hex>)*]
display.visualizations.charting.chart.rangeValues = [<string>(, <string>)*]
display.visualizations.charting.chart.bubbleMaximumSize = <int>
display.visualizations.charting.chart.bubbleMinimumSize = <int>
display.visualizations.charting.chart.bubbleSizeBy = [area|diameter]
display.visualizations.charting.fieldDashStyles = <string>
display.visualizations.charting.lineWidth = <float>
display.visualizations.custom.drilldown = [all|none]
display.visualizations.custom.height = <int>
display.visualizations.custom.type = <string>
display.visualizations.singlevalueHeight = <int>
display.visualizations.singlevalue.beforeLabel = <string>
display.visualizations.singlevalue.afterLabel = <string>
display.visualizations.singlevalue.underLabel = <string>
display.visualizations.singlevalue.unit = <string>
display.visualizations.singlevalue.unitPosition = [before|after]
display.visualizations.singlevalue.drilldown = [all|none]
display.visualizations.singlevalue.colorMode = [block|none]
display.visualizations.singlevalue.rangeValues = [<string>(, <string>)*]
display.visualizations.singlevalue.rangeColors = [<string>(, <string>)*]
display.visualizations.singlevalue.trendInterval = <string>
display.visualizations.singlevalue.trendColorInterpretation = [standard|inverse]
display.visualizations.singlevalue.showTrendIndicator = 0 | 1
display.visualizations.singlevalue.showSparkline = 0 | 1
display.visualizations.singlevalue.trendDisplayMode = [percent|absolute]
display.visualizations.singlevalue.colorBy = [value|trend]
display.visualizations.singlevalue.useColors = 0 | 1
display.visualizations.singlevalue.numberPrecision = [0|0.0|0.00|0.000|0.0000]
display.visualizations.singlevalue.useThousandSeparators = 0 | 1
display.visualizations.mapHeight = <int>
display.visualizations.mapping.type = [marker|choropleth]
display.visualizations.mapping.drilldown = [all|none]
display.visualizations.mapping.map.center = (<float>,<float>)
display.visualizations.mapping.map.zoom = <int>
display.visualizations.mapping.map.scrollZoom = 0 | 1
display.visualizations.mapping.map.panning    = 0 | 1
display.visualizations.mapping.choroplethLayer.colorMode = [auto|sequential|divergent|categorical]
display.visualizations.mapping.choroplethLayer.maximumColor = <string>
display.visualizations.mapping.choroplethLayer.minimumColor = <string>
display.visualizations.mapping.choroplethLayer.colorBins = <int>
display.visualizations.mapping.choroplethLayer.neutralPoint = <float>
display.visualizations.mapping.choroplethLayer.shapeOpacity = <float>
display.visualizations.mapping.choroplethLayer.showBorder = 0 | 1
display.visualizations.mapping.markerLayer.markerOpacity = <float>
display.visualizations.mapping.markerLayer.markerMinSize = <int>
display.visualizations.mapping.markerLayer.markerMaxSize = <int>
display.visualizations.mapping.legend.placement = [bottomright|none]
display.visualizations.mapping.data.maxClusters = <int>
display.visualizations.mapping.showTiles = 0 | 1
display.visualizations.mapping.tileLayer.tileOpacity = <float>
display.visualizations.mapping.tileLayer.url = <string>
display.visualizations.mapping.tileLayer.minZoom = <int>
display.visualizations.mapping.tileLayer.maxZoom = <int>

# Patterns options
display.page.search.patterns.sensitivity = <float>

# Page options
display.page.search.mode = [fast|smart|verbose]
* This setting has no effect on saved search execution when dispatched by the
  scheduler. It only comes into effect when the search is opened in the UI and
  run manually.

display.page.search.timeline.format = [hidden|compact|full]
display.page.search.timeline.scale = [linear|log]
display.page.search.showFields = 0 | 1
display.page.search.tab = [events|statistics|visualizations|patterns]
# Deprecated
display.page.pivot.dataModel = <string>

#*******
# Table format settings
#*******

# Format options
display.statistics.format.<index> = [color|number]
display.statistics.format.<index>.field = <string>
display.statistics.format.<index>.fields = [<string>(, <string>)*]

# Color format options
display.statistics.format.<index>.scale = [category|linear|log|minMidMax|sharedCategory|threshold]
display.statistics.format.<index>.colorPalette = [expression|list|map|minMidMax|sharedList]

# Number format options
display.statistics.format.<index>.precision = <int>
display.statistics.format.<index>.useThousandSeparators = <bool>
display.statistics.format.<index>.unit = <string>
display.statistics.format.<index>.unitPosition = [before|after]

# Scale options for 'category'
display.statistics.format.<index>.scale.categories = [<string>(, <string>)*]

# Scale options for 'log'
display.statistics.format.<index>.scale.base = <int>

# Scale options for 'minMidMax'
display.statistics.format.<index>.scale.minType = [number|percent|percentile]
display.statistics.format.<index>.scale.minValue = <float>
display.statistics.format.<index>.scale.midType = [number|percent|percentile]
display.statistics.format.<index>.scale.midValue = <float>
display.statistics.format.<index>.scale.maxType = [number|percent|percentile]
display.statistics.format.<index>.scale.maxValue = <float>

# Scale options for 'threshold'
display.statistics.format.<index>.scale.thresholds = [<float>(, <float>)*]

# Color palette options for 'expression'
display.statistics.format.<index>.colorPalette.rule = <string>

# Color palette options for 'list'
display.statistics.format.<index>.colorPalette.colors = [<hex>(, <hex>)*]
display.statistics.format.<index>.colorPalette.interpolate = <bool>

# Color palette options for 'map'
display.statistics.format.<index>.colorPalette.colors = {<string>:<hex>(, <string>:<hex>)*}

# Color palette options for 'minMidMax'
display.statistics.format.<index>.colorPalette.minColor = <hex>
display.statistics.format.<index>.colorPalette.midColor = <hex>
display.statistics.format.<index>.colorPalette.maxColor = <hex>

#*******
# Other settings
#*******

embed.enabled = 0 | 1
* Specifies whether a saved search is shared for access with a guestpass.
* Search artifacts of a search can be viewed via a guestpass only if:
  * A token has been generated that is associated with this saved search.
    The token is associated with a particular user and app context.
  * The user to whom the token belongs has permissions to view that search.
  * The saved search has been scheduled and there are artifacts available.
    Only artifacts are available via guestpass: we never dispatch a search.
  * The save search is not disabled, it is scheduled, it is not real-time,
    and it is not an alert.

defer_scheduled_searchable_idxc = <bool>
* Specifies whether to defer a continuous saved search during a searchable rolling restart or searchable rolling upgrade of an indexer cluster.
* Note: When disabled, a continuous saved search might return partial results.
* Defaults: true (enabled).

#*******
# deprecated settings
#*******

sendresults = <bool>
* use action.email.sendresult

action_rss = <bool>
* use action.rss

action_email = <string>
* use action.email and action.email.to

role = <string>
* see saved search permissions

userid = <string>
* see saved search permissions

query  = <string>
* use search

nextrun  = <int>
* not used anymore, the scheduler maintains this info internally

qualifiedSearch = <string>
* not used anymore, the Splunk software computes this value during runtime
