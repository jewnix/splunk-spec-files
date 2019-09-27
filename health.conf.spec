#   Version 7.1.8
#
# This file sets the default thresholds for Splunk Enterprise's built
# in Health Report.
#
# Feature stanzas contain indicators, and each indicator has two thresholds:
# * Yellow: Indicates something is wrong and should be investigated.
# * Red: Means that the indicator is effectively not working.
#
# There is a health.conf in the $SPLUNK_HOME/etc/system/default/ directory.
# Never change or copy the configuration files in the default directory.
# The files in the default directory must remain intact and in their original
# location.
#
# To set custom configurations, create a new file with the name health.conf in
# the $SPLUNK_HOME/etc/system/local/ directory. Then add the specific settings
# that you want to customize to the local configuration file.
#
# To learn more about configuration files (including precedence), see the
# documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

[health_reporter]
full_health_log_interval = <number>
* The amount of time, in seconds, that elapses between each ‘PeriodicHealthReporter=INFO’ log entry.
* Default: 30.

suppress_status_update_ms = <number>
* The minimum amount of time, in milliseconds, that must elapse between an indicator's health status changes.
* Changes that occur earlier will be suppressed.
* Default: 300.

[clustering]
health_report_period = <number>
* The amount of time, in seconds, that elapses between each Clustering health report run.
* Default: 20.
disabled = [0|1]
* A value of 1 disables the clustering feature health check.
* Default: 0 (enabled)

[feature:*]
suppress_status_update_ms = <number>
* The minimum amount of time, in milliseconds, that must elapse between an indicator's health status changes.
* Changes that occur earlier will be suppressed.
* Default: 300.

indicator:<indicator name>:<indicator color> = <number>
* There are various indicator names. See your health.conf for the complete list.
* There are two valid colors: yellow and red.
* These settings should not be adjusted lightly. If the numbers are set too
  high, you might inadvertently mask serious errors that the Health Report is
  trying to bring to your attention.
