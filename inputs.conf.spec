#   Version 7.1.1

# This file contains possible settings you can use to configure inputs,
# distributed inputs such as forwarders, and file system monitoring in
# inputs.conf.
#
# There is an inputs.conf in $SPLUNK_HOME/etc/system/default/.  To set custom
# configurations, place an inputs.conf in $SPLUNK_HOME/etc/system/local/.  For
# examples, see inputs.conf.example. You must restart Splunk to enable new
# configurations.
#
# To learn more about configuration files (including precedence), see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles
#

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top of
#     the file.
#   * Each conf file should have at most one default stanza. If there are
#     multiple default stanzas, settings are combined. In the case of
#     multiple definitions of the same setting, the last definition in the
#     file wins.
#   * If an setting is defined at both the global level and in a specific
#   stanza, the value in the specific stanza takes precedence.

#*******
# GENERAL SETTINGS:
# The following settings are valid for all input types (except file system
# change monitor, which is described in a separate section in this file).
# You must first enter a stanza header in square brackets, specifying the input
# type. See further down in this file for examples.
# Then, use any of the following settings.
#
# To specify global settings for Windows Event Log inputs, place them in
# the [WinEventLog] global stanza as well as the [default] stanza.
#*******

host = <string>
* Sets the host key/field to a static value for this stanza.
* Primarily used to control the host field, which the input applies to events
  that come in through this input stanza.
* Detail: Sets the host key initial value. The input uses this key during
  parsing/indexing, in particular to set the host field. It also uses this
  field at search time.
* As a convenience, the input prepends the chosen string with 'host::'.
* WARNING: Do not put the <string> value in quotes. Use host=foo, not host="foo".
* If set to '$decideOnStartup', will be interpreted as hostname of executing
  machine; this will occur on each splunkd startup.
* If you run multiple instances of the software on the same system (hardware
  or virtual machine), choose unique values for 'host' to differentiate
  your data, e.g. myhost-sh-1 or myhost-idx-2.
* The literal default conf value is $decideOnStartup, but at installation
  time, the setup logic adds the local hostname as determined by DNS to the
  $SPLUNK_HOME/etc/system/local/inputs.conf default stanza, which is the
  effective default value.
* If you remove the 'host' setting from $SPLUNK_HOME/etc/system/local/inputs.conf
  or remove $SPLUNK_HOME/etc/system/local/inputs.conf, the setting changes to
  '$decideOnStartup'. Apps that need a resolved host value should use the
  'host_resolved' property in the response for the REST 'GET' call of the input source.
  This property is set to the hostname of the local Splunk instance. It is a read only 
  property that is not written to inputs.conf.

index = <string>
* Sets the index to store events from this input.
* Primarily used to specify the index to store events coming in via this input
  stanza.
* Detail: Sets the index key's initial value. The key is used when selecting an
  index to store the events.
* Defaults to "main" (or whatever you have set as your default index).

source = <string>
* Sets the source key/field for events from this input.
* NOTE: Overriding the source key is generally not recommended. Typically, the
  input layer will provide a more accurate string to aid problem
  analysis and investigation, accurately recording the file from which the data
  was retrieved.  Please consider use of source types, tagging, and search
  wildcards before overriding this value.
* Detail: Sets the source key's initial value. The key is used during
  parsing/indexing, in particular to set the source field during
  indexing.  It is also the source field used at search time.
* As a convenience, the chosen string is prepended with 'source::'.
* WARNING: Do not quote the <string> value: source=foo, not source="foo".
* Defaults to the input file path.

sourcetype = <string>
* Sets the sourcetype key/field for events from this input.
* Primarily used to explicitly declare the source type for this data, as
  opposed to allowing it to be determined via automated methods.  This is
  typically important both for searchability and for applying the relevant
  configuration for this type of data during parsing and indexing.
* Detail: Sets the sourcetype key's initial value. The key is used during
  parsing/indexing, in particular to set the source type field during
  indexing. It is also the source type field used at search time.
* As a convenience, the chosen string is prepended with 'sourcetype::'.
* WARNING: Do not quote the <string> value: sourcetype=foo, not sourcetype="foo".
* If unset, Splunk picks a source type based on various aspects of the data.
  There is no hard-coded default.

queue = [parsingQueue|indexQueue]
* Specifies where the input processor should deposit the events it reads.
* Set queue to "parsingQueue" to apply props.conf and other parsing rules to
  your data. For more information about props.conf and rules for timestamping
  and linebreaking, refer to props.conf and the online documentation at
  http://docs.splunk.com/Documentation.
* Set queue to "indexQueue" to send your data directly into the index.
* Defaults to parsingQueue.

# Pipeline Key defaulting.

* Pipeline keys in general can be defaulted in inputs stanzas.
* The list of user-available modifiable pipeline keys is described in
  transforms.conf.spec; see transforms.conf.spec for further information on
  these keys.
* The currently-defined keys which are available literally in inputs stanzas
  are as follows:

queue = <value>
_raw = <value>
_meta = <value>
_time = <value>
* Inputs have special support for mapping host, source, sourcetype, and index
  to their metadata names such as host -> Metadata:Host
* Defaulting these values is not recommended, and is
  generally only useful as a workaround to other product issues.
* Defaulting these keys in most cases will override the default behavior of
  input processors; but this behavior is not guaranteed in all cases.
* Values defaulted here, as with all values provided by inputs, can be
  altered by transforms at parse-time.

# ***********
# This section contains options for routing data using inputs.conf rather than
# outputs.conf.
# Note concerning routing via inputs.conf:
# This is a simplified set of routing options you can use as data comes in.
# For more flexible options or details on configuring required or optional
# settings, see outputs.conf.spec.

_TCP_ROUTING = <tcpout_group_name>,<tcpout_group_name>,<tcpout_group_name>, ...
* Comma-separated list of tcpout group names.
* Using this, you can selectively forward the data to specific indexer(s).
* Specify the tcpout group the forwarder should use when forwarding the data.
  The tcpout group names are defined in outputs.conf with
  [tcpout:<tcpout_group_name>].
* Defaults to groups specified in "defaultGroup" in [tcpout] stanza in
  outputs.conf.
* To forward data to all tcpout group names that have been defined in
  outputs.conf, set to '*' (asterisk).
* To forward data from the "_internal" index, _TCP_ROUTING must explicitly be
  set to either "*" or a specific splunktcp target group.

_SYSLOG_ROUTING = <syslog_group_name>,<syslog_group_name>,<syslog_group_name>, ...
* Comma-separated list of syslog group names.
* Using this, you can selectively forward the data to specific destinations as
  syslog events.
* Specify the syslog group to use when forwarding the data.
  The syslog group names are defined in outputs.conf with
  [syslog:<syslog_group_name>].
* Defaults to groups present in "defaultGroup" in [syslog] stanza in
  outputs.conf.
* The destination host must be configured in outputs.conf, using
  "server=[<ip>|<servername>]:<port>".

_INDEX_AND_FORWARD_ROUTING = <string>
* Only has effect if using selectiveIndexing feature in outputs.conf.
* If set for any input stanza, should cause all data coming from that input
  stanza to be labeled with this setting.
* When selectiveIndexing is in use on a forwarder:
  * data without this label will not be indexed by that forwarder.
  * data with this label will be indexed in addition to any forwarding.
* This setting does not actually cause data to be forwarded or not forwarded in
  any way, nor does it control where the data is forwarded in multiple-forward
  path cases.
* Defaults to not present.

#************
# Blacklist
#************

[blacklist:<path>]
* Protect files on the file system from being indexed or previewed.
* The input treats a file as blacklisted if the file starts with any of the
  defined blacklisted <paths>.
* Blacklisting of a file with the specified path occurs even if a monitor 
  stanza defines a whitelist that matches the file path.
* The preview endpoint will return an error when asked to preview a
  blacklisted file.
* The oneshot endpoint and command will also return an error.
* When a blacklisted file is monitored (monitor:// or batch://), filestatus
  endpoint will show an error.
* For fschange with the 'sendFullEvent' option enabled, contents of
  blacklisted files will not be indexed.

#*******
# Valid input types follow, along with their input-specific settings:
#*******


#*******
# MONITOR:
#*******

[monitor://<path>]
* This directs a file monitor input to watch all files in <path>.
* <path> can be an entire directory or a single file.
* You must specify the input type and then the path, so put three slashes in
  your path if you are starting at the root on *nix systems (to include the
  slash that indicates an absolute path).

# Additional settings:

host_regex = <regular expression>
* If specified, <regular expression> extracts host from the path to the file
  for each input file.
    * Detail: This feature examines the source key; if source is set
      explicitly in the stanza, that string will be matched, not the original
      filename.
* Specifically, the first group of the regex is used as the host.
* If the regex fails to match, the default "host =" setting is used.
* If host_regex and host_segment are both set, the input ignores host_regex.
* Defaults to unset.

host_segment = <integer>
* If set to N, the Nth "/"-separated segment of the path is set as host. If
  host_segment=3, for example, the third segment is used.
* If the value is not an integer or is less than 1, the default "host ="
  setting is used.
* On Windows machines, the drive letter and colon before the backslash count 
  as one segment.
    * For example, if you set host_segment=3 and the monitor path is 
      D:\logs\servers\host01, Splunk software sets the host as "servers" because
      that is the third segment.
* Defaults to unset.

whitelist = <regular expression>
* If set, files from this input are monitored only if their path matches the
  specified regex.
* Takes precedence over the deprecated _whitelist setting, which functions
  the same way.

blacklist = <regular expression>
* If set, files from this input are NOT monitored if their path matches the
  specified regex.
* Takes precedence over the deprecated _blacklist setting, which functions
  the same way.
* If a file matches the regexes in both the blacklist and whitelist settings,
  the file is NOT monitored. Blacklists take precedence over whitelists.

Note concerning wildcards and monitor:
* You can use wildcards to specify your input path for monitored input. Use
  "..." for recursive directory matching and "*" for wildcard matching in a
  single directory segment.
* "..." recurses through directories. This means that /foo/.../bar will match
  foo/1/bar, foo/1/2/bar, etc.
* You can use multiple "..." specifications in a single input path. For
  example: /foo/.../bar/...
* The asterisk (*) matches anything in a single path segment; unlike "...", it
  does not recurse. For example, /foo/*/bar matches the files
  /foo/1/bar, /foo/2/bar, etc. However, it does not match
  /foo/bar or /foo/1/2/bar.
  A second example: /foo/m*r/bar matches /foo/mr/bar, /foo/mir/bar,
  /foo/moor/bar, etc.
* You can combine "*" and "..." as needed: foo/.../bar/* matches any file in
  the bar directory within the specified path.

crcSalt = <string>
* Use this setting to force the input to consume files that have matching CRCs
  (cyclic redundancy checks).
    * (The input only performs CRC checks against, by default, the first 256
      bytes of a file. This behavior prevents the input from indexing the same
      file twice, even though you may have renamed it -- as, for example, with
      rolling log files. However, because the CRC is based on only the first
      few lines of the file, it is possible for legitimately different files
      to have matching CRCs, particularly if they have identical headers.)
* If set, <string> is added to the CRC.
* If set to the literal string <SOURCE> (including the angle brackets), the
  full directory path to the source file is added to the CRC. This ensures
  that each file being monitored has a unique CRC.   When crcSalt is invoked,
  it is usually set to <SOURCE>.
* Be cautious about using this setting with rolling log files; it could lead
  to the log file being re-indexed after it has rolled.
* In many situations, initCrcLength can be used to achieve the same goals.
* Defaults to empty.

initCrcLength = <integer>
* This setting adjusts how much of a file the input reads before trying to
  identify whether it is a file that has already been seen. You might want to
  adjust this if you have many files with common headers (comment headers,
  long CSV headers, etc) and recurring filenames.
* CAUTION: Improper use of this setting will cause data to be re-indexed.  You
  might want to consult with Splunk Support before adjusting this value - the
  default is fine for most installations.
* Defaults to 256 (bytes).
* Must be in the range 256-1048576.

ignoreOlderThan = <nonnegative integer>[s|m|h|d]
* The monitor input will compare the modification time on files it encounters
  with the current time.  If the time elapsed since the modification time
  is greater than this setting, it will be placed on the ignore list.
* Files placed on the ignore list will not be checked again for any
  reason until the Splunk software restarts, or the file monitoring subsystem
  is reconfigured.  This is true even if the file becomes newer again at a
  later time.
  * Reconfigurations occur when changes are made to monitor or batch
    inputs via the UI or command line.
* Use IgnoreOlderThan to increase file monitoring performance when
  monitoring a directory hierarchy containing many unchanging older
  files, and when removing or blacklisting those files from the monitoring
  location is not a reasonable option.
* Do NOT select a time that files you want to read could reach in
  age, even temporarily.  Take potential downtime into consideration!
  * Suggested value: 14d, which means 2 weeks
  * For example, a time window in significant numbers of days or small
    numbers of weeks are probably reasonable choices.
  * If you need a time window in small numbers of days or hours,
    there are other approaches to consider for performant monitoring
    beyond the scope of this one setting.
* NOTE: Most modern Windows file access APIs do not update file
  modification time while the file is open and being actively written to.
  Windows delays updating modification time until the file is closed.
  Therefore you might have to choose a larger time window on Windows
  hosts where files may be open for long time periods.
* Value must be: <number><unit>. For example, "7d" indicates one week.
* Valid units are "d" (days), "h" (hours), "m" (minutes), and "s"
  (seconds).
* Defaults to unset, meaning there is no threshold and no files are
  ignored for modification time reasons.

followTail = [0|1]
* WARNING: Use of followTail should be considered an advanced administrative
  action.
* Treat this setting as an 'action':
  * Enable this setting and start the Splunk software.
  * Wait enough time for the input to identify the related files.
  * Disable the setting and restart.
* DO NOT leave followTail enabled in an ongoing fashion.
* Do not use followTail for rolling log files (log files that get renamed as
  they age), or files whose names or paths vary.
* You can use this to force the input to skip past all current data for a
  given stanza.
  * In more detail: this is intended to mean that if you start the monitor
    with a stanza configured this way, all data in the file at the time it is
    first encountered will not be read. Only data that arrives after the first
    encounter time will be read.
  * This can be used to "skip over" data from old log files, or old portions of
    log files, to get started on current data right away.
* If set to 1, monitoring starts at the end of the file (like tail -f).
* If set to 0, monitoring starts at the beginning of the file.
* Defaults to 0.

alwaysOpenFile = [0|1]
* Opens a file to check whether it has already been indexed, by skipping the
  modification time/size checks.
* Only useful for files that do not update modification time or size.
* Only known to be needed when monitoring files on Windows, mostly for
  Internet Information Server logs.
* This flag should only be used as a last resort, as it increases load and
  slows down indexing.
* Defaults to 0.

time_before_close = <integer>
* Modification time delta required before the file monitor can close a file on
  EOF.
* Tells the system not to close files that have been updated in past <integer>
  seconds.
* Defaults to 3.

multiline_event_extra_waittime = [true|false]
* By default, the file monitor sends an event delimiter when:
  * It reaches EOF of a file it monitors and
  * Ihe last character it reads is a newline.
* In some cases, it takes time for all lines of a multiple-line event to
  arrive.
* Set to true to delay sending an event delimiter until the time that the
  file monitor closes the file, as defined by the 'time_before_close' setting,
  to allow all event lines to arrive.
* Defaults to false.

recursive = [true|false]
* If false, the input will not monitor sub-directories that it finds within
  a monitored directory.
* Defaults to true.

followSymlink = [true|false]
* Whether or not to follow any symbolic links within a monitored directory.
* If set to false, the input ignores symbolic links found within a monitored
  directory.
* If set to true, the input follows symbolic links and monitor files at the
  symbolic link destination.
* Additionally, any whitelists or blacklists that the input stanza defines
  also apply to files at the symbolic link's destination.
* Defaults to true.

_whitelist = ...
* This setting is deprecated.
* It is still honored, unless the 'whitelist' setting also exists.

_blacklist = ...
* This setting is deprecated.
* It is still honored, unless the 'blacklist' setting also exists.

# dedicatedFD = ...
* This setting has been removed.  It is no longer needed.

#****************************************
# BATCH  ("Upload a file" in Splunk Web):
#****************************************

NOTE: Batch should only be used for large archives of historic data. If you
want to continuously monitor a directory or index small archives, use 'monitor'
(see above). 'batch' reads in the file and indexes it, and then deletes the
file on disk.

[batch://<path>]
* A one-time, destructive input of files in <path>.
* For continuous, non-destructive inputs of files, use 'monitor' instead.

# Additional settings:

move_policy = sinkhole
* IMPORTANT: This setting is required. You *must* include
  "move_policy = sinkhole" when you define batch inputs.
* This setting causes the input to load the file destructively.
* Do not use the 'batch' input type for files you do not want to delete after
  indexing.
* The "move_policy" setting exists for historical reasons, but remains as an
  explicit double check.  As an administrator you must very explicitly declare
  that you want the data in the monitored directory (and its sub-directories) to
  be deleted after being read and indexed.

host_regex = see MONITOR, above.
host_segment = see MONITOR, above.
crcSalt = see MONITOR, above.

# IMPORTANT: 'batch' inputs do not use the following setting:
# source = <string>

followSymlink = [true|false]
* Works similarly to the same setting for monitor, but does not delete files
  after following a symbolic link out of the monitored directory.

# The following settings work identically as for [monitor::] stanzas,
# documented above
host_regex = <regular expression>
host_segment = <integer>
crcSalt = <string>
recursive = [true|false]
whitelist = <regular expression>
blacklist = <regular expression>
initCrcLength = <integer>

#*******
# TCP:
#*******

[tcp://<remote server>:<port>]
* Configures the input to listen on a specific TCP network port.
* If a <remote server> makes a connection to this instance, this stanza is
  used to configure the input.
* If you do not specify <remote server>, this stanza matches all connections
  on the specified port.
* Generates events with source set to tcp:portnumber, for example: tcp:514
* If you do not specify a sourcetype, generates events with sourcetype
  set to tcp-raw.

# Additional settings:

connection_host = [ip|dns|none]
* "ip" sets the host to the IP address of the system sending the data.
* "dns" sets the host to the reverse DNS entry for the IP address of the system
  sending the data.
* "none" leaves the host as specified in inputs.conf, typically the splunk
  system hostname.
* Defaults to "dns".

queueSize = <integer>[KB|MB|GB]
* The maximum size of the in-memory input queue.
* Defaults to 500KB.

persistentQueueSize = <integer>[KB|MB|GB|TB]
* Maximum size of the persistent queue file.
* Defaults to 0 (no persistent queue).
* If set to some value other than 0, persistentQueueSize must be larger than
  the in-memory queue size (as defined by the 'queueSize' setting in
  inputs.conf or 'maxSize' settings in [queue] stanzas in server.conf).
* Persistent queues can help prevent loss of transient data. For information on
  persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
  interact, see the online documentation.
* Defaults to 0 (no persistent queue).

requireHeader = <bool>
* Require a header be present at the beginning of every stream.
* This header may be used to override indexing settings.
* Defaults to false.

listenOnIPv6 = <no | yes | only>
* Select whether the input listens on IPv4, IPv6, or both
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the input uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or addresses to accept connections from.
* Separate multiple rules with commas or spaces.
* Each rule can be in one of the following formats:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A Classless Inter-Domain Routing (CIDR) block of addresses
       (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard
       (examples: "myhost.example.com", "*.splunk.com")
    4. A single '*' which matches anything
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one that
  matches.
  For example, "!10.1/16, *" allows connections from everywhere except
  the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

rawTcpDoneTimeout = <seconds>
* Specifies timeout value for sending Done-key.
* If a connection over this port remains idle for more than
  'rawTcpDoneTimeout' seconds after receiving data, it adds a Done-key. This
  declares that the last event has been completely received.
* Defaults to 10 seconds.

[tcp:<port>]
* Configures the input listen on the specified TCP network port.
* This stanza is similar to [tcp://<remote server>:<port>], but listens for
  connections to the specified port from any host.
* Generates events with a source of tcp:<port>.
* If you do not specify a sourcetype, generates events with a source type of
  tcp-raw.
* This stanza supports the following settings:

connection_host = [ip|dns|none]
queueSize = <integer>[KB|MB|GB]
persistentQueueSize = <integer>[KB|MB|GB|TB]
requireHeader = <bool>
listenOnIPv6 = <no | yes | only>
acceptFrom = <network_acl> ...
rawTcpDoneTimeout = <seconds>

#*******
# Data distribution:
#*******

# Global settings for splunktcp. Used on the receiving side for data forwarded
# from a forwarder.

[splunktcp]
route = [has_key|absent_key:<key>:<queueName>;...]
* Settings for the light forwarder.
* The receiver sets these parameters automatically -- you DO NOT need to set
  them.
* The property route is composed of rules delimited by ';' (semicolon).
* The receiver checks each incoming data payload via cooked tcp port against
  the route rules.
* If a matching rule is found, the receiver sends the payload to the specified
  <queueName>.
* If no matching rule is found, the receiver sends the payload to the default
  queue specified by any queue= for this stanza. If no queue= key is set in
  the stanza or globally, the events will be sent to the parsingQueue.

enableS2SHeartbeat = [true|false]
* This specifies the global keepalive setting for all splunktcp ports.
* This option is used to detect forwarders which might have become unavailable
  due to network, firewall, or other problems.
* The receiver monitors each connection for presence of heartbeat, and if the
  heartbeat is not seen for s2sHeartbeatTimeout seconds, it closes the
  connection.
* Defaults to true (heartbeat monitoring enabled).

s2sHeartbeatTimeout = <seconds>
* This specifies the global timeout value for monitoring heartbeats.
* The receiver closes a forwarder connection if it does not receive
  a heartbeat for 's2sHeartbeatTimeout' seconds.
* Defaults to 600 seconds (10 minutes).

inputShutdownTimeout = <seconds>
* Used during shutdown to minimize data loss when forwarders are connected to a
  receiver.
* During shutdown, the tcp input processor waits for the specified number of
  seconds and then closes any remaining open connections. If, however, all
  connections close before the end of the timeout period, shutdown proceeds
  immediately, without waiting for the timeout.

stopAcceptorAfterQBlock = <seconds>
* Specifies the time, in seconds, to wait before closing the splunktcp port.
* If the receiver is unable to insert received data into the configured queue
  for more than the specified number of seconds, it closes the splunktcp port.
* This action prevents forwarders from establishing new connections to this
  receiver.
* Forwarders that have an existing connection will notice the port is closed
  upon test-connections and move to other receivers.
* Once the queue unblocks, and TCP Input can continue processing data, the
  receiver starts listening on the port again.
* This setting should not be adjusted lightly as extreme values can interact
  poorly with other defaults.
* Defaults to 300 (5 minutes).

listenOnIPv6 = no|yes|only
* Select whether this receiver listens on IPv4, IPv6, or both protocols.
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the input uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or IP addresses from which to accept connections.
* Specify multiple rules with commas or spaces.
* Each rule can be in the following forms:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A CIDR block of addresses (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard (examples:
       "myhost.example.com", "*.splunk.com")
    4. A single '*', which matches anything.
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one
  that matches. For example, "!10.1/16, *" allows connections from everywhere
  except the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

negotiateProtocolLevel = <unsigned integer>
* If set, allow forwarders that connect to this indexer (or specific port)
  to send data using only up to the specified feature level of the splunk
  forwarder protocol.
* If set to a lower value than the default will deny the use of newer
  forwarder protocol features during connection negotiation.  This may
  impact indexer efficiency.
* Defaults to 1 if negotiateNewProtocol is true, otherwise 0

negotiateNewProtocol = [true|false]
* Controls the default setting of negotiateProtocolLevel setting above
* DEPRECATED; set 'negotiateProtocolLevel' instead.
* Defaults to true.

concurrentChannelLimit = <unsigned integer>
* Each forwarder that connects to this indexer may use up to
  <concurrentChannelLimit> unique channel codes.
* In other words, each forwarder may have up to <concurrentChannelLimit>
  channels in flight concurrently.
* The receiver closes a forwarder connection if a forwarder attempts to exceed
  this value.
* This setting only applies when the new forwarder protocol is in use.
* Defaults to 300.

# Forwarder-specific settings for splunktcp.

[splunktcp://[<remote server>]:<port>]
* Receivers use this input stanza.
* This is the same as the [tcp://] stanza, except the remote server is assumed
  to be a Splunk instance, most likely a forwarder.
* <remote server> is optional. If you specify it, the receiver only listen for
  data from <remote server>.
  * Use of <remote server is not recommended. Use the 'acceptFrom' setting,
    which supersedes this setting.

connection_host = [ip|dns|none]
* For splunktcp, the host or connection_host will be used if the remote Splunk
  instance does not set a host, or if the host is set to "<host>::<localhost>".
* "ip" sets the host to the IP address of the system sending the data.
* "dns" sets the host to the reverse DNS entry for IP address of the system
  sending the data.
* "none" leaves the host as specified in inputs.conf, typically the splunk
  system hostname.
* Defaults to "ip".

compressed = [true|false]
* Specifies whether the receiver communicates with the forwarder in compressed format.
* Applies to non-SSL receiving only. There is no compression setting required for SSL.
* If set to true, the receiver communicates with the forwarder in compressed format.
* If set to true, there is no longer a requirement to also set 'compressed = true'
  in the outputs.conf file on the forwarder.
* Defaults to false.

enableS2SHeartbeat = [true|false]
* This specifies the keepalive setting for the splunktcp port.
* This option is used to detect forwarders which might have become unavailable
  due to network, firewall, or other problems.
* The receiver monitors the connection for presence of heartbeat, and if it
  does not see the heartbeat s2sHeartbeatTimeout seconds, it closes the
  connection.
* This overrides the default value specified at the global [splunktcp] stanza.
* Defaults to true (heartbeat monitoring enabled).

s2sHeartbeatTimeout = <seconds>
* This specifies the timeout value for monitoring heartbeats.
* The receiver closes the forwarder connection if it does not see a heartbeat
  for 's2sHeartbeatTimeout' seconds.
* This overrides the default value specified at the global [splunktcp] stanza.
* Defaults to 600 seconds (10 minutes).

queueSize = <integer>[KB|MB|GB]
* The maximum size of the in-memory input queue.
* Defaults to 500KB.

negotiateProtocolLevel = <unsigned integer>
* See comments for [splunktcp].

negotiateNewProtocol = [true|false]
* See the description for [splunktcp].

concurrentChannelLimit = <unsigned integer>
* See the description for [splunktcp].

[splunktcp:<port>]
* This input stanza is the same as [splunktcp://[<remote server>]:<port>], but
  does not have a remote server restriction.
* Please see documentation for [splunktcp://[<remote server>]:<port>] for
  following supported settings:

connection_host = [ip|dns|none]
compressed = [true|false]
enableS2SHeartbeat = [true|false]
s2sHeartbeatTimeout = <seconds>
queueSize = <integer>[KB|MB|GB]
negotiateProtocolLevel = <unsigned integer>
negotiateNewProtocol = [true|false]
concurrentChannelLimit = <unsigned integer>

# Access control settings.
[splunktcptoken://<token name>]
* This stanza is optional.
* Use this stanza to specify forwarders from which to accept data.
* You must configure a token on the receiver, then configure the same
  token on forwarders.
* The receiver discards data from forwarders that do not have the
  token configured.
* This setting is enabled for all receiving ports.

token = <string>
* Value of token.

# SSL settings for data distribution:

[splunktcp-ssl:<port>]
* Use this stanza type if you are receiving encrypted, parsed data from a
  forwarder.
* Set <port> to the port on which the forwarder sends the encrypted data.
* Forwarder settings are set in outputs.conf on the forwarder.
* Compression for SSL is enabled by default. On the forwarder you can still
  specify compression with the 'useClientSSLCompression' setting in
  outputs.conf.
* The 'compressed' setting is used for non-SSL connections. However, if you
  still specify 'compressed' for SSL, ensure that the 'compressed' setting is
  the same as on the forwarder, as splunktcp protocol expects the same
  'compressed' setting from forwarders.

connection_host = [ip|dns|none]
* For splunktcp, the host or connection_host will be used if the remote Splunk
  instance does not set a host, or if the host is set to "<host>::<localhost>".
* "ip" sets the host to the IP address of the system sending the data.
* "dns" sets the host to the reverse DNS entry for IP address of the system
  sending the data.
* "none" leaves the host as specified in inputs.conf, typically the splunk
  system hostname.
* Defaults to "ip".

compressed = [true|false]
* See comments for [splunktcp:<port>].

enableS2SHeartbeat = true|false
* See comments for [splunktcp:<port>].

s2sHeartbeatTimeout = <seconds>
* See comments for [splunktcp:<port>].

listenOnIPv6 = no|yes|only
* Select whether this receiver listens on IPv4, IPv6, or both protocols.
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the input uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or IP addresses from which to accept connections.
* Specify multiple rules with commas or spaces.
* Each rule can be in the following forms:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A CIDR block of addresses (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard (examples:
       "myhost.example.com", "*.splunk.com")
    4. A single '*', which matches anything.
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one that
  matches. For example, "!10.1/16, *" allows connections from everywhere except
  the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

negotiateProtocolLevel = <unsigned integer>
* See comments for [splunktcp].

negotiateNewProtocol = [true|false]
* See comments for [splunktcp].

concurrentChannelLimit = <unsigned integer>
* See comments for [splunktcp].

# To specify global ssl settings, that are applicable for all ports, add the
# settings to the SSL stanza.
# Specify any ssl setting that deviates from the global setting here.
# For a detailed description of each ssl setting, refer to the [SSL] stanza.

serverCert = <path>
sslPassword = <password>
requireClientCert = <bool>
sslVersions = <string>
cipherSuite = <cipher suite string>
ecdhCurves = <comma separated list of ec curves>
dhFile = <path>
allowSslRenegotiation = true|false
sslQuietShutdown = [true|false]
sslCommonNameToCheck = <commonName1>, <commonName2>, ...
sslAltNameToCheck = <alternateName1>, <alternateName2>, ...

[tcp-ssl:<port>]
* Use this stanza type if you are receiving encrypted, unparsed data from a
  forwarder or third-party system.
* Set <port> to the port on which the forwarder/third-party system is sending
  unparsed, encrypted data.
* To create multiple SSL inputs, you can add the following attributes to each 
[tcp-ssl:<port>] input stanza. If you do not configure a certificate in the 
port, the certificate information is pulled from the default [SSL] stanza: 
  * serverCert = <path_to_cert> 
  * sslRootCAPath = <path_to_cert> This attribute should only be added 
    if you have not configured your sslRootPath in server.conf. 
  * sslPassword = <password>

listenOnIPv6 = <no | yes | only>
* Select whether the receiver listens on IPv4, IPv6, or both protocols.
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the receiver uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or IP addresses from which to accept connections.
* Specify multiple rules with commas or spaces.
* Each rule can be in the following forms:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A CIDR block of addresses (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard (examples:
       "myhost.example.com", "*.splunk.com")
    4. A single '*', which matches anything.
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one that
  matches. For example, "!10.1/16, *" allows connections from everywhere except
  the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

[SSL]
* Set the following specifications for receiving Secure Sockets Layer (SSL)
  communication underneath this stanza name.

serverCert = <path>
* The full path to the server certificate Privacy-Enhanced Mail (PEM) format
  file.
* PEM is the most common text-based storage format for SSL certificate files.
* There is no default.

sslPassword = <password>
* Server certificate password, if any.
* Initially set to plain-text password.
* Upon first use, the input encrypts and rewrites the password to
  $SPLUNK_HOME/etc/system/local/inputs.conf.

password = <password>
* This setting is DEPRECATED.
* Do not use this setting. Use the 'sslPassword' setting instead.

rootCA = <path>
* This setting is DEPRECATED.
* Do not use this setting. Use 'server.conf/[sslConfig]/sslRootCAPath' instead.
* Used only if 'sslRootCAPath' is unset.

requireClientCert = <bool>
* Determines whether a client must present an SSL certificate to authenticate.
* Full path to the root CA (Certificate Authority) certificate store.
* The <path> must refer to a PEM format file containing one or more root CA
  certificates concatenated together.
* Certificates with the same Common Name as the CA's certificate will fail
  this check.
* Defaults to false for self-signed and third-party certificates. If using the 
default certificates, this attribute defaults to true and will override an existing 
false setting.

sslVersions = <string>
* A comma-separated list of SSL versions to support.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2"
* The special version "*" selects all supported versions. The version "tls"
  selects all versions "tls1.0" or newer.
* To remove a version from the list, prefix it with "-".
* SSLv2 is always disabled. You can specify "-ssl2" in the version list, but
  doing so has no effect.
* When configured in Federal Information Processing Standard (FIPS) mode, the
  "ssl3" version is always disabled, regardless of this configuration.
* The default can vary. See the sslVersions setting in 
* $SPLUNK_HOME/etc/system/default/inputs.conf for the current default.

supportSSLV3Only = <bool>
* This setting is DEPRECATED.
* SSLv2 is now always disabled.
* Use the "sslVersions" setting to set the list of supported SSL versions.

cipherSuite = <cipher suite string>
* If set, uses the specified cipher string for the input processors.
* Must specify 'dhFile' to enable any Diffie-Hellman ciphers.
* The default can vary. See the cipherSuite setting in 
* $SPLUNK_HOME/etc/system/default/inputs.conf for the current default.

ecdhCurveName = <string>
* This setting is DEPRECATED.
* Use the 'ecdhCurves' setting instead.
* This setting specifies the Elliptic Curve Diffie-Hellman (ECDH) curve to
  use for ECDH key negotiation.
* Splunk only supports named curves that have been specified by their SHORT name.
* The list of valid named curves by their short/long names
  can be obtained by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Default is empty string.

ecdhCurves = <comma separated list of ec curves>
* ECDH curves to use for ECDH key negotiation.
* The curves should be specified in the order of preference.
* The client sends these curves as a part of Client Hello.
* The server supports only the curves specified in the list.
* Splunk only supports named curves that have been specified by their SHORT names.
  (see struct ASN1_OBJECT in asn1.h)
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Example setting: ecdhCurves = prime256v1,secp384r1,secp521r1
* The default can vary. See the ecdhCurves setting in 
* $SPLUNK_HOME/etc/system/default/inputs.conf for the current default.

dhFile = <path>
* Full path to the Diffie-Hellman parameter file.
* DH group size should be no less than 2048 bits.
* This file is required in order to enable any Diffie-Hellman ciphers.
* Not set by default.

dhfile = <path>
* This setting is DEPRECATED.
* Use the 'dhFile' setting instead.

allowSslRenegotiation = true|false
* In the SSL protocol, a client may request renegotiation of the connection
  settings from time to time.
* Setting this to false causes the server to reject all renegotiation
  attempts, which breaks the connection.
* This limits the amount of CPU a single TCP connection can use, but it can
  cause connectivity problems, especially for long-lived connections.
* Defaults to true.

sslQuietShutdown = [true|false]
* Enables quiet shutdown mode in SSL.
* Defaults to false.

sslCommonNameToCheck = <commonName1>, <commonName2>, ...
* Check the common name of the client's certificate against this list of names.
* If there is no match, assume that the Splunk instance is not authenticated
  against this server.
* This setting is optional.
* Defaults to no common name checking.
* requireClientCert must be set to true for this setting to work.

sslAltNameToCheck = <alternateName1>, <alternateName2>, ...
* Check the alternate name of the client certificate against this list of names.
* If there is no match, assume that the Splunk instance is not authenticated
  against this server.
* This setting is optional.
* Defaults to no alternate name checking.
* For this setting to work, the 'requireClientCert'
  setting must be set to true.

#*******
# UDP:
#*******

[udp://<remote server>:<port>]
* Similar to the [tcp://] stanza, except that this stanza causes the Splunk
  instance to listen on a UDP port.
* Only one stanza per port number is currently supported.
* Configures the instance to listen on a specific port.
* If you specify <remote server>, the specified port only accepts data
  from that host.
* If <remote server> is empty - [udp://<port>] - the port accepts data sent
  from any host.
  * The use of <remote server> is not recommended. Use the 'acceptFrom'
    setting, which supersedes this setting.
* Generates events with source set to udp:portnumber, for example: udp:514
* If you do not specify a sourcetype, generates events with sourcetype set
  to udp:portnumber.

# Additional settings:

connection_host = [ip|dns|none]
* "ip" sets the host to the IP address of the system sending the data.
* "dns" sets the host to the reverse DNS entry for IP address of the system
  sending the data.
* "none" leaves the host as specified in inputs.conf, typically the splunk
  system hostname.
* Defaults to "ip".
* If the input is configured with a 'sourcetype' that has a transform that
  overrides the 'host' field e.g. 'sourcetype=syslog', that will take
  precedence over the host specified here.

_rcvbuf = <integer>
* Specifies the receive buffer for the UDP port (in bytes).
* If you set the value to 0 or a negative number, the input ignores the value.
* Note: If the default value is too large for an OS, the instance tries to set
  the value to 1572864/2. If that value is also too large, the instance
  retries with 1572864/(2*2). It continues to retry by halving the value until
  it succeeds.
* Defaults to 1,572,864.

no_priority_stripping = [true|false]
* Setting for receiving syslog data.
* If you set this setting to true, the instance does NOT strip the <priority>
  syslog field from received events.
* NOTE: Do NOT set this setting if you want to strip <priority>.
* Default is false.

no_appending_timestamp = [true|false]
* Whether or not to append a timestamp and host to received events.
* If you set this setting to true, the instance does NOT append a timestamp
  and host to received events.
* NOTE: Do NOT set this setting if you want to append timestamp and host
  to received events.
* Default is false.

queueSize = <integer>[KB|MB|GB]
* Maximum size of the in-memory input queue.
* Defaults to 500KB.

persistentQueueSize = <integer>[KB|MB|GB|TB]
* Maximum size of the persistent queue file.
* Defaults to 0 (no persistent queue).
* If set to some value other than 0, persistentQueueSize must be larger than
  the in-memory queue size (as defined by the 'queueSize' setting in
  inputs.conf or 'maxSize' settings in [queue] stanzas in server.conf).
* Persistent queues can help prevent loss of transient data. For information on
  persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
  interact, see the online documentation.

listenOnIPv6 = <no | yes | only>
* Select whether the instance listens on the IPv4, IPv6, or both protocols.
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the input uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or IP addresses from which to accept connections.
* Specify multiple rules with commas or spaces.
* Each rule can be in the following forms:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A CIDR block of addresses (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard (examples:
       "myhost.example.com", "*.splunk.com")
    4. A single '*', which matches anything.
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one that
  matches.
  For example, "!10.1/16, *" allows connections from everywhere except
  the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

[udp:<port>]
* This input stanza is the same as [udp://<remote server>:<port>], but does
  not have a <remote server> restriction.
* See the documentation for [udp://<remote server>:<port>] to configure
  supported settings:

connection_host = [ip|dns|none]
_rcvbuf = <integer>
no_priority_stripping = [true|false]
no_appending_timestamp = [true|false]
queueSize = <integer>[KB|MB|GB]
persistentQueueSize = <integer>[KB|MB|GB|TB]
listenOnIPv6 = <no | yes | only>
acceptFrom = <network_acl> ...

#*******
# FIFO (First In, First Out queue):
#*******

[fifo://<path>]
* This stanza configures the monitoring of a FIFO at the specified path.

queueSize = <integer>[KB|MB|GB]
* Maximum size of the in-memory input queue.
* Defaults to 500KB.

persistentQueueSize = <integer>[KB|MB|GB|TB]
* Maximum size of the persistent queue file.
* Defaults to 0 (no persistent queue).
* If set to some value other than 0, persistentQueueSize must be larger than
  the in-memory queue size (as defined by the 'queueSize' setting in
  inputs.conf or 'maxSize' settings in [queue] stanzas in server.conf).
* Persistent queues can help prevent loss of transient data. For information on
  persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
  interact, see the online documentation.

#*******
# Scripted Input:
#*******

[script://<cmd>]
* Runs <cmd> at a configured interval (see below) and indexes the output
  that <cmd> returns.
* The <cmd> must reside in one of the following directories:
  * $SPLUNK_HOME/etc/system/bin/
  * $SPLUNK_HOME/etc/apps/$YOUR_APP/bin/
  * $SPLUNK_HOME/bin/scripts/
* The path to <cmd> can be an absolute path, make use of an environment
  variable such as $SPLUNK_HOME, or use the special pattern of an initial '.'
  as the first directory to indicate a location inside the current app.
* The '.' specification must be followed by a platform-specific directory
  separator.
  * For example, on UNIX:
        [script://./bin/my_script.sh]
    Or on Windows:
        [script://.\bin\my_program.exe]
    This '.' pattern is strongly recommended for app developers, and necessary
    for operation in search head pooling environments.
* <cmd> can also be a path to a file that ends with a ".path" suffix. A file
  with this suffix is a special type of pointer file that points to a command
  to be run. Although the pointer file is bound by the same location
  restrictions mentioned above, the command referenced inside it can reside
  anywhere on the file system. The .path file must contain exactly one line:
  the path to the command to run, optionally followed by command-line
  arguments. The file can contain additional empty lines and lines that begin
  with '#'. The input ignores these lines.

interval = [<number>|<cron schedule>]
* How often to run the specified command (in seconds), or a valid cron
  schedule.
* NOTE: when you specify a cron schedule, the input does not run the
  script on start-up.
* If you specify the interval as a number, it may have a fractional
  component; e.g., 3.14
* The cron implementation for data inputs does not currently support names
  of months or days.
* Defaults to 60.0 seconds.
* The special value 0 forces this scripted input to be run continuously;
  that is, as soon as the script exits, the input restarts it.
* The special value -1 causes the scripted input to run once on start-up.

passAuth = <username>
* User to run the script as.
* If you provide a username, the instance generates an auth token for that
  user and passes it to the script via stdin.

queueSize = <integer>[KB|MB|GB]
* Maximum size of the in-memory input queue.
* Defaults to 500KB.

persistentQueueSize = <integer>[KB|MB|GB|TB]
* Maximum size of the persistent queue file.
* Defaults to 0 (no persistent queue).
* If set to some value other than 0, persistentQueueSize must be larger than
  the in-memory queue size (as defined by the 'queueSize' setting in
  inputs.conf or 'maxSize' settings in [queue] stanzas in server.conf).
* Persistent queues can help prevent loss of transient data. For information on
  persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
  interact, see the online documentation.

index = <index name>
* The index where the input sends the data.
* Note: this parameter will be passed as a command-line argument to <cmd> in
  the format: -index <index name>.
  If the script does not need the index info, it can ignore this argument.
* If you do not specify an index, the script uses the default index.

send_index_as_argument_for_path = [true|false]
* Whether or not to pass the index as an argument when specified for
  stanzas that begin with 'script://'
* When you set this setting to true, the script passes the argument as
  '-index <index name>'.
* To avoid passing the index as a command line argument, set this to false.
* Defaults to true.

start_by_shell = [true|false]
* Whether or not to run the specified command through the operating system
  shell or command prompt.
* If you set this setting to true, the host operating system runs the
  specified command through the OS shell ("/bin/sh -c" on UNIX,
  "cmd.exe /c" on Windows.)
* If you set the setting to false, the input runs the program directly
  without attempting to expand shell metacharacters.
* On Unix hosts, defaults to true.
* On Windows hosts defaults to false.
* You might want to explicitly set the setting to false for scripts
  that you know do not need UNIX shell metacharacter expansion. This is
  a Splunk best practice.

#*******
# File system change monitor (fschange monitor)
#*******
#
# The file system change monitor has been deprecated as of Splunk Enterprise
# version 5.0 and might be removed in a future version of the product.
#
# You cannot simultaneously monitor a directory with both the 'fschange'
# and 'monitor' stanza types.

[fschange:<path>]
* Monitors changes (such as additions, updates, and deletions) to this
  directory and any of its sub-directories.
* <path> is the direct path. Do not preface it with '//' like with
  other inputs.
* Sends an event for every change.

# Additional settings:
# NOTE: The 'fschange' stanza type does not use the same settings as
# other input types. It uses only the following settings:

index = <index name>
* The index where the input sends the data.
* Defaults to _audit, unless you either do not set the 'signedaudit'
  setting, or set 'signedaudit' to false.
* If you set 'signedaudit' to false, events go into the default index.

signedaudit = [true|false]
* Whether or not to send cryptographically signed add/update/delete events.
* If you set this setting to true, the input does the following to
  events that it generates:
  * Puts the events in the _audit index.
  * Sets the event sourcetype to 'audittrail'
* If you set the setting to false, the input:
  * Places events in the default index.
  * Sets the sourcetype to whatever you specify (or "fs_notification"
    by default).
* You must set 'signedaudit' to false if you want to set the index for
  fschange events.
* You must also enable auditing in audit.conf.
* Defaults to false.

filters = <filter1>,<filter2>,...
* Each filter is applied left to right for each file or directory
  found during the monitor poll cycle.
* See the "File System Monitoring Filters" section below for help
  on how to define a fschange filter.

recurse = [true|false]
* Whether or not the fschange input should look through all sub-directories
  for changes to files in a directory.
* If you set this setting to true, the input recurses through
  sub-directories within the directory specified in [fschange].
* Defaults to true.

followLinks = [true|false]
* Whether or not the fschange input should follow any symbolic
  links it encounters.
* If you set this setting to true, the input follows symbolic links.
* Do not set this setting to true unless you can confirm that
  doing so will not create a file system loop (For example, in
  Directory A, symbolic link B points back to Directory A.)
* Defaults to false.

pollPeriod = <integer>
* How often, in seconds, to check a directory for changes.
* Defaults to 3600 seconds (1 hour).

hashMaxSize = <integer>
* Calculate a SHA256 hash for every file that is less than or equal to
  <integer> bytes.
* The input uses this hash as an additional method for detecting changes to the
  file/directory.
* Defaults to -1 (disabled).

fullEvent = [true|false]
* Whether or not to send the full event if the input detects an add or
  update change.
* Set to true to send the full event if an add or update change is detected.
* Further qualified by the 'sendEventMaxSize' setting.
* Defaults to false.

sendEventMaxSize = <integer>
* Limits the size of event data that the fschange input sends.
* Only send the full event if the size of the event is less than or equal to
  <integer> bytes.
* This limits the size of indexed file data.
* Defaults to -1, which is unlimited.

sourcetype = <string>
* Set the source type for events from this input.
* The input automatically prepends "sourcetype=" to <string>.
* Defaults to "audittrail" if you set the 'signedaudit' setting to true.
* Defaults to "fs_notification" if you set the 'signedaudit' setting to false.

host = <string>
* Set the host name for events from this input.
* Defaults to whatever host sent the event.

filesPerDelay = <integer>
* The number of files that the fschange input processes between processing
  delays, as specified by the 'delayInMills' setting.
* After a delay of 'delayInMills' milliseconds, the fschange input processes
  <integer> files, then waits 'delayInMills' milliseconds again before
  repeating this process.
* This is used to throttle file system monitoring so it consumes less CPU.
* Defaults to 10.

delayInMills = <integer>
* The delay, in milliseconds, that the fschange input waits prior to
  processing 'filesPerDelay' files.
* After a delay of 'delayInMills' milliseconds, the fschange input processes
  <integer> files, then waits 'delayInMills' milliseconds again before
  repeating this process.
* This is used to throttle file system monitoring so it consumes less CPU.
* Defaults to 100.


#*******
# File system monitoring filters:
#*******

[filter:<filtertype>:<filtername>]
* Defines a filter of type <filtertype> and names it <filtername>.
* <filtertype>:
  * Filter types are either 'blacklist' or 'whitelist.'
  * A whitelist filter processes all file names that match the
    regular expression list that you define within the stanza.
  * A blacklist filter skips all file names that match the
    regular expression list.
* <filtername>
  * The fschange input uses filter names that you specify with
    the 'filters' setting for a given fschange stanza.
  * You can specify multiple filters buy separating them with commas.

regex<integer> = <regex>
* Blacklist and whitelist filters can include a set of regular expressions.
* The name of each regex MUST be 'regex<integer>', where <integer>
  starts at 1 and increments.
* The input applies each regular expression in numeric order:
  regex1=<regex>
  regex2=<regex>
  ...

#*******
# http: (HTTP Event Collector)
#*******

# Global settings for the HTTP Event Collector (HEC) Input.

[http]
port = <number>
* The event collector data endpoint server port.
* Defaults to 8088.

disabled = [0|1]
* Whether or not the event collector input is active.
* Set this setting to 1 to disable the input, and 0 to enable it.
* Defaults to 1 (disabled).

outputgroup = <string>
* The name of the output group that the event collector forwards data to.
* Defaults to empty string.

useDeploymentServer = [0|1]
* Whether or not the event collector input should write its configuration to
  a deployment server repository.
* When you set this setting to 1 (enabled), the input writes its
  configuration to the directory that you specify with the
  'repositoryLocation' setting in serverclass.conf.
* You must copy the full contents of the splunk_httpinput app directory
  to this directory for the configuration to work.
* When enabled, only the tokens defined in the splunk_httpinput app in this
  repository will be viewable and editable via the API and the Data Inputs
  page in Splunk Web.
* When disabled, the input writes its configuration to
  $SPLUNK_HOME/etc/apps by default.
* Defaults to 0 (disabled).

index = <string>
* The default index to use.
* Defaults to the "default" index.

sourcetype = <string>
* The default source type for the events.
* If you do not specify a sourcetype, the input does not set a sourcetype
  for events it generates.

enableSSL = [0|1]
* Whether or not to use SSL for the event collector endpoint server.
* HEC shares SSL settings with the Splunk management server and cannot have
  'enableSSL' set to true when the Splunk management server has SSL disabled.
* Defaults to 0 (enabled).

dedicatedIoThreads = <number>
* Defines the number of dedicated input/output threads in the event collector
  input.
* Defaults to 0 (The input uses a single thread).

replyHeader.<name> = <string>
* Add a static header to all HTTP responses this server generates
* For example, "replyHeader.My-Header = value" will cause the
  response header "My-Header: value" to be included in the reply to
  every HTTP request made to the event collector endpoint server

maxSockets = <int>
* The number of simultaneous HTTP connections that the event collector input
  accepts simultaneously.
* Set this setting to constrain resource usage.
* If you set this setting to 0, the input automatically sets it to
  one third of the maximum allowable open files on the host.
* If this number is less than 50, the input sets it to 50. If this number
  is  greater than 400000, the input sets it to 400000.
* If this number is negative, the input does not enforce a limit on
  connections.
* Defaults to 0.

maxThreads = <int>
* The number of threads that can be used by active HTTP transactions.
* Set this to constrain resource usage.
* If you set this setting to 0, the input automatically sets the limit to
  one third of the maximum allowable threads on the host.
* If this number is less than 20, the input sets it to 20. If this number is
  greater than 150000, the input sets it to 150000.
* If the 'maxSockets' setting has a positive value and 'maxThreads'
  is greater than 'maxSockets', then the input sets 'maxThreads' to be equal
  to 'maxSockets'.
* If set to a negative number, the input does not enforce a limit on threads.
* Defaults to 0.

keepAliveIdleTimeout = <int>
* How long, in seconds, that the HTTP Input data server allows a keep-alive
  connection to remain idle before forcibly disconnecting it.
* If this number is less than 7200, it will be set to 7200.
* Defaults to 7200 seconds.

busyKeepAliveIdleTimeout = <int>
* How long, in seconds, that the HTTP Input data server allows a keep-alive
  connection to remain idle while in a busy state before forcibly disconnecting it.
* Use caution when configuring this setting as a value that is too large
  can result in file descriptor exhaustion due to idling connections.
* If this number is less than 12, it will be set to 12.
* Defaults to 12 seconds.

serverCert = <path>
* The full path to the server certificate PEM format file.
* The same file may also contain a private key.
* Default is $SPLUNK_HOME/etc/auth/server.pem.
* The Splunk software automatically generates certificates when it first
  starts.
* You may replace the auto-generated certificate with your own certificate.

sslKeysfile = <filename>
* This setting is DEPRECATED.
* Use the 'serverCert' setting instead.
* File is in the directory specified by 'caPath' (see below).
* Defaults to server.pem.

sslPassword = <password>
* The server certificate password.
* Initially set to plain-text password.
* Upon first use, it will be encrypted and rewritten.
* Defaults to "password".

sslKeysfilePassword = <password>
* This setting is DEPRECATED.
* Use the 'sslPassword' setting instead.

caCertFile = <filename>
* This setting is DEPRECATED.
* Use the 'server.conf/[sslConfig]/sslRootCAPath' setting instead.
* Used only if you do not set the 'sslRootCAPath' setting.
* Specifies the file name (relative to 'caPath') of the CA
  (Certificate Authority) certificate PEM format file containing one or
  more certificates concatenated together.
* Defaults to cacert.pem.

caPath = <path>
* This setting is DEPRECATED.
* Use absolute paths for all certificate files.
* If certificate files given by other settings in this stanza are not absolute
  paths, then they will be relative to this path.
* Defaults to $SPLUNK_HOME/etc/auth.

sslVersions = <versions_list>
* A comma-separated list of SSL versions to support.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2"
* The special version "*" selects all supported versions. The version "tls"
  selects all versions "tls1.0" or newer.
* To remove a version from the list, prefix it with "-".
* SSLv2 is always disabled. You can specify "-ssl2" in the version list, but
  doing so has no effect.
* When configured in Federal Information Processing Standard (FIPS) mode, the
  "ssl3" version is always disabled, regardless of this configuration.
* Defaults to "*,-ssl2".  (anything newer than SSLv2)

cipherSuite = <cipher suite string>
* The cipher string to use for the HTTP server.
* Use this setting to ensure that the server does not accept connections using
  weak encryption protocols.
* If you set this setting, the input uses the specified cipher string for
  the HTTP server.
* If you do not set the setting, the input uses the default cipher
  string that OpenSSL provides.

listenOnIPv6 = no|yes|only
* Select whether this input listens on IPv4, IPv6, or both.
* Set this to 'yes' to listen on both IPv4 and IPv6 protocols.
* Set to 'only' to listen on only the IPv6 protocol.
* If not present, the input uses the setting in the [general] stanza
  of server.conf.

acceptFrom = <network_acl> ...
* Lists a set of networks or IP addresses from which to accept connections.
* Specify multiple rules with commas or spaces.
* Each rule can be in the following forms:
    1. A single IPv4 or IPv6 address (examples: "10.1.2.3", "fe80::4a3")
    2. A CIDR block of addresses (examples: "10/8", "fe80:1234/32")
    3. A DNS name, possibly with a '*' used as a wildcard (examples:
       "myhost.example.com", "*.splunk.com")
    4. A single '*', which matches anything.
* You can also prefix an entry with '!' to cause the rule to reject the
  connection. The input applies rules in order, and uses the first one that
  matches. For example, "!10.1/16, *" allows connections from everywhere except
  the 10.1.*.* network.
* Defaults to "*" (accept from anywhere)

requireClientCert = <bool>
* Requires that any client connecting to the HEC port has a certificate that
  can be validated by the certificate authority specified in the
  'caCertFile' setting.
* Defaults to false.

ecdhCurveName = <string>
* This setting is DEPRECATED.
* Use the 'ecdhCurves' setting instead.
* This setting specifies the ECDH curve to use for ECDH key negotiation.
* Splunk only supports named curves that have been specified by their SHORT name.
* The list of valid named curves by their short/long names
  can be obtained by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Default is empty string.

ecdhCurves = <comma separated list of ec curves>
* ECDH curves to use for ECDH key negotiation.
* The curves should be specified in the order of preference.
* The client sends these curves as a part of Client Hello.
* The server supports only the curves specified in the list.
* Splunk only supports named curves that have been specified by their SHORT names.
  (see struct ASN1_OBJECT in asn1.h)
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Default is empty string.
* Example setting: ecdhCurves = prime256v1,secp384r1,secp521r1

crossOriginSharingPolicy = <origin_acl> ...
* List of the HTTP Origins for which to return Access-Control-Allow-* (CORS)
  headers.
* These headers tell browsers that we trust web applications at those sites
  to make requests to the REST interface.
* The origin is passed as a URL without a path component (for example
  "https://app.example.com:8000").
* This setting can take a list of acceptable origins, separated
  by spaces and/or commas.
* Each origin can also contain wildcards for any part.  Examples:
    *://app.example.com:*  (either HTTP or HTTPS on any port)
    https://*.example.com  (any host under example.com, including example.com itself).
* An address can be prefixed with a '!' to negate the match, with
  the first matching origin taking precedence.  For example,
  "!*://evil.example.com:* *://*.example.com:*" to not avoid
  matching one host in a domain.
* A single "*" can also be used to match all origins.
* By default, the list is empty.

forceHttp10 = auto|never|always
* Whether or not the REST HTTP server forces clients that connect
  to it to use the HTTP 1.0 specification for web communications.
* When set to "always", the REST HTTP server does not use some
  HTTP 1.1 features such as persistent connections or chunked
  transfer encoding.
* When set to "auto" it does this only if the client did not send
  a User-Agent header, or if the user agent is known to have bugs
  in its support of HTTP/1.1.
* When set to "never" it always allows HTTP 1.1, even to
  clients it suspects may be buggy.
* Defaults to "auto".

sslCommonNameToCheck = <commonName1>, <commonName2>, ...
* If you set this setting and also set 'requireClientCert' to true,
  splunkd limits most inbound HTTPS connections to hosts that use
  a cert with one of the listed common names.
* The most important scenario is distributed search.
* This feature does not work with the deployment server and client
  communication over SSL.
* This setting is optional.
* Defaults to no common name checking.

sslAltNameToCheck = <alternateName1>, <alternateName2>, ...
* If you set this setting and also set 'requireClientCert' to true,
  splunkd can verify certificates that have a so-called
  "Subject Alternate Name" that matches any of the alternate
  names in this list.
  * Subject Alternate Names are effectively extended descriptive
    fields in SSL certs beyond the commonName. A common practice for
    HTTPS certs is to use these values to store additional valid
    hostnames or domains where the cert should be considered valid.
* Accepts a comma-separated list of Subject Alternate Names to consider
  valid.
* Items in this list are never validated against the SSL Common Name.
* This feature does not work with the deployment server and client
  communication over SSL.
* Optional.  Defaults to no alternate name checking

sendStrictTransportSecurityHeader = true|false
* If set to true, the REST interface sends a "Strict-Transport-Security"
  header with all responses to requests made over SSL.
* This can help avoid a client being tricked later by a Man-In-The-Middle
  attack to accept a non-SSL request. However, this requires a commitment that
  no non-SSL web hosts will ever be run on this hostname on any port.  For
  example, if Splunk Web is in default non-SSL mode this can break the
  ability of browser to connect to it.  Enable with caution.
* Defaults to false.

allowSslCompression = true|false
* If set to true, the server will allow clients to negotiate
  SSL-layer data compression.
* Defaults to true.

allowSslRenegotiation = true|false
* In the SSL protocol, a client may request renegotiation of the connection
  settings from time to time.
* Setting this to false causes the server to reject all renegotiation
  attempts, which breaks the connection.
* This limits the amount of CPU a single TCP connection can use, but it can
  cause connectivity problems, especially for long-lived connections.
* Defaults to true.

ackIdleCleanup = true|false
* If set to true, the server removes the ACK channels that are idle
  for 'maxIdleTime' seconds.
* Default to true.

maxIdleTime = <int>
* The maximum number of seconds the ACK channels are idle before they are
  removed.
* Defaults to 600 seconds.

channel_cookie = <string>
* The name of the cookie to use when sending data with a specified channel ID.
* The value of the cookie will be the channel sent. For example, if you have
  set 'channel_cookie=foo' and sent a request with channel ID set to 'bar',
  then you will have a cookie in the response with the value 'foo=bar'.
* If no channel ID is present in the request, then no cookie will be returned.
* This setting is to be used for load balancers (for example, AWS ELB) that can
  only provide sticky sessions on cookie values and not general header values.
* If no value is set (the default), then no cookie will be returned.
* Defaults to the empty string (no cookie).

#*******
# HTTP Event Collector (HEC) - Local stanza for each token
#*******

[http://name]

token = <string>
* The value of the HEC token.

disabled = [0|1]
* Whether or not this token is active.
* Defaults to 0 (enabled).

description = <string>
* A human-readable description of this token.
* Defaults to empty string.

indexes = <string>
* The indexes the event for this token can go to.
* If you do not specify this value, the index list is empty, and any index
  can be used.

index = <string>
* The default index to use for this token.
* Defaults to the default index.

sourcetype = <string>
* The default sourcetype to use if it is not specified in an event.
* Defaults to empty string.

outputgroup = <string>
* The name of the forwarding output group to send data to.
* Defaults to empty string.

queueSize = <integer>[KB|MB|GB]
* The maximum size of the in-memory input queue.
* Defaults to 500KB.

persistentQueueSize = <integer>[KB|MB|GB|TB]
* Maximum size of the persistent queue file.
* Defaults to 0 (no persistent queue).
* If set to some value other than 0, persistentQueueSize must be larger than
  the in-memory queue size (as defined by the 'queueSize' setting in
  inputs.conf or 'maxSize' settings in [queue] stanzas in server.conf).
* Persistent queues can help prevent loss of transient data. For information on
  persistent queues and how the 'queueSize' and 'persistentQueueSize' settings
  interact, see the online documentation.

connection_host = [ip|dns|proxied_ip|none]
* Specify the host if an event doesn't have host set.
* "ip" sets the host to the IP address of the system sending the data.
* "dns" sets the host to the reverse DNS entry for IP address of the system
  sending the data.
* "proxied_ip" checks whether an X-Forwarded-For header was sent
  (presumably by a proxy server) and if so, sets the host to that value.
  Otherwise, the IP address of the system sending the data is used.
* "none" leaves the host as specified in the HTTP header.

useACK = [true|false]
* When set to true, acknowledgment (ACK) is enabled. Events in a request will
  be tracked until they are indexed. An events status (indexed or not) can be
  queried from the ACK endpoint with the ID for the request.
* When set to false, acknowledgment is not enabled.
* This setting can be set at the stanza level.
* Defaults to false.

allowQueryStringAuth = [true|false]
* Enable or disable sending authorization token with query string.
* This is a token level config, it may only be set for a particular token.
* To use this feature, set to true and configure client application to include 
  the token in the query string portion of the URL they use to send data to 
  splunk in the format of "https://<URL>?<your=query-string>&token=<your-token>" 
  or "https://<URL>?token=<your-token>" if the token is the first element in the 
  query string.
* If a token is sent in both the query string and an HTTP header, the one in the 
  query string takes precedence, even if this feature is disabled. In other words, 
  if a token is present in the query string, any token in the header for that 
  request will not be used."
* Note: Query string may be observed in transit and/or logged in cleartext; it 
  provides no confidentiality protection for the transmitted tokens. Before use 
  in production, consult security personnel of your organization to understand 
  and plan to mitigate the risks. At a minimum, always use HTTPS on when this 
  feature os enabled, check your client application, proxy and logging configurations 
  to make sure token is not logged in clear text, give minimal access permissions 
  to the token in Splunk and restrict the use of the token only to trusted client 
  applications. 
* Defaults to false.

#*******
# WINDOWS INPUTS:
#*******

* Windows platform specific input processor.
# ***********
# Splunk on Windows ships with several Windows-only inputs. They are
# defined in the default inputs.conf.

* Use the "disabled=" setting to enable/disable any of them.
* A short summary of the inputs follows:
  * Perfmon: Monitors Windows performance counters, objects, and instances.
  * WinRegMon: Tracks and report any changes that occur in the
    local system Registry.
  * ADMon: Indexes existing Active Directory (AD) objects and listens for AD
    changes.
  * WMI: Retrieves event logs remotely and locally through the Windows
    Management.  Instrumentation subsystem. It can also gather performance
    data remotely, as well as receive various system notifications. See
    wmi.conf.spec for information on how to configure this input.

#*******
# The following Windows input specifications are for parsing on non-Windows
# platforms.
#*******

#*******
# Performance Monitor
#*******

[perfmon://<name>]

* This section explains possible settings for configuring
  the Windows Performance Monitor input.
* Each perfmon:// stanza represents an individually configured performance
  monitoring input. If you configure the input through Splunk Web, then the
  value of "<NAME>" matches what was specified there. While you can add
  performance monitor inputs manually, Splunk recommends that you use Splunk
  Web to configure them, because it is easy to mistype the values for
  Performance Monitor objects, counters and instances.
* Note: The perfmon stanza is for local systems ONLY. To define performance
  monitor inputs for remote machines, use wmi.conf.

object = <string>
* This is a valid Performance Monitor object as defined within Performance
  Monitor (for example, "Process," "Server," "PhysicalDisk.")
* You can specify a single valid Performance Monitor object or use a
  regular expression (regex) to specify multiple objects.
* This setting is required, and the input will not run if the setting is
  not present.
* There is no default.

counters = <semicolon-separated strings>
* This can be a single counter, or multiple valid Performance Monitor
  counters.
* This setting is required, and the input will not run if the setting is
  not present.
* '*' is equivalent to all available counters for a given Performance
  Monitor object.
* There is no default.

instances = <semicolon-separated strings>
* This can be a single instance, or multiple valid Performance Monitor
  instances.
* '*' is  equivalent to all available instances for a given Performance Monitor
  counter.
* If applicable instances are available for a counter and this setting is not
  present, then the input logs data for all available instances (this is the
  same as setting 'instances = *').
* If there are no applicable instances for a counter, then this setting
  can be safely omitted.
* There is no default.

interval = <integer>
* How often, in seconds, to poll for new data.
* This setting is required, and the input will not run if the setting is
  not present.
* The recommended setting depends on the Performance Monitor object,
  counter(s) and instance(s) that you define in the input, and how much
  performance data you require.
  * Objects with numerous instantaneous or per-second counters, such
    as "Memory," "Processor" and "PhysicalDisk" should have shorter
    interval times specified (anywhere from 1-3 seconds).
  * Less volatile counters such as "Terminal Services", "Paging File",
    and "Print Queue" can have longer times configured.
* Default is 300 seconds.

mode = [single|multikv]
* Specifies how the performance monitor input prints events.
* Set to 'single' to print each event individually, or 'multikv' to
  print events in multikv (formatted multiple key-value pair) format.
* Defaults to single.

samplingInterval = <sampling interval in ms>
* Advanced setting.
* How often, in milliseconds, to poll for new data.
* Enables high-frequency performance sampling. The input collects
  performance data every sampling interval. It then reports averaged data
  and other statistics at every interval.
* The minimum legal value is 100, and the maximum legal value must be less
  than what the 'interval' setting to.
* If not specified, high-frequency sampling does not take place.
* Defaults to not specified (disabled).

stats = <average;count;dev;min;max>
* Advanced setting.
* Reports statistics for high-frequency performance
  sampling.
* Acceptable values are: average, count, dev, min, max.
* You can specify multiple values by separating them with semicolons.
* If not specified, the input does not produce high-frequency sampling
  statistics.
* Defaults to not specified (disabled).

disabled = [0|1]
* Specifies whether or not the input is enabled.
* 1 to disable the input, 0 to enable it.
* Defaults to 0 (enabled).

index = <string>
* Specifies the index that this input should send the data to.
* This setting is optional.
* If no value is present, defaults to the default index.

showZeroValue = [0|1]
* Specfies whether or not zero value event data should be collected.
* Set to 1 to capture zero value event data, and 0 to ignore such data.
* Defaults to 0 (ignore zero value event data)

useEnglishOnly = [true|false]
* Controls which Windows Performance Monitor API the input uses.
* If true, the input uses PdhAddEnglishCounter() to add the counter string.
  This ensures that counters display in English regardless of the Windows
  host locale.
* If false, the input uses PdhAddCounter() to add the counter string.
* Note: if you set this setting to true, the 'object' setting does not
  accept a regular expression as a value on hosts that have a non-English
  locale.
* Defaults to false.

formatString = <double format specifier>
* Controls the print format for double-precision statistic counters.
* Do not use quotes when specifying this string.
* Defaults to "%.20g" (without quotes).

###
# Direct Access File Monitor (does not use file handles)
# For Windows systems only.
###

[MonitorNoHandle://<path>]

* This input intercepts file writes to the specific file.
* <path> must be a fully qualified path name to a specific file. Wildcards
  and directories are not accepted.
* You can specify more than one stanza of this type.

disabled = [0|1]
* Whether or not the input is enabled.
* Defaults to 0 (enabled).

index = <string>
* Specifies the index that this input should send the data to.
* This setting is optional.
* Defaults to the default index.

#*******
# Windows Event Log Monitor
#*******

[WinEventLog://<name>]

* This section explains possible settings for configuring the
  Windows Event Log monitor.
* Each WinEventLog:// stanza represents an individually configured WinEventLog
  monitoring input. If you you configure the input through Splunk Web, the
  value of "<NAME>" matches what was specified there. While you can add
  event log monitor inputs manually, Splunk recommends that you use Splunk
  Web to configure Windows event log monitor inputs because it is
  easy to mistype the values for event log channels.
* Note: The WinEventLog stanza is for local systems only. To define event log
  monitor inputs for remote machines, use wmi.conf.
* To specify settings that should apply to all Windows Event Log inputs 
  (for example, 'index', 'source', etc.), create a WinEventLog] stanza
   and put the settings there.

start_from = <string>
* How the input should chronologically read the Event Log channels.
* If you set this setting to 'oldest', the input reads Windows event logs
  from oldest to newest.
* If you set this setting to 'newest' the input reads Windows event logs
  in reverse, from newest to oldest. Once the input consumes the backlog of
  events, it stops.
* If you set this setting to 'newest', and at the same time set the
  'current_only' setting to 0, the combination can result in the input 
  indexing duplicate events.
* Do not set this setting to 'newest' and at the same time set the
  'current_only' setting to 1. This results in the input not collecting
  any events because you instructed it to read existing events from oldest
  to newest and read only incoming events concurrently (A logically
  impossible combination.)
* Defaults to oldest.

use_old_eventlog_api = <bool>
* Whether or not to read Event Log events with the Event Logging API.
* This is an advanced setting. Contact Splunk Support before you change it.
  If set to true, the input uses the Event Logging API (instead of the Windows Event Log API) to read from the Event Log on Windows Server 2008, Windows Vista, and later installations.
* Defaults to false (Use the API that is specific to the OS.)

use_threads = <integer>
* Specifies the number of threads, in addition to the default writer thread, that can be created to filter events with the blacklist/whitelist regular expression.
  The maximum number of threads is 15.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to 0

thread_wait_time_msec = <integer>
* The interval, in milliseconds, between attempts to re-read Event Log files when a read error occurs.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to 5000

suppress_checkpoint = <bool>
* Whether or not the Event Log strictly follows the 'checkpointInterval' setting when it saves a checkpoint.
  By default, the Event Log input saves a checkpoint from between zero and 'checkpointInterval' seconds, depending on incoming event volume.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

suppress_sourcename = <bool>
* Whether or not to exclude the 'sourcename' field from events.
  When set to true, the input excludes the 'sourcename' field from events and thruput performance (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

suppress_keywords = <bool>
* Whether or not to exclude the 'keywords' field from events.
  When set to true, the input excludes the 'keywords' field from events and thruput performance (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

suppress_type = <bool>
* Whether or not to exclude the 'type' field from events.
  When set to true, the input excludes the 'type' field from events and thruput performance (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

suppress_task = <bool>
* Whether or not to exclude the 'task' field from events.
  When set to true, the input excludes the 'task' field from events and thruput performance (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

suppress_opcode = <bool>
* Whether or not to exclude the 'opcode' field from events.
  When set to true, the input excludes the 'opcode' field from events and thruput performance (the number of events processed per second) improves.
* This is an advanced setting. Contact Splunk Support before you change it.
* Defaults to false

current_only = [0|1]
* Whether or not to acquire only events that arrive while the instance is
  running.
* If you set this setting to 1, the input only acquires events that arrive
  while the instance runs and the input is enabled. The input does not read
  data which was stored in the Windows Event Log while the instance was not
  running. This means that there will be gaps in the data if you restart the
  instance or experiences downtime.
* If you set the setting to 0, the input first gets all existing events
  already stored in the log that have higher event IDs (have arrived more
  recently) than the most recent events acquired. The input then monitors
  events that arrive in real time.
* If you set this setting to 0, and at the same time set the
  'start_from' setting to 'newest', the combination can result in the
  indexing of duplicate events. 
* Do not set this setting to 1 and at the same time set the
  'start_from' setting to 'newest'. This results in the input not collecting
  any events because you instructed it to read existing events from oldest
  to newest and read only incoming events concurrently (A logically
  impossible combination.)
* Defaults to 0 (false), gathering stored events first before monitoring
  live events.

batch_size = <integer>
* How many Windows Event Log items to read per request.
* If troubleshooting identifies that the Event Log input is a bottleneck in
  acquiring data, increasing this value can help.
  * NOTE: Splunk Support has seen cases where large values can result in a
    stall in the Event Log subsystem.
    If you increase this value significantly, monitor closely for trouble.
* In local testing and in customer acceptance testing, 10 worked well
  for both throughput and reliability.
* The default value is 10.

checkpointInterval = <integer>
* How often, in seconds, that the Windows Event Log input saves a checkpoint.
* Checkpoints store the eventID of acquired events. This lets the input
  continue monitoring at the correct event after a shutdown or outage.
* The default value is 0.

disabled = [0|1]
* Whether or not the input is enabled.
* Set to 1 to disable the input, and 0 to enable it.
* The default is 0 (enabled).

evt_resolve_ad_obj = [1|0]
* How the input should interact with Active Directory while indexing Windows
  Event Log events.
* If you set this setting to 1, the input resolves the Active
  Directory Security IDentifier (SID) objects to their canonical names for
  a specific Windows Event Log channel.
* If you enable the setting, the rate at which the input reads events
  on high-traffic Event Log channels can decrease. Latency can also increase
  during event acquisition. This is due to the overhead involved in performing
  AD translations.
* When you set this setting to 1, you can optionally specify the domain
  controller name or dns name of the domain to bind to with the 'evt_dc_name'
  setting.  The input connects to that domain controller to resolve the AD
  objects.
* If you set this setting to 0, the input does not attempt any resolution.
* Defaults to 0 (disabled) for all channels.

evt_dc_name = <string>
* Which Active Directory domain controller to bind to for AD object
  resolution.
* If you prefix a dollar sign to a value (for example, $my_domain_controller),
  the input interprets the value as an environment variable. If the
  environment variable has not been defined on the host, it is the same
  as if the value is blank.
* This setting is optional.
* This setting can be set to the NetBIOS name of the domain controller
  or the fully-qualified DNS name of the domain controller. Either name
  type can, optionally, be preceded by two backslash characters. The following
  examples represent correctly formatted domain controller names:

    * "FTW-DC-01"
    * "\\FTW-DC-01"
    * "FTW-DC-01.splunk.com"
    * "\\FTW-DC-01.splunk.com"
    * $my_domain_controller

evt_dns_name = <string>
* The fully-qualified DNS name of the domain that the input should bind to for
  AD object resolution.
* This setting is optional.

evt_resolve_ad_ds = [auto|PDC]
* How the input should choose the domain controller to bind for
  AD resolution.
* This setting is optional.
* If set to PDC, the input only contacts the primary domain controller
  to resolve AD objects.
* If set to auto, the input lets Windows chose the best domain controller.
* If you set the 'evt_dc_name' setting, the input ignores this setting.
* Defaults to 'auto' (let Windows determine the domain controller to use.)

evt_ad_cache_disabled = [0|1]
* Enables or disables the AD object cache.
* Defaults to 0.

evt_ad_cache_exp = <time in seconds>
* The expiration time, in seconds, for AD object cache entries.
* This setting is optional.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 3600.

evt_ad_cache_exp_neg = <time in seconds>
* The expiration time, in seconds, for negative AD object cache entries.
* This setting is optional.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 10.

evt_ad_cache_max_entries = <number of entries>
* The maximum number of AD object cache entries.
* This setting is optional.
* The minimum allowed value is 10 and the maximum allowed value is 40000.
* Defaults to 1000.

evt_sid_cache_disabled = [0|1]
* Enables or disables account Security IDentifier (SID) cache.
* This setting is global. It affects all Windows Event Log stanzas.
* Defaults to 0.

evt_sid_cache_exp = <time in seconds>
* The expiration time for account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Event Log stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 3600.

evt_sid_cache_exp_neg = <time in seconds>
* The expiration time for negative account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Event Log stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 10.

evt_sid_cache_max_entries = <number of entries>
* The maximum number of account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Event Log stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 40000.
* Defaults to 10.

index = <string>
* Specifies the index that this input should send the data to.
* This setting is optional.
* If no value is present, defaults to the default index.

# Event Log filtering
#
# Filtering at the input layer is desirable to reduce the total
# processing load in network transfer and computation on the Splunk
# nodes that acquire and processing Event Log data.

whitelist = <list of eventIDs> | key=regex [key=regex]
blacklist = <list of eventIDs> | key=regex [key=regex]

whitelist1 = <list of eventIDs> | key=regex [key=regex]
whitelist2 = <list of eventIDs> | key=regex [key=regex]
whitelist3 = <list of eventIDs> | key=regex [key=regex]
whitelist4 = <list of eventIDs> | key=regex [key=regex]
whitelist5 = <list of eventIDs> | key=regex [key=regex]
whitelist6 = <list of eventIDs> | key=regex [key=regex]
whitelist7 = <list of eventIDs> | key=regex [key=regex]
whitelist8 = <list of eventIDs> | key=regex [key=regex]
whitelist9 = <list of eventIDs> | key=regex [key=regex]
blacklist1 = <list of eventIDs> | key=regex [key=regex]
blacklist2 = <list of eventIDs> | key=regex [key=regex]
blacklist3 = <list of eventIDs> | key=regex [key=regex]
blacklist4 = <list of eventIDs> | key=regex [key=regex]
blacklist5 = <list of eventIDs> | key=regex [key=regex]
blacklist6 = <list of eventIDs> | key=regex [key=regex]
blacklist7 = <list of eventIDs> | key=regex [key=regex]
blacklist8 = <list of eventIDs> | key=regex [key=regex]
blacklist9 = <list of eventIDs> | key=regex [key=regex]

* These settings are optional.
* Both numbered and unnumbered whitelists and blacklists support two formats:
  * A comma-separated list of event IDs.
  * A list of key=regular expression pairs.
  * You cannot combine these formats. You can use either format on a specific
    line.

* Numbered whitelist settings are permitted from 1 to 9, so whitelist1 through
  whitelist9 and blacklist1 through blacklist9 are supported.
* If no whitelist or blacklist rules are present, the input reads all events.

###
# Event Log whitelist and blacklist formats
####

* Event ID list format:
  * A comma-separated list of terms.
  * Terms may be a single event ID (e.g. 6) or range of event IDs (e.g. 100-200)
  * Example: 4,5,7,100-200
    * This applies to events with IDs 4, 5, 7, or any event ID between 100
      and 200, inclusive.
  * The event ID list format provides no additional functionality over the
    key=regex format, but can be easier to understand:
    List format:      4,5,7,100-200
    Regex equivalent: EventCode=%^(4|5|7|1..|200)$%

* key=regex format:
  * A whitespace-separated list of Event Log components to match, and
    regular expressions to match against against them.
  * There can be one match expression or multiple expressions per line.
  * The key must belong to the set of valid keys provided below.
  * The regex consists of a leading delimiter, the regex expression, and a
    trailing delimeter. Examples: %regex%, *regex*, "regex"
  * When multiple match expressions are present, they are treated as a
    logical AND.  In other words, all expressions must match for the line to
    apply to the event.
  * If the value represented by the key does not exist, it is not considered
    a match, regardless of the regex.
  * Example:
    whitelist = EventCode=%^200$% User=%jrodman%
    Include events only if they have EventCode 200 and relate to User jrodman

# Valid keys for the key=regex format:

* The following keys are equivalent to the fields that appear in the text of
  the acquired events:
  * Category, CategoryString, ComputerName, EventCode, EventType, Keywords,
    LogName, Message, OpCode, RecordNumber, Sid, SidType, SourceName,
    TaskCategory, Type, User
* There are two special keys that do not appear literally in the event.
  * $TimeGenerated: The time that the computer generated the event
  * $Timestamp: The time that the event was received and recorded by the
                Event Log service.
* The 'EventType' key is only available on Windows Server 2003 /
  Windows XP and earlier.
* The 'Type' key is only available on Windows Server 2008 /
  Windows Vista and later.
* For a detailed definition of these keys, see the 
  "Monitor Windows Event Log Data" topic in the online documentation.

suppress_text = [0|1]
* Whether or not to include the description of the event text for a
  given Event Log event.
* This setting is optional.
* Set this setting to 1 to suppress the inclusion of the event
  text description.
* Set this value to 0 to include the event text description.
* Defaults to 0.

renderXml = [true|false]
* Whether or not the input returns the event data in XML (eXtensible Markup
  Language) format or in plain text.
* Set this to true to render events in XML.
* If you set this setting to true, you should also set the 'suppress_text',
  'suppress_sourcename', 'suppress_keywords', 'suppress_task', and 'suppress_opcode'
  settings to true to improve thruput performance.
* Set this to false to output events in plain text.
* Defaults to false.

#*******
# Active Directory Monitor
#*******

[admon://<name>]

* This section explains possible settings for configuring the Active Directory
  monitor input.
* Each admon:// stanza represents an individually configured Active
  Directory monitoring input. If you configure the input with Splunk Web,
  then the value of "<NAME>" matches what was specified there. While
  you can add Active Directory monitor inputs manually, Splunk recommends
  that you use Splunk Web to configure Active Directory monitor
  inputs because it is easy to mistype the values for Active Directory
  monitor objects.

targetDc = <string>
* The fully qualified domain name of a valid, network-accessible
  Active Directory domain controller.
* Defaults to the DC that the local host used to connect to AD. The
  input binds to its root Distinguished Name (DN).

startingNode = <string>
* Where in the Active Directory directory tree to start monitoring.
* The user that you configure the Splunk software to run as at
  installation determines where the input starts monitoring.
* If not specified, the input attempts to start at the root of
  the directory tree.

monitorSubtree = [0|1]
* Whether or not to monitor the subtree(s) of a given Active
  Directory tree path.
* Set this to 1 to monitor subtrees of a given directory tree
  path and 0 to monitor only the path itself.
* Defaults to 1 (monitor subtrees of a given directory tree path).

disabled = [0|1]
* Whether or not the input is enabled.
* Set this to 1 to disable the input and 0 to enable it.
* Defaults to 0 (enabled.)

index = <string>
* The index to store incoming data into for this input.
* This setting is optional.
* Defaults to the default index.

printSchema = [0|1]
* Whether or not to print the Active Directory schema.
* Set this to 1 to print the schema and 0 to not print
  the schema.
* Defaults to 1 (print the Active Directory schema).

baseline = [0|1]
* Whether or not to query baseline objects.
* Baseline objects are objects which currently reside in Active Directory.
* Baseline objects also include previously deleted objects.
* Set this to 1 to query baseline objects, and 0 to not query
  baseline objects.
* Defaults to 0 (do not query baseline objects).

##
# Remote Queue Monitor
##

[remote_queue:<name>]

* This section explains possible settings for configuring a remote queue.
* Each remote_queue: stanza represents an individually configured remote
  queue monitoring input.

remote_queue.* = <string>
* Optional.
* With remote queues, communication between the indexer and the remote queue
  system may require additional configuration, specific to the type of remote
  queue.  You can pass configuration information to the storage system by
  specifying the settings through the following schema:
  remote_queue.<scheme>.<config-variable> = <value>.  For example:
  remote_queue.sqs.access_key = ACCESS_KEY

##
# SQS specific settings
##

remote_queue.sqs.access_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Specifies the access key to use when authenticating with the remote queue
  system supporting the SQS API.
* If not specified, the indexer will look for these environment variables:
  AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY (in that order). If the environment
  variables are not set and the indexer is running on EC2, the indexer
  attempts to use the secret key from the IAM role.
* Default: unset

remote_queue.sqs.secret_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Specifies the secret key to use when authenticating with the remote queue
  system supporting the SQS API.
* If not specified, the indexer will look for these environment variables:
  AWS_SECRET_ACCESS_KEY or AWS_SECRET_KEY (in that order). If the environment
  variables are not set and the indexer is running on EC2, the indexer
  attempts to use the secret key from the IAM role.
* Default: unset

remote_queue.sqs.auth_region = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The authentication region to use when signing the requests when interacting
  with the remote queue system supporting the SQS API.
* If not specified and the indexer is running on EC2, the auth_region will be
  constructed automatically based on the EC2 region of the instance where the
  the indexer is running.
* Default: unset

remote_queue.sqs.endpoint = <URL>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The URL of the remote queue system supporting the SQS API.
* The scheme, http or https, can be used to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint will be constructed automatically based on the
  auth_region as follows: https://sqs.<auth_region>.amazonaws.com
* Example: https://sqs.us-west-2.amazonaws.com/

remote_queue.sqs.max_connections = <unsigned int>
* Currently not supported. This setting is related to a feature that is still
  under development.
* Specifies the maximum number of HTTP connections to have in progress for
  certain queue operations.
* A value of 0 means unlimited.
* Default: 8

remote_queue.sqs.message_group_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the Message Group ID for Amazon Web Services Simple Queue Service
  (SQS) First-In, First-Out (FIFO) queues.
* Setting a Message Group ID controls how messages within an AWS SQS queue are
  processed.
* For information on SQS FIFO queues and how messages in those queues are
  processed, see "Recommendations for FIFO queues" in the AWS SQS Developer
  Guide.
* This setting is optional.
* If you configure this setting, Splunk software assumes that the SQS queue is
  a FIFO queue, and that messages in the queue should be processed first-in,
  first-out.
* Otherwise, Splunk software assumes that the SQS queue is a standard queue.
* Can be between 1-128 alphanumeric or punctuation characters.
* Note: FIFO queues must have Content-Based Deduplication enabled.
* Defaults to unset.

remote_queue.sqs.retry_policy = max_count|none
* Currently not supported. This setting is related to a feature that is still
  under development.
* Optional.
* Sets the retry policy to use for remote queue operations.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation will be
    retried upon intermittent failure.
  + "none": Do not retry file operations upon failure.
* Defaults: max_count

remote_queue.sqs.max_count.max_retries_per_part = <unsigned int>
* Currently not supported. This setting is related to a feature that is still
  under development.
* Optional.
* When the remote_queue.sqs.retry_policy setting is max_count, sets the maximum
  number of times a queue operation will be retried upon intermittent failure.
* Defaults: 9

remote_queue.sqs.timeout.connect = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the connection timeout, in seconds, to use when interacting with
  SQS for this queue.
* Default: 5

remote_queue.sqs.timeout.read = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the read timeout, in seconds, to use when interacting with SQS for
  this queue.
* Default: 60

remote_queue.sqs.timeout.write = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the write timeout, in seconds, to use when interacting with SQS for
  this queue.
* Default: 60

remote_queue.sqs.timeout.receive_message = <unsigned int>
* Optional.
* Sets the receive message wait time in seconds.
* When greater than 0, enables "long polling," that is if there are no messages
  immediately available, will wait at most this amount of time for a message to
  become available.
* When 0, disables long polling.
* When unset, uses the value configured for the queue via the AWS SQS console.
* Maximum value: 20
* Default: 20

remote_queue.sqs.timeout.visibility = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the default "visibility timeout," in seconds, to use when
  explicitly changing the visibility of specific messages in the queue.
* Note that this does not change the implicit visibility timeout configured for
  the queue via the AWS SQS console.
* Default: 60

remote_queue.sqs.buffer.visibility = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the default time in seconds before
  remote_queue.sqs.timeout.visibility at which visibility of
  specific messages in the queue needs to be changed.
* Default: 15

remote_queue.sqs.min_pending_messages = <unsigned int>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the default "minimum number of pending messages" to use before
  receiving messages off remote queue.
  Messages are only received when sum of internal queue message count and
  pending object GET (from large messages storage) count is below
  the set value.
* Default: 10

remote_queue.sqs.large_message_store.endpoint = <URL>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The URL of the remote storage system supporting the S3 API.
* The scheme, http or https, can be used to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint will be constructed automatically based on the
  auth_region as follows: https://s3-<auth_region>.amazonaws.com
* Example: https://s3-us-west-2.amazonaws.com/
* Defaults to unset.

remote_queue.sqs.large_message_store.path = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Points to the remote storage location where messages larger than the
  underlying queue's maximum message size will reside.
* The format for this attribute is: <scheme>://<remote-location-specifier>
  * The "scheme" identifies a supported external storage system type.
  * The "remote-location-specifier" is an external system-specific string for
    identifying a location inside the storage system.
* These external systems are supported:
   - Object stores that support AWS's S3 protocol. These use the scheme "s3".
     For example, "path=s3://mybucket/some/path".
* If not specified, messages exceeding the underlying queue's maximum message
  size are dropped.
* Defaults to unset.

compressed = [true|false]
* See the description for TCPOUT ATTRIBUTES in outputs.conf.spec.

negotiateProtocolLevel = <unsigned integer>
* See the description for TCPOUT ATTRIBUTES in outputs.conf.spec.

channelReapInterval = <integer>
* See the description for TCPOUT ATTRIBUTES in outputs.conf.spec.

channelTTL = <integer>
* See the description for TCPOUT ATTRIBUTES in outputs.conf.spec.

channelReapLowater = <integer>
* See the description for TCPOUT ATTRIBUTES in outputs.conf.spec.

concurrentChannelLimit = <unsigned integer>
* See the description for [splunktcp].

###
# Windows Registry Monitor
###

[WinRegMon://<name>]

* This section explains possible settings for configuring the Windows Registry
  Monitor input.
* Each WinRegMon:// stanza represents an individually configured
  WinRegMon monitoring input.
* If you configure the inputs with Splunk Web, the value of "<NAME>" matches
  what was specified there. While you can add event log monitor inputs
  manually, recommends that you use Splunk Web to configure
  Windows registry monitor inputs because it is easy to mistype the values
  for Registry hives and keys.
* The WinRegMon input is for local systems only.

proc = <string>
* Which processes this input should monitor for Registry access.
* If set, matches against the process name which performed the Registry
  access.
* The input includes events from processes that match the regular expression
  that you specify here.
* The input filters out events for processes that do not match the
  regular expression.
* There is no default.

hive = <string>
* The Registry hive(s) that this input should monitor for Registry access.
* If set, matches against the Registry key that was accessed.
* The input includes events from Registry hives that match the
  regular expression that you specify here.
* The input filters out events for Registry hives that do not match the
  regular expression.
* There is no default.

type = <string>
* A regular expression that specifies the type(s) of Registry event(s)
  that you want the input to monitor.
* There is no default.

baseline = [0|1]
* Whether or not the input should get a baseline of Registry events
  when it starts.
* If you set this to 1, the input captures a baseline for
  the specified hive when it starts for the first time. It then
  monitors live events.
* Defaults to 0 (do not capture a baseline for the specified hive
  first before monitoring live events).

baseline_interval = <integer>
* Selects how much downtime in continuous registry monitoring should trigger
  a new baseline for the monitored hive and/or key.
* In detail:
  * Sets the minimum time interval, in seconds, between baselines.
  * At startup, a WinRegMon input will not generate a baseline if less time
    has passed since the last checkpoint than baseline_interval chooses.
  * In normal operation, checkpoints are updated frequently as data is
    acquired, so this will cause baselines to occur only when monitoring was
    not operating for a period of time.
* If baseline is set to 0 (disabled), has no effect.
* Defaults to 0 (always baseline on startup, if baseline is 1)

disabled = [0|1]
* Whether or not the input is enabled.
* Set this to 1 to disable the input, or 0 to enable it.
* Defaults to 0 (enabled).

index = <string>
* The index that this input should send the data to.
* This setting is optional.
* Defaults to the default index.

###
# Windows Host Monitoring
###

[WinHostMon://<name>]

* This section explains possible settings for configuring the Windows host
  monitor input.
* Gathers status information from the local Windows system components as
  per the type field below.
* Each WinHostMon:// stanza represents an WinHostMon monitoring input.
* The "<name>" component of the stanza name will be used as the source field
  on generated events, unless an explicit source setting is added to the
  stanza.  It does not affect what data is collected (see type setting for
  that).
* If you configure the input in Splunk web, the value of "<name>" matches
  what was specified there.
* Note: The WinHostMon input is for local Windows systems only. You
  can not monitor Windows host information remotely.

type = <semicolon-separated strings>
* An expression that specifies the type(s) of host inputs
  that you want the input to monitor.
* Type can be (case insensitive)
  Computer;Process;Processor;NetworkAdapter;Service;OperatingSystem;Disk;Driver;Roles

interval = <integer>
* The interval, in seconds, between when the input runs to gather
  Windows host information and generate events.
* See interval in the Scripted input section for more information.

disabled = [0|1]
* Whether or not the input is enabled.
* Set this to 1 to disable the input, or 0 to enable it.
* Defaults to 0 (enabled).

index = <string>
* The index that this input should send the data to.
* This setting is optional.
* Defaults to the default index.

[WinPrintMon://<name>]

* This section explains possible settings for configuring the Windows print
  monitor input.
* Each WinPrintMon:// stanza represents an WinPrintMon monitoring input.
  The value of "<name>" matches what was specified in Splunk Web.
* Note: The WinPrintMon input is for local Windows systems only.
* The "<name>" component of the stanza name will be used as the source field
  on generated events, unless an explicit source setting is added to the
  stanza.  It does not affect what data is collected (see type setting for
  that).

type = <semicolon-separated strings>
* An expression that specifies the type(s) of print inputs
  that you want the input to monitor.
* Type can be (case insensitive)
  Printer;Job;Driver;Port

baseline = [0|1]
* Whether or not to capture a baseline of print objects when the
  input starts for the first time.
* If you set this to 1, the input captures a baseline of
  the current print objects when the input starts for the first time.
* Defaults to 0 (do not capture a baseline.)

disabled = [0|1]
* Whether or not the input is enabled.
* Set to 1 to disable the input, or 0 to enable it.
* Defaults to 0 (enabled).

index = <string>
* The index that this input should send the data to.
* This setting is optional.
* Defaults to the default index.

[WinNetMon://<name>]

* This section explains possible settings for configuring
  a Network Monitor input.
* Each WinNetMon:// stanza represents an individually configured network
  monitoring input.  The value of "<name>" matches what was specified
  in Splunk Web. Splunk recommends that you use Splunk Web to
  configure Network Monitor inputs because it is easy to mistype
  the values for Network Monitor objects.

remoteAddress = <regular expression>
* A regular expression that represents the remote IP address of a
  host that is involved in network communication.
* This setting accepts a regular expression that matches against
  IP addresses only, not host names. For example: 192\.163\..*
* The input includes events for remote IP addresses that match
  the regular expression that you specify here.
* The input filters out events for remote IP addresses that do not
  match the regular expression.
* Defaults to unset (including all remote address events).

process = <regular expression>
* A regular expression that represents the process or application that
  performed a network access.
* The input includes events for processes that match the
  regular expression that you specify here.
* The input filters out events for processes that do not match the
  regular expression.
* Defaults to unset (including all processes and application events).

user = <regular expression>
* A regular expression that represents the Windows user name that
  performed a network access.
* The input includes events for user names that match the
  regular expression that you specify here.
* The input filters out events for user names that do not match the
  regular expression.
* Defaults to unset (including all user name events).

addressFamily = ipv4;ipv6
* Determines the events to include by network address family.
* Setting ipv4 alone will include only TCP/IP v4 packets, while ipv6 alone
  will include only TCP/IP v6 packets.
* To specify both families, separate them with a semicolon.
  For example: ipv4;ipv6
* Defaults to unset (including events with both address families).

packetType = connect;accept;transport.
* Determines the events to include by network packet type.
* To specify multiple packet types, separate them with a semicolon.
  For example: connect;transport
* Defaults to unset (including events with any packet type).

direction = inbound;outbound
* Determines the events to include by network transport direction.
* To specify multiple directions, separate them with a semicolon.
  For example: inbound;outbound
* Defaults to unset (including events with any direction).

protocol = tcp;udp
* Determines the events to include by network protocol.
* To specify multiple protocols, separate them with a semicolon.
  For example: tcp;udp
* For more information about protocols, see
  http://www.ietf.org/rfc/rfc1700.txt
* Defaults to unset (including events with all protocols).

readInterval = <integer>
* How often, in milliseconds, that the input should read the network
  kernel driver for events.
* Advanced option. Use the default value unless there is a problem
  with input performance.
* Set this to adjust the frequency of calls into the network kernel driver.
* Choosing lower values (higher frequencies) can reduce network
  performance, while higher numbers (lower frequencies) can cause event
  loss.
* The minimum allowed value is 10 and the maximum allowed value is 1000.
* Defaults to unset, handled as 100 (msec).

driverBufferSize = <integer>
* The maximum number of packets that the network kernel driver retains 
  for retrieval by the input.
* Set to adjust the maximum number of network packets retained in
  the network driver buffer.
* Advanced option. Use the default value unless there is a problem
  with input performance.
* Configuring this setting to lower values can result in event loss, while
  higher values can increase the size of non-paged memory on the host.
* The minimum allowed value is 128 and the maximum allowed value is 32768.
* Defaults to unset, handled as 32768 (packets).

userBufferSize = <integer>
* The maximum size, in megabytes, of the user mode event buffer.
* Controls amount of packets cached in the the user mode.
* Advanced option. Use the default value unless there is a problem
  with input performance.
* Configuring this setting to lower values can result in event loss, while
  higher values can increase the amount of memory that the network
  monitor uses.
* The minimum allowed value is 20 and the maximum allowed value is 500.
* Defaults to unset, handled as 20 (megabytes).

mode = single|multikv
* Specifies how the network monitor input generates events.
* Set to 'single' to generate one event per packet, or 'multikv' to
  generate combined events of many packets in multikv format (many packets
  described in a single table as one event).
* Defaults to single.

multikvMaxEventCount = <integer>
* The maximum number of packets to combine in multikv format when you set
  the 'mode' setting to 'multikv'.
* Has no effect when 'mode' is set to 'single'.
* Advanced option.
* The minimum allowed value is 10 and the maximum allowed value is 500.
* Defaults to 100.

multikvMaxTimeMs = <integer>
* The maximum amount of time, in milliseconds, to accumulate packet data to
  combine into a large tabular event in multikv format.
* Has no effect when 'mode' is set to 'single'.
* Advanced option.
* The minimum allowed value is 100 and the maximum allowed value is 5000.
* Defaults to 1000.

sid_cache_disabled = 0|1
* Enables or disables account Security IDentifier (SID) cache.
* This setting is global. It affects all Windows Network Monitor stanzas.
* Defaults to 0.

sid_cache_exp = <time in seconds>
* The expiration time for account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Network Monitor stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 3600.

sid_cache_exp_neg = <time in seconds>
* The expiration time for negative account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Network Monitor stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 31536000.
* Defaults to 10.

sid_cache_max_entries = <number of entries>
* The maximum number of account SID cache entries.
* This setting is optional.
* This setting is global. It affects all Windows Network Monitor stanzas.
* The minimum allowed value is 10 and the maximum allowed value is 40000.
* Defaults to 10.

disabled = 0|1
* Whether or not the input is enabled.
* Defaults to 0 (enabled.)

index = <string>
* The index that this input should send the data to.
* This setting is optional.
* Defaults to the default index.

[powershell://<name>]
* Runs Windows PowerShell version 3 commands or scripts.

script = <command>
* A PowerShell command-line script or .ps1 script file that the input
  should run.
* There is no default.

schedule = [<number>|<cron schedule>]
* How often to run the specified PowerShell command or script.
* You can specify a number in seconds, or provide a valid cron
  schedule.
* Defaults to running the command or script once, at startup.

[powershell2://<name>]
* Runs Windows PowerShell version 2 commands or scripts.

script = <command>
* A PowerShell command-line script or .ps1 script file that the input
  should run.

schedule = <schedule>
* How often to run the specified PowerShell command or script.
* You can provide a valid cron schedule.
* Defaults to running the command or script once, at startup.
