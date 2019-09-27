#   Version 7.1.1
#
# This file contains attributes and values that you can use to configure
# data transformations.  and event signing in transforms.conf.
#
# Transforms.conf is commonly used for:
# * Configuring regex-based host and source type overrides.
# * Anonymizing certain types of sensitive incoming data, such as credit
#   card or social security numbers.
# * Routing specific events to a particular index, when you have multiple
#   indexes.
# * Creating new index-time field extractions. NOTE: We do not recommend
#   adding to the set of fields that are extracted at index time unless it
#   is absolutely necessary because there are negative performance
#   implications.
# * Creating advanced search-time field extractions that involve one or more
#   of the following:
#   * Reuse of the same field-extracting regular expression across multiple
#     sources, source types, or hosts.
#   * Application of more than one regex to the same source, source type, or
#     host.
#   * Using a regex to extract one or more values from the values of another
#     field.
#   * Delimiter-based field extractions (they involve field-value pairs that
#     are separated by commas, colons, semicolons, bars, or something
#     similar).
#   * Extraction of multiple values for the same field (multivalued field
#     extraction).
#   * Extraction of fields with names that begin with numbers or
#     underscores.
#   * NOTE: Less complex search-time field extractions can be set up
#           entirely in props.conf.
# * Setting up lookup tables that look up fields from external sources.
#
# All of the above actions require corresponding settings in props.conf.
#
# You can find more information on these topics by searching the Splunk
# documentation (http://docs.splunk.com/Documentation)
#
# There is a transforms.conf file in $SPLUNK_HOME/etc/system/default/. To
# set custom configurations, place a transforms.conf
# $SPLUNK_HOME/etc/system/local/. For examples, see the
# transforms.conf.example file.
#
# You can enable configurations changes made to transforms.conf by typing
# the following search string in Splunk Web:
#
# | extract reload=t
#
# To learn more about configuration files (including precedence) please see
# the documentation located at
# http://docs.splunk.com/Documentation/Splunk/latest/Admin/Aboutconfigurationfiles

# GLOBAL SETTINGS
# Use the [default] stanza to define any global settings.
#  * You can also define global settings outside of any stanza, at the top
#    of the file.
#  * Each conf file should have at most one default stanza. If there are
#    multiple default stanzas, attributes are combined. In the case of
#    multiple definitions of the same attribute, the last definition in the
#    file wins.
#  * If an attribute is defined at both the global level and in a specific
#    stanza, the value in the specific stanza takes precedence.


[<unique_transform_stanza_name>]
* Name your stanza. Use this name when you configure field extractions,
  lookup tables, and event routing in props.conf. For example, if you are
  setting up an advanced search-time field extraction, in props.conf you
  would add REPORT-<class> = <unique_transform_stanza_name> under the
  [<spec>] stanza that corresponds with a stanza you've created in
  transforms.conf.
* Follow this stanza name with any number of the following attribute/value
  pairs, as appropriate for what you intend to do with the transform.
* If you do not specify an entry for each attribute, Splunk uses the default
  value.

REGEX = <regular expression>
* Enter a regular expression to operate on your data.
* NOTE: This attribute is valid for both index-time and search-time field
  extraction.
* REGEX is required for all search-time transforms unless you are setting up
  an ASCII-only delimiter-based field extraction, in which case you can use
  DELIMS (see the DELIMS attribute description, below).
* REGEX is required for all index-time transforms.
* REGEX and the FORMAT attribute:
  * Name-capturing groups in the REGEX are extracted directly to fields.
    This means that you do not need to specify the FORMAT attribute for
    simple field extraction cases (see the description of FORMAT, below).
  * If the REGEX extracts both the field name and its corresponding field
    value, you can use the following special capturing groups if you want to
    skip specifying the mapping in FORMAT:
      _KEY_<string>, _VAL_<string>.
  * For example, the following are equivalent:
    * Using FORMAT:
      * REGEX  = ([a-z]+)=([a-z]+)
      * FORMAT = $1::$2
    * Without using FORMAT
      * REGEX  = (?<_KEY_1>[a-z]+)=(?<_VAL_1>[a-z]+)
    * When using either of the above formats, in a search-time extraction,
      the regex will continue to match against the source text, extracting
      as many fields as can be identified in the source text.
* Defaults to an empty string.

FORMAT = <string>
* NOTE: This option is valid for both index-time and search-time field extraction. However, FORMAT
  behaves differently depending on whether the extraction is performed at index time or
  search time.
* This attribute specifies the format of the event, including any field names or values you want
  to add.
* FORMAT for index-time extractions:
  * Use $n (for example $1, $2, etc) to specify the output of each REGEX
    match.
  * If REGEX does not have n groups, the matching fails.
  * The special identifier $0 represents what was in the DEST_KEY before the
    REGEX was performed.
  * At index time only, you can use FORMAT to create concatenated fields:
    * Example: FORMAT = ipaddress::$1.$2.$3.$4
  * When you create concatenated fields with FORMAT, "$" is the only special
    character. It is treated as a prefix for regex-capturing groups only if
    it is followed by a number and only if the number applies to an existing
    capturing group. So if REGEX has only one capturing group and its value
    is "bar", then:
      * "FORMAT = foo$1" yields "foobar"
      * "FORMAT = foo$bar" yields "foo$bar"
      * "FORMAT = foo$1234" yields "foo$1234"
      * "FORMAT = foo$1\$2" yields "foobar\$2"
  * At index-time, FORMAT defaults to <stanza-name>::$1
* FORMAT for search-time extractions:
  * The format of this field as used during search time extractions is as
    follows:
    * FORMAT = <field-name>::<field-value>( <field-name>::<field-value>)*
      where:
      * field-name  = [<string>|$<extracting-group-number>]
      * field-value = [<string>|$<extracting-group-number>]
  * Search-time extraction examples:
      * 1. FORMAT = first::$1 second::$2 third::other-value
      * 2. FORMAT = $1::$2
  * If you configure FORMAT with a variable <field-name>, such as in the second
    example above, the regular expression is repeatedly applied to the source key
    to match and extract all field/value pairs in the event.
  * When you use FORMAT to set both the field and the value (such as FORMAT =
    third::other-value), and the value is not an indexed token, you must set the
    field to INDEXED_VALUE = false in fields.conf. Not doing so can cause 
    inconsistent search results.
  * NOTE: You cannot create concatenated fields with FORMAT at search time.
    That functionality is only available at index time.
  * At search-time, FORMAT defaults to an empty string.

MATCH_LIMIT = <integer>
* Only set in transforms.conf for REPORT and TRANSFORMS field extractions.
   For EXTRACT type field extractions, set this in props.conf.
* Optional. Limits the amount of resources that are spent by PCRE
  when running patterns that will not match.
* Use this to set an upper bound on how many times PCRE calls an internal
  function, match(). If set too low, PCRE may fail to correctly match a pattern.
* Defaults to 100000

DEPTH_LIMIT = <integer>
* Only set in transforms.conf for REPORT and TRANSFORMS field extractions.
   For EXTRACT type field extractions, set this in props.conf.
* Optional. Limits the amount of resources that are spent by PCRE
  when running patterns that will not match.
* Use this to limit the depth of nested backtracking in an internal PCRE
  function, match(). If set too low, PCRE might fail to correctly match a pattern.
* Default: 1000

CLONE_SOURCETYPE = <string>
* This name is wrong; a transform with this setting actually clones and
  modifies events, and assigns the new events the specified sourcetype.
* If CLONE_SOURCETYPE is used as part of a transform, the transform will
  create a modified duplicate event, for all events that the transform is
  applied to via normal props.conf rules.
* Use this feature if you need to store both the original and a modified
  form of the data in your system, or if you want to send the original and a
  modified form to different outbound systems.
  * A typical example would be to retain sensitive information according to
    one policy and a version with the sensitive information removed
    according to another policy.  For example, some events may have data
    that you must retain for 30 days (such as personally identifying
    information) and only 30 days with restricted access, but you need that
    event retained without the sensitive data for a longer time with wider
    access.
* Specifically, for each event handled by this transform, a near-exact copy
  is made of the original event, and the transformation is applied to the
  copy.  The original event will continue along normal data processing
  unchanged.
* The <string> used for CLONE_SOURCETYPE selects the sourcetype that will be
  used for the duplicated events.
* The new sourcetype MUST differ from the the original sourcetype.  If the
  original sourcetype is the same as the target of the CLONE_SOURCETYPE,
  Splunk will make a best effort to log warnings to splunkd.log, but this
  setting will be silently ignored at runtime for such cases, causing the
  transform to be applied to the original event without cloning.
* The duplicated events will receive index-time transformations & sed
  commands all transforms which match its new host/source/sourcetype.
  * This means that props matching on host or source will incorrectly be
    applied a second time. (SPL-99120)
* Can only be used as part of of an otherwise-valid index-time transform.  For
  example REGEX is required, there must be a valid target (DEST_KEY or
  WRITE_META), etc as above.

LOOKAHEAD = <integer>
* NOTE: This option is valid for all index time transforms, such as
  index-time field creation, or DEST_KEY modifications.
* Optional. Specifies how many characters to search into an event.
* Defaults to 4096.
* You may want to increase this value if you have event line lengths that
  exceed 4096 characters (before linebreaking).

WRITE_META = [true|false]
* NOTE: This attribute is only valid for index-time field extractions.
* Automatically writes REGEX to metadata.
* Required for all index-time field extractions except for those where
  DEST_KEY = _meta (see the description of the DEST_KEY attribute, below)
* Use instead of DEST_KEY = _meta.
* Defaults to false.

DEST_KEY = <KEY>
* NOTE: This attribute is only valid for index-time field extractions.
* Specifies where Splunk stores the expanded FORMAT results in accordance
  with the REGEX match.
* Required for index-time field extractions where WRITE_META = false or is
  not set.
* For index-time extractions, DEST_KEY can be set to a number of values
  mentioned in the KEYS section at the bottom of this file.
  * If DEST_KEY = _meta (not recommended) you should also add $0 to the
    start of your FORMAT attribute.  $0 represents the DEST_KEY value before
    Splunk performs the REGEX (in other words, _meta).
    * The $0 value is in no way derived *from* the REGEX match. (It
      does not represent a captured group.)
* KEY names are case-sensitive, and should be used exactly as they appear in
  the KEYs list at the bottom of this file. (For example, you would say
  DEST_KEY = MetaData:Host, *not* DEST_KEY = metadata:host .)

DEFAULT_VALUE = <string>
* NOTE: This attribute is only valid for index-time field extractions.
* Optional. Splunk writes the DEFAULT_VALUE to DEST_KEY if the REGEX fails.
* Defaults to empty.

SOURCE_KEY = <string>
* NOTE: This attribute is valid for both index-time and search-time field
  extractions.
* Optional. Defines the KEY that Splunk applies the REGEX to.
* For search time extractions, you can use this attribute to extract one or
  more values from the values of another field. You can use any field that
  is available at the time of the execution of this field extraction
* For index-time extractions use the KEYs described at the bottom of this
  file.
  * KEYs are case-sensitive, and should be used exactly as they appear in
    the KEYs list at the bottom of this file. (For example, you would say
    SOURCE_KEY = MetaData:Host, *not* SOURCE_KEY = metadata:host .)
* If <string> starts with "field:" or "fields:" the meaning is changed.
  Instead of looking up a KEY, it instead looks up an already indexed field.
  For example, if a CSV field name "price" was indexed then
  "SOURCE_KEY = field:price" causes the REGEX to match against the contents
  of that field.  It's also possible to list multiple fields here with
  "SOURCE_KEY = fields:name1,name2,name3" which causes MATCH to be run
  against a string comprising of all three values, separated by space
  characters.
* SOURCE_KEY is typically used in conjunction with REPEAT_MATCH in
  index-time field transforms.
* Defaults to _raw, which means it is applied to the raw, unprocessed text
  of all events.

REPEAT_MATCH = [true|false]
* NOTE: This attribute is only valid for index-time field extractions.
* Optional. When set to true Splunk runs the REGEX multiple times on the
  SOURCE_KEY.
* REPEAT_MATCH starts wherever the last match stopped, and continues until
  no more matches are found. Useful for situations where an unknown number
  of REGEX matches are expected per event.
* Defaults to false.

DELIMS = <quoted string list>
* NOTE: This attribute is only valid for search-time field extractions.
* IMPORTANT: If a value may contain an embedded unescaped double quote
  character, such as "foo"bar", use REGEX, not DELIMS. An escaped double
  quote (\") is ok. Non-ASCII delimiters also require the use of REGEX.
* Optional. Used in place of REGEX when dealing with ASCII-only delimiter-
  based field extractions, where field values (or field/value pairs) are
  separated by delimiters such as colons, spaces, line breaks, and so on.
* Sets delimiter characters, first to separate data into field/value pairs,
  and then to separate field from value.
* Each individual ASCII character in the delimiter string is used as a
  delimiter to split the event.
* Delimiters must be specified within double quotes (eg. DELIMS="|,;").
  Special escape sequences are \t (tab), \n (newline), \r (carriage return),
  \\ (backslash) and \" (double quotes).
* When the event contains full delimiter-separated field/value pairs, you
  enter two sets of quoted characters for DELIMS:
* The first set of quoted delimiters extracts the field/value pairs.
* The second set of quoted delimiters separates the field name from its
  corresponding value.
* When the event only contains delimiter-separated values (no field names)
  you use just one set of quoted delimiters to separate the field values.
  Then you use the FIELDS attribute to apply field names to the extracted
  values (see FIELDS, below).
  * Alternately, Splunk reads even tokens as field names and odd tokens as
    field values.
* Splunk consumes consecutive delimiter characters unless you specify a list
  of field names.
* The following example of DELIMS usage applies to an event where
  field/value pairs are separated by '|' symbols and the field names are
  separated from their corresponding values by '=' symbols:
    [pipe_eq]
    DELIMS = "|", "="
* Defaults to "".

FIELDS = <quoted string list>
* NOTE: This attribute is only valid for search-time field extractions.
* Used in conjunction with DELIMS when you are performing delimiter-based
  field extraction and only have field values to extract.
* FIELDS enables you to provide field names for the extracted field values,
  in list format according to the order in which the values are extracted.
* NOTE: If field names contain spaces or commas they must be quoted with " "
        (to escape, use \).
* The following example is a delimiter-based field extraction where three
  field values appear in an event. They are separated by a comma and then a
  space.
    [commalist]
    DELIMS = ", "
    FIELDS = field1, field2, field3
* Defaults to "".

MV_ADD = [true|false]
* NOTE: This attribute is only valid for search-time field extractions.
* Optional. Controls what the extractor does when it finds a field which
  already exists.
* If set to true, the extractor makes the field a multivalued field and
  appends the newly found value, otherwise the newly found value is
  discarded.
* Defaults to false

CLEAN_KEYS = [true|false]
* NOTE: This attribute is only valid for search-time field extractions.
* Optional. Controls whether Splunk "cleans" the keys (field names) it
  extracts at search time.
  "Key cleaning" is the practice of replacing any non-alphanumeric
  characters (characters other than those falling between the a-z, A-Z, or
  0-9 ranges) in field names with underscores, as well as the stripping of
  leading underscores and 0-9 characters from field names.
* Add CLEAN_KEYS = false to your transform if you need to extract field
  names that include non-alphanumeric characters, or which begin with
  underscores or 0-9 characters.
* Defaults to true.

KEEP_EMPTY_VALS = [true|false]
* NOTE: This attribute is only valid for search-time field extractions.
* Optional. Controls whether Splunk keeps field/value pairs when the value
  is an empty string.
* This option does not apply to field/value pairs that are generated by
  Splunk's autokv extraction. Autokv ignores field/value pairs with empty
  values.
* Defaults to false.

CAN_OPTIMIZE = [true|false]
* NOTE: This attribute is only valid for search-time field extractions.
* Optional. Controls whether Splunk can optimize this extraction out
  (another way of saying the extraction is disabled).
* You might use this if you're running searches under a Search Mode setting
  that disables field discovery--it ensures that Splunk *always* discovers
  specific fields.
* Splunk only disables an extraction if it can determine that none of the
  fields identified by the extraction will ever be needed for the successful
  evaluation of a search.
* NOTE: This option should be rarely set to false.
* Defaults to true.


#*******
# Lookup tables
#*******
# NOTE: Lookup tables are used ONLY during search time

filename = <string>
* Name of static lookup file.
* File should be in $SPLUNK_HOME/etc/system/lookups/, or in
  $SPLUNK_HOME/etc/<app_name>/lookups/ if the lookup belongs to a specific app.
* If file is in multiple 'lookups' directories, no layering is done.
* Standard conf file precedence is used to disambiguate.
* Only file names are supported. Paths are explicitly not supported. If you
  specify a path, the Splunk software strips the path to use the value after
  the final path separator.
* The Splunk software then looks for this filename in
  $SPLUNK_HOME/etc/system/lookups/ or $SPLUNK_HOME/etc/<app_name>/lookups/.
* Defaults to empty string.

collection = <string>
* Name of the collection to use for this lookup.
* Collection should be defined in $SPLUNK_HOME/etc/<app_name>/collections.conf
  for some <app_name>
* If collection is in multiple collections.conf file, no layering is done.
* Standard conf file precedence is used to disambiguate.
* Defaults to empty string (in which case the name of the stanza is used).

max_matches = <integer>
* The maximum number of possible matches for each input lookup value
  (range 1 - 1000).
* If the lookup is non-temporal (not time-bounded, meaning the time_field
  attribute is not specified), Splunk uses the first <integer> entries, in
  file order.
* If the lookup is temporal, Splunk uses the first <integer> entries in
  descending time order.  In other words, up <max_matches> lookup entries
  will be allowed to match, and if more than this many the ones nearest to
  the lookup value will be used.
* Default = 1000 if the lookup is not temporal, default = 1 if it is
  temporal.

min_matches = <integer>
* Minimum number of possible matches for each input lookup value.
* Default = 0 for both temporal and non-temporal lookups, which means that
  Splunk outputs nothing if it cannot find any matches.
* However, if min_matches > 0, and Splunk get less than min_matches, then
  Splunk provides the default_match value provided (see below).

default_match = <string>
* If min_matches > 0 and Splunk has less than min_matches for any given
  input, it provides this default_match value one or more times until the
  min_matches threshold is reached.
* Defaults to empty string.

case_sensitive_match = <bool>
* NOTE: To disable case-sensitive matching with input fields and
  values from events, the KV Store lookup data must be entirely
  in lower case. The input data can be of any case, but the KV Store
  data must be lower case.
* If set to false, case insensitive matching will be performed for all
  fields in a lookup table
* Defaults to true (case sensitive matching)

match_type = <string>
* A comma and space-delimited list of <match_type>(<field_name>)
  specification to allow for non-exact matching
* The available match_type values are WILDCARD, CIDR, and EXACT.  EXACT is
  the default and does not need to be specified.  Only fields that should
  use WILDCARD or CIDR matching should be specified in this list

external_cmd = <string>
* Provides the command and arguments to invoke to perform a lookup. Use this
  for external (or "scripted") lookups, where you interface with with an
  external script rather than a lookup table.
* This string is parsed like a shell command.
* The first argument is expected to be a python script (or executable file)
  located in $SPLUNK_HOME/etc/<app_name>/bin (or ../etc/searchscripts).
* Presence of this field indicates that the lookup is external and command
  based.
* Defaults to empty string.

fields_list = <string>
* A comma- and space-delimited list of all fields that are supported by the
  external command.

index_fields_list = <string>
* A comma- and space-delimited list of fields that need to be indexed
  for a static .csv lookup file.
* The other fields are not indexed and not searchable. 
* Restricting the fields enables better lookup performance.
* Defaults to all fields that are defined in the .csv lookup file header. 

external_type = [python|executable|kvstore|geo]
* Type of external command.
* "python" a python script
* "executable" a binary executable
* "geo" a point-in-polygon lookup
* Defaults to "python".

time_field = <string>
* Used for temporal (time bounded) lookups. Specifies the name of the field
  in the lookup table that represents the timestamp.
* Defaults to an empty string, meaning that lookups are not temporal by
  default.

time_format = <string>
* For temporal lookups this specifies the 'strptime' format of the timestamp
  field.
* You can include subseconds but Splunk will ignore them.
* Defaults to %s.%Q or seconds from unix epoch in UTC an optional milliseconds.

max_offset_secs = <integer>
* For temporal lookups, this is the maximum time (in seconds) that the event
  timestamp can be later than the lookup entry time for a match to occur.
* Default is 2000000000 (no maximum, effectively).

min_offset_secs = <integer>
* For temporal lookups, this is the minimum time (in seconds) that the event
  timestamp can be later than the lookup entry timestamp for a match to
  occur.
* Defaults to 0.

batch_index_query = <bool>
* For large file based lookups, this determines whether queries can be
  grouped to improve search performance.
* Default is unspecified here, but defaults to true (at global level in
  limits.conf)

allow_caching = <bool>
* Allow output from lookup scripts to be cached
* Default is true

max_ext_batch = <integer>
* The maximum size of external batch (range 1 - 1000).
* Only used with kvstore.
* Default = 300.

filter = <string>
* Filter results from the lookup table before returning data. Create this filter
  like you would a typical search query using Boolean expressions and/or comparison operators.
* For KV Store lookups, filtering is done when data is initially retrieved to improve performance.
* For CSV lookups, filtering is done in memory.

feature_id_element = <string>
* If lookup file is a kmz file, this field can be used to specify the xml path from
  placemark down to the name of this placemark.
* Default = /Placemark/name
* ONLY for Kmz files

check_permission = <bool>
* Specifies whether the system can verify that a user has write permission to a lookup 
  file when that user uses the outputlookup command to modify that file. If the user does 
  not have write permissions, the system prevents the modification.
* The check_permission setting is only respected when output_check_permission
  is set to "true" in limits.conf. 
* You can set lookup table file permissions in the .meta file for each lookup file, or 
  through the Lookup Table Files page in Settings. By default, only users who have the 
  admin or power role can write to a shared CSV lookup file.
* Default: false
* This setting applies only to CSV lookup configurations.

replicate = true|false
* Indicates whether to replicate CSV lookups to indexers.
* When false, the CSV lookup is replicated only to search heads in a search head cluster
  so that input lookup commands can use this lookup on the search heads.
* When true, the CSV lookup is replicated to both indexers and search heads.
* Only for CSV lookup files.
* Note that replicate=true works only if it is included in replication whitelist,
  See distSearch.conf/[replicationWhitelist] option.
* Defaults to true.

[statsd-dims:<unique_transforms_stanza_name>]
* 'statsd-dims' prefix indicates this stanza is applicable only to statsd metric
  type input data.
* This stanza is used to define regular expression to match and extract dimensions
  out of statsd dotted name segments.
* By default, only the unmatched segments of the statsd dotted name segment
  becomes the metric_name.

REGEX = <regular expression>
* Splunk supports named capturing group extraction format (?<dim1>group)(?<dim2>group)..
  to provide dimension names of the corresponding values being extracted out.

REMOVE_DIMS_FROM_METRIC_NAME = <boolean>
* By default, this is set to true.
* If set to false, the matched dimension values from the regex above would also
  be a part of the metric name.
* If true, the matched dimension values would not be a part of metric name.


#*******
# KEYS:
#*******
* NOTE: Keys are case-sensitive. Use the following keys exactly as they
        appear.

queue : Specify which queue to send the event to (can be nullQueue, indexQueue).
        * indexQueue is the usual destination for events going through the
          transform-handling processor.
        * nullQueue is a destination which will cause the events to be
          dropped entirely.
_raw  : The raw text of the event.
_meta : A space-separated list of metadata for an event.
_time : The timestamp of the event, in seconds since 1/1/1970 UTC.

MetaData:Host       : The host associated with the event.
                      The value must be prefixed by "host::"

_MetaData:Index     : The index where the event should be stored.

MetaData:Source     : The source associated with the event.
                      The value must be prefixed by "source::"

MetaData:Sourcetype : The sourcetype of the event.
                      The value must be prefixed by "sourcetype::"

_TCP_ROUTING        : Comma separated list of tcpout group names (from outputs.conf)
                      Defaults to groups present in 'defaultGroup' for [tcpout].

_SYSLOG_ROUTING     : Comma separated list of syslog-stanza  names (from outputs.conf)
                      Defaults to groups present in 'defaultGroup' for [syslog].

* NOTE: Any KEY (field name) prefixed by '_' is not indexed by Splunk, in general.

[accepted_keys]

<name> = <key>

* Modifies Splunk's list of key names it considers valid when automatically
  checking your transforms for use of undocumented SOURCE_KEY or DEST_KEY
  values in index-time transformations.
* By adding entries to [accepted_keys], you can tell Splunk that a key that
  is not documented is a key you intend to work for reasons that are valid
  in your environment / app / etc.
* The 'name' element is simply used to disambiguate entries, similar
  to -class entries in props.conf.  The name can be anything of your
  choosing, including a descriptive name for why you use the key.
* The entire stanza defaults to not being present, causing all keys not
  documented just above to be flagged.
