#   Version 7.1.2
#
# This file contains possible attributes and values you can use to configure
# distributed search.
#
# To set custom configurations, place a distsearch.conf in
# $SPLUNK_HOME/etc/system/local/.  For examples, see distsearch.conf.example.
# You must restart Splunk to enable configurations.
#
# To learn more about configuration files (including precedence) please see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles
#
# These attributes are all configured on the search head, with the exception of
# the optional attributes listed under the SEARCH HEAD BUNDLE MOUNTING OPTIONS
# heading, which are configured on the search peers.

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top of
#     the file.
#   * Each conf file should have at most one default stanza. If there are
#     multiple default stanzas, attributes are combined. In the case of
#     multiple definitions of the same attribute, the last definition in the
#     file wins.
#   * If an attribute is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.

[distributedSearch]
* Set distributed search configuration options under this stanza name.
* Follow this stanza name with any number of the following attribute/value
  pairs.
* If you do not set any attribute, Splunk uses the default value (if there
  is one listed).

disabled = [true|false]
* Toggle distributed search off (true) and on (false).
* Defaults to false (your distributed search stanza is enabled by default).

heartbeatMcastAddr = <IP address>
* This setting is deprecated

heartbeatPort = <port>
* This setting is deprecated

ttl = <integer>
* This setting is deprecated

heartbeatFrequency = <int, in seconds>
* This setting is deprecated

statusTimeout = <int, in seconds>
* Set connection timeout when gathering a search peer's basic
  info (/services/server/info).
* Note: Read/write timeouts are automatically set to twice this value.
* Defaults to 10.

removedTimedOutServers = [true|false]
* This setting is no longer supported, and will be ignored.

checkTimedOutServersFrequency = <integer, in seconds>
* This setting is no longer supported, and will be ignored.

autoAddServers = [true|false]
* This setting is deprecated

bestEffortSearch = [true|false]
* Whether to remove a peer from search when it does not have any of our
  bundles.
* If set to true searches will never block on bundle replication, even when a
  peer is first added - the peers that don't have any common bundles will
  simply not be searched.
* Defaults to false

skipOurselves = [true|false]
* This setting is deprecated

servers = <comma separated list of servers>
* Initial list of servers.
* Each member of this list must be a valid uri in the format of scheme://hostname:port

disabled_servers = <comma separated list of servers>
* A list of disabled search peers. Peers in this list are not monitored or searched.
* Each member of this list must be a valid uri in the format of scheme://hostname:port

quarantined_servers = <comma separated list of servers>
* A list of quarantined search peers.
* Each member of this list must be a valid uri in the format of scheme://hostname:port
* The admin may quarantine peers that seem unhealthy and are degrading search
  performancce of the whole deployment.
* Quarantined peers are monitored but not searched by default.
* A user may use the splunk_server arguments to target a search to qurantined peers
  at the risk of slowing the search.
* When a peer is quarantined, running realtime searches will NOT be restarted. Running
  realtime searches will continue to return results from the quarantined peers. Any
  realtime searches started after the peer has been quarantined will not contact the peer.
* Whenever a quarantined peer is excluded from search, appropriate warnings will be displayed
  in the search.log and Job Inspector
 
shareBundles = [true|false]
* Indicates whether this server will use bundle replication to share search
  time configuration with search peers.
* If set to false, the search head assumes that all the search peers can access
  the correct bundles via share storage and have configured the options listed
  under "SEARCH HEAD BUNDLE MOUNTING OPTIONS".
* Defaults to true.

useSHPBundleReplication = <bool>|always
* Relevant only in search head pooling environments. Whether the search heads
  in the pool should compete with each other to decide which one should handle
  the bundle replication (every time bundle replication needs to happen) or
  whether each of them should individually replicate the bundles.
* When set to always and bundle mounting is being used then use the search head
  pool guid rather than  each individual server name to identify bundles (and
  search heads to the remote peers).
* Defaults to true

trySSLFirst = <bool>
* This setting is no longer supported, and will be ignored.

peerResolutionThreads = <int>
* This setting is no longer supported, and will be ignored.

defaultUriScheme = [http|https]
* When a new peer is added without specifying a scheme for the uri to its management
  port we will use this scheme by default.
* Defaults to https

serverTimeout = <int, in seconds>
* REMOVED, this setting is now ignored and has been replaced by
  connectionTimeout, sendTimeout, receiveTimeout

connectionTimeout = <int, in seconds>
* Amount of time in seconds to use as a timeout during search peer connection
  establishment.

sendTimeout = <int, in seconds>
* Amount of time in seconds to use as a timeout while trying to write/send data
  to a search peer.

receiveTimeout = <int, in seconds>
* Amount of time in seconds to use as a timeout while trying to read/receive
  data from a search peer.

authTokenConnectionTimeout = <number, in seconds>
* Maximum number of seconds to connect to a remote search peer, when getting
  its auth token
* Fractional seconds are allowed
* Default is 5

authTokenSendTimeout = <number, in seconds>
* Maximum number of seconds to send a request to the remote peer, when getting
  its auth token
* Fractional seconds are allowed
* Default is 10

authTokenReceiveTimeout = <number, in seconds>
* Maximum number of seconds to receive a response from a remote peer, when
  getting its auth token
* Fractional seconds are allowed
* Default is 10

#******************************************************************************
# DISTRIBUTED SEARCH KEY PAIR GENERATION OPTIONS
#******************************************************************************

[tokenExchKeys]

certDir = <directory>
* This directory contains the local Splunk instance's distributed search key
  pair.
* This directory also contains the public keys of servers that distribute
  searches to this Splunk instance.

publicKey = <filename>
* Name of public key file for this Splunk instance.

privateKey = <filename>
* Name of private key file for this Splunk instance.

genKeyScript = <command>
* Command used to generate the two files above.

#******************************************************************************
# REPLICATION SETTING OPTIONS
#******************************************************************************

[replicationSettings]

connectionTimeout = <int, in seconds>
* The maximum number of seconds to wait before timing out on initial connection
  to a peer.

sendRcvTimeout = <int, in seconds>
* The maximum number of seconds to wait for the sending of a full replication
  to a peer.

replicationThreads = <positive int>|auto
* The maximum number of threads to use when performing bundle replication to peers.
* If you configure this setting to "auto", the peer autotunes the number of threads it uses for bundle replication.
** If the peer has less than 4 CPUs, it allocates 2 threads.
** If the peer has 4 or more, but less than 8 CPUs, it allocates up to '# of CPUs - 2' threads.
** If the peer has 8 or more, but less than 16 CPUs, it allocates up to '# of CPUs - 3' threads.
** If the peer has 16 or more CPUs, it allocates up to '# of CPUs - 4' threads.
* Defaults to 5.

maxMemoryBundleSize = <int>
* The maximum size (in MB) of bundles to hold in memory. If the bundle is
  larger than this the bundles will be read and encoded on the fly for each
  peer the replication is taking place.
* Defaults to 10

maxBundleSize = <int>
* The maximum size (in MB) of the bundle for which replication can occur. If
  the bundle is larger than this  bundle replication will not occur and an
  error message will be logged.
* Defaults to: 2048 (2GB)

concerningReplicatedFileSize = <int>
* Any individual file within a bundle that is larger than this value (in MB)
  will trigger a splunkd.log message.
* Where possible, avoid replicating such files, e.g. by customizing your blacklists.
* Defaults to: 500

excludeReplicatedLookupSize = <int>
* Any lookup file larger than this value (in MB) will be excluded from the knowledge bundle that the search head replicates to its search peers.
* When this value is set to 0, this feature is disabled.
* Defaults to 0

allowStreamUpload = auto | true | false
* Whether to enable streaming bundle replication for peers.
* If set to auto, streaming bundle replication will be used when connecting to
  peers with a complete implementation of this feature (Splunk 6.0 or higher).
* If set to true, streaming bundle replication will be used when connecting to
  peers with a complete or experimental implementation of this feature (Splunk
  4.2.3 or higher).
* If set to false, streaming bundle replication will never be used.
  Whatever the value of this setting, streaming bundle replication will not be
  used for peers that completely lack support for this feature.
* Defaults to: auto

allowSkipEncoding = <bool>
* Whether to avoid URL-encoding bundle data on upload.
* Defaults to: true

allowDeltaUpload = <bool>
* Whether to enable delta-based bundle replication.
* Defaults to: true

sanitizeMetaFiles = <bool>
* Whether to sanitize or filter *.meta files before replication.
* This feature can be used to avoid unnecessary replications triggered by
  writes to *.meta files that have no real effect on search behavior.
* The types of stanzas that "survive" filtering are configured via the
  replicationSettings:refineConf stanza.
* The filtering process removes comments and cosmetic whitespace.
* Defaults to: true

[replicationSettings:refineConf]

replicate.<conf_file_name> = <bool>
* Controls whether Splunk replicates a particular type of *.conf file, along
  with any associated permissions in *.meta files.
* These settings on their own do not cause files to be replicated. A file must
  still be whitelisted (via replicationWhitelist) to be eligible for inclusion
  via these settings.
* In a sense, these settings constitute another level of filtering that applies
  specifically to *.conf files and stanzas with *.meta files.
* Defaults to: false

#******************************************************************************
# REPLICATION WHITELIST OPTIONS
#******************************************************************************

[replicationWhitelist]

<name> = <whitelist_pattern>
* Controls Splunk's search-time conf replication from search heads to search
  nodes.
* Only files that match a whitelist entry will be replicated.
* Conversely, files which are not matched by any whitelist will not be
  replicated.
* Only files located under $SPLUNK_HOME/etc will ever be replicated in this
  way.
  * The regex will be matched against the filename, relative to $SPLUNK_HOME/etc.
    Example: for a file "$SPLUNK_HOME/etc/apps/fancy_app/default/inputs.conf"
             this whitelist should match "apps/fancy_app/default/inputs.conf"
  * Similarly, the etc/system files are available as system/...
    user-specific files are available as users/username/appname/...
* The 'name' element is generally just descriptive, with one exception:
  if <name> begins with "refine.", files whitelisted by the given pattern will
  also go through another level of filtering configured in the
  replicationSettings:refineConf stanza.
* The whitelist_pattern is the Splunk-style pattern matching, which is
  primarily regex-based with special local behavior for '...' and '*'.
  * ... matches anything, while * matches anything besides directory separators.
    See props.conf.spec for more detail on these.
  * Note '.' will match a literal dot, not any character.
* Note that these lists are applied globally across all conf data, not to any
  particular app, regardless of where they are defined.  Be careful to pull in
  only your intended files.

#******************************************************************************
# REPLICATION BLACKLIST OPTIONS
#******************************************************************************

[replicationBlacklist]

<name> = <blacklist_pattern>
* All comments from the replication whitelist notes above also apply here.
* Replication blacklist takes precedence over the whitelist, meaning that a
  file that matches both the whitelist and the blacklist will NOT be
  replicated.
* This can be used to prevent unwanted bundle replication in two common
  scenarios:
    * Very large files, which part of an app may not want to be replicated,
      especially if they are not needed on search nodes.
    * Frequently updated files (for example, some lookups) will trigger
      retransmission of all search head data.
* Note that these lists are applied globally across all conf data. Especially
  for blacklisting, be careful to constrain your blacklist to match only data
  your application will not need.

#******************************************************************************
# BUNDLE ENFORCER WHITELIST OPTIONS
#******************************************************************************

[bundleEnforcerWhitelist]

<name> = <whitelist_pattern>
* Peers uses this to make sure knowledge bundle sent by search heads and
  masters do not contain alien files.
* If this stanza is empty, the receiver accepts the bundle unless it contains
  files matching the rules specified in [bundleEnforcerBlacklist]. Hence, if
  both [bundleEnforcerWhitelist] and [bundleEnforcerBlacklist] are empty (which
  is the default), then the receiver accepts all bundles.
* If this stanza is not empty, the receiver accepts the bundle only if it
  contains only files that match the rules specified here but not those in
  [bundleEnforcerBlacklist].
* All rules are regexs.
* This stanza is empty by default.

#******************************************************************************
# BUNDLE ENFORCER BLACKLIST OPTIONS
#******************************************************************************

[bundleEnforcerBlacklist]

<name> = <blacklist_pattern>
* Peers uses this to make sure knowledge bundle sent by search heads and
  masters do not contain alien files.
* This list overrides [bundleEnforceWhitelist] above. That means the receiver
  rejects (i.e. removes) the bundle if it contains any file that matches the
  rules specified here even if that file is allowed by [bundleEnforcerWhitelist].
* If this stanza is empty, then only [bundleEnforcerWhitelist] matters.
* This stanza is empty by default.

#******************************************************************************
# SEARCH HEAD BUNDLE MOUNTING OPTIONS
# You set these attributes on the search peers only, and only if you also set
# shareBundles=false in [distributedSearch] on the search head. Use them to
# achieve replication-less bundle access. The search peers use a shared storage
# mountpoint to access the search head bundles ($SPLUNK_HOME/etc).
#******************************************************************************

[searchhead:<searchhead-splunk-server-name>]
* <searchhead-splunk-server-name> is the name of the related searchhead
  installation.
* This setting is located in server.conf, serverName = <name>

mounted_bundles = [true|false]
* Determines whether the bundles belong to the search head specified in the
  stanza name are mounted.
* You must set this to "true" to use mounted bundles.
* Default is "false".

bundles_location = <path_to_bundles>
* The path to where the search head's bundles are mounted. This must be the
  mountpoint on the search peer,  not on the search head. This should point to
  a directory that is equivalent to $SPLUNK_HOME/etc/. It must contain at least
  the following subdirectories: system, apps, users.


#******************************************************************************
# DISTRIBUTED SEARCH GROUP DEFINITIONS
# These are the definitions of the distributed search groups. A search group is
# a set of search peers as identified by thier host:management-port. A search 
# may be directed to a search group using the splunk_server_group argument.The
# search will be dispatched to only the members of the group.
#******************************************************************************

[distributedSearch:<splunk-server-group-name>]
* <splunk-server-group-name> is the name of the splunk-server-group that is
  defined in this stanza

servers = <comma separated list of servers>
* List of search peers that are members of this group. Comma serparated list
  of peer identifiers i.e. hostname:port

default = [true|false]
* Will set this as the default group of peers against which all searches are
  run unless a server-group is not explicitly specified.
