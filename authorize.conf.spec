#   Version 7.1.8
#
# This file contains possible attribute/value pairs for creating roles in
# authorize.conf.  You can configure roles and granular access controls by
# creating your own authorize.conf.

# There is an authorize.conf in $SPLUNK_HOME/etc/system/default/.  To set
# custom configurations, place an authorize.conf in
# $SPLUNK_HOME/etc/system/local/. For examples, see authorize.conf.example.
# You must restart Splunk to enable configurations.
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top
#     of the file.
#   * Each conf file should have at most one default stanza. If there are
#     multiple default stanzas, attributes are combined. In the case of
#     multiple definitions of the same attribute, the last definition in
#     the file wins.
#   * If an attribute is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.

[default]
srchFilterSelecting = <boolean>
* Determines whether a role's search filters will be used for selecting or
  eliminating during role inheritance.
* Selecting will join the search filters with an OR when combining the
  filters.
* Eliminating will join the search filters with an AND when combining the
  filters.
    * All roles will default to true (in other words, selecting).
* Example:
  * role1 srchFilter = sourcetype!=ex1 with selecting=true
  * role2 srchFilter = sourcetype=ex2 with selecting = false
  * role3 srchFilter = sourcetype!=ex3 AND index=main with selecting = true
  * role3 inherits from role2 and role 2 inherits from role1
  * Resulting srchFilter = ((sourcetype!=ex1) OR 
    (sourcetype!=ex3 AND index=main)) AND ((sourcetype=ex2))

[capability::<capability>]
* DO NOT edit, remove, or add capability stanzas. The existing capabilities
  are the full set of Splunk system capabilities.
* Splunk adds all of its capabilities this way
* For the default list of capabilities and assignments, see authorize.conf
  under the 'default' directory
* Only alphanumeric characters and "_" (underscore) are allowed in 
  capability names.
  Examples: 
  * edit_visualizations 
  * view_license1
* Descriptions of specific capabilities are listed below.

[role_<roleName>]
<capability> = <enabled>
* A capability that is enabled for this role.
* You can list many of these.
* Note that 'enabled' is the only accepted value here, as capabilities are
  disabled by default.
* Roles inherit all capabilities from imported roles, and inherited
  capabilities cannot be disabled.
* Role names cannot have uppercase characters. User names, however, are
  case-insensitive.

importRoles = <string>
* Semicolon delimited list of other roles and their associated capabilities
  that should be imported.
* Importing other roles also imports the other aspects of that role, such as
  allowed indexes to search.
* By default a role imports no other roles.

grantableRoles = <string>
* Semicolon delimited list of roles that can be granted when edit_user
  capability is present.
* By default, a role with edit_user capability can create/edit a user and
  assign any role to them. But when grantableRoles is present, the roles
  that can be assigned will be restricted to the ones provided.
* For a role that has no edit_user capability, grantableRoles has no effect.
* Defaults to not present.
* Example: grantableRoles = role1;role2;role3

srchFilter = <string>
* Semicolon delimited list of search filters for this Role.
* By default we perform no search filtering.
* To override any search filters from imported roles, set this to '*', as
  the 'admin' role does.

srchTimeWin = <number>
* Maximum time span of a search, in seconds.
    * This time window limit is applied backwards from the latest time
      specified in a search.
* By default, searches are not limited to any specific time window.
* To override any search time windows from imported roles, set this to '0'
  (infinite), as the 'admin' role does.
* -1 is a special value that implies no search window has been set for 
  this role
    * This is equivalent to not setting srchTimeWin at all, which means it
      can be easily overridden by an imported role

srchDiskQuota = <number>
* Maximum amount of disk space (MB) that can be used by search jobs of a
  user that belongs to this role
* In search head clustering environments, this setting takes effect on a 
  per-member basis. There is no cluster-wide accounting.
* The dispatch manager checks the quota at the dispatch time of a search
  and additionally the search process will check at intervals that are defined
  in the 'disk_usage_update_period' setting in limits.conf as long as the
  search is active.
* The quota can be exceeded at times, since the search process does not check
  the quota constantly.
* Exceeding this quota causes the search to be auto-finalized immediately,
  even if there are results that have not yet been returned.
* Defaults to '100', for 100 MB.

srchJobsQuota = <number>
* Maximum number of concurrently running historical searches a member of
  this role can have.
* This excludes real-time searches, see rtSrchJobsQuota.
* Defaults to 3.

rtSrchJobsQuota = <number>
* Maximum number of concurrently running real-time searches a member of this
  role can have.
* Defaults to 6.

srchMaxTime = <number><unit>
* Maximum amount of time that searches of users from this role will be
  allowed to run.
* Once the search has been ran for this amount of time it will be auto
  finalized, If the role
* Inherits from other roles, the maximum srchMaxTime value specified in the
  included roles.
* This maximum does not apply to real-time searches.
* Examples: 1h, 10m, 2hours, 2h, 2hrs, 100s
* Defaults to 100days

srchIndexesDefault = <string>
* A semicolon-delimited list of indexes to search when no index is specified.
* These indexes can be wild-carded ("*"), with the exception that '*' does not
  match internal indexes.
* To match internal indexes, start with '_'. All internal indexes are
  represented by '_*'.
* The wildcard character '*' is limited to match either all the non-internal 
  indexes or all the internal indexes, but not both at once.
* If you make any changes in the "Indexes searched by default" Settings panel
  for a role in Splunk Web, those values take precedence, and any wildcards
  you specify in this setting are lost.
* Defaults to none.

srchIndexesAllowed = <string>
* Semicolon delimited list of indexes this role is allowed to search
* Follows the same wildcarding semantics as srchIndexesDefault
* If you make any changes in the "Indexes" Settings panel
  for a role in Splunk Web, those values take precedence, and any wildcards
  you specify in this setting are lost.
* Defaults to none.

deleteIndexesAllowed = <string>
* Semicolon delimited list of indexes this role is allowed to delete
* This setting must be used in conjunction with the delete_by_keyword
  capability
* Follows the same wildcarding semantics as srchIndexesDefault
* Defaults to none

cumulativeSrchJobsQuota = <number>
* Maximum number of concurrently running historical searches in total
  across all members of this role
* Requires enable_cumulative_quota = true in limits.conf to take effect.
* If a user belongs to multiple roles, the user's searches count against 
  the role with the largest cumulative search quota. Once the quota for 
  that role is consumed, the user's searches count against the role with 
  the next largest quota, and so on.
* In search head clustering environments, this setting takes effect on a 
  per-member basis. There is no cluster-wide accounting.

cumulativeRTSrchJobsQuota = <number>
* Maximum number of concurrently running real-time searches in total
  across all members of this role
* Requires enable_cumulative_quota = true in limits.conf to take effect.
* If a user belongs to multiple roles, the user's searches count against 
  the role with the largest cumulative search quota. Once the quota for 
  that role is consumed, the user's searches count against the role with 
  the next largest quota, and so on.
* In search head clustering environments, this setting takes effect 
  on a per-member basis. There is no cluster-wide accounting.

### Descriptions of Splunk system capabilities. Capabilities are added to roles, 
 to which users are then assigned. When a user is assigned a role, they acquire 
 the capabilities added to that role.

[capability::accelerate_datamodel]
* Lets a user enable or disable datamodel acceleration.

[capability::accelerate_search]
* Lets a user enable or disable acceleration for reports. 
* The assigned role must also be granted the schedule_search capability.

[capability::run_multi_phased_searches]
* Lets a user in a distributed search environment run searches with 
  three or more map-reduce phases
* Allows users to take advantage of the search performance gains 
  related to parallel reduce functionality. 
* Multiphased searches can lead to higher resource utilization on 
  indexers, but they can also reduce resource utilization on search heads. 

[capability::admin_all_objects]
* Lets a user access all objects in the system, such as user
  objects and knowledge objects.
* Lets a user bypasses any ACL restrictions, much the way root access in 
  a *nix environment does.
* Splunk checks this capability when accessing manager pages and objects.

[capability::change_authentication]
* Lets a user change authentication settings through the
  authentication endpoints. 
* Lets the user reload authentication.

[capability::change_own_password]
* Lets a user change their own password. You can remove this capability 
  to control the password for a user.

[capability::delete_by_keyword]
* Lets a user use the "delete" search operator. Note that this does not
  actually delete the raw data on disk, instead it masks the data 
  (via the index) from showing up in search results.

[capability::dispatch_rest_to_indexers]
* Lets a user dispatch the REST search command to indexers.

[capability::edit_deployment_client]
* Lets a user edit the deployment client. 
* Lets a user edit a deployment client admin endpoint.

[capability::edit_deployment_server]
* Lets a user edit the deployment server. 
* Lets a user edit a deployment server admin endpoint.
* Lets a user change or create remote inputs that are pushed to the 
  forwarders and other deployment clients.

[capability::edit_dist_peer]
* Lets a user add and edit peers for distributed search.

[capability::edit_encryption_key_provider]
* Lets a user view and edit keyprovider properties when using
  the Server-Side Encryption (SSE) feature for a remote storage volume.

[capability::edit_forwarders]
* Lets a user edit settings for forwarding data, including settings 
  for SSL, backoff schemes, etc.
* Also used by TCP and Syslog output admin handlers.

[capability::edit_health]
* Lets a user disable or enable health reporting for a feature in the splunkd 
  health status tree through the server/health-config/{feature_name} endpoint.

[capability::edit_httpauths]
* Lets a user edit and end user sessions through the httpauth-tokens endpoint.

[capability::edit_indexer_cluster]
* Lets a user edit or manage indexer clusters.

[capability::edit_indexerdiscovery]
* Lets a user edit settings for indexer discovery, including settings 
  for master_uri, pass4SymmKey, etc.
* Also used by Indexer Discovery admin handlers.
 
[capability::edit_input_defaults]
* Lets a user change the default hostname for input data through the server
  settings endpoint.

[capability::edit_monitor]
* Lets a user add inputs and edit settings for monitoring files.
* Also used by the standard inputs endpoint as well as the one-shot input
  endpoint.

[capability::edit_modinput_winhostmon]
* Lets a user add and edit inputs for monitoring Windows host data.

[capability::edit_modinput_winnetmon]
* Lets a user add and edit inputs for monitoring Windows network data.

[capability::edit_modinput_winprintmon]
* Lets a user add and edit inputs for monitoring Windows printer data.

[capability::edit_modinput_perfmon]
* Lets a user add and edit inputs for monitoring Windows performance.

[capability::edit_modinput_admon]
* Lets a user add and edit inputs for monitoring Splunk's Active Directory.

[capability::edit_roles]
* Lets a user edit roles.
* Lets a user change the mappings from users to roles.
* Used by both the user and role endpoint.

[capability::edit_roles_grantable]
* Lets the user edit roles and change user-to-role mapings for a limited 
  set of roles. 
* To limit this ability, also assign the edit_roles_grantable capability
and configure grantableRoles in authorize.conf. For example:
grantableRoles = role1;role2;role3. This lets user create roles using the
subset of capabilities that the user has in their grantable_roles
configuration. 

[capability::edit_scripted]
* Lets a user create and edit scripted inputs.

[capability::edit_search_head_clustering]
* Lets a user edit and manage search head clustering.
  
[capability::edit_search_scheduler]
* Lets the user disable and enable the search scheduler.

[capability::edit_search_schedule_priority]
* Lets a user assign a search a higher-than-normal schedule priority.

[capability::edit_search_schedule_window]
* Lets a user edit a search schedule window.

[capability::edit_search_server]
* Lets a user edit general distributed search settings like timeouts,
  heartbeats, and blacklists.

[capability::edit_server]
* Lets the user edit general server and introspection settings, such 
  as the server name, log levels, etc.
* This capability also inherits the ability to read general server 
  and introspection settings.

[capability::edit_server_crl]
* Lets a user reload Certificate Revocation List within Splunk.

[capability::edit_sourcetypes]
* Lets a user create and edit sourcetypes.

[capability::edit_splunktcp]
* Lets a user change settings for receiving TCP input from another Splunk
  instance.

[capability::edit_splunktcp_ssl]
* Lets a user view and edit SSL-specific settings for Splunk TCP input.

[capability::edit_splunktcp_token]
* Lets a user view or edit splunktcptokens. The tokens can be used on a 
  receiving system to only accept data from forwarders that have been 
  configured with the same token.

[capability::edit_tcp]
* Lets a user change settings for receiving general TCP inputs.

[capability::edit_telemetry_settings]
* Lets a user change settings to opt-in and send telemetry data.

[capability::edit_token_http]
* Lets a user create, edit, display, and remove settings for HTTP token input.
* Enables the HTTP Events Collector feature.

[capability::edit_udp]
* Lets a user change settings for UDP inputs.

[capability::edit_user]
* Lets a user create, edit, or remove other users. To limit this ability, 
  assign the edit_roles_grantable capability and configure grantableRoles 
  in authorize.conf. For example: grantableRoles = role1;role2;role3.
* Also lets a user manage certificates for distributed search.
 
[capability::edit_view_html]
* Lets a user create, edit, or otherwise modify HTML-based views.

[capability::edit_web_settings]
* Lets a user change the settings for web.conf through the system settings
  endpoint.

[capability::export_results_is_visible]
* Lets a user show or hide the Export button in Splunk Web.
* Disable this setting to hide the Export button and prevent users with 
  this role from exporting search results.

[capability::get_diag]
* Lets the user get remote diag from an
  instance through the /streams/diag endpoint.

[capability::get_metadata]
* Lets a user use the "metadata" search processor.

[capability::get_typeahead]
* Enables typeahead for a user, both the typeahead endpoint and the
  'typeahead' search processor.

[capability::indexes_edit]
* Lets a user change any index settings such as file size and memory limits.

[capability::input_file]
* Lets a user add a file as an input through inputcsv (except for 
  dispatch=t mode) and inputlookup.

[capability::license_tab]
* (Deprecated) Lets a user access and change the license.

[capability::license_edit]
* Lets a user access and change the license.

[capability::license_view_warnings]
* Lets a user see if they are exceeding limits or reaching the expiration 
  date of their license. 
* License warnings are displayed on the system banner.

[capability::list_accelerate_search]
* This capability is a subset of the 'accelerate_search' capability.
* This capability grants access to the summaries that are required to run accelerated reports.
* Users with this capability, but without the 'accelerate_search' capability, can run,
  but not create, accelerated reports.

[capability::list_deployment_client]
* Lets a user list the deployment clients.

[capability::list_deployment_server]
* Lets a user list the deployment servers.
  
[capability::list_forwarders]
* Lets a user list settings for data forwarding.
* Used by TCP and Syslog output admin handlers.

[capability::list_health]
* Lets a user monitor the health of various Splunk features
  (such as inputs, outputs, clustering, etc) through REST endpoints.

[capability::list_httpauths]
* Lets a user list user sessions through the httpauth-tokens endpoint.

[capability::list_indexer_cluster]
* Lets a user list indexer cluster objects such as buckets, peers, etc.

[capability::list_indexerdiscovery]
* Lets a user view settings for indexer discovery.
* Used by Indexer Discovery handlers.
 
[capability::list_inputs]
* Lets a user view the list of inputs, including files, TCP, UDP, Scripts, etc.

[capability::list_introspection]
* Lets a user read introspection settings and statistics for indexers, search,
  processors, queues, etc.

[capability::list_search_head_clustering]
* Lets a user list search head clustering objects such as artifacts, delegated
  jobs, members, captain, etc.

[capability::list_search_scheduler]
* Lets a user list search scheduler settings.

[capability::list_settings]
* Lets a user list general server and introspection settings such as the server
  name, log levels, etc.

[capability::list_metrics_catalog]
* Lets a user list metrics catalog information such as the metric names,
  dimensions, and dimension values.

[capability::list_storage_passwords]
* Lets a user access the /storage/passwords endpoint. 
* Lets the user perform GETs. 
* The admin_all_objects capability must added to the role in order for the user to
  perform POSTs to the /storage/passwords endpoint.
  
[capability::never_lockout]
* Lets a user account never lockout.

[capability::never_expire]
* Lets a user account never expire.

[capability::output_file]
* Lets a user create file outputs, including outputcsv (except for 
  dispatch=t mode) and outputlookup.

[capability::request_remote_tok]
* Lets a user get a remote authentication token.
* Used for distributing search to old 4.0.x Splunk instances.
* Also used for some distributed peer management and bundle replication.

[capability::rest_apps_management]
* Lets a user edit settings for entries and categories in the python remote
  apps handler.
* See restmap.conf for more information.

[capability::rest_apps_view]
* Lets a user list various properties in the python remote apps handler.
* See restmap.conf for more info

[capability::rest_properties_get]
* Lets a user get information from the services/properties endpoint.

[capability::rest_properties_set]
* Lets a user edit the services/properties endpoint.

[capability::restart_splunkd]
* Lets a user restart Splunk through the server control handler.

[capability::rtsearch]
* Lets a user run realtime searches.

[capability::run_collect]
* Lets a user run the collect command.

[capability::run_mcollect]
* Lets a user run the mcollect and meventcollect commands.

[capability::run_debug_commands]
* Lets a user run debugging commands, for example "summarize".

[capability::schedule_rtsearch]
* Lets a user schedule real time saved searches. The scheduled_search
scheduled_search and rtsearch capabilities must be enabled for the role.

[capability::schedule_search]
* Lets a user schedule saved searches, create and update alerts, and 
  review triggered alert information.

[capability::search]
* Lets a user run a search.

[capability::search_process_config_refresh]
* Lets a user manually flush idle search processes through the 
  "refresh search-process-config"CLI command.

[capability::use_file_operator]
* Lets a user use the "file" search operator. The "file" search operator is DEPRECATED.

[capability::web_debug]
* Lets a user access /_bump and /debug/** web debug endpoints.
