#   Version 7.2.0
#
# This file contains possible attributes and values for defining server
# classes to which deployment clients can belong. These attributes and
# values specify what content a given server class member will receive from
# the deployment server.
#
# For examples, see serverclass.conf.example. You must reload deployment
# server ("splunk reload deploy-server"), or restart splunkd, for changes to
# this file to take effect.
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles



#***************************************************************************
# Configure the server classes that are used by a deployment server instance.
#
# Server classes are essentially categories.  They use filters to control
# what clients they apply to, contain a set of applications, and may define
# deployment server behavior for the management of those applications.  The
# filters can be based on DNS name, IP address, build number of client
# machines, platform, and the so-called clientName.  If a target machine
# matches the filter, then the apps and configuration content that make up
# the server class will be deployed to it.

# Property Inheritance
#
# Stanzas in serverclass.conf go from general to more specific, in the
# following order:
# [global] -> [serverClass:<name>] -> [serverClass:<scname>:app:<appname>]
#
# Some properties defined at a general level (say [global]) can be
# overridden by a more specific stanza as it applies to them. All
# overridable properties are marked as such.



###########################################
########### FIRST LEVEL: global ###########
###########################################

# Global stanza that defines properties for all server classes.
[global]

disabled = true|false
* Toggles deployment server component off and on.
* Set to true to disable.
* Defaults to false.

crossServerChecksum = true|false
* Ensures that each app will have the same checksum across different deployment
  servers.
* Useful if you have multiple deployment servers behind a load-balancer.
* Defaults to false.

excludeFromUpdate = <path>[,<path>]...
* Specifies paths to one or more top-level files or directories (and their
  contents) to exclude from being touched during app update.  Note that
  each comma-separated entry MUST be prefixed by "$app_root$/" (otherwise a
  warning will be generated).
* Can be overridden at the serverClass level.
* Can be overridden at the app level.
* Requires version 6.2.x or higher for both the Deployment Server and Client.

repositoryLocation = <path>
* The repository of applications on the server machine.
* Can be overridden at the serverClass level.
* Defaults to $SPLUNK_HOME/etc/deployment-apps

targetRepositoryLocation = <path>
* The location on the deployment client where to install the apps defined
  for this Deployment Server.
* If this value is unset, or set to empty, the repositoryLocation path is used.
* Useful only with complex (for example, tiered) deployment strategies.
* Defaults to $SPLUNK_HOME/etc/apps, the live
  configuration directory for a Splunk instance.

tmpFolder = <path>
* Working folder used by deployment server.
* Defaults to $SPLUNK_HOME/var/run/tmp

continueMatching = true | false
* Controls how configuration is layered across classes and server-specific
  settings.
* If true, configuration lookups continue matching server classes, beyond
  the first match.
* If false, only the first match will be used.
* A serverClass can override this property and stop the matching.
* Matching is done in the order in which server classes are defined.
* Can be overridden at the serverClass level.
* Defaults to true

endpoint = <URL template string>
* The endpoint from which content can be downloaded by a deployment client.
  The deployment client knows how to substitute values for variables in the
  URL.
* Any custom URL can also be supplied here, as long as it uses the specified
  variables.
* Need not be specified unless you have a very specific need, for example:
  To acquire deployment application files from a third-party Web server, for
  extremely large environments.
* Can be overridden at the serverClass level.
* Defaults to $deploymentServerUri$/services/streams/deployment?name=$serverClassName$:$appName$

filterType = whitelist | blacklist
* The whitelist setting indicates a filtering strategy that pulls in a
  subset:
    * Items are not considered to match the stanza by default.
    * Items that match any whitelist entry, and do not match any blacklist
      entry are considered to match the stanza.
    * Items that match any blacklist entry are not considered to match the
      stanza, regardless of whitelist.
* The blacklist setting indicates a filtering strategy that rules out a subset:
    * Items are considered to match the stanza by default.
    * Items that match any blacklist entry, and do not match any whitelist
      entry are considered to not match the stanza.
    * Items that match any whitelist entry are considered to match the
      stanza.
* More briefly:
    * whitelist: default no-match -> whitelists enable -> blacklists disable
    * blacklist: default match -> blacklists disable-> whitelists enable
* Can be overridden at the serverClass level, and the serverClass:app level.
* Defaults to whitelist

whitelist.<n> = <clientName> | <IP address> | <hostname> | <instanceId>
blacklist.<n> = <clientName> | <IP address> | <hostname> | <instanceId>
* 'n' is an unsigned integer. The sequence may start at any value and may be
  non-consecutive.
* The value of this attribute is matched against several things in order:
    * Any clientName specified by the client in its deploymentclient.conf file
    * The IP address of the connected client
    * The hostname of the connected client, as provided by reverse DNS lookup
    * The hostname of the client, as provided by the client
    * For Splunk version > 6.4, the instanceId of the client. This is a GUID
      string, e.g. 'ffe9fe01-a4fb-425e-9f63-56cc274d7f8b'.
* All of these can be used with wildcards.  * will match any sequence of
  characters.  For example:
    * Match a network range: 10.1.1.*
    * Match a domain: *.splunk.com
* Can be overridden at the serverClass level, and the serverClass:app level.
* There are no whitelist or blacklist entries by default.
* These patterns are PCRE regular expressions, with the following aids for
  easier entry:
    * You can specify simply '.' to mean '\.'
    * You can specify simply '*' to mean '.*'
* Matches are always case-insensitive; you do not need to specify the '(?i)' prefix.

# Note: Overriding one type of filter (whitelist/blacklist) causes the other to
# be overridden (and hence not inherited from parent) too.

# Example with filterType=whitelist:
#     whitelist.0=*.splunk.com
#     blacklist.0=printer.splunk.com
#     blacklist.1=scanner.splunk.com
# This will cause all hosts in splunk.com, except 'printer' and 'scanner', to
# match this server class.

# Example with filterType=blacklist:
#     blacklist.0=*
#     whitelist.0=*.web.splunk.com
#     whitelist.1=*.linux.splunk.com
# This will cause only the 'web' and 'linux' hosts to match the server class.
# No other hosts will match.

# Deployment client machine types (hardware type of respective host machines)
# can also be used to match DCs.
# This filter will be used only if match of a client could not be decided using
# the whitelist/blacklist filters.  The value of each machine type is
# designated by the hardware platform itself; a few common ones are:
#       linux-x86_64, windows-intel, linux-i686, freebsd-i386, darwin-i386, sunos-sun4u.
# The method for finding it varies by platform; once a deployment client is
# connected to the DS, however, you can determine the value of DC's machine
# type with this Splunk CLI command on the DS:
#       <code>./splunk list deploy-clients</code>
# The <code>utsname</code> values in the output are the respective DCs' machine
# types.

whitelist.from_pathname = <pathname>
blacklist.from_pathname = <pathname>
* As as alternative to a series of (whitelist|blacklist).<n>, the <clientName>,
  <IP address>, and <hostname> list can be imported from <pathname> that is
  either a plain text file or a comman-separated values (CSV) file.
* May be used in conjunction with (whitelist|blacklist).select_field,
  (whitelist|blacklist).where_field, and (whitelist|blacklist).where_equals.
* If used by itself, then <pathname> specifies a plain text file where one
  <clientName>, <IP address>, or <hostname> is given per line.
* If used on conjuction with select_field, where_field, and where_equals, then
  <pathname> specifies a CSV file.
* The <pathname> is relative to $SPLUNK_HOME.
* May also be used in conjunction with (whitelist|blacklist).<n> to specify
  additional values, but there is no direct relation between them.
* At most one from_pathname may be given per stanza.

whitelist.select_field = <field name> | <positive integer>
blacklist.select_field = <field name> | <positive integer>
* Specifies which field of the CSV file contains the <clientName>, <IP address>,
  or <hostname> either by field name or number.
* If <field name> is given, then the first line of the CSV file MUST be a
  header line containing the name(s) of all the field(s) and <field name>
  specifies which field contains the value(s) to be used.  Note that field
  names are case-sensitive.
* If <positive integer> is given, then it specifies the column number (starting
  at 1) of the field that contains the value(s) to be used. In this case, the
  first line of the CSV file MUST NOT be a header line.
* MUST be used in conjuction with (whitelist|blacklist).from_pathname.
* May be used in conjuction with (whitelist|blacklist).where_field and
  (whitelist|blacklist).where_equals.
* At most one select_field may be given per stanza.

whitelist.where_field = <field name> | <positive integer>
blacklist.where_field = <field name> | <positive integer>
* Specifies that only a subset of values are to be selected from
  (whitelist|blacklist).select_field.
* Specifies which field of the CSV file contains values to be compared against
  for equality with the (whitelist|blacklist).where_equals values.
* Like (whitelist|blacklist).select_field, the field may be specified by either
  name or number.  However, select_field and where_field MUST be specified the
  same way, i.e., either BOTH by name or BOTH by number.
* MUST be used in conjuction with (whitelist|blacklist).select_field and
  (whitelist|blacklist).where_equals.
* At most one where_field may be given per stanza.

whitelist.where_equals = <comma-separated list>
blacklist.where_equals = <comma-separated list>
* Specifies the value(s) that the value of (whitelist|blacklist).where_field
  must equal in order to be selected via (whitelist|blacklist).select_field.
* If more than one value is specified (separated by commas), then the value
  of (whitelist|blacklist).where_field may equal ANY ONE of the values.
* Each value is a PCRE regular expression with the following aids for easier
  entry:
    * You can specify simply '.' to mean '\.'
    * You can specify simply '*' to mean '.*'
* Matches are always case-insensitive; you do not need to specify the '(?i)'
  prefix.
* MUST be used in conjuction with (whitelist|blacklist).select_field and
  (whitelist|blacklist).where_field.
* At most one where_equals may be given per stanza.

machineTypesFilter = <comma-separated list>
* Not used unless specified.
* Boolean OR logic is employed: a match against any element in the list
  constitutes a match.
* This filter is used in boolean AND logic with white/blacklist filters.
  Only clients which match the white/blacklist AND which match this
  machineTypesFilter will be included.
  * In other words, the match is an intersection of the matches for the
    white/blacklist and the matches for MachineTypesFilter.
* This filter can be overridden at the serverClass and serverClass:app
  levels.
* These patterns are PCRE regular expressions, with the following aids for
  easier entry:
    * You can specify simply '.' to mean '\.'
    * You can specify simply '*' to mean '.*'
* Matches are always case-insensitive; you do not need to specify the '(?i)'
  prefix.
* Unset by default.

restartSplunkWeb = true | false
* If true, restarts SplunkWeb on the client when a member app or a directly
  configured app is updated.
* Can be overridden at the serverClass level and the serverClass:app level.
* Defaults to false

restartSplunkd = true | false
* If true, restarts splunkd on the client when a member app or a directly
  configured app is updated.
* Can be overridden at the serverClass level and the serverClass:app level.
* Defaults to false

issueReload = true | false
* If true, triggers a reload of internal processors at the client when a
  member app or a directly configured app is updated 
* If you don't want to immediately start using an app that is pushed to a
  client, you should set this to false.
* defaults to false

restartIfNeeded = true | false
* This is only valid on forwarders that are newer than 6.4.
* If true and issueReload is also true, then when an updated app is delpoyed
  to the client, that client will try to reload that app. If it fails, it will
  then restart.
* defaults to false

stateOnClient = enabled | disabled | noop
* If set to "enabled", sets the application state to enabled on the client,
  regardless of state on the deployment server.
* If set to "disabled", set the application state to disabled on the client,
  regardless of state on the deployment server.
* If set to "noop", the state on the client will be the same as on the
  deployment server.
* Can be overridden at the serverClass level and the serverClass:app level.
* Defaults to enabled.

precompressBundles = true | flase
* Controls whether the Deployment Server will generate both .bundle and
  .bundle.gz files. The pre-compressed files offer improved performance as
  the DS is not required to compress the bundles on the fly for each  client
  that it has to send the bundle to. However, this setting is only
  beneficial if there is no SSL compression in use and the client has
  support for HTTP compression.

* Deployment Server / server.conf
*   allowSslCompression = false
*   useHTTPServerCompression = true
*
* Deployment Client / server.conf 
*   useHTTPClientCompression = true
*
* This option is inherited and available upto the serverclass level (not
  app). Apps belonging to server classes that required precompression will
  be compressed, even if they belong to a server class which does not
  require precompression
* Defaults to true


#################################################
########### SECOND LEVEL: serverClass ###########
#################################################

[serverClass:<serverClassName>]
* This stanza defines a server class. A server class is a collection of
  applications; an application may belong to multiple server classes.
* serverClassName is a unique name that is assigned to this server class.
* A server class can override all inheritable properties in the [global] stanza.
* A server class name may only contain: letters, numbers, space, underscore,
  dash, dot, tilde, and the '@' symbol.  It is case-sensitive.

# NOTE:
# The keys listed below are all described in detail in the
# [global] section above. They can be used with serverClass stanza to
# override the global setting
continueMatching = true | false
endpoint = <URL template string>
excludeFromUpdate = <path>[,<path>]...
filterType = whitelist | blacklist
whitelist.<n> = <clientName> | <IP address> | <hostname>
blacklist.<n> = <clientName> | <IP address> | <hostname>
machineTypesFilter = <comma-separated list>
restartSplunkWeb = true | false
restartSplunkd = true | false
issueReload = true | false
restartIfNeeded = true | false
stateOnClient = enabled | disabled | noop
repositoryLocation = <path>


########################################
########### THIRD LEVEL: app ###########
########################################

[serverClass:<server class name>:app:<app name>]
* This stanza maps an application (which must already exist in
  repositoryLocation) to the specified server class.
* server class name - the server class to which this content should be
  added.
* app name can be '*' or the name of an app:
    * The value '*' refers to all content in the repositoryLocation, adding
      it to this serverClass. '*' stanza cannot be mixed with named stanzas,
      for a given server class.
    * The name of an app explicitly adds the app to a server class.
      Typically apps are named by the folders that contain them.
    * An application name, if it is not the special '*' sign explained
      directly above, may only contain: letters, numbers, space, underscore,
      dash, dot, tilde, and the '@' symbol.  It is case-sensitive.

appFile=<file name>
* In cases where the app name is different from the file or directory name,
  you can use this parameter to specify the file name. Supported formats
  are: directories, .tar files, and .tgz files.

# May override higher-level settings.
issueReload = true | false
restartIfNeeded = true | false
excludeFromUpdate = <path>[,<path>]...
