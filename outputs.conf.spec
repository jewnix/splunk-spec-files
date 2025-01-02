#   Version 9.4.0
#
# Forwarders require outputs.conf. Splunk instances that do not forward
# do not use it. Outputs.conf determines how the forwarder sends data to
# receiving Splunk instances, either indexers or other forwarders.
#
# To configure forwarding, create an outputs.conf file in
# $SPLUNK_HOME/etc/system/local/. For examples of its use, see
# outputs.conf.example.
#
# You must restart the Splunk software to enable configurations.
#
# To learn more about configuration files (including precedence) see the topic
# "About Configuration Files" in the Splunk Enterprise Admin manual.
#
# To learn more about forwarding, see the topic "About forwarding and
# receiving data" in the Splunk Enterprise Forwarding manual.

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top
#     of the file.
#   * Each conf file should have at most one default stanza. If there are
#     multiple default stanzas, settings are combined. In the case of
#     multiple definitions of the same setting, the last definition in the
#     file wins.
#   * If an setting is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.
#   * Do not use the 'sslPassword', 'socksPassword', or 'token' settings
#     to set passwords in this stanza as they may remain readable to
#     attackers, specify these settings in the [tcpout] stanza instead.

####
# TCP Output stanzas
####

# There are three levels of TCP Output stanzas:
# * Global: [tcpout]
# * Target group: [tcpout:<target_group>]
# * Single server: [tcpout-server://<ip address>:<port>]
#
# Settings at more specific levels override settings at higher levels. For
# example, an setting set for a single server overrides the value of that
# setting, if any, set at that server's target group stanza. See the
# online documentation on configuring forwarders for details.
#
# This spec file first describes the three levels of stanzas (and any
# settings unique to a particular level). It then describes the optional
# settings, which you can set at any of the three levels.
# Default: true
# If set to 'true', prevents the logs from being forwarded to the indexing tiers.

#----TCP Output Global Configuration -----
# You can overwrite the global configurations specified here in the
# [tcpout] stanza in stanzas for specific target groups, as described later.
# You can only set the 'defaultGroup' and 'indexAndForward' settings
# here, at the global level.
#
# Starting with version 4.2, the [tcpout] stanza is no longer required.

[tcpout]

defaultGroup = <comma-separated list>
* A comma-separated list of one or more target group names, specified later
  in [tcpout:<target_group>] stanzas.
* The forwarder sends all data to the specified groups.
* If you don't want to forward data automatically, don't configure this setting.
* Can be overridden by the '_TCP_ROUTING' setting in the inputs.conf file, 
  which in turn can be overridden by a props.conf or transforms.conf modifier.
* Starting with version 4.2, this setting is no longer required.

indexAndForward = <boolean>
* Set to "true" to index all data locally, in addition to forwarding it.
* This is known as an "index-and-forward" configuration.
* This setting is only available for heavy forwarders.
* This setting is only available at the top level [tcpout] stanza. It
  cannot be overridden in a target group.
* Default: false

enableOldS2SProtocol = <boolean>
* Whether or not the forwarder enables use of versions 3 and lower of the Splunk-to-Splunk protocol,
  otherwise known as the "old" S2S protocol, to connect with other Splunk platform instances.
* A value of "true" means the forwarder can use the old protocol, depending on other settings
  you configure.
* A value of "false" means the forwarder uses only version 4 of the S2S protocol,
  and does not use any of the old protocol versions.
* When you disable the use of old S2S protocols, forwarders always use the new protocol. Indexers
  that run a version of Splunk Enterprise below 6.0 only support the old protocol, and forwarders
  can't connect to those indexers over S2S.
* If you give 'negotiateProtocolLevel' a value of 0, or 'negotiateNewProtocol' a value of 
  "false" in inputs.conf or outputs.conf to use the old S2S protocol, the forwarder will instead override these
  settings to use the lowest protocol version that all instances support.
* This setting is only available for configuration at the top level [tcpout] stanza. You 
  can't override it in a target group with settings that force usage of the older protocol.
* Default: false

certRotationCheckInterval = <positive integer>[s|m|h|d]
* The interval between attempts to rotate forwarder certificates automatically.
* This setting is valid on forwarders only. It does not work
  with other Splunk platform instances. 
* Default: 1d

#----Target Group Configuration -----

# If you specify multiple servers in a target group, the forwarder
# performs auto load-balancing, sending data alternately to each available
# server in the group. For example, assuming you have three servers
# (server1, server2, server3) and autoLBFrequency=30, the forwarder sends
# all data to server1 for 30 seconds, then it sends all data to server2 for
# the next 30 seconds, then all data to server3 for the next 30 seconds,
# finally cycling back to server1.
#
# You can have as many target groups as you want.
# If you specify more than one target group, the forwarder sends all data
# to each target group. This is known as "cloning" the data.
#
# NOTE: A target group stanza name cannot contain spaces or colons.
# Splunk software ignores target groups whose stanza names contain
# spaces or colons.

[tcpout:<target_group>]

server = <comma-separated list>
* A comma-separated list of one or more systems to send data to over a
  TCP socket.
* You can specify each element as either an IP address or a hostname
  and a port number. For example: 192.168.1.10:9997, mysplunkserver.com:9997
* Required if the 'indexerDiscovery' setting is not set.
* Typically used to specify receiving Splunk systems, although you can use
  it to send data to non-Splunk systems (see the 'sendCookedData' setting).
* For each system you list, the following information is required:
  * The IP address or server name where one or more systems are listening.
  * The port on which the syslog server is listening.

blockWarnThreshold = <integer>
* The output pipeline send failure count threshold after which a
  failure message appears as a banner in Splunk Web.
* Optional.
* To disable Splunk Web warnings on blocked output queue conditions, set this
  to a large value (for example, 2000000).
* Default: 100

indexerDiscovery = <string>
* The name of the manager node to use for indexer discovery.
* Instructs the forwarder to fetch the list of indexers from the manager node
  specified in the corresponding [indexer_discovery:<name>] stanza.
* No default.

token = <string>
* The access token for receiving data.
* If you configured an access token for receiving data from a forwarder,
  Splunk software populates that token here.
* If you configured a receiver with an access token and that token is not
  specified here, the receiver rejects all data sent to it.
* This setting is optional.
* No default.

queueSize = <integer>[KB|MB|GB]
* See the description of 'queueSize' in the inputs.conf specification file
  for details on this setting.
* If you do not set a value for 'persistentQueueSize', splunkd
  ignores the value for 'queueSize'.
* Default: 0 (no in-memory part of persistent queue)

persistentQueueSize = <integer>[KB|MB|GB|TB]
* See the description of 'persistentQueueSize' in the inputs.conf specification file
  for details on this setting.
* Splunkd applies this limit for each target group for each ingestion pipeline.
* If both the 'queueSize' and 'maxQueueSize' settings have values of 0, the tcpout
  persistent queue becomes a disk-only queue.
* The naming convention of the persistent queue file on disk is
  "pq_<group-name>_<pipeline number>".
  * For example, if you set "parallelIngestionPipelines=2" in server.conf,
  * with two target groups 'splunk-group1' and 'splunk-group2', the
    persistent queue files appear as follows:
    * $SPLUNK_HOME/var/run/splunk/tcpout/pq_splunk-group1_0
    * $SPLUNK_HOME/var/run/splunk/tcpout/pq_splunk-group1_1
    * $SPLUNK_HOME/var/run/splunk/tcpout/pq_splunk-group2_0
    * $SPLUNK_HOME/var/run/splunk/tcpout/pq_splunk-group2_1
* Default: 0 (no on-disk persistent queue)

#----Single server configuration-----

# You can define specific configurations for individual indexers on a
# server-by-server basis. However, each server must also be part of a
# target group.

[tcpout-server://<ip address>:<port>]
* Optional. There is no requirement to have a [tcpout-server] stanzas.

#####
#TCPOUT SETTINGS
#####

# These settings are optional and can appear in any of the three stanza levels.

[tcpout<any of above>]

#----General Settings----

disabled = <boolean>
* Whether or not to disable forwarding to the receiver or output group, as defined by the forwarding stanza.
* Set to true to disable forwarding to this receiver or output group.
* Default: false

sendCookedData = <boolean>
* Whether or not to send processed or unprocessed data to the receiving server.
* A value of "true" means Splunk software processes the events before sending them
  to the server, thus "cooking" them.
* A value of "false" means events are raw and untouched prior to sending.
* Set to "false" if you are sending events to a third-party system.
* Default: true

heartbeatFrequency = <integer>
* How often, in seconds, to send a heartbeat packet to the receiving server.
* This setting is a mechanism for the forwarder to know that the receiver
  (indexer) is alive. If the indexer does not send a return packet to the
  forwarder, the forwarder declares the receiver unreachable and does not
  forward data to it.
* The forwarder only sends heartbeats if the 'sendCookedData' setting
  is set to "true".
* Default: 30

blockOnCloning = <boolean>
* Whether or not the tcpout processor blocks, or stops processing events,
  in situations where they cannot be sent to cloned output target groups.
* This setting only applies when you have defined multiple output target 
  groups for a forwarder, and are thus cloning the data. It does not
  apply to single output groups.
* A value of "true" means that when a situation occurs where all target groups
  that you have defined are unable to receive events, then the tcpout
  processor waits for 'dropClonedEventsonQueueFull' seconds before
  it begins to drop events.
  * If 'dropClonedEventsonQueueFull' has a value of "-1", then the tcpout 
    processor stops processing events indefinitely. This prevents the tcpout
    processor from dropping events, but can cause further blocking up
    the processing chain.
  * See the 'dropClonedEventsonQueueFull' setting description for 
    additional information on the setting.
* A value of "false" means the tcpout processor drops events as soon
  as all cloned output groups are down and the queues for those groups
  fill up.
* If at least one output group is up and at least one queue for 
  the group is not full, then the processor does not drop events.
* Default: true (stop processing events when an output group blockage
  occurs, but do not drop events for at least
  'dropClonedEventsOnQueueFull' seconds)

blockWarnThreshold = <integer>
* The output pipeline send failure count threshold, after which a
  failure message appears as a banner in Splunk Web.
* To disable Splunk Web warnings on blocked output queue conditions, set this
  to a large value (for example, 2000000).
* This setting is optional.
* Default: 100

compressed = <boolean>
* Whether or not forwarders and receivers communicate with one another in 
  compressed format.
* A value of "true" means the receiver communicates with the forwarder in
  compressed format for forwarding that does not use TLS/SSL.
* A value of "true" means the receiver communicates with the forwarder in
  compressed format for TLS/SSL forwarding if either
  'useClientSSLCompression' has a value of "false" or the TLS/SSL
  connection does not use 'zlib' compression.
* If set to "true", you do not need to set the 'compressed' setting to
  "true" in the inputs.conf file on the receiver for compression of data
  to occur.
* If you use this setting, the 'tcpout_connections' group in the metrics.log
  file shows throughput values after compression has occurred.
* Default: false

negotiateProtocolLevel = <unsigned integer>
* When setting up a connection to an indexer, Splunk software tries to
  negotiate the use of the Splunk forwarder protocol with the
  specified feature level based on the value of this setting.
* If set to a lower value than the default, this setting denies the
  use of newer forwarder protocol features when it negotiates a connection.
  This might impact indexer efficiency.
* Default (if 'negotiateNewProtocol' is "true"): 1
* Default (if 'negotiateNewProtocol' is not "true"): 0

negotiateNewProtocol = <boolean>
* The default value of the 'negotiateProtocolLevel' setting.
* DEPRECATED. Set 'negotiateProtocolLevel' instead.
* Default: true

channelReapInterval = <integer>
* How often, in milliseconds, that channel codes are reaped, or made
  available for re-use.
* This value sets the minimum time between reapings. In practice,
  consecutive reapings might be separated by greater than the number of
  milliseconds specified here.
* Default: 60000 (1 minute)

channelTTL = <integer>
* How long, in milliseconds, a channel can remain "inactive" before
  it is reaped, or before its code is made available for reuse by a
  different channel.
* Default: 300000 (5 minutes)

channelReapLowater = <integer>
* This value essentially determines how many active-but-old channels Splunk
  software keeps "pinned" in memory on both sides of a
  Splunk-to-Splunk connection.
* If the number of active channels is greater than 'channelReapLowater',
  Splunk software reaps old channels to make their channel codes available
  for re-use.
* If the number of active channels is less than 'channelReapLowater',
  Splunk software does not reap channels, no matter how old they are.
* A non-zero value helps ensure that Splunk software does not waste network
  resources by "thrashing" channels in the case of a forwarder sending
  a trickle of data.
* Default: 10

socksServer = <string>
* The IP address or server name of the Socket Secure version 5 (SOCKS5) server.
* Required. Specify this value as either an IP address or hostname and port
  number, for example: 192.168.1.10:8080 or mysplunkserver.com:8080.
* This setting specifies the port on which the SOCKS5 server is listening.
* After you configure and restart the forwarder, it connects to the SOCKS5
  proxy host, and optionally authenticates to the server on demand if
  you provide credentials.
* NOTE: Only SOCKS5 servers are supported.
* No default.

socksUsername = <string>
* The SOCKS5 username to use when authenticating against the SOCKS5 server.
* Optional.

socksPassword = <string>
* The SOCKS5 password to use when authenticating against the SOCKS5 server.
* Optional.

socksResolveDNS = <boolean>
* Whether or not a forwarder should rely on the SOCKS5 proxy server Domain
  Name Server (DNS) to resolve hostnames of indexers in the output group to 
  which the forwarder sends data.
* A value of "true" means the forwarder sends the hostnames of the indexers to the
  SOCKS5 server, and lets the SOCKS5 server do the name resolution. It
  does not attempt to resolve the hostnames on its own.
* A value of "false" means the forwarder attempts to resolve the hostnames of the
  indexers through DNS on its own.
* Optional.
* Default: false

#----Queue Settings----

maxQueueSize = [<integer>|<integer>[KB|MB|GB]|auto]
* The maximum size of the forwarder output queue.
* The size can be limited based on the number of entries, or on the total
  memory used by the items in the queue.
* If specified as a lone integer (for example, "maxQueueSize=100"),
  the 'maxQueueSize' setting indicates the maximum count of queued items.
* If specified as an integer followed by KB, MB, or GB
  (for example, maxQueueSize=100MB), the 'maxQueueSize' setting indicates
  the maximum random access memory (RAM) size of all the items in the queue.
* If set to "auto", this setting configures a value for the output queue
  depending on the value of the 'useACK' setting:
  * If 'useACK' is set to "false", the output queue uses 500KB.
  * If 'useACK' is set to "true", the output queue uses 7MB.
* If you enable indexer acknowledgment by configuring the 'useACK'
  setting to "true", the forwarder creates a wait queue where it temporarily
  stores data blocks while it waits for indexers to acknowledge the receipt
  of data it previously sent.
  * The forwarder sets the wait queue size to triple the value of what
    you set for 'maxQueueSize.'
  * For example, if you set "maxQueueSize=1024KB" and "useACK=true",
    then the output queue is 1024KB and the wait queue is 3072KB.
  * Although the wait queue and the output queue sizes are both controlled
    by this setting, they are separate.
  * The wait queue only exists if 'useACK' is set to "true".
* Limiting the queue sizes by quantity is historical. However,
  if you configure queues based on quantity, keep the following in mind:
  * Queued items can be events or blocks of data.
    * Non-parsing forwarders, such as universal forwarders, send
      blocks, which can be up to 64KB.
    * Parsing forwarders, such as heavy forwarders, send events, which
      are the size of the events. Some events are as small as
      a few hundred bytes. In unusual cases (data dependent), you might
      arrange to produce events that are multiple megabytes.
* Default: auto
  * if 'useACK' is set to "true" and this setting is set to "auto", then
    the output queue is 7MB and the wait queue is 21MB.

dropEventsOnQueueFull = <integer>[ms|s|m]
* The amount of time to wait before the output queue throws out all
  new events until it has space.
* If set to 0ms(milliseconds), 0s(seconds), or 0m(minutes),
  the queue immediately throws out all new events until it has space.
* If set to a positive number, the queue waits the specified number of
  milliseconds, seconds, or minutes before throwing out all new events.
  If "ms", "s", or "m" is not specified, the default unit is seconds. 
* If set to -1 or 0, the output queue is blocked because it is full, but events 
  are not dropped. 
* If any target group queue is blocked, no more data reaches any other
  target group.
* CAUTION: Do not set to a positive integer if you are monitoring files 
  because the files will not be fully ingested if the queue remains blocked
  for the specified amount of time.
* Default: -1

dropClonedEventsOnQueueFull = <integer>[ms|s|m]
* The amount of time to wait before dropping events from the group.
* If set to 0ms(milliseconds), 0s(seconds), or 0m(minutes), the queue 
  immediately throws out all new events until it has space.
* If set to a positive number, the queue does not block completely, but
  waits up to the specified number of milliseconds, seconds, or minutes to 
  queue events to a group.
  * If it cannot queue to a group for more than the specified amount of time, 
    the queue begins dropping events from the group and makes sure that at
    least one group in the cloning configuration can receive events.
  * The queue blocks if it cannot deliver events to any of the cloned groups.
* If set to -1, the TcpOutputProcessor ensures that each group
  receives all of the events. If one of the groups is down, the
  TcpOutputProcessor blocks everything.
* Default: 5 seconds

#######
# Backoff Settings When Unable To Send Events to Indexer
# The settings in this section determine forwarding behavior when there are
# repeated failures in sending events to an indexer ("sending failures").
#######

maxFailuresPerInterval = <integer>
* The maximum number of failures allowed per interval before a forwarder
  applies backoff (stops sending events to the indexer for a specified
  number of seconds). The interval is defined in the 'secsInFailureInterval'
  setting.
* Default: 2

secsInFailureInterval = <integer>
* The number of seconds contained in a failure interval.
* If the number of write failures to the indexer exceeds
  'maxFailuresPerInterval' in the specified 'secsInFailureInterval' seconds,
  the forwarder applies backoff.
* The backoff time period range is 1-10 * 'autoLBFrequency'.
* Default: 1

backoffOnFailure = <positive integer>
* The number of seconds a forwarder backs off, or stops sending events,
  before attempting to make another connection with the indexer.
* Default: 30

maxConnectionsPerIndexer = <integer>
* The maximum number of allowed connections per indexer.
* In the presence of failures, the maximum number of connection attempts
  per indexer at any point in time.
* Default: 2

connectionsPerTarget = [<integer>|auto]
* The maximum number of allowed outbound connections for each target IP address
  as resolved by DNS on the machine.
* A value of "auto" or < 1 means splunkd configures a value for connections for each
  target IP address. Depending on the number of IP addresses that DNS resolves,
  splunkd sets 'connectionsPerTarget' as follows:
  * If the number of resolved target IP addresses is greater than or equal to 10,
    'connectionsPerTarget' gets a value of 1.
  * If the number of resolved target IP addresses is greater than 5
    and less than 10, 'connectionsPerTarget' gets a value of 2.
  * If the number of resolved target IP addresses is greater than 3
    or less than equal to 5, 'connectionsPerTarget' gets a value of 3.
  * If the number of resolved target IP addresses is less than or equal to 3,
    'connectionsPerTarget' gets a value of 4.
* Default: auto

connectionTimeout = <integer>
* The time to wait, in seconds, for a forwarder to establish a connection
  with an indexer.
* The connection times out if an attempt to establish a connection
  with an indexer does not complete in 'connectionTimeout' seconds.
* Default: 20

readTimeout = <integer>
* The time to wait, in seconds, for a forwarder to read from a socket it has
  created with an indexer.
* The connection times out if a read from a socket does not complete in
  'readTimeout' seconds.
* This timeout is used to read acknowledgment when indexer acknowledgment is
  enabled (when you set 'useACK' to "true").
* Default: 300 seconds (5 minutes)

writeTimeout = <integer>
* The time to wait, in seconds, for a forwarder to complete a write to a
  socket it has created with an indexer.
* The connection times out if a write to a socket does not finish in
  'writeTimeout' seconds.
* Default: 300 seconds (5 minutes)

connectionTTL = <integer>
* The time, in seconds, for a forwarder to keep a socket connection
  open with an existing indexer despite switching to a new indexer.
* This setting reduces the time required for indexer switching.
* Useful during frequent indexer switching potentially caused
  by using the 'autoLBVolume' setting.
* Default: 0 seconds

tcpSendBufSz = <integer>
* The size of the TCP send buffer, in bytes.
* Only use this setting if you are a TCP/IP expert.
* Useful to improve throughput with small events, like Windows events.
* Default: the system default

ackTimeoutOnShutdown = <integer>
* The time to wait, in seconds, for the forwarder to receive indexer
  acknowledgments during a forwarder shutdown.
* The connection times out if the forwarder does not receive indexer
  acknowledgements (ACKs) in 'ackTimeoutOnShutdown' seconds during
  forwarder shutdown.
* Default: 30 seconds

polling_interval = <integer>
* The initial time to wait upon splunk start, in seconds, for the forwarder to fetch
  the list of indexers from the indexer discovery server specified in
  the corresponding [indexer_discovery:<name>] stanza. Subsequently polling interval
  is set by indexer discovery server response.
* Default: 5 seconds

dnsResolutionInterval = <integer>
* The base time interval, in seconds, at which indexer Domain Name Server
  (DNS) names are resolved to IP addresses.
* This is used to compute runtime dnsResolutionInterval as follows:
  Runtime interval =
   'dnsResolutionInterval' + (number of indexers in server settings - 1) * 30.
* The DNS resolution interval is extended by 30 seconds for each additional
  indexer in the server setting.
* Default: 300 seconds (5 minutes)

forceTimebasedAutoLB = <boolean>
* Forces existing data streams to switch to a newly elected indexer every
  auto load balancing cycle.
* On universal forwarders, use the 'EVENT_BREAKER_ENABLE' and
  'EVENT_BREAKER' settings in props.conf rather than 'forceTimebasedAutoLB'
  for improved load balancing, line breaking, and distribution of events.
* Default: false

#----Index Filter Settings.
# These settings are only applicable under the global [tcpout] stanza.
# This filter does not work if it is created under any other stanza.

forwardedindex.<n>.whitelist = <regular expression>
forwardedindex.<n>.blacklist = <regular expression>
* These filters determine which events get forwarded to the index,
  based on the indexes the events are targeted to.
* An ordered list of allow lists and deny lists, which together
  decide if events are forwarded to an index.
* The order is determined by <n>. <n> must start at 0 and continue with
  positive integers, in sequence. There cannot be any gaps in the sequence.
  * For example:
    forwardedindex.0.whitelist, forwardedindex.1.blacklist,
    forwardedindex.2.whitelist, ...
* The filters can start from either whitelist or blacklist. They are tested
  from forwardedindex.0 to forwardedindex.<max>.
* If both 'forwardedindex.<n>.whitelist' and 'forwardedindex.<n>.blacklist' are
  present for the same value of n, then 'forwardedindex.<n>.whitelist' is
  honored. 'forwardedindex.<n>.blacklist' is ignored in this case.
* In general, you do not need to change these filters from their default
  settings in $SPLUNK_HOME/system/default/outputs.conf.
* Filtered out events are not indexed if you do not enable local indexing.

forwardedindex.filter.disable = <boolean>
* Whether or not index filtering is active.
* A value of "true" means index filtering is disabled. Events for all indexes
  are then forwarded.
* Default: false

#----Automatic Load-Balancing
# Automatic load balancing is the only way to forward data.
# Round-robin method of load balancing is no longer supported.

autoLBFrequency = <integer>
* The amount of time, in seconds, that a forwarder sends data to an indexer
  before redirecting outputs to another indexer in the pool.
* Use this setting when you are using automatic load balancing of outputs
  from universal forwarders (UFs).
* Every 'autoLBFrequency' seconds, a new indexer is selected randomly from the
  list of indexers provided in the server setting of the target group
  stanza.
* Default: 30

autoLBFrequencyIntervalOnGroupFailure = <integer>
* When the entire target group is not reachable,
  'autoLBFrequencyIntervalOnGroupFailure' is the amount of time, in seconds,
  that a forwarder waits before attempting to connect to a target host in the
  group.
* While 'autoLBFrequencyIntervalOnGroupFailure' is in effect, 'autoLBFrequency'
  is ignored. Once first connection is established to a group, 'autoLBFrequency'
  comes into effect again.
* This setting is applied only when
  'autoLBFrequencyIntervalOnGroupFailure' is less than 'autoLBFrequency'.
* Every 'autoLBFrequencyIntervalOnGroupFailure' seconds, a new indexer is
  selected randomly from the list of indexers provided in the server setting
  of the target group stanza.
* -1 means this setting is not active.
* Default: -1

autoLBVolume = <integer>
* The volume of data, in bytes, to send to an indexer before a new indexer
  is randomly selected from the list of indexers provided in the server
  setting of the target group stanza.
* This setting is closely related to the 'autoLBFrequency' setting.
  The forwarder first uses 'autoLBVolume' to determine if it needs to
  switch to another indexer. If the 'autoLBVolume' is not reached,
  but the 'autoLBFrequency' is, the forwarder switches to another
  indexer as the forwarding target.
* A non-zero value means that volume-based forwarding is active.
* 0 means the volume-based forwarding is not active.
* Default: 0

maxSendQSize = <integer>
* The size of the tcpout client send buffer, in bytes.
  If tcpout client(indexer/receiver connection) send buffer is full,
  a new indexer is randomly selected from the list of indexers provided
  in the server setting of the target group stanza.
* This setting allows forwarder to switch to new indexer/receiver if current
  indexer/receiver is slow.
* A non-zero value means that max send buffer size is set.
* 0 means no limit on max send buffer size.
* Default: 0

autoBatch = <boolean>
* When set to 'true', the forwarder automatically sends chunks/events in batches
  to target receiving instance connection. The forwarder creates batches only
  if there are two or more chunks/events available in output connection queue.
* When set to 'false', the forwarder sends one chunk/event to target receiving
  instance connection. This is old legacy behavior.
* Default: true

#----Secure Sockets Layer (SSL) Settings----

# To set up SSL on the forwarder, set the following setting/value pairs.
# If you want to use SSL for authentication, add a stanza for each receiver
# that must be certified.

useSSL = <true|false|legacy>
* Whether or not the forwarder uses SSL to connect to the receiver, or relies
  on the 'clientCert' setting to be active for SSL connections.
* You do not need to set 'clientCert' if 'requireClientCert' is set to
  "false" on the receiver.
* A value of "true" means the forwarder uses SSL to connect to the receiver.
* A value of "false" means the forwarder does not use SSL to connect to the
  receiver.
* The special value "legacy" means the forwarder uses the 'clientCert' property to
  determine whether or not to use SSL to connect.
* Default: legacy

sslPassword = <password>
* The password associated with the Certificate Authority certificate (CAcert).
* The default Splunk CAcert uses the password "password".
* No default.

clientCert = <path>
* The full path to the client SSL certificate in Privacy Enhanced Mail (PEM)
  format.
* If you have not set 'useSSL', then this connection uses SSL if and only if
  you specify this setting with a valid client SSL certificate file.
* No default.

sslCertPath = <path>
* DEPRECATED.
* Use the 'clientCert' setting instead.
* The full path to the client SSL certificate.

cipherSuite = <string>
* The specified cipher string for the input processors.
* This setting ensures that the server does not accept connections using weak
  encryption protocols.
* The default can vary. See the 'cipherSuite' setting in
  $SPLUNK_HOME/etc/system/default/outputs.conf for the current default.

sslCipher = <string>
* The specified cipher string for the input processors.
* DEPRECATED.
* Use the 'cipherSuite' setting instead.

ecdhCurves = <comma-separated list>
* A list of Elliptic Curve-Diffie-Hellmann curves to use for ECDH
  key negotiation.
* The curves should be specified in the order of preference.
* The client sends these curves as a part of an SSL Client Hello.
* The server supports only the curves specified in the list.
* Splunk software only supports named curves that have been specified
  by their SHORT names.
* The list of valid named curves by their short and long names can be obtained
  by running this CLI command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Example setting: "ecdhCurves = prime256v1,secp384r1,secp521r1"
* The default can vary. See the 'ecdhCurves' setting in
  $SPLUNK_HOME/etc/system/default/outputs.conf for the current default.

sslRootCAPath = <path>
* The full path to the root Certificate Authority (CA) certificate store.
* DEPRECATED.
* Use the 'server.conf/[sslConfig]/sslRootCAPath' setting instead.
* Used only if 'sslRootCAPath' in server.conf is not set.
* The <path> must refer to a PEM format file containing one or more root
  CA certificates concatenated together.
* No default.

sslVerifyServerCert = <boolean>
* Serves as an additional step for authenticating your indexers.
* A value of "true" ensures that the server you are connecting to has a valid
  SSL certificate. 
  * NOTE: Certificates with the same Common Name as the CA's certificate 
    will fail this check.
* Both the common name and the alternate name of the server are then checked
  for a match.
* Default: false

tlsHostname = <string>
* A Transport Layer Security (TLS) extension that allows sending an identifier
  with SSL Client Hello.
* Default: empty string

sslVerifyServerName = <boolean>
* Whether or not splunkd, as a client, performs a TLS hostname validation check
  on an SSL certificate that it receives upon an initial connection
  to a server.
* A TLS hostname validation check ensures that a client
  communicates with the correct server, and has not been redirected to
  another by a machine-in-the-middle attack, where a malicious party inserts
  themselves between the client and the target server, and impersonates
  that server during the session.
* Specifically, the validation check forces splunkd to verify that either
  the Common Name or the Subject Alternate Name in the certificate that the
  server presents to the client matches the host name portion of the URL that
  the client used to connect to the server.
* For this setting to have any effect, the 'sslVerifyServerCert' setting must
  have a value of "true". If it doesn't, TLS hostname validation is not possible
  because certificate verification is not on.
* A value of "true" for this setting means that splunkd performs a TLS hostname
  validation check, in effect, verifying the server's name in the certificate.
  If that check fails, splunkd terminates the SSL handshake immediately. This terminates
  the connection between the client and the server. Splunkd logs this failure at
  the ERROR logging level.
* A value of "false" means that splunkd does not perform the TLS hostname
  validation check. If the server presents an otherwise valid certificate, the
  client-to-server connection proceeds normally.
* Default: false

sslCommonNameToCheck = <comma-separated list>
* Checks the Common Name of the server's certificate against one or more of the
  names you specify for this setting.
* Separate multiple common names with commas.
* The Common Name identifies the host name associated with the certificate.
  For example, example www.example.com or example.com
* If there is no match, assume that Splunk software is not authenticated
  against this server.
* You must set the 'sslVerifyServerCert' setting to "true" for this setting
  to work.
* This setting is optional.
* Default: empty string (no common name checking).

sslAltNameToCheck = <comma-separated list>
* Checks the alternate name of the server's certificate against one or more of
  the names you specify for this setting.
* Separate multiple subject alternate names with commas.
* If there is no match, assume that Splunk software is not authenticated
  against this server.
* You must set the 'sslVerifyServerCert' setting to "true" for this setting to work.
* This setting is optional.
* Default: no alternate name checking

useClientSSLCompression = <boolean>
* Whether or not compression on TLS/SSL connections is enabled.
* Server-side compression in splunkd is on by default. Configuring this
  setting on the client side enables compression between both server and
  client.
* If server-side compression is off, this client-side setting has no effect.
* A value of "true" means compression on TLS/SSL is enabled.
* If you use this setting, the 'tcpout_connections' group in the metrics.log
  file shows throughput values before compression occurs.
* Default: true

sslQuietShutdown = <boolean>
* Enables quiet shutdown mode in SSL.
* Default: false

sslVersions = <comma-separated list>
* A comma-separated list of SSL versions to support.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2"
* The special version "*" selects all supported versions. The version "tls"
  selects all versions tls1.0 or newer
* If you prefix a version with "-", it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list, but
  does nothing.
* When configured in FIPS mode, "ssl3" is always disabled regardless
  of this configuration.
* The default can vary. See the 'sslVersions' setting in
  $SPLUNK_HOME/etc/system/default/outputs.conf for the current default.

#----Forwarder Certificate Renewal Settings----

autoCertRotation = <boolean>
* Whether or not forwarders attempt to renew TLS certificates that they use 
  before the certificates expire.
* TLS certificates expire after a certain period of validity. When a forwarder has been
  configured to use a TLS certificate for network connections, it can attempt to renew
  the certificate automatically up to and including the certificate expiration time.
* Forwarder certificate renewal works with forwarders that connect to Splunk Cloud
  Platform instances only.
* A forwarder performs a check every 'certRotationCheckInterval' to determine if a forwarder
  certificate needs renewal.
* A TLS certificate meets renewal criteria when:
  * It has been configured for the forwarder to use it
  * It is within its validity window, which means the current date must be between
    its 'Not Before' and 'Not After' dates, inclusive
  * Less than or equal to 50% of its validity period remains. For example, a certificate with a
    validity period of 52 weeks is eligible for renewal after 26 weeks from its start of validity.
* A certificate that has not been renewed remains until it either expires
  or the forwarder successfully completes forwarder certificate renewal.
* After forwarder certificate renewal is complete, the renewed certificate replaces the existing one.
* A value of "true" means that the forwarder attempts to automatically perform forwarder certificate renewal
  check and attempts to renew the certificate until the certificate successfully renews.
* A value of "false" means that the forwarder does not attempt to perform forwarder certificate renewal.
* Default: false

#----Indexer Acknowledgment ----
# Indexer acknowledgment ensures that forwarded data is reliably delivered
# to the receiver.
#
# If the receiver is an indexer, it indicates that the indexer has received
# the data, indexed it, and written it to the file system. If the receiver
# is an intermediate forwarder, it indicates that the intermediate forwarder
# has successfully forwarded the data to the terminating indexer and has
# received acknowledgment from that indexer.
#
# Indexer acknowledgment is a complex feature that requires
# careful planning. Before using it, read the online topic describing it in
# the Splunk Enterprise Distributed Deployment manual.

useACK = <boolean>
* Whether or not to use indexer acknowledgment.
* Indexer acknowledgment is an optional capability on forwarders that helps
  prevent loss of data when sending data to an indexer.
* A value of "true" means the forwarder retains a copy of each sent event
  until the receiving system sends an acknowledgment.
  * The receiver sends an acknowledgment when it has fully handled the event
    (typically when it has written it to disk in indexing).
  * If the forwarder does not receive an acknowledgment, it resends the data
    to an alternative receiver.
  * NOTE: The maximum memory used for the outbound data queues increases
    significantly by default (500KB -> 28MB) when the 'useACK' setting is
    enabled. This is intended for correctness and performance.
* A value of "false" means the forwarder considers the data fully processed
  when it finishes writing it to the network socket.
* You can configure this setting at the [tcpout] or [tcpout:<target_group>]
  stanza levels. You cannot set it for individual servers at the
  [tcpout-server: ...] stanza level.
* Default: false

####
# HTTP Output stanzas
####

[httpout]

httpEventCollectorToken = <string>
* The value of the HEC token.
* HEC uses this token to authenticate inbound connections.
* No default.

uri = <string>
* The URI and management port of the Http Event Collector(HEC) end point.
* For example, https://SplunkHEC01.example.com:8088
* No default.

batchSize = <integer>
* The size, in bytes, of the HTTP OUT send buffer.
* HTTP OUT batch pipeline data before sending out.
* If the current buffer size is greater than 'batchSize', HEC sends the data
  out immediately.
* Default: 65536

batchTimeout = <integer>
* How often, in seconds, to send out pipeline data.
* HTTP OUT batch pipeline data before sending out.
* If the wait time is greater than 'batchTimeout', HEC sends the data 
  out immediately.
* Default: 30

# These settings can be used to configure TLS for HTTP output.

clientCert = <path>
* The full path to the location of the client TLS/SSL certificate.
* The certificate file must be in Privacy Enhanced Mail (PEM) format.
* No default.

sslPassword = <string>
* The password for the client certificate.
* This setting is optional.
* No default.

cipherSuite = <string>
* The cipher string to use for negotiating ciphers with the TLS server.
* This setting ensures that the client does not accept connections using weak
  encryption protocols.
* The default can vary. See the 'cipherSuite' setting in
  $SPLUNK_HOME/etc/system/default/server.conf for the current default.

ecdhCurves = <comma-separated list>
* A list of elliptic curves to use for the Elliptic-curve Diffie-Hellman
  (ECDH) key negotiation protocol.
* The client sends elliptic curves as part of the Client Hello
* during a TLS handshake.
* Specify elliptic curves in the order that you prefer them.
* The server supports only the curves specified in the list.
* Splunk software only supports named curves that you specify
  by their short names.
* You can get the list of valid named curves by their short and long names
  by running this CLI command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Example configuration: "ecdhCurves = prime256v1,secp384r1,secp521r1"
* See the 'ecdhCurves' setting in
  $SPLUNK_HOME/etc/system/default/server.conf for the current default.

sslVerifyServerCert = <boolean>
* Whether or not splunkd, as a client, validates the TLS certificate that a server presents
  to it when it connects to a server.
* This setting serves as an additional step for authenticating connections to indexers.
* A value of "true" means that the client inspects and validates the certificate
  that it receives from the server upon connecting to it.
  * This ensures that the server you are connecting to has a valid
    TLS/SSL certificate. 
  * The client then checks both the Common Name and the Subject Alternative Name 
    of the server in the certificate for a match.
  * If the validation check does not pass, the client terminates the handshake
    between it and the server immediately, which terminates the connection.
  * NOTE: Certificates that contain the same X.509 Common Name as a certificate
    authority (CA) certificate are not suitable for this validation check, even
    if the same CA issued the certificate. 
  * A value of "false" means that the client does not check the TLS certificate that
    it receives as part of the session negotiation. The client considers any valid
    TLS certificate as acceptable
* Default: false

tlsHostname = <string>
* The host name of the server that the client is trying to reach when
  it initiates a TLS connection to that server.
* As part of the TLS handshake, when a client connects to a server, the
  client can provide that server with the host name it was trying to
  reach when it initiated the connection. This prevents problems with
  mismatches of Common Names when the TLS connection begins.
* This is called Server Name Indication (SNI), and is an extension of
  the TLS protocol.
* The client performs SNI during the TLS Client Hello.
* Default: empty string

sslVerifyServerName = <boolean>
* Whether or not splunkd, as a client, performs a TLS hostname validation check
  on a TLS certificate that it receives upon an initial connection
  to a server.
* A TLS hostname validation check ensures that a client
  communicates with the correct server, and has not been redirected to
  another by a machine-in-the-middle attack, where a malicious party inserts
  themselves between the client and the target server, and impersonates
  that server during the session.
* Specifically, the validation check forces splunkd to verify that either
  the Common Name or the Subject Alternative Name in the certificate that the
  server presents to the client matches the host name portion of the URL that
  the client used to connect to the server.
* For this setting to have any effect, the 'sslVerifyServerCert' setting must
  have a value of "true". If it doesn't, TLS hostname validation is not possible
  because certificate verification is not on.
* A value of "true" for this setting means that splunkd performs a TLS hostname
  validation check, in effect, verifying the server's name in the certificate.
  If that check fails, splunkd terminates the TLS handshake immediately. This terminates
  the connection between the client and the server. Splunkd logs this failure at
  the ERROR logging level.
* A value of "false" means that splunkd does not perform the TLS hostname
  validation check. If the server presents an otherwise valid certificate, the
  client-to-server connection proceeds normally.
* Default: false

sslCommonNameToCheck = <comma-separated list>
* One or more Common Names of the server certificate that the client checks against
  when it connects to a server using TLS.
* The Common Name (CN) is an X.509 standard field in a certificate that identifies the
  host name that is associated with the certificate.
  * The CN can be a short host name or a fully qualified domain name. For example, 
    the CN can be one of "example", "www.example.com", or "example.com".
* If the client cannot match the CN in the certificate that the server presents,
  then the client cannot authenticate the server, and terminates the session 
  negotiation immediately.
* For this setting to have any affect, the 'sslVerifyServerCert' setting must have
  a value of "true".
* This setting is optional.
* Default: empty string (no common name checking).

sslAltNameToCheck = <comma-separated list>
* One or more Subject Alternative Names of the server certificate that the client checks
  against when it connects to a server using TLS.
* The Subject Alternative Name (SAN) is an extension to the X.509 standard that
  lets you specify additional host names for a TLS certificate. The SAN can be a
  short host name or a fully qualified domain name.
* If the client cannot match the SAN in the certificate that the server presents,
  then the client cannot authenticate the server, and terminates the session 
  negotiation immediately.
* For this setting to have any affect, the 'sslVerifyServerCert' setting must have
  a value of "true".
* This setting is optional.
* Default: empty string (no alternate name checking)

useClientSSLCompression = <boolean>
* Whether or not compression of network traffic that passes through
  a TLS/SSL connection is turned on.
* Server-side compression in splunkd is on by default. Configuring this
  setting on the client side enables compression between both server and
  client.
* If server-side compression is off, this client-side setting has no effect.
* A value of "true" means TLS/SSL compression is turned on.
* A value of "false" means TLS/SSL compression is turned off.
* If you use this setting, the 'tcpout_connections' group in the metrics.log
  file shows throughput values before compression occurs.
* Default: true

sslQuietShutdown = <boolean>
* Whether or not quiet SSL shutdown mode is turned on.
* When a client is finished with a TLS connection, it can shut that
  connection down normally or quietly.
* A normal SSL shutdown between a local node, in this case the client, 
  and a peer node, in this case the server, involves either
  node sending a message to the other to terminate the TLS/SSL connection. 
  This message is called the "close_notify" message.
* When a local node sends this message, the peer node returns the same message
  upon receipt, then stops sending further messages over TLS. The TLS connection
  remains open until the peer also closes the connection on its side.
* A "quiet" SSL shutdown means that neither node sends this message when it
  terminates the TLS connection. Instead, the node sets the connection to the
  "shutdown" state immediately.
* A value of "true" means that the client uses quiet SSL shutdown mode to
  terminate TLS connections.
* A value of false means that the client shuts down TLS connections using the
  normal shutdown process.
* Default: false

sslVersions = <comma-separated list>
* A list of TLS or SSL versions to support for secure network connections.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2"
* The special version "*" selects all supported versions. The version "tls"
  selects all versions tls1.0 or newer
* If you prefix a version with "-", it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list, but
  does nothing.
* When the Splunk platform instance operates in Federal Information 
  Processing Standards (FIPS) mode, the "ssl3" version is not valid.
* The default can vary. See the 'sslVersions' setting in
  $SPLUNK_HOME/etc/system/default/outputs.conf for the current default.

############
#----Syslog output----
############
# The syslog output processor is not available for universal or light
# forwarders.

# The following configuration is used to send output using syslog.

[syslog]

defaultGroup = <target_group>, <target_group>, ...

dropEventsOnQueueFull = <integer>[ms|s|m]
* See 'dropEventsOnQueueFull' in the "[tcpout]" stanza for
  information on this setting.

dropClonedEventsOnQueueFull = <integer>[ms|s|m]
* See 'dropClonedEventsOnQueueFull' in the "[tcpout]" stanza for
  information on this setting.

#######
# For the following settings, see the [syslog:<target_group>] stanza.

type = [tcp|udp]
priority = <<integer>> | NO_PRI
maxEventSize = <integer>

[syslog:<target_group>]

#----REQUIRED SETTINGS----
# The following settings are required for a syslog output group.

server = [<ip>|<servername>]:<port>
* The IP address or server name and port where the syslog server is running.
* Required.
* This setting specifies the port on which the syslog server listens.
* Default: 514

#----OPTIONAL SETTINGS----

# The following are optional settings for syslog output:

type = [tcp|udp]
* The network protocol to use.
* Default: udp

priority = <<integer>>|NO_PRI
* The priority value included at the beginning of each syslog message.
* The priority value ranges from 0 to 191 and is made up of a Facility
  value and a Level value.
* Enclose the priority value in "<>" delimeters. For example, specify a
  priority of 34 as follows: <34>
* The integer must be one to three digits in length.
* The value you enter appears in the syslog header.
* The value mimics the number passed by a syslog interface call. See the
  *nix man page for syslog for more information.
* Calculate the priority value as follows: Facility * 8 + Severity
  For example, if Facility is 4 (security/authorization messages)
  and Severity is 2 (critical conditions), the priority will be
  (4 * 8) + 2 = 34. Set the setting to <34>.
* If you do not want to add a priority value, set the priority to "<NO_PRI>".
* The table of facility and severity (and their values) is located in
  RFC3164. For example, http://www.ietf.org/rfc/rfc3164.txt section 4.1.1
* The table is reproduced briefly below. Some values are outdated.
  Facility:
     0 kernel messages
     1 user-level messages
     2 mail system
     3 system daemons
     4 security/authorization messages
     5 messages generated internally by syslogd
     6 line printer subsystem
     7 network news subsystem
     8 UUCP subsystem
     9 clock daemon
    10 security/authorization messages
    11 FTP daemon
    12 NTP subsystem
    13 log audit
    14 log alert
    15 clock daemon
    16 local use 0  (local0)
    17 local use 1  (local1)
    18 local use 2  (local2)
    19 local use 3  (local3)
    20 local use 4  (local4)
    21 local use 5  (local5)
    22 local use 6  (local6)
    23 local use 7  (local7)
  Severity:
    0  Emergency: system is unusable
    1  Alert: action must be taken immediately
    2  Critical: critical conditions
    3  Error: error conditions
    4  Warning: warning conditions
    5  Notice: normal but significant condition
    6  Informational: informational messages
    7  Debug: debug-level messages
* Default: <13> (Facility of "user" and Severity of "Notice")

syslogSourceType = <string>
* Specifies an additional rule for handling data, in addition to that
  provided by the 'syslog' source type.
* This string is used as a substring match against the sourcetype key. For
  example, if the string is set to "syslog", then all sourcetypes
  containing the string 'syslog' receive this special treatment.
* To match a sourcetype explicitly, use the pattern
  "sourcetype::sourcetype_name".
    * Example: syslogSourceType = sourcetype::apache_common
* Data that is "syslog" or matches this setting is assumed to already be in
  syslog format.
* Data that does not match the rules has a header, optionally a timestamp
  (if defined in 'timestampformat'), and a hostname added to the front of
  the event. This is how Splunk software causes arbitrary log data to match syslog expectations.
* No default.

timestampformat = <format>
* If specified, Splunk software prepends formatted timestamps to events
  forwarded to syslog.
* As above, this logic is only applied when the data is not syslog, or the
  type specified in the 'syslogSourceType' setting, because it is assumed
  to already be in syslog format.
* If the data is not in syslog-compliant format and you do not specify a
 'timestampformat', the output will not be RFC3164-compliant.
* The format is a strftime (string format time)-style timestamp formatting
  string. This is the same implementation used in the 'eval' search command,
  Splunk logging, and other places in splunkd.
  * For example: %b %e %H:%M:%S for RFC3164-compliant output
    * %b - Abbreviated month name (Jan, Feb, ...)
    * %e - Day of month
    * %H - Hour
    * %M - Minute
    * %s - Second
* For a more exhaustive list of the formatting specifiers, refer to the
  online documentation.
* Do not put the string in quotes.
* No default. No timestamp is added to the front of events.

maxEventSize = <integer>
* The maximum size of an event, in bytes, that Splunk software will transmit.
* All events exceeding this size are truncated.
* Optional.
* Default: 1024

#---- Routing Data to Syslog Server -----
# To route data to syslog servers:
# 1) Decide which events to route to which servers.
# 2) Edit the props.conf, transforms.conf, and outputs.conf files on the
#    forwarders.

# Edit $SPLUNK_HOME/etc/system/local/props.conf and set a TRANSFORMS-routing
# setting as shown below.
#
# [<spec>]
# TRANSFORMS-routing=<unique_stanza_name>

* <spec> can be:
  * <sourcetype>, the source type of an event
  * host::<host>, where <host> is the host for an event
  * source::<source>, where <source> is the source for an event

* Use the <unique_stanza_name> when creating your entry in transforms.conf.

# Edit $SPLUNK_HOME/etc/system/local/transforms.conf and set rules to match
# your props.conf stanza:
#
#  [<unique_stanza_name>]
#  REGEX = <your_regex>
#  DEST_KEY = _SYSLOG_ROUTING
#  FORMAT = <unique_group_name>

* Set <unique_stanza_name> to match the name you created in props.conf.
* Enter the regex rules in 'REGEX' to determine which events get
  conditionally routed.
* Set 'DEST_KEY' to "_SYSLOG_ROUTING" to send events via syslog.
* Set 'FORMAT' to match the syslog group name you create in outputs.conf.

####
#----IndexAndForward Processor-----
####

# The IndexAndForward processor determines the default behavior for indexing
# data on a Splunk instance. It has the "index" property, which determines
# whether indexing occurs.
#
# When the Splunk platform instance is not configured as a forwarder, 
# 'index' is set to "true". That is, the Splunk platform instance indexes 
# data by default.
#
# When the Splunk platform instance is configured as a forwarder, the
# processor sets 'index' to "false". That is, the Splunk platform instance
# does not index data by default.
#
# The IndexAndForward processor has no effect on the universal forwarder,
# which can never index data.
#
# If the [tcpout] stanza configures the indexAndForward setting, the value
# of that setting overrides the default value of 'index'. However, if you
# set 'index' in the [indexAndForward] stanza described below, it
# supersedes any value set in [tcpout].

[indexAndForward]

index = <boolean>
* Whether or not indexing is enabled on a Splunk platform instance.
* A value of "true" means the Splunk platform instance indexes data.
* A value of "false" means the Splunk platform instance does not index data.
* The default can vary. It depends on whether the Splunk
  platform instance is configured as a forwarder, and whether it is
  modified by any value configured for the 'indexAndForward'
  setting in the [tcpout] stanza.

selectiveIndexing = <boolean>
* Whether or not to index specific events that have the
  '_INDEX_AND_FORWARD_ROUTING' setting configured.
* A value of "true" means you can choose to index only specific events that have
  the '_INDEX_AND_FORWARD_ROUTING' setting configured.
* Configure the '_INDEX_AND_FORWARD_ROUTING' setting in inputs.conf as:
  [<input_stanza>]
  _INDEX_AND_FORWARD_ROUTING = local
* Default: false

[indexer_discovery:<name>]

pass4SymmKey = <string>
* The security key used to communicate between the cluster manager
  and the forwarders.
* This value must be the same for all forwarders and the manager node.
* You must explicitly set this value for each forwarder.
* If you specify a password here, you must also specify the same password
  on the manager node identified by the 'manager_uri' setting.

send_timeout = <decimal>
* The low-level timeout, in seconds, for sending messages to the manager node.
* Fractional seconds are allowed (for example, 60.95 seconds).
* Default: 30

rcv_timeout = <decimal>
* The low-level timeout, in seconds, for receiving messages from the manager node.
* Fractional seconds are allowed (for example, 60.95 seconds).
* Default: 30

cxn_timeout = <decimal>
* The low-level timeout, in seconds, for connecting to the manager node.
* Fractional seconds are allowed (for example, 60.95 seconds).
* Default: 30

manager_uri = <string>
* The URI and management port of the cluster manager used in indexer discovery.
* For example, https://SplunkManager01.example.com:8089

master_uri = <string>
* DEPRECATED. Use the 'manager_uri' setting instead.

####
# Remote Queue Output
####

[remote_queue:<name>]

* This section explains possible settings for configuring a remote queue.
* Each remote_queue stanza represents an individually configured remote
  queue output.
* NOTE: Only ONE remote queue stanza is supported as an
  output queue.

remote_queue.* = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* This section explains possible settings for configuring a remote queue.
* With remote queues, the splunk indexer might require additional configuration,
  specific to the type of remote queue. You can pass configuration information
  to the splunk indexer by specifying the settings through the following schema:
  remote_queue.<scheme>.<config-variable> = <value>.
  For example:
  remote_queue.sqs.access_key = ACCESS_KEY
* This setting is optional.
* No default.

remote_queue.type = sqs|kinesis|sqs_smartbus|sqs_smartbus_cp|asq
* Currently not supported. This setting is related to a feature that is
  still under development.
* Required.
* Specifies the remote queue type, which can be "SQS", "Kinesis", "SQS Smartbus",
  "SQS Smartbus CP" or "ASQ".
* If the type is "sqs_smartbus_cp", the [cloud_processing_queue] stanza must be present.

compressed = <boolean>
* See the description for TCPOUT SETTINGS in outputs.conf.spec.

negotiateProtocolLevel = <unsigned integer>
* See the description for TCPOUT SETTINGS in outputs.conf.spec.

channelReapInterval = <integer>
* See the description for TCPOUT SETTINGS in outputs.conf.spec.

channelTTL = <integer>
* See the description for TCPOUT SETTINGS in outputs.conf.spec.

channelReapLowater = <integer>
* See the description for TCPOUT SETTINGS in outputs.conf.spec.

concurrentChannelLimit = <unsigned integer>
* See the description for [splunktcp] in inputs.conf.spec.

####
# Simple Queue Service (SQS) specific settings
####

remote_queue.sqs.access_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The access key to use when authenticating with the remote queue
  system that supports the SQS API.
* If not specified, the forwarder looks for the environment variables
  AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the forwarder
  attempts to use the secret key from the IAM (Identity and Access
  Management) role.
* Optional.
* Default: not set

remote_queue.sqs.secret_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the secret key to use when authenticating with the remote queue
  system supporting the SQS API.
* If not specified, the forwarder looks for the environment variables
  AWS_SECRET_ACCESS_KEY or AWS_SECRET_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the forwarder
  attempts to use the secret key from the IAM (Identity and Access
  Management) role.
* Optional.
* Default: not set

remote_queue.sqs.auth_region = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The authentication region to use when signing the requests while interacting
  with the remote queue system supporting the Simple Queue Service (SQS) API.
* If not specified and the forwarder is running on EC2, the auth_region is
  constructed automatically based on the EC2 region of the instance where the
  the forwarder is running.
* Optional.
* Default: not set

remote_queue.sqs.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote queue system supporting the Simple Queue Service (SQS) API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://sqs.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via the 'remote_queue.sqs.auth_region' setting
  or a value constructed automatically based on the EC2 region of the
  running instance.
* Example: https://sqs.us-west-2.amazonaws.com/
* Optional.

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
* If you configure this setting, Splunk software assumes that the SQS queue is
  a FIFO queue, and that messages in the queue should be processed first-in,
  first-out.
* Otherwise, Splunk software assumes that the SQS queue is a standard queue.
* Can be between 1-128 alphanumeric or punctuation characters.
* NOTE: FIFO queues must have Content-Based De-duplication enabled.
* Optional.
* Default: not set

remote_queue.sqs.retry_policy = max_count|none
* Sets the retry policy to use for remote queue operations.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation is
    retried upon intermittent failure. Set max_count with the
    'max_count.max_retries_per_part' setting.
  + "none": Do not retry file operations upon failure.
* Optional.
* Default: max_count

remote_queue.sqs.max_count.max_retries_per_part = <unsigned integer>
* When the 'remote_queue.sqs.retry_policy' setting is "max_count", sets the
  maximum number of times a queue operation will be retried upon intermittent
  failure.
* Optional.
* Default: 9

remote_queue.sqs.timeout.connect = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the connection timeout, in milliseconds, to use when interacting with
  the SQS for this queue.
* Default: 5000

remote_queue.sqs.timeout.read = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the read timeout, in milliseconds, to use when interacting with the
  SQS for this queue.
* Optional.
* Default: 60000

remote_queue.sqs.timeout.write = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the write timeout, in milliseconds, to use when interacting with
  the SQS for this queue.
* Optional.
* Default: 60000

remote_queue.sqs.large_message_store.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote storage system supporting the S3 API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://s3.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via 'remote_queue.sqs.auth_region' or a value
  constructed automatically based on the EC2 region of the running instance.
* Example: https://s3.us-west-2.amazonaws.com/
* Optional.
* Default: not set

remote_queue.sqs.large_message_store.path = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The remote storage location where messages larger than the underlying
  queue's maximum message size will reside.
* The format for this value is: <scheme>://<remote-location-specifier>
  * The "scheme" identifies a supported external storage system type.
  * The "remote-location-specifier" is an external system-specific string for
    identifying a location inside the storage system.
* The following external systems are supported:
  * Object stores that support AWS's S3 protocol. These stores use the scheme
    "s3". For example, "path=s3://mybucket/some/path".
* If not specified, the queue drops messages exceeding the underlying queue's
  maximum message size.
* Optional.
* Default: not set

remote_queue.sqs.send_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The interval that the remote queue output processor waits for data to
  arrive before sending a partial batch to the remote queue.
* Examples: 30s, 1m
* Optional.
* Default: 30s

remote_queue.sqs.max_queue_message_size = <integer>[KB|MB|GB]
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum message size to which events are batched for upload to
  the remote queue.
* Specify this value as an integer followed by KB, MB, or GB (for example,
  10MB is 10 megabytes)
* Queue messages are sent to the remote queue when the next event processed
  would otherwise result in a message exceeding the maximum message size.
* The maximum value for this setting is 5GB.
* Optional.
* Default: 10MB

remote_queue.sqs.enable_data_integrity_checks = <boolean>
* If "true", Splunk software sets the data checksum in the metadata field of
  the HTTP header during upload operation to S3.
* The checksum is used to verify the integrity of the data on uploads.
* Default: false

remote_queue.sqs.enable_signed_payloads  = <boolean>
* If "true", Splunk software signs the payload during upload operation to S3.
* This setting is valid only for remote.s3.signature_version = v4
* Default: true

####
# Kinesis specific settings
####

remote_queue.kinesis.access_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the access key to use when authenticating with the remote queue
  system supporting the Kinesis API.
* If not specified, the forwarder looks for the environment variables
  AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the forwarder
  attempts to use the secret key from the IAM role.
* Optional.
* Default: not set

remote_queue.kinesis.secret_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the secret key to use when authenticating with the remote queue
  system supporting the Kinesis API.
* If not specified, the forwarder looks for the environment variables
  AWS_SECRET_ACCESS_KEY or AWS_SECRET_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the forwarder
  attempts to use the secret key from the IAM role.
* Optional.
* Default: not set

remote_queue.kinesis.auth_region = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The authentication region to use when signing the requests when interacting
  with the remote queue system supporting the Kinesis API.
* If not specified and the forwarder is running on EC2, the auth_region is
  constructed automatically based on the EC2 region of the instance where the
  the forwarder is running.
* Optional.
* Default: not set

remote_queue.kinesis.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote queue system supporting the Kinesis API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://kinesis.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via the 'remote_queue.kinesis.auth_region' setting
  or a value constructed automatically based on the EC2 region of the running instance.
* Optional.
* Example: https://kinesis.us-west-2.amazonaws.com/

remote_queue.kinesis.enable_data_integrity_checks = <boolean>
* If "true", Splunk software sets the data checksum in the metadata field
  of the HTTP header during upload operation to S3.
* The checksum is used to verify the integrity of the data on uploads.
* Default: false

remote_queue.kinesis.enable_signed_payloads  = <boolean>
* If "true", Splunk software signs the payload during upload operation to S3.
* This setting is valid only for remote.s3.signature_version = v4
* Default: true

remote_queue.kinesis.retry_policy = max_count|none
* Sets the retry policy to use for remote queue operations.
* Optional.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation is
    retried upon intermittent failure. Specify the max_count with the
    'max_count.max_retries_per_part' setting.
  + "none": Do not retry file operations upon failure.
* Default: max_count

remote_queue.kinesis.max_count.max_retries_per_part = <unsigned integer>
* When the 'remote_queue.kinesis.retry_policy' setting is max_count,
  sets the maximum number of times a queue operation is retried
  upon intermittent failure.
* Optional.
* Default: 9

remote_queue.kinesis.timeout.connect = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the connection timeout, in milliseconds, to use when interacting with
  Kinesis for this queue.
* Default: 5000

remote_queue.kinesis.timeout.read = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* Sets the read timeout, in milliseconds, to use when interacting with Kinesis
  for this queue.
* Default: 60000

remote_queue.kinesis.timeout.write = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the write timeout, in milliseconds, to use when interacting with
  Kinesis for this queue.
* Optional.
* Default: 60000

remote_queue.kinesis.large_message_store.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote storage system supporting the S3 API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://s3.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via 'remote_queue.kinesis.auth_region' or a value
  constructed automatically based on the EC2 region of the running instance.
* Example: https://s3.us-west-2.amazonaws.com/
* Optional.
* Default: not set

remote_queue.kinesis.large_message_store.path = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The remote storage location where messages larger than the underlying
  queue's maximum message size will reside.
* The format for this setting is: <scheme>://<remote-location-specifier>
  * The "scheme" identifies a supported external storage system type.
  * The "remote-location-specifier" is an external system-specific string for
    identifying a location inside the storage system.
* The following external systems are supported:
  * Object stores that support AWS's S3 protocol. These stores use the
    scheme "s3".
    For example, "path=s3://mybucket/some/path".
* If not specified, the queue drops messages exceeding the underlying queue's
  maximum message size.
* Optional.
* Default: not set

remote_queue.kinesis.send_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The interval that the remote queue output processor waits for data to
  arrive before sending a partial batch to the remote queue.
* For example, 30s, 1m
* Optional.
* Default: 30s

remote_queue.kinesis.max_queue_message_size = <integer>[KB|MB|GB]
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum message size to which events are batched for upload to the remote
  queue.
* Specify this value as an integer followed by KB or MB (for example, 500KB
  is 500 kilobytes).
* Queue messages are sent to the remote queue when the next event processed
  would otherwise result in the message exceeding the maximum message size.
* The maximum value for this setting is 5GB.
* Optional.
* Default: 10MB

remote_queue.kinesis.tenantId = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The ID of the tenant that owns the messages being
  written to the remote queue.
* If not specified, the messages do not belong to any tenant.
* Optional.
* Default: not set

####
# Simple Queue Service Smartbus (SQS Smartbus) or Simple Queue Service Smartbus CP (SQS Smartbus CP) specific settings
####

# The settings for SQS Smartbus (sqs_smartbus) and SQS Smartbus CP (sqs_smartbus_cp)
# are identical in the remote queue output. The following section uses "sqs_smartbus"
  as an example. 

remote_queue.sqs_smartbus.encoding_format = protobuf|s2s
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the encoding format used to write data to the
  remote queue.
* Default: protobuf

remote_queue.sqs_smartbus.access_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The access key to use when authenticating with the remote queue
  system that supports the SQS API.
* If not specified, the splunk instance looks for the environment variables
  AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the splunk instance
  attempts to use the secret key from the IAM (Identity and Access
  Management) role.
* Optional.
* Default: not set

remote_queue.sqs_smartbus.secret_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the secret key to use when authenticating with the remote queue
  system supporting the SQS API.
* If not specified, the splunk instance looks for the environment variables
  AWS_SECRET_ACCESS_KEY or AWS_SECRET_KEY (in that order). If the environment
  variables are not set and the forwarder is running on EC2, the splunk instance
  attempts to use the secret key from the IAM (Identity and Access
  Management) role.
* Optional.
* Default: not set

remote_queue.sqs_smartbus.auth_region = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The authentication region to use when signing the requests while interacting
  with the remote queue system supporting the Simple Queue Service (SQS) API.
* If not specified and the splunk instance is running on EC2, the auth_region is
  constructed automatically based on the EC2 region of the instance where the
  the splunk instance is running.
* Default: not set

remote_queue.sqs_smartbus.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote queue system supporting the Simple Queue Service (SQS) API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://sqs.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via the 'remote_queue.sqs.auth_region' setting
  or a value constructed automatically based on the EC2 region of the
  running instance.
* Example: https://sqs.us-west-2.amazonaws.com/
* Optional.

remote_queue.sqs_smartbus.message_group_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the Message Group ID for Amazon Web Services Simple Queue Service
  (SQS) First-In, First-Out (FIFO) queues.
* Setting a Message Group ID controls how messages within an AWS SQS queue are
  processed.
* For information on SQS FIFO queues and how messages in those queues are
  processed, see "Recommendations for FIFO queues" in the AWS SQS Developer
  Guide.
* If you configure this setting, Splunk software assumes that the SQS queue is
  a FIFO queue, and that messages in the queue should be processed first-in,
  first-out.
* Otherwise, Splunk software assumes that the SQS queue is a standard queue.
* Can be between 1-128 alphanumeric or punctuation characters.
* NOTE: FIFO queues must have Content-Based De-duplication enabled.
* Optional.
* Default: not set

remote_queue.sqs_smartbus.retry_policy = max_count|none
* Sets the retry policy to use for remote queue operations.
* Optional.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation is
    retried upon intermittent failure. Set max_count with the
    'max_count.max_retries_per_part' setting.
  + "none": Do not retry file operations upon failure.
* Default: max_count

remote_queue.sqs_smartbus.max_count.max_retries_per_part = <unsigned integer>
* When the 'remote_queue.sqs_smartbus.retry_policy' setting is "max_count", sets the
  maximum number of times a queue operation will be retried upon intermittent
  failure.
* Optional.
* Default: 3

remote_queue.sqs_smartbus.timeout.connect = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the connection timeout, in milliseconds, to use when interacting with
  the SQS for this queue.
* Optional.
* Default: 5000

remote_queue.sqs_smartbus.timeout.read = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the read timeout, in milliseconds, to use when interacting with the
  SQS for this queue.
* Optional.
* Default: 60000

remote_queue.sqs_smartbus.timeout.write = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Sets the write timeout, in milliseconds, to use when interacting with
  the SQS for this queue.
* Optional.
* Default: 60000

remote_queue.sqs_smartbus.large_message_store.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote storage system supporting the S3 API.
* Use the scheme, either http or https, to enable or disable SSL connectivity
  with the endpoint.
* If not specified, the endpoint is constructed automatically based on the
  auth_region as follows: https://s3.<auth_region>.amazonaws.com
* If specified, the endpoint must match the effective auth_region, which is
  either a value specified via 'remote_queue.sqs_smartbus.auth_region' or a value
  constructed automatically based on the EC2 region of the running instance.
* Example: https://s3.us-west-2.amazonaws.com/
* Optional.
* Default: not set

remote_queue.sqs_smartbus.large_message_store.path = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The remote storage location where messages larger than the underlying
  queue's maximum message size will reside.
* The format for this value is: <scheme>://<remote-location-specifier>
  * The "scheme" identifies a supported external storage system type.
  * The "remote-location-specifier" is an external system-specific string for
    identifying a location inside the storage system.
* The following external systems are supported:
  * Object stores that support AWS's S3 protocol. These stores use the scheme
    "s3". For example, "path=s3://mybucket/some/path".
* If not specified, the queue drops messages exceeding the underlying queue's
  maximum message size.
* Optional.
* Default: not set

remote_queue.sqs_smartbus.large_message_store.sslVerifyServerCert = <boolean>
* If set to true, the Splunk platform verifies the certificate presented by the S3
  server and checks that the common name and alternative name match the ones
  specified in 'remote_queue.sqs_smartbus.large_message_store.sslCommonNameToCheck' and
  'remote_queue.sqs_smartbus.large_message_store.sslAltNameToCheck'.
* Default: false

remote_queue.sqs_smartbus.large_message_store.sslVersions = <comma-separated list>
* Comma-separated list of SSL versions to connect to
  'remote.sqs_smartbus.large_message_store.endpoint'.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* The special version "*" selects all supported versions.  The version "tls"
  selects all versions tls1.0 or newer.
* If a version is prefixed with "-" it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list
  but does nothing.
* When configured in FIPS mode, ssl3 is always disabled regardless
  of this configuration.
* Default: tls1.2

remote_queue.sqs_smartbus.large_message_store.sslCommonNameToCheck = 
  <comma-separated list>
* If this value is set, and 
  'remote_queue.sqs_smartbus.large_message_store.sslVerifyServerCert' is set to true,
  the Splunk platform instance checks the common name of the certificate presented by
  the remote server (specified in
  'remote_queue.sqs_smartbus.large_message_store.endpoint') against this list
  of common names.
* Default: not set

remote_queue.sqs_smartbus.large_message_store.sslAltNameToCheck = <comma-separated list>
* If this value is set, and 
  'remote_queue.sqs_smartbus.large_message_store.sslVerifyServerCert' is set to true,
  the Splunk platform instance checks the alternate name(s) of the certificate
  presented by the remote server (specified in 
  'remote_queue.sqs_smartbus.large_message_store.endpoint') against this list of
  subject alternate names.
* Default: not set

remote_queue.sqs_smartbus.large_message_store.sslRootCAPath = <path>
* Full path to the Certificate Authority (CA) certificate PEM format file
  containing one or more certificates concatenated together. S3 certificate
  will be validated against the CAs present in this file.
* Default: The value of [sslConfig]/'caCertFile' in server.conf

remote_queue.sqs_smartbus.large_message_store.cipherSuite = <cipher suite string>
* If set, uses the specified cipher string for the SSL connection.
* If not set, uses the default cipher string.
* Must specify 'dhFile' to enable any Diffie-Hellman ciphers.
* Default: TLSv1+HIGH:TLSv1.2+HIGH:@STRENGTH

remote_queue.sqs_smartbus.large_message_store.ecdhCurves = <comma-separated list>
* ECDH curves to use for ECDH key negotiation.
* Specify the curves in the order of preference.
* The client sends these curves as a part of Client Hello.
* Splunk software only supports named curves specified
  by their short names.
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* e.g. ecdhCurves = prime256v1,secp384r1,secp521r1
* Default: not set

remote_queue.sqs_smartbus.large_message_store.dhFile = <string>
* PEM format Diffie-Hellman parameter file name.
* DH group size must be no less than 2048bits.
* This file is required in order to enable any Diffie-Hellman ciphers.
* Optional.
* Default: not set

remote_queue.sqs_smartbus.send_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The interval that the remote queue output processor waits for data to
  arrive before sending a partial batch to the remote queue.
* Examples: 100ms, 5s
* Default: 4s

remote_queue.sqs_smartbus.consume_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The interval that the remote output worker consumes from data queue.
* Examples: 50ms, 1s
* Default: 100ms

remote_queue.sqs_smartbus.max_queue_message_size = <integer>[KB|MB|GB]
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum message size for batched events for upload to the remote queue.
* Queue messages contain a series of one or more events. When an event causes the message
  size to exceed this setting, the message is sent to the remote queue.
* Specify this value as an integer followed by KB, MB, or GB (for example,
  10MB is 10 megabytes)
* Default: 10MB

remote_queue.sqs_smartbus.enable_data_integrity_checks = <boolean>
* If "true", Splunk software sets the data checksum in the metadata field of
  the HTTP header during upload operation to S3.
* The checksum is used to verify the integrity of the data on uploads.
* Default: false

remote_queue.sqs_smartbus.enable_signed_payloads  = <boolean>
* If "true", Splunk software signs the payload during upload operation to S3.
* This setting is valid only for remote.s3.signature_version = v4
* Default: true

remote_queue.sqs_smartbus.drop_data = <boolean>
* Currently not supported. This setting is related to a feature that is still
  under development.
* Determines whether Splunk software drops the data from all Splunk managed internal
  indexes and indexes listed in 'remote_queue.sqs_smartbus.drop_data_index_list'
* A value of "true" means that Splunk software drops the data.
* Default: false

remote_queue.sqs_smartbus.drop_data_index_list = <comma-separated list>
* Currently not supported. This setting is related to a feature that is still
  under development.
* A comma-separated list of indexes for which you want to drop the data.
  For example: index_1, index_2, index_3.
* If 'remote_queue.sqs_smartbus.drop_data' is set to "true" then Splunk software
  drops the data from 'drop_data_index_list'.
* Default: not set

remote_queue.sqs_smartbus.executor_max_workers_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of worker threads available per pipeline set to execute SQS output
  worker tasks.
* A value of 0 is equivalent to 1.
* The maximum value for this setting is 20.
* Default: 10

remote_queue.sqs_smartbus.executor_max_jobs_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of jobs that each worker thread per pipeline set can queue.
* A value of 0 is equivalent to 1.
* The maximum value for this setting is 100.
* Default: 50

remote_queue.sqs_smartbus.large_message_store.encryption_scheme = sse-s3 | sse-c | none
* Currently not supported. This setting is related to a feature that is
  still under development.
* The encryption scheme used by remote storage.
* Default: none.

remote_queue.sqs_smartbus.large_message_store.kms_endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The endpoint to connect to for generating KMS keys.
* This setting is required if 'large_message_store.encryption_scheme' is
  set to sse-c.
* Examples: https://kms.us-east-2.amazonaws.com
* No default.

remote_queue.sqs_smartbus.large_message_store.key_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The ID for the primary key that KMS uses to generate a data key pair. 
  The primary key is stored in AWS.
* This setting is required if 'large_message_store.encryption_scheme' is
  set to sse-c.
* Examples: alias/sqsssekeytrial, 23456789-abcd-1234-11aa-c50f99011223
* No default.

remote_queue.sqs_smartbus.large_message_store.key_refresh_interval = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The time interval to refresh primary key.
* Default: 24h

remote_queue.sqs_smartbus.enable_inline_data = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies whether to bypass S3 and use SQS directly to send events.
* A value of "true" means that if the data packet is small enough to fit in
  SQS (256KB max), the Splunk Cloud Platform will use SQS to send event data.
* This setting only applies when remote_queue.sqs_smartbus.encoding_format=protobuf
* Default: false

remote_queue.sqs_smartbus.check_replication_enabled = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies whether to enable cross-region replication status checks of
  uploaded ingest blobs on remote storage.
* Default: false

remote_queue.sqs_smartbus.check_replication_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The interval that the remote queue output processor waits before checking
  the replication status of an uploaded ingest blob on remote storage.
* Examples: 100ms, 5s
* Default: 60s

remote_queue.sqs_smartbus.check_replication_executor_max_workers_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of worker threads available per pipeline set to execute SQS output
  replication related tasks such as replication status checks.
* A value of 0 is equivalent to 5.
* Default: 5

remote_queue.sqs_smartbus.check_replication_executor_max_jobs_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of jobs that each replication executor worker thread per pipeline set
  can queue.
* A value of 0 is equivalent to 1000.
* Default: 1000

remote_queue.sqs_smartbus.enable_shared_receipts = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* If "true", receipts will be shared among ingest blobs.
* Default: false

####
# Azure Storage Queue (ASQ) specific settings
####

remote_queue.asq.encoding_format = protobuf|s2s
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the encoding format used to write data to the
  remote queue.
* Default: s2s

remote_queue.asq.enable_inline_data = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies whether to use ASQ directly to send events.
* A value of "true" means that if the data packet is small enough to fit in
  ASQ (64KB max), the Splunk Cloud Platform will use ASQ to send event data.
* This setting only applies when remote_queue.asq.encoding_format = protobuf
* Default: false

remote_queue.asq.access_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The access key to use when authenticating with the remote queue
  system that supports the ASQ API.
* Default: not set

remote_queue.asq.secret_key = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the secret key to use when authenticating with the remote queue
  system supporting the ASQ API.
* Default: not set

remote_queue.asq.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote queue system supporting the ASQ API.
* Example: https://somestorage.queue.core.windows.net/
* Default: not set

remote_queue.asq.retry_policy = [max_count|none]
* Currently not supported. This setting is related to a feature that is still
  under development.
* The retry policy to use for remote queue operations.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation can be
    retried upon intermittent failure. Set max_count with the
    'max_count.max_retries_in_total' setting.
  + "none": Do not retry file operations upon failure.
* This setting is optional.
* Default: "max_count"

remote_queue.asq.max_count.max_retries_in_total = <unsigned integer>
* Currently not supported. This setting is related to a feature that is still
  under development.
* When 'remote_queue.asq.retry_policy' is set to "max_count", sets the
  maximum number of times a queue operation can be retried upon
  intermittent failure.
* This setting is optional.
* Default: 3

remote_queue.asq.timeout.connect = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The connection timeout, in seconds, when interacting with
  ASQ for this queue.
* This setting is optional.
* Default: 5

remote_queue.asq.timeout.read = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The read timeout, in seconds, when interacting with ASQ for
  this queue.
* This setting is optional.
* Default: 60

remote_queue.asq.timeout.write = <unsigned integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The write timeout, in seconds, when interacting with ASQ for
  this queue.
* This setting is optional.
* Default: 60

remote_queue.asq.large_message_store.endpoint = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The URL of the remote storage system supporting the Azure API.
* Example: https://somestorage.blob.core.windows.net/
* Default: not set

remote_queue.asq.large_message_store.path = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The remote storage location where messages that are larger than the
  underlying queue maximum message size will reside.
* If not specified, messages exceeding the underlying queue's maximum message
  size are dropped.
* For Microsoft Azure Blob storage, this is specified
  as "azure://<container-name>/path_to_blob" Note that "<container-name>"
  is needed here only if 'remote_queue.asq.large_message_store.container_name'
  is not set.
* No default.

remote_queue.asq.large_message_store.container_name = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the Azure container to use complying with Microsoft Azure
  Storage Container naming convention.
* This setting is optional.
* No default.

remote_queue.asq.large_message_store.sslVerifyServerCert = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* If set to true, the Splunk platform verifies the certificate
  presented by the Azure server.
* Default: false

remote_queue.asq.large_message_store.sslVersions = <versions_list>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Comma-separated list of SSL versions to connect to
  'remote.asq.large_message_store.endpoint'.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* The special version "*" selects all supported versions.  The version "tls"
  selects all versions tls1.0 or newer.
* If a version is prefixed with "-" it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list
  but does nothing.
* When configured in FIPS mode, ssl3 is always disabled regardless
  of this configuration.
* Default: tls1.2

remote_queue.asq.large_message_store.sslRootCAPath = <path>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Full path to the Certificate Authority (CA) certificate PEM format file
  containing one or more certificates concatenated together. The S3 certificate
  will be validated against the CAs present in this file.
* Default: [sslConfig/caCertFile] in server.conf

remote_queue.asq.large_message_store.cipherSuite = <cipher suite string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* If set, uses the specified cipher string for the SSL connection.
* If not set, uses the default cipher string.
* Default: TLSv1+HIGH:TLSv1.2+HIGH:@STRENGTH

remote_queue.asq.send_interval = <number><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* The interval that the remote queue output processor waits for data to
  arrive before sending a partial batch to the remote queue.
* Examples: 100ms, 5s
* Default: 4s

remote_queue.asq.max_queue_message_size = <integer>[KB|MB|GB]
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum message size for batched events for upload to the remote queue.
* Queue messages contain a series of one or more events. When an event causes
  the message size to exceed this setting, the message is sent to the remote queue.
* Specify this value as an integer followed by KB, MB, or GB (for example,
  10MB is 10 megabytes)
* Default: 10MB

remote_queue.asq.drop_data = <boolean>
* Currently not supported. This setting is related to a feature that is still
  under development.
* Determines whether Splunk software drops the data from all Splunk managed internal
  indexes and indexes listed in 'remote_queue.asq.drop_data_index_list'
* A value of "true" means that Splunk software drops the data.
* Default: false

remote_queue.asq.drop_data_index_list = <comma-separated list>
* Currently not supported. This setting is related to a feature that is still
  under development.
* A comma-separated list of indexes for which you want to drop the data.
  For example: index_1, index_2, index_3.
* If 'remote_queue.asq.drop_data' is set to "true" then Splunk software
  drops the data from 'drop_data_index_list'.
* Default: not set

remote_queue.asq.executor_max_workers_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of worker threads available per pipeline set to execute
  ASQ output worker tasks.
* A value of 0 is equivalent to 1.
* The maximum value for this setting is 20.
* Default: 10

remote_queue.asq.executor_max_jobs_count = <positive integer>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The maximum number of jobs that each worker thread per pipeline set can queue.
* A value of 0 is equivalent to 1.
* The maximum value for this setting is 100.
* Default: 50

remote_queue.asq.large_message_store.encryption_scheme = azure-sse-kv | azure-sse-ms | azure-sse-c
* Currently not supported. This setting is related to a feature that is
  still under development.
* The encryption scheme to use for containers that are currently being stored.
* azure-sse-kv: Maps to the Azure customer-managed keys in a key vault.
  See the Azure documentation for customer-managed keys for Azure Store
  encryption for details.
* azure-sse-ms: Maps to the Azure Microsoft-managed keys in Microsoft key store.
  See the Azure documentation for Azure Storage encryption for data at rest for
  details.
* azure-sse-c: Maps to the Azure customer-provided encryption keys in a Key Vault.
  See the Azure documentation for customer-provided keys for Azure Store
  encryption for details.
* Default: azure-sse-ms

remote_queue.asq.azure-sse-kv.encryptionScope = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Required if remote_queue.asq.large_message_store.encryption_scheme = azure-sse-kv
* Specifies the key used for encrypting blobs within the scope of this index.
* No default.

remote_queue.asq.large_message_store.azure-sse-c.key_type = azure_kv
* Currently not supported. This setting is related to a feature that is
  still under development.
* The mechanism that a Splunk platform indexer uses to generate the key for
  sending data to Azure Storage.
* Affects the 'azure-sse-c' encryption scheme only.
* The only valid value is "azure_kv", which indicates the Azure Key Vault
  Key Management Service (Azure KMS).
* You must also specify the required KMS settings:
  'remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_id',
  'remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_tenant_id',
  'remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_client_id',
  and 'remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_client_secret'.
  If you do not specify those settings, the indexer cannot start while the
  'remote_queue.asq.large_message_store.encryption_scheme' setting
  has a value of "azure-sse-c".
* Default: azure_kv

remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The Azure Key Vault key identifier for key encryption and decryption.
* The key identifier must include the key version.
* Required if 'remote_queue.asq.large_message_store.encryption_scheme' has
  a value of "azure-sse-c".
* Example: "https://<key-vault-name>.vault.azure.net/keys/<key-name>/<key-version>"
* No default.

remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_tenant_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The ID of the Azure Active Directory tenant for authenticating
  with the the Key Vault.
* For more details about the tenant ID, check your Azure Active Directory subscription.
* Required only for client token-based authentication.
* No default.

remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_client_id = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the ID of the client, also called the application ID, which is the unique
  identifier that the Azure Active Directory issues to an application registration
  that identifies a specific application and the associated configurations.
* You can obtain the client ID for an application from the Azure Portal in the
  Overview section for the registered application.
* Required only for client token-based authentication.
* Optional for managed identity authentication.
* No default.

remote_queue.asq.large_message_store.azure-sse-c.azure_kv.key_vault_client_secret = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the secret key to use when authenticating the Key Vault using the client_id.
* You generate the secret key through the Azure Portal.
* Required only for client token-based authentication.
* No default.

remote_queue.asq.large_message_store.enable_shared_receipts = <boolean>
* Currently not supported. This setting is related to a feature that is
  still under development.
* If "true", receipts will be shared among ingest blobs.
* Default: false

####
# Remote File System (RFS) Output
####
[rfs]
* Global settings that individual rfs output destinations can inherit.

partitionBy = legacy | (year|month|day) [, sourcetype]
* Specifies schema to partition and store events into seperate files on the
  rfsoutput destination(s). It affects the file storage location specified by
  the "path" for any given destination in the manner described below.
  * legacy - no partitioning and the events are batched together on the order of
    arrival. This appends path segments that encode the latest timestamp among
    all events in the batch similar to the strftime format "%Y/%m/%d".
  * year|month|day - span of event timestamp to use as the primary partition key.
    This encodes primary field as multiple path segments and appends to the path
    in the decreasing order of significance. For example, "day" produces
    "year=%Y/month=%m/day=%d", "month" produces "year=%Y/month=%m" and "year"
    produces "year=%Y".
  * sourcetype - optional secondary partition key applied over primary partition key.
    This appends a single path segment encoded in the form "sourcetype=<sourcetype>".
* Examples:
    Illustrated below is the set of possible settings and how they affect the
    file storage path, for events generated on August 15, 2022.
    * partitionBy = day, sourcetype
       Results file path into "<path>/year=2022/month=08/day=15/sourcetype=<srctype>/"
    * partitionBy = day
       Results file path into "<path>/year=2022/month=08/day=15/"
    * partitionBy = month
       Results file path into "<path>/year=2022/month=08/"
    * partitionBy = year
       Results file path into "<path>/year=2022/"
    * partitionBy = legacy
       Results file path into "<path>/2022/08/15/"
* Default: legacy

dropEventsOnUploadError = <boolean>
* Whether or not the ingest actions feature drops events if it encounters an
  error when uploading events to output destination.
* A value of "true" means that, if there is an error writing to the destination, the
  error will be logged, and the events in that batch dropped. Ingest will not be
  blocked, but data might be lost.
* A value of "false" means, if there is an error writing to the destination, the
  error will be logged, and events will NOT be dropped. splunkd will continually
  attempt to write the batch. Because events are not dropped, this might cause
  queues to become blocked, and data ingestion to stop.
* This setting is optional.
* Default: false

batchSizeThresholdKB = <integer>
* The size, in kilobytes, of the uncompressed events in the RfsOutputProcessor send buffer.
  RfsOutputProcessor batches events before writing them into files on the destination.
  If the current buffer size is greater than 'batchSizeThresholdKB' kilobytes, then
  the data will be written to the destination immediately.
* This threshold may not be honored if the total memory usage for raw events exceeds
  limits.conf/[ingest_actions]/rfs.provider.rawdata_limit_mb for a storage provider.
* If you increase this setting, you may also want to increase the value of
  server.conf/[queue:rfsQueue]/maxSize.
* Not applicable if the rfs destination is a file system destination; that is, if the pathname starts with 'file://'.
* Default: 131072 (128 MiB)
* Max threshold value: 5242880 (5 GiB)

batchTimeout = <integer>
* RfsOutputProcessor batches events before flushing to the destination.
* If a batch has not hit any other criteria for being flushed, and
  the batch is at least this many seconds old, flush the batch.
* This threshold may not be honored if the total memory usage for raw events exceeds
  limits.conf/[ingest_actions]/rfs.provider.rawdata_limit_mb for a storage provider.
* Default = 30

compression = none|gzip|lz4|zstd
* Sets the algorithm to use for compressing files before writing to the destination.
* The RfsOutputProcessor writes files with the appropriate extension for the compression
  algorithm, for example, .zst for zstd, .gz for gzip and .lz4 for lz4.
* To change the compression setting, delete the destination and recreate again with desired compression type.
* Default: zstd

compressionLevel = <integer>
* Sets compression level for the specified compression algorithm,
  when RfsOutputProcessor writes files. Must be between 0 and 10.
* Default: 3

format = json|ndjson|raw
* Specifies output format when RfsOutputProcessor writes events into files 
  on the destination.
* json: The file will include a JSON array. Each event will be element of 
  the JSON array.
* ndjson: The file will include multiple JSON objects separated by a newline 
  character. Each event is corresponding to one JSON object.
* raw: The file includes multiple raw events separated by a newline character.
* Default: json

format.json.index_time_fields = <boolean>
* Specifies whether to include index-time fields when RfsOutputProcessor 
  writes events to the destination in HEC JSON format.
* Default: true

format.ndjson.index_time_fields = <boolean>
* Specifies whether to include index-time fields when RfsOutputProcessor 
  writes events to the destination in new line delimited JSON format.
* Default: true

fs.appendToFileUntilSizeMB = <integer>
* Applicable only if rfs destination is a file system (local or nfs) destination.
* For file system, rfs output will create one active output file for each hour of that partition
  and will continuously append the events in its respective hourly output file.
* Note: For file system, only partitionBy = day[, sourcetype] is allowed.
* Once the size of the output file for the current hour exceeds fs.appendToFileUntilSizeMB,
  a new hourly output file with a new sequence number will be created.
* The recommended value for fs.appendToFileUntilSizeMB is the default value, 2048.
* Do not set the value below 250, otherwise this threshold might not be honored, causing
  file size to potentially be much larger.
* Output file size may not be precisely equal to fs.appendToFileUntilSizeMB, as it depends
  on how much data can be fetched from the pipeline. To ensure file size is similar to the
  given value for fs.appendToFileUntilSizeMB, set fs.appendToFileUntilSizeMB to 2048 or larger.
* Default: 2048
* Max threshold value: 17180 (16 GiB)

fs.timeBeforeClosingFileSecs = <integer>
* Applicable only if rfs destination is a file system (local or nfs) destination.
* After every batchTimeout seconds, the instance checks whether an open file descriptor
  has not been used within the last fs.timeBeforeClosingFileSecs seconds. If so, the
  instance closes the file descriptor.
* Do not manually remove the destination files while the instance has the file descriptor
  opened. Doing so can result in data loss.
* A high value setting can result in less file descriptor availability for other system uses.
* The effective closing time for an open file descriptor can be in a range from batchTimeout
  to (batchTimeout + fs.timeBeforeClosingFileSecs)
* Must be set to a non-zero positive number. Otherwise, the value is overridden
  by the default value specified in the global [rfs] stanza.
* Default: 30

[rfs:<name>]

* This section explains the configuration settings for the ingest actions feature
  to send data to an external storage interface, such as AWS S3 or a file-system mount.
* Each [rfs:<name>] stanza represents an individually configured location.
* The "name" is a unique identifier for the storage destination, and is shown
  as a routing destination when using the ingest actions UI.
  For example: [rfs:syslog_filtered_events], [rfs:threat_detection_logs] etc.

path = <string>
* Required.
* This setting points to the storage location where files would be stored.
* The format for specifying storage location is:
  <scheme>://<storage-location-specifier>
    * The "scheme" identifies the storage interface used.
    * Currently "s3" and "file" are the only supported schemes.
    * The "storage-location-specifier" is a system-specific string for
      identifying a location inside the storage system.
    * For AWS S3, this is specified as "path=s3://mybucket/some/path"
    * For filesystem interface, this is specified as "file://my/local/path"

description = <string>
* Optional.
* A general description to explain the configuration settings for the ingest actions
  feature to send data to a destination.
* No default.

remote.* = <string>
* Optional.
* This section explains possible settings for configuring a remote output.
* With remote outputs, the splunk indexer might require additional configuration,
  specific to the type of remote storage. You can pass configuration information
  to the splunk indexer by specifying the settings through the following schema:
  remote_queue.<scheme>.<config-variable> = <value>.
  For example:
  remote.s3.access_key = ACCESS_KEY
  Refer to "Volume settings" in indexes.conf for all settings.
* This setting is optional.
* No default.

remote.s3.access_key = <string>
* Specifies the access key to use when authenticating with the remote storage
  system supporting the S3 API.
* If not specified, the indexer will look for these environment variables:
  AWS_ACCESS_KEY_ID or AWS_ACCESS_KEY (in that order).
* If the environment variables are not set and the indexer is running on EC2,
  the indexer attempts to use the access key from the IAM role.
* Optional.
* No default.

remote.s3.secret_key = <string>
* Specifies the secret key to use when authenticating with the remote storage
  system supporting the S3 API.
* If not specified, the indexer will look for these environment variables:
  AWS_SECRET_ACCESS_KEY or AWS_SECRET_KEY (in that order).
* If the environment variables are not set and the indexer is running on EC2,
  the indexer attempts to use the secret key from the IAM role.
* Optional.
* No default.

remote.s3.signature_version = v2|v4
* The signature version to use when authenticating with the remote storage
  system supporting the S3 API.
* For 'sse-kms' and 'sse-c' server-side encryption schemes, and for 'cse'
  client-side encryption scheme, you must use signature_version=v4.
* For signature_version=v2 you must set url_version=v1.
* Optional.
* Default: v4

remote.s3.url_version = v1|v2
* Specifies which url version to use, both for parsing the endpoint/path, and
* for communicating with the remote storage. This value only needs to be
* specified when running on non-AWS S3-compatible storage that has been configured
* to use v2 urls.
* In v1 the bucket is the first element of the path.
* Example: mydomain.com/bucketname/rest/of/path
* In v2 the bucket is the outermost subdomain in the endpoint.
* Exmaple: bucketname.mydomain.com/rest/of/path
* Default: v1

remote.s3.supports_versioning = <boolean>
* Specifies whether the remote storage supports versioning.
* Versioning is a means of keeping multiple variants of an object
  in the same bucket on the remote storage.
* This setting determines how splunkd removes data from remote storage.
  If set to true, splunkd will delete all versions of objects at
  time of data removal. Otherwise, if set to false, splunkd will use a simple DELETE
  (See https://docs.aws.amazon.com/AmazonS3/latest/dev/DeletingObjectVersions.html).
* Optional.
* Default: true

remote.s3.endpoint = <URL>
* The URL of the remote storage system supporting the S3 API.
* The scheme, http or https, can be used to enable or disable SSL connectivity
  with the endpoint.
* If not specified and the indexer is running on EC2, the endpoint will be
  constructed automatically based on the EC2 region of the instance where the
  indexer is running, as follows: https://<bucketname>.s3.<region>.amazonaws.com
* Example: https://<bucketname>.s3.us-west-2.amazonaws.com
* Optional.

remote.s3.encryption = sse-s3 | sse-kms | none
* The encryption scheme to use for output to remote storage for data stored (data at rest).
* sse-s3: Search for "Protecting Data Using Server-Side Encryption with AWS S3-Managed
          Encryption Keys" on the Amazon Web Services documentation site.
* sse-kms: Search for "Protecting Data Using Server-Side Encryption with CMKs Stored in AWS
           Key Management Service (SSE-KMS)" on the Amazon Web Services documentation site.
* Note: sse-c is not supported for RfsOutputProcessor
* Optional.
* No default.

remote.s3.auth_region = <string>
* The authentication region to use for signing requests when interacting
  with the remote storage system supporting the S3 API.
* Used with v4 signatures only.
* If unset and the endpoint (either automatically constructed or explicitly
  set with remote.s3.endpoint setting) uses an AWS URL (for example,
  https://<bucketname>.s3.us-west-1.amazonaws.com), the instance attempts to extract
  the value from the endpoint URL (for example, "us-west-1").  See the
  description for the remote.s3.endpoint setting.
* If unset and an authentication region cannot be determined, the request
  will be signed with an empty region value. This can lead to rejected
  requests when using non-AWS S3-compatible storage.
* Optional.
* No default.

remote.s3.retry_policy = max_count
* Sets the retry policy to use for remote file operations.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a file operation will be
    retried upon intermittent failure both for individual parts of a multipart
    download or upload and for files as a whole.
* Optional.
* Default: max_count

remote.s3.sslVerifyServerCert = <boolean>
* If this is set to true, Splunk verifies certificate presented by S3
  server and checks that the common name/alternate name matches the ones
  specified in 'remote.s3.sslCommonNameToCheck' and
  'remote.s3.sslAltNameToCheck'.
* Optional
* Default: false

remote.s3.sslVersions = <versions_list>
* Comma-separated list of SSL versions to connect to 'remote.s3.endpoint'.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* The special version "*" selects all supported versions.  The version "tls"
  selects all versions tls1.0 or newer.
* If a version is prefixed with "-" it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list
  but does nothing.
* When configured in FIPS mode, ssl3 is always disabled regardless
  of this configuration.
* Optional.
* Default: tls1.2

remote.s3.sslCommonNameToCheck = <commonName1>, <commonName2>, ..
* If this value is set, and 'remote.s3.sslVerifyServerCert' is set to true,
  splunkd checks the common name of the certificate presented by
  the remote server (specified in 'remote.s3.endpoint') against this list
  of common names.
* Default: not set

remote.s3.sslAltNameToCheck = <alternateName1>, <alternateName2>, ..
* If this value is set, and 'remote.s3.sslVerifyServerCert' is set to true,
  splunkd checks the alternate name(s) of the certificate presented by
  the remote server (specified in 'remote.s3.endpoint') against this list of
  subject alternate names.
* No default.

remote.s3.sslRootCAPath = <path>
* Full path to the Certificate Authority (CA) certificate PEM format file
  containing one or more certificates concatenated together. S3 certificate
  will be validated against the CAs present in this file.
* Optional.
* Default: The value of '[sslConfig]/caCertFile' in server.conf

remote.s3.cipherSuite = <cipher suite string>
* If set, uses the specified cipher string for the SSL connection.
* If not set, uses the default cipher string.
* Must specify 'dhFile' to enable any Diffie-Hellman ciphers.
* Optional.
* Default: TLSv1+HIGH:TLSv1.2+HIGH:@STRENGTH

remote.s3.ecdhCurves = <comma-separated list>
* ECDH curves to use for ECDH key negotiation.
* The curves should be specified in the order of preference.
* The client sends these curves as a part of Client Hello.
* Splunk software only supports named curves specified
  by their SHORT names.
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* e.g. ecdhCurves = prime256v1,secp384r1,secp521r1
* Optional.
* No default.

remote.s3.kms.auth_region = <string>
* Required if 'remote.s3.auth_region' is unset and Splunk can not
  automatically extract this information.
* Similar to 'remote.s3.auth_region'.
* If not specified, KMS access uses 'remote.s3.auth_region'.
* No default.

remote.s3.kms.key_id = <string>
* Required if remote.s3.encryption = sse-kms
* Specifies the identifier for Customer Master Key (CMK) on KMS. It can be the
  unique key ID or the Amazon Resource Name (ARN) of the CMK or the alias
  name or ARN of an alias that refers to the CMK.
* Examples:
  Unique key ID: 1234abcd-12ab-34cd-56ef-1234567890ab
  CMK ARN: arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
  Alias name: alias/ExampleAlias
  Alias ARN: arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias
* No default.

remote.s3.kms.<ssl_settings> = <...>
* Optional.
* See the descriptions of the SSL settings for remote.s3.<ssl_settings>
  above. e.g. remote.s3.sslVerifyServerCert.
* Valid ssl_settings are sslVerifyServerCert, sslVersions, sslRootCAPath,
  sslAltNameToCheck, sslCommonNameToCheck, cipherSuite, ecdhCurves, and dhFile.
* All of these settings are optional.
* All of these settings have the same defaults as
  'remote.s3.<ssl_settings>'.

remote.s3.metadata_max_attempts = <integer>
* Imposes a maximum number of times an operation will be
  retried upon failing to retrieve credentials from EC2 metadata service endpoint.
* This value must be between 1 and 10.
* Default: 10

remote.sts.assume_role.role_arn = <string>
* This feature is supported on Splunk Cloud only.
* The Amazon Resource Name (ARN) of the role to assume.
* Normally, splunkd will use whatever credentials are available (i.e. access_key/secret_key, instance
  IAM roles, etc) to directly access AWS services, such as S3 and KMS. If this is set, instead of
  using those credentials directly, splunkd will contact the STS AssumeRole API to get credentials
  associated with the role here, and use that "assumed" role to access other services.
* Make sure only to specify this when need temporary security credentials
  to access AWS resources that you might not normally have access to.
* Example:
  arn:aws:iam::111122223333:role/SplunkIngestActions
* Only applicable when the rfs destination is an aws s3 destination (path starts with 's3://').
* No default

remote.sts.assume_role.external_id = <string>
* This feature is supported on Splunk Cloud only.
* A unique identifier that might be required when you assume a role in another account.
* If the account to which the role belongs requires an external ID to assume,
  then must provide that value here.
* No default

remote.sts.assume_role.duration_secs = <integer>
* The duration, in seconds, of the role session.
* The value specified can range from 900 seconds (15 minutes) up to
  the maximum session duration set for the role.
* If you specify a value higher than this setting or the administrator setting (whichever is lower),
  the operation fails. For example, if you specify a session duration of 12 hours,
  but your administrator set the maximum session duration to 6 hours, your operation fails.
* Default: 3600

authMethod = <string>
* The authentication method used to access the remote destination.
* Optional.
* Do not configure this setting in outputs.conf. The system populates
* this setting when you choose an Authentication Method in the New or Edit
* Destination setup window in Splunk Web.
* Choosing “Access key and Secret key” in Splunk Web sets this
* setting to “basic”.
* Choosing “IAM role” in Splunk Web sets this setting to "iam".
* No default.

partitionBy = legacy | (year|month|day) [, sourcetype]
* Specifies schema to partition and store events forwarded to this destination.
  Any setting will override the global partitionBy settings of [rfs] stanza.
  Refer to the detailed description of this property under global [rfs] stanza
  and how it affects the file storage path.
* Default: Inherited partitionBy setting from the global [rfs] stanza.

dropEventsOnUploadError = <boolean>
* Whether or not the ingest actions feature drops events if it encounters an
  error when uploading events to remote storage.
* A value of "true" means that, if there is an error writing to a remote file system, the
  error will be logged, and the events in that batch dropped. Ingest will not be
  blocked, but data might be lost.
* A value of "false" means, if there is an error writing to a remote file system, the
  error will be logged, and events will NOT be dropped. splunkd will continually
  attempt to write the batch. Because events are not dropped, this might cause
  queues to become blocked, and data ingestion to stop.
* This setting is optional.
* Default: Inherited dropEventsOnUploadError setting from the global [rfs] stanza.

batchSizeThresholdKB = <integer>
* The size, in kilobytes, of the uncompressed events in the RfsOutputProcessor send buffer.
* RfsOutputProcessor batches events before flushing them to destination.
* If the current buffer size is greater than 'batchSizeThresholdKB' kilobytes, then
* the data will be written to the destination immediately.
* If you increase this setting, you may also want to increase the value of
  server.conf/[queue:rfsQueue]/maxSize.
* Not applicable if the rfs destination is a file system destination; that is, if the pathname starts with 'file://'
* Default: Inherited batchSizeThresholdKB setting from the global [rfs] stanza.

batchTimeout = <integer>
* RfsOutputProcessor batches events before flushing to the destination.
* If a batch has not hit any other criteria for being flushed, and
  the batch is at least this many seconds old, flush the batch.
* Default: Inherited batchTimeout setting from the global [rfs] stanza.

compression = none|gzip|lz4|zstd
* Sets the algorithm to use for compressing files before writing to the destination.
* The RfsOutputProcessor writes files with the appropriate extension for the compression
  algorithm, for example, .zst for zstd, .gz for gzip and .lz4 for lz4.
* Default: Inherited compression setting from the global [rfs] stanza.

compressionLevel = <integer>
* Sets compression level for the specified compression algorithm,
  when RfsOutputProcessor writes files. Must be between 0 and 10.
* Default: Inherited compressionLevel setting from the global [rfs] stanza.

format = json|ndjson|raw
* Specifies output format when RfsOutputProcessor writes events into files 
  on the destination.
* json: The file will include a JSON array. Each event will be element of 
  the JSON array.
* ndjson: The file will include multiple JSON objects separated by a newline 
  character. Each event is corresponding to one JSON object.
* raw: The file includes multiple raw events separated by a newline character.
* Default: Inherited format setting from the global [rfs] stanza.

format.json.index_time_fields = <boolean>
* Specifies whether to include index-time fields when RfsOutputProcessor 
  writes events to the destination in HEC JSON format.
* Default: Inherited format.json.index_time_fields setting from the global 
  [rfs] stanza.

format.ndjson.index_time_fields = <boolean>
* Specifies whether to include index-time fields when RfsOutputProcessor 
  writes events to the destination in new line delimited JSON format.
* Default: Inherited format.ndjson.index_time_fields setting from the global 
  [rfs] stanza.

fs.appendToFileUntilSizeMB = <integer>
* Applicable only if rfs destination is a file system (local or nfs) destination.
* For file system, rfs output will create one active output file for each hour of that partition
  and will continuously append the events in its respective hourly output file.
* Note: For file system, only partitionBy = day[, sourcetype] is allowed.
* Once the size of the output file for the current hour exceeds fs.appendToFileUntilSizeMB,
  a new hourly output file with a new sequence number will be created.
* The recommended value for fs.appendToFileUntilSizeMB is the default value, 2048.
* Do not set the value below 250, otherwise this threshold might not be honored, causing
  file size to potentially be much larger.
* Output file size may not be precisely equal to fs.appendToFileUntilSizeMB, as it depends
  on how much data can be fetched from the pipeline. To ensure file size is similar to the
  given value for fs.appendToFileUntilSizeMB, set fs.appendToFileUntilSizeMB to 2048 or larger.
* Default: Inherited fs.appendToFileUntilSizeMB setting from the global [rfs] stanza.

fs.timeBeforeClosingFileSecs = <integer>
* Applicable only if rfs destination is a file system (local or nfs) destination.
* After every batchTimeout seconds, the instance checks whether an open file descriptor
  has not been used within the last fs.timeBeforeClosingFileSecs seconds. If so, the
  instance closes the file descriptor.
* Do not manually remove the destination files while the instance has the file descriptor
  opened. Doing so can result in data loss.
* A high value setting can result in less file descriptor availability for other system uses.
* The effective closing time for an open file descriptor can be in a range from batchTimeout
  to (batchTimeout + fs.timeBeforeClosingFileSecs)
* Must be set to a non-zero positive number. Otherwise, the value is overridden
  by the default value specified in the global [rfs] stanza.
* Default: Inherited fs.timeBeforeClosingFileSecs setting from the global [rfs] stanza.

####
# Cloud Processing Queue Output
####

[cloud_processing_queue]

* This section explains possible settings for configuring a cloud processing queue.
* Each cloud_processing_queue stanza represents an individually configured cloud
  processing queue output.
* NOTE: Only 1 cloud processing queue stanza is supported as an
  output queue.

cloud_processing_queue.* = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* Optional.
* This section explains possible settings for configuring a cloud processing queue.
* With cloud processing queues, the indexer might require additional configuration,
  which is specific to the type of cloud processing queue.
  You can pass configuration information to the indexer by specifying the settings
  through the following schema: cloud_processing_queue.<scheme>.<config-variable> = <value>.
  For example:
  cloud_processing_queue.cp_queue.encoding_format = s2s
* No default.

cloud_processing_queue.type = cp_queue
* Currently not supported. This setting is related to a feature that is
  still under development.
* Required.
* Specifies the cloud processing queue type, for example, CP Queue.

####
# Cloud Processing Queue (CP Queue) specific settings
####

cloud_processing_queue.cp_queue.encoding_format = s2s
* Currently not supported. This setting is related to a feature that is
  still under development.
* Specifies the encoding format used to write data to the
  cloud processing queue.
* Default: s2s

cloud_processing_queue.cp_queue.retry_policy = max_count|none
* Sets the retry policy to use for cloud processing queue operations.
* A retry policy specifies whether and how to retry file operations that fail
  for those failures that might be intermittent.
* Retry policies:
  + "max_count": Imposes a maximum number of times a queue operation is
    retried upon intermittent failure. Set "max_count" with the
    'max_count.max_retries_per_part' setting.
  + "none": Do not retry file operations upon failure.
* Optional.
* Default: max_count

cloud_processing_queue.cp_queue.max_count.max_retries_per_part = <unsigned integer>
* When the 'cloud_processing_queue.cp_queue.retry_policy' setting is "max_count", 
  sets the maximum number of times a queue operation will be retried upon intermittent
  failure.
* Optional.
* Default: 3

cloud_processing_queue.cp_queue.large_message_store.sslVerifyServerCert = <boolean>
* A value of "true" means the Splunk platform verifies the certificate presented by the S3
  server and checks that the common name and alternate name match the ones
  specified in 'cloud_processing_queue.cp_queue.large_message_store.sslCommonNameToCheck' and
  'cloud_processing_queue.cp_queue.large_message_store.sslAltNameToCheck'.
* Default: false

cloud_processing_queue.cp_queue.large_message_store.sslVersions = <comma-separated list>
* A list of TLS versions to use to connect to the large message store.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* The special version "*" selects all supported versions.  The version "tls"
  selects all versions tls1.0 or newer.
* If a version is prefixed with "-" it is removed from the list.
* SSLv2 is always disabled; "-ssl2" is accepted in the version list
  but does nothing.
* When configured in FIPS mode, ssl3 is always disabled regardless
  of this configuration.
* Default: tls1.2

cloud_processing_queue.cp_queue.large_message_store.sslRootCAPath = <string>
* Full path to the Certificate Authority (CA) certificate PEM format file
  containing one or more certificates concatenated together.
  The S3 certificate will be validated against the CAs present in this file.
* Default: The value of [sslConfig]/'caCertFile' in server.conf

cloud_processing_queue.cp_queue.large_message_store.cipherSuite = <cipher suite string>
* If set, uses the specified cipher string for the SSL connection.
* If not set, uses the default cipher string.
* You must specify 'dhFile' to enable any Diffie-Hellman ciphers.
* Default: TLSv1+HIGH:TLSv1.2+HIGH:@STRENGTH

cloud_processing_queue.cp_queue.large_message_store.ecdhCurves = <comma-separated list>
* ECDH curves to use for ECDH key negotiation.
* Specify the curves in the order of preference.
* The client sends these curves as a part of Client Hello.
* Splunk software only supports named curves specified
  by their short names.
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* e.g. ecdhCurves = prime256v1,secp384r1,secp521r1
* Default: not set

cloud_processing_queue.cp_queue.large_message_store.encryption_scheme = sse-s3 | none
* Currently not supported. This setting is related to a feature that is
  still under development.
* The encryption scheme used by remote storage.
* Default: none.

cloud_processing_queue.cp_queue.large_message_store.key_refresh_interval = <string>
* Currently not supported. This setting is related to a feature that is
  still under development.
* The time interval to refresh primary key.
* Default: 24h

####
# Cloud Processing API (CP Client) specific settings
####

cloud_processing_queue.cp_client.retry_policy = max_count|none
* The retry policy to use for cloud processing API operations.
* A retry policy determines whether and how to retry API operations that fail
  for those failures that might be intermittent.
* The following retry policies are available:
  + "max_count": Imposes a maximum number of times an operation is
    retried upon intermittent failure. Set "max_count" with the
    'cloud_processing_queue.max_count.max_retries_per_part' setting.
  + "none": Do not retry file operations upon failure.
* This setting is optional.
* Default: max_count

cloud_processing_queue.cp_client.max_count.max_retries_per_part = <unsigned integer>
* The maximum number of times that the cloud processing API will retry an
  operation after an intermittent failure.
* This setting is valid only when the 'cloud_processing_queue.cp_client.retry_policy'
  setting has a value of "max_count".
* This setting is optional.
* Default: 9

cloud_processing_queue.cp_client.backoff_strategy = constant | exponential
* Currently not supported. This setting is related to a feature that is
  still under development.
* The backoff strategy that the cloud processing API is to use when
  it retries requests after an intermittent failure.
* A value of "constant" means that the backoff strategy makes a retry attempt
  every 'cloud_processing_queue.cp_client.backoff_strategy.constant.delay'.
* A value of "exponential" means that the backoff strategy doubles each retry
  attempt, starting with 1 second, but caps at a maximum of 5 minutes between
  attempts.
* Optional
* Default: exponential

cloud_processing_queue.cp_client.backoff_strategy.constant.delay = <interval><unit>
* Currently not supported. This setting is related to a feature that is
  still under development.
* How long that the cloud processing API must wait between
  successive retries after it encounters an intermittent failure
  in an API operation.
* This setting is valid only when
  'cloud_processing_queue.cp_client.backoff_strategy' has a value of "constant".
* This setting is optional.
* Default: 300ms
