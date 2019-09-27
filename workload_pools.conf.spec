#   Version 7.2.1
#
############################################################################
# OVERVIEW
############################################################################
# This file contains descriptions of the settings that you can use to
# configure workloads for splunk.
#
# There is a workload_pools.conf file in the $SPLUNK_HOME/etc/system/default/ directory.
# Never change or copy the configuration files in the default directory.
# The files in the default directory must remain intact and in their original
# location.
#
# To set custom configurations, create a new file with the name workload_pools.conf in
# the $SPLUNK_HOME/etc/system/local/ directory. Then add the specific settings
# that you want to customize to the local configuration file.
# For examples, see workload_pools.conf.example. You may need to restart the Splunk instance
# to enable configuration changes.
#
# To learn more about configuration files (including file precedence) see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles
#
############################################################################
# GLOBAL SETTINGS
############################################################################
# Use the [default] stanza to define any global settings.
#   * You can also define global settings outside of any stanza, at the top of
#     the file.
#   * Each .conf file should have at most one default stanza. If there are
#     multiple default stanzas, settings are combined. In the case of
#     multiple definitions of the same setting, the last definition in the
#     file takes precedence.
#   * If a setting is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.
#
# CAUTION: Do not alter the settings in the workload_pools.conf file unless you know
#     what you are doing.  Improperly configured worloads might result in
#     splunkd crashes, memory overuse, or both.

[general]
enabled = <bool>
* Specifies whether workload management has been enabled on the system or not.
* This setting only applies to the default stanza as a global setting.
* Default: false

default_pool = <string>
* Specifies the default workload pool to be used at runtime for search workloads.
* Admin users could specify workload pools associated with roles. If no workload
  pool can be found, then we fall back to this default_pool that is defined in
  the general stanza in workload.conf.
* This setting is only applicable when workload management has been enabled in
  the system. If workload management has been enabled, this is a mandatory setting.

ingest_pool = <string>
* Specifies the workload pool for the splunkd process that controls ingestion
  and other actions in the Splunk deployment.
* Use this setting to guarantee a minimum lower-bound for resources for tasks
  controlled and managed by splunkd.
* This setting is only applicable when workload management has been enabled in
  the system. If workload management has been enabled, this is a mandatory setting.

workload_pool_base_dir_name = <string>
* Specifies the base controller directory name for Splunk cgroups on Linux to be used by a Splunk deployment.
* Workload pools created from the workload management page are all created relative
  to this base directory.
* This setting is only applicable when workload management has been enabled in
  the system. If workload management has been enabled, this is a mandatory setting.
* Default: splunk

[workload_pool:<pool_name>]
cpu_weight = <number>
* Specifies the cpu weight to be used by this workload pool.
* This is effectively a relative ratio or fraction of the total weights assigned
  across all the workload pools.
* Note that this is not a percentage and instead a relative weight as a fraction
  of the total weight calculated by summing all workload pool weights.
* This is a mandatory parameter for the creation of a workload pool and only
  allows positive integral values.
* Default is unset

mem_weight = <number>
* Specifies the memory weight to be used by this workload pool.
* This is effectively a ratio or fraction of the total weights assigned
  across all the workload pools.
* Note that this is not a percentage and instead a relative weight as a fraction
  of the total weight calculated by summing all workload pool weights.
* This is a mandatory parameter for the creation of a workload pool and only
  allows positive integral values.
* Default is unset
