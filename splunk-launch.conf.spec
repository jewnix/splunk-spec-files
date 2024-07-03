#   Version 9.2.1

# splunk-launch.conf contains values used at startup time, by the Splunk
# command and by Windows services.
#

# Note: this conf file is different from most splunk conf files.  There is
# only one in the whole system, located at
# $SPLUNK_HOME/etc/splunk-launch.conf; further, there are no stanzas,
# explicit or implicit.  Finally, any splunk-launch.conf files in
# etc/apps/... or etc/users/... will be ignored.


# Lines beginning with a # are comments and are ignored.

#*******
# Environment variables
#
# Primarily, this file simply sets environment variables to be used by
# Splunk programs.
#
# These environment variables are the same type of system environment
# variables that can be set, on unix, using:
#   bourne shells:
#       $ export ENV_VAR=value
#   c-shells:
#       % setenv ENV_VAR value
#
# or at a windows command prompt:
#   C:\> SET ENV_VAR=value
#*******

<environment_variable>=<value>

* Any desired environment variable can be set to any value.
  Whitespace is trimmed from around both the key and value.
  Variable substitution (VAR=$OTHER_VAL) is not supported.
* Environment variables set here will be available to all Splunk 
  platform processes, barring operating system limitations.


#*******
# Specific Splunk environment settings
#
# These settings are primarily treated as environment variables, though some
# have some additional logic (defaulting).
#
# There is no need to explicitly set any of these values in typical
# environments.
#*******

SPLUNK_HOME = <string>
* The fully qualified path to the Splunk platform instance installation directory.
* The comment in the auto-generated splunk-launch.conf is informational, not
  a live setting, and does not need to be uncommented.
* If not set, the Splunk platform automatically determines the location of SPLUNK_HOME
  based on the location of the splunk CLI executable.
    * Specifically, the parent of the directory containing splunk or splunk.exe
* Must be set if Common Criteria mode is enabled.
* NOTE: Splunk plans to submit Splunk Enterprise for Common Criteria
  evaluation. Splunk does not support using the product in Common
  Criteria mode until it has been certified by the National Information Assurance
  Partnership (NIAP). See the "Securing Splunk Enterprise" manual for information on
  the status of Common Criteria certification.
* Default: not set

SPLUNK_DB = <string>
* The comment in the auto-generated splunk-launch.conf is informational, not
  a live setting, and does not need to be uncommented.
* The fully qualified path to the directory containing the index
  directories for the Splunk platform instance.
* Primarily used by paths expressed in indexes.conf
* The comment in the autogenerated splunk-launch.conf is informational, not
  a live setting, and does not need to be uncommented.
* If unset, the path becomes $SPLUNK_HOME/var/lib/splunk (unix) or
     %SPLUNK_HOME%\var\lib\splunk (windows>)
* Default: not set

SPLUNK_BINDIP = <ip address>
* The network IP address that splunkd and splunkweb should bind to, as
  opposed to binding to the default for the local operating system.
* If not set, the Splunk platform makes no specific request to the operating
  system when binding to ports or opening a listening socket. This means it 
  effectively binds to '*', meaning an unspecified bind. Operating system 
  behavior and configuration controls the exact result in this case.
* NOTE: When using this setting you must update 'mgmtHostPort' in web.conf to
  match. Otherwise, the command line and splunkweb cannot reach splunkd.
* For splunkd, this sets both the management port and the ports that receive
  from forwarders.
* This setting is useful for a host with multiple IP addresses, either to enable
  or restrict access. But using a firewall is typically a superior
  method of restriction.
* Does not override web.conf/[settings]/server.socket_host for SplunkWeb
  if set; the latter is preferred when SplunkWeb behavior is the focus.
* Default: not set

SPLUNK_OS_USER = <string> | <nonnegative integer>
* The OS user whose privileges splunkd adopts when running.
* Example: SPLUNK_OS_USER=fnietzsche. Splunkd starts with a root login.
  Immediately upon starting, splunkd abandons the root user's privileges,
  and acquires fnietzsche's privileges. User fnietzsche owns any files 
  that splunkd creates (index data, logs, etc.) When fnietzsche starts splunkd
  the next time, the files are readable.
* When 'splunk enable boot-start -user <user>' is invoked, SPLUNK_OS_USER
  is set to <user> as a side effect.
* On UNIX, username or apposite numeric UID are both acceptable;
  on Windows, only usernames are acceptable.
* Default: not set

SPLUNK_FIPS = [0|1]
* Whether or not the Splunk platform instance operates in Federal Information
  Processing Standards (FIPS) mode, and uses the algorithms and restrictions
  that apply to the FIPS Publication 140-2 standard.
* If the machine on which the Splunk platform instance operates runs a kernel
  that operates in FIPS mode, this setting is "true" by default.
* Configure this setting to ensure that your Splunk platform instance operates
  fully within US federal guidelines set by the FIPS publication.
* NOTE: This setting is one-time only. 
  * If you need for the instance to be fully FIPS-compliant, configure it to 
    "true" before you start it for the first time. If you do not do this,
    the Splunk secret key that the instance generates on first-time startup
    might not meet FIPS guidance.
  * If you configure it to "true" and then start the Splunk platform instance, 
    you cannot later configure it to "false". You must reinstall the software.
* Running the Splunk platform in FIPS mode can result in the platform operating
  more slowly than if you ran it in normal mode.
* Default: 0

PYTHONHTTPSVERIFY = [0|1]
* Whether or not the Splunk platform instance sets up TLS validation for the httplib
  module in the Python interpreter embedded with the Splunk package.
* Default: 0

PYTHONUTF8 = [0|1]
* Determines whether the Splunk platform instance enables the UTF-8 mode
  in the Python interpreter embedded with the Splunk package.
* A value of 1 means UTF-8 mode is enabled.
* This setting applies regardless of the system locale encoding.
* Default: 1

#*******
# Service/server names.
#
# These settings are considered internal, and altering them is not
# supported.
#
# On Windows, they influence the expected name of the service;
# on UNIX they influence the reported name of the appropriate
# server or daemon process.
#
# On Linux distributions that run systemd, this is the name of the
# unit file for the service that Splunk Enterprise runs as.
# For example, if you set 'SPLUNK_SERVER_NAME' to 'splunk'
# then the corresponding unit file should be named 'splunk.service'.
#
# If you want to run multiple instances of Splunk as *services* on
# Windows, you must change the names for instances after the first.
# This is because the first instance takes up the service names
# 'Splunkd' and 'Splunkweb', and you may not have multiple services with
# same name.
#*******

SPLUNK_SERVER_NAME = <string>
* Names the splunkd server/service.
* Defaults to splunkd (UNIX), or Splunkd (Windows).

SPLUNK_WEB_NAME = <string>
* No longer used.

#*******
# File system check enable/disable
#
# CAUTION!
# USE OF THIS ADVANCED SETTING IS NOT SUPPORTED. IRREVOCABLE DATA LOSS
# CAN OCCUR. YOU USE THE SETTING SOLELY AT YOUR OWN RISK.
# CAUTION!
#
# When the Splunk software encounters a file system that it does not recognize,
# it runs a utility called 'locktest' to confirm that it can write to the
# file system correctly. If 'locktest' fails for any reason, splunkd
# cannot start.
#
# The following setting lets you temporarily bypass the 'locktest'
# check (for example, when a software vendor introduces a new default
# file system on a popular operating system). When it is active, splunkd
# starts regardless of its ability to interact with the file system.
#
# Use this setting if and only if:
#
# * You are a skilled Splunk administrator and know what you are doing.
# * You use Splunk software in a development environment.
# * You want to recover from a situation where the default
#   filesystem has changed outside your control, such as
#   during an operating system upgrade.
# * You want to recover from a situation where a Splunk bug
#   has invalidated a previously functional file system after an upgrade.
# * You want to evaluate the performance of a file system for which
#   Splunk has not yet offered support.
# * You have been given explicit instruction from Splunk Support to use
#   the setting to solve a problem where the Splunk software does not start
#   because of a failed file system check.
# * You understand and accept all the risks of using the setting,
#   up to and including LOSING ALL YOUR DATA WITH NO CHANCE OF RECOVERY
#   while the setting is active.
#
# If none of these scenarios applies to you, then DO NOT USE THE SETTING.
#
# CAUTION!
# USE OF THIS ADVANCED SETTING IS NOT SUPPORTED. IRREVOCABLE DATA LOSS
# CAN OCCUR. YOU USE THE SETTING SOLELY AT YOUR OWN RISK.
# CAUTION!
#*******

OPTIMISTIC_ABOUT_FILE_LOCKING = [0|1]
* Whether or not Splunk software skips the file system lock check on
  unrecognized file systems.
* CAUTION: USE THIS SETTING AT YOUR OWN RISK. YOU CAN LOSE ANY DATA
  THAT HAS BEEN INDEXED WHILE THE SETTING IS ACTIVE.
* When set to 1, Splunk software skips the file system check, and
  splunkd starts whether or not it can recognize the file system.
* Defaults to 0 (Run the file system check.)

<<<<<<< HEAD
SPLUNK_PYTHON_DONT_ESCAPE_PRINTABLE = 0|1
* Determines whether the Splunk Python interpreter escapes non-printable
  characters such as ASCII 0–32,127, when logging with the Python
  logging module.
* Exceptions: \t (chr(9)/0x09), \n (chr(10)/0x0a), \r (chr(13)/0x0d)
* When set to 1, scripts that log when using Splunk's Python interpreter
  will NOT escape non-printable characters and may be in log files
* Defaults to 0 (Non-printable characters WILL be escaped)

ENABLE_CPUSHARES = <boolean>
* Whether or not Splunk software adds 'CPUShares=1024' to the systemd service
  unit file named Splunkd.service by default, in /etc/systemd/system.
* Supported for only Linux.
* Defaults: true
