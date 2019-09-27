#   Version 7.0.1
#
# Specification for user-seed.conf.  Allows configuration of Splunk's
# initial username and password.  Currently, only one user can be configured
# with user-seed.conf.
#
# Specification for user-seed.conf.  Allows configuration of Splunk's initial username and password.
# Currently, only one user can be configured with user-seed.conf.
#
# To override the default username and password, place user-seed.conf in 
# $SPLUNK_HOME/etc/system/local. You must restart Splunk to enable configurations.
# If the $SPLUNK_HOME/etc/passwd file is present, the settings in this file (user-seed.conf) are not used.
#
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles
# To learn more about configuration files (including precedence) please see the documentation 
# located at http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

[user_info]
* Default is Admin.

USERNAME = <string> 
          * Username you want to associate with a password.
          * Default is Admin.

PASSWORD = <password>
          * Password you wish to set for that user.
          * Default is changeme.
