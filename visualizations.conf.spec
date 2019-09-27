#   Version 6.5.0
#
# This file contains definitions for visualizations an app makes avialable
# to the system. An app intending to share visualizations with the system
# should include a visualizations.conf in $SPLUNK_HOME/etc/apps/<appname>/default
#
# visualizations.conf should include one stanza for each visualization to be shared
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

#*******
# The possible attribute/value pairs for visualizations.conf are:
#*******

[<stanza name>]
* Create a unique stanza name for each visualization. It should match the name
  of the visualization 
* Follow the stanza name with any number of the following attribute/value
  pairs.
* If you do not specify an attribute, Splunk uses the default.

allow_user_selection = <bool>
* Optional.
* Whether the visualization should be available for users to select
* Defaults to true

default_height = <int>
* Optional.
* The default height of the visualization in pixels
* Defaults to 250

description = <string>
* Required.
* The short description that will show up in the visualization picker
* Defaults to ""

disabled = <bool>
* Optional.
* Disable the visualization by setting to true.
* If set to true, the visualization is not available anywhere in Splunk
* Defaults to false.

label = <string>
* Required.
* The human-readable label or title of the visualization
* Will be used in dropdowns and lists as the name of the visualization
* Defaults to <app_name>.<viz_name>

search_fragment = <string>
* Required.
* An example part of a search that formats the data correctly for the viz. Typically the last pipe(s) in a search query.
* Defaults to ""
