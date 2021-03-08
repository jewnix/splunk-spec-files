#   Version 7.2.9
#
# This file contains possible attributes and values for configuring
# authentication via authentication.conf.
#
# There is an authentication.conf in $SPLUNK_HOME/etc/system/default/.  To
# set custom configurations, place an authentication.conf in
# $SPLUNK_HOME/etc/system/local/. For examples, see
# authentication.conf.example.  You must restart Splunk to enable
# configurations.
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
#     multiple definitions of the same attribute, the last definition in the
#     file wins.
#   * If an attribute is defined at both the global level and in a specific
#     stanza, the value in the specific stanza takes precedence.

[authentication]
* Follow this stanza name with any number of the following attribute/value
  pairs.

authType = [Splunk|LDAP|Scripted|SAML|ProxySSO]
* Specify which authentication system to use.
* Supported values: Splunk, LDAP, Scripted, SAML, ProxySSO.
* Defaults to Splunk.

authSettings = <authSettings-key>,<authSettings-key>,...
* Key to look up the specific configurations of chosen authentication
  system.
* <authSettings-key> is the name of a stanza header that specifies
  attributes for scripted authentication, SAML, ProxySSO and for an LDAP
  strategy. Those stanzas are defined below.
* For LDAP, specify the LDAP strategy name(s) here. If you want Splunk to
  query multiple LDAP servers, enter a comma-separated list of all
  strategies. Each strategy must be defined in its own stanza. The order in
  which you specify the strategy names will be the order Splunk uses to
  query their servers when looking for a user.
* For scripted authentication, <authSettings-key> should be a single 
  stanza name.

passwordHashAlgorithm = [SHA512-crypt|SHA256-crypt|SHA512-crypt-<num_rounds>|SHA256-crypt-<num_rounds>|MD5-crypt]
* For the default "Splunk" authType, this controls how hashed passwords are
  stored in the $SPLUNK_HOME/etc/passwd file.
* "MD5-crypt" is an algorithm originally developed for FreeBSD in the early
  1990's which became a widely used standard among UNIX machines.  It was
  also used by Splunk up through the 5.0.x releases.  MD5-crypt runs the
  salted password through a sequence of 1000 MD5 operations.
* "SHA256-crypt" and "SHA512-crypt" are newer versions that use 5000 rounds
  of the SHA256 or SHA512 hash functions.  This is slower than MD5-crypt and
  therefore more resistant to dictionary attacks.  SHA512-crypt is used for
  system passwords on many versions of Linux.
* These SHA-based algorithm can optionally be followed by a number of rounds
  to use.  For example, "SHA512-crypt-10000" will use twice as many rounds
  of hashing as the default implementation.  The number of rounds must be at
  least 1000.
  If you specify a very large number of rounds (i.e. more than 20x the
  default value of 5000), splunkd may become unresponsive and connections to
  splunkd (from splunkweb or CLI) will time out.
* This setting only affects new password settings (either when a user is
  added or a user's password is changed)  Existing passwords will continue
  to work but retain their previous hashing algorithm.
* The default is "SHA512-crypt".

defaultRoleIfMissing = <splunk role>
* OPTIONAL
* Applicable for LDAP authType, if the LDAP server does not return any groups or
  groups cannot be mapped to Splunk roles, we will use this value if provided.
* Default is empty string.

externalTwoFactorAuthVendor = <string>
* OPTIONAL.
* A valid multifactor vendor string will enable multifactor authentication
  and loads support for the corresponding vendor if supported by Splunk.
* Empty string will disable multifactor authentication in Splunk.
* Currently Splunk supports Duo and RSA as multifactor authentication vendors.

externalTwoFactorAuthSettings = <externalTwoFactorAuthSettings-key>
* OPTIONAL.
* Key to look up the specific configuration of chosen multifactor
  authentication vendor.

#####################
# LDAP settings
#####################

[<authSettings-key>]
* Follow this stanza name with the attribute/value pairs listed below.
* For multiple strategies, you will need to specify multiple instances of
  this stanza, each with its own stanza name and a separate set of
  attributes.
* The <authSettings-key> must be one of the values listed in the
  authSettings attribute, specified above in the [authentication] stanza.

host = <string>
* REQUIRED
* This is the hostname of LDAP server.
* Be sure that your Splunk server can resolve the host name.

SSLEnabled = [0|1]
* OPTIONAL
* Defaults to disabled (0)
* See the file $SPLUNK_HOME/etc/openldap/ldap.conf for SSL LDAP settings

port = <integer>
* OPTIONAL
* This is the port that Splunk should use to connect to your LDAP server.
* Defaults to port 389 for non-SSL and port 636 for SSL

bindDN = <string>
* OPTIONAL, leave this blank to retrieve your LDAP entries using
  anonymous bind (must be supported by the LDAP server)
* Distinguished name of the user that will be retrieving the LDAP entries
* This user must have read access to all LDAP users and groups you wish to
  use in Splunk.

bindDNpassword = <password>
* OPTIONAL, leave this blank if anonymous bind is sufficient
* Password for the bindDN user.

userBaseDN = <string>
* REQUIRED
* This is the distinguished names of LDAP entries whose subtrees contain the users
* Enter a ';' delimited list to search multiple trees.

userBaseFilter = <string>
* OPTIONAL
* This is the LDAP search filter you wish to use when searching for users.
* Highly recommended, especially when there are many entries in your LDAP
  user subtrees
* When used properly, search filters can significantly speed up LDAP queries
* Example that matches users in the IT or HR department:
    * userBaseFilter = (|(department=IT)(department=HR))
    * See RFC 2254 for more detailed information on search filter syntax
* This defaults to no filtering.

userNameAttribute = <string>
* REQUIRED
* This is the user entry attribute whose value is the username.
* NOTE: This attribute should use case insensitive matching for its values,
  and the values should not contain whitespace
    * Usernames are case insensitive in Splunk
* In Active Directory, this is 'sAMAccountName'
* A typical attribute for this is 'uid'

realNameAttribute = <string>
* REQUIRED
* This is the user entry attribute whose value is their real name 
  (human readable).
* A typical attribute for this is 'cn'

emailAttribute = <string>
* OPTIONAL
* This is the user entry attribute whose value is their email address.
* Defaults to 'mail'

groupMappingAttribute  = <string>
* OPTIONAL
* This is the user entry attribute whose value is used by group entries to
  declare membership.
* Groups are often mapped with user DN, so this defaults to 'dn'
* Set this if groups are mapped using a different attribute
  * Usually only needed for OpenLDAP servers.
  * A typical attribute used to map users to groups is 'uid'
    * For example, assume a group declares that one of its members is
      'splunkuser'
    * This implies that every user with 'uid' value 'splunkuser' will be
      mapped to that group

groupBaseDN = [<string>;<string>;...]
* REQUIRED
* This is the distinguished names of LDAP entries whose subtrees contain 
  the groups.
* Enter a ';' delimited list to search multiple trees.
* If your LDAP environment does not have group entries, there is a
  configuration that can treat each user as its own group
  * Set groupBaseDN to the same as userBaseDN, which means you will search
    for groups in the same place as users
  * Next, set the groupMemberAttribute and groupMappingAttribute to the same
    attribute as userNameAttribute
    * This means the entry, when treated as a group, will use the username
      value as its only member
  * For clarity, you should probably also set groupNameAttribute to the same
    value as userNameAttribute as well

groupBaseFilter = <string>
* OPTIONAL
* The LDAP search filter Splunk uses when searching for static groups
* Like userBaseFilter, this is highly recommended to speed up LDAP queries
* See RFC 2254 for more information
* This defaults to no filtering

dynamicGroupFilter = <string>
* OPTIONAL
* The LDAP search filter Splunk uses when searching for dynamic groups
* Only configure this if you intend to retrieve dynamic groups on your LDAP server
* Example: '(objectclass=groupOfURLs)'

dynamicMemberAttribute = <string>
* OPTIONAL
* Only configure this if you intend to retrieve dynamic groups on your
  LDAP server
* This is REQUIRED if you want to retrieve dynamic groups
* This attribute contains the LDAP URL needed to retrieve members dynamically
* Example: 'memberURL'

groupNameAttribute = <string>
* REQUIRED
* This is the group entry attribute whose value stores the group name.
* A typical attribute for this is 'cn' (common name)
* Recall that if you are configuring LDAP to treat user entries as their own
  group, user entries must have this attribute

groupMemberAttribute = <string>
* REQUIRED
* This is the group entry attribute whose values are the groups members
* Typical attributes for this are 'member' and 'memberUid'
* For example, consider the groupMappingAttribute example above using
  groupMemberAttribute 'member'
  * To declare 'splunkuser' as a group member, its attribute 'member' must
    have the value 'splunkuser'

nestedGroups = <bool>
* OPTIONAL
* Controls whether Splunk will expand nested groups using the
  'memberof' extension.
* Set to 1 if you have nested groups you want to expand and the 'memberof'
* extension on your LDAP server.

charset = <string>
* OPTIONAL
* ONLY set this for an LDAP setup that returns non-UTF-8 encoded data. LDAP
  is supposed to always return UTF-8 encoded data (See RFC 2251), but some
  tools incorrectly return other encodings.
* Follows the same format as CHARSET in props.conf (see props.conf.spec)
* An example value would be "latin-1"

anonymous_referrals = <bool>
* OPTIONAL
* Set this to 0 to turn off referral chasing
* Set this to 1 to turn on anonymous referral chasing
* IMPORTANT: We only chase referrals using anonymous bind. We do NOT support
  rebinding using credentials.
* If you do not need referral support, we recommend setting this to 0
* If you wish to make referrals work, set this to 1 and ensure your server
  allows anonymous searching
* Defaults to 1

sizelimit = <integer>
* OPTIONAL
* Limits the amount of entries we request in LDAP search
* IMPORTANT: The max entries returned is still subject to the maximum
  imposed by your LDAP server
  * Example: If you set this to 5000 and the server limits it to 1000,
             you'll still only get 1000 entries back
* Defaults to 1000

timelimit = <integer>
* OPTIONAL
* Limits the amount of time in seconds we will wait for an LDAP search
  request to complete
* If your searches finish quickly, you should lower this value from the
  default
* Defaults to 15 seconds
* Maximum value is 30 seconds

network_timeout = <integer>
* OPTIONAL
* Limits the amount of time a socket will poll a connection without activity
* This is useful for determining if your LDAP server cannot be reached
* IMPORTANT: As a connection could be waiting for search results, this value
             must be higher than 'timelimit'
* Like 'timelimit', if you have a fast connection to your LDAP server, we
  recommend lowering this value
* Defaults to 20

ldap_negative_cache_timeout = <nonnegative decimal>
* The amount of time, in seconds, that Splunk software remembers that a non-existent
  user on an LDAP provider does not exist.
* This setting is useful when you want to avoid frequent LDAP queries for users
  that do not exist on the LDAP provider.
* This setting does not prevent LDAP queries on login. Login always queries the LDAP
  provider to confirm that a user exists.
* Default: 86400

#####################
# Map roles
#####################

[roleMap_<authSettings-key>]
* The mapping of Splunk roles to LDAP groups for the LDAP strategy specified
  by <authSettings-key>
* IMPORTANT: this role mapping ONLY applies to the specified strategy.
* Follow this stanza name with several Role-to-Group(s) mappings as defined
  below.
* Note: Importing groups for the same user from different strategies is not 
  supported.

<Splunk RoleName> = <LDAP group string>
* Maps a Splunk role (from authorize.conf) to LDAP groups
* This LDAP group list is semicolon delimited (no spaces).
* List several of these attribute value pairs to map several Splunk roles to
  LDAP Groups

#####################
# Scripted authentication
#####################

[<authSettings-key>]
* Follow this stanza name with the following attribute/value pairs:

scriptPath = <string>
* REQUIRED
* This is the full path to the script, including the path to the program
  that runs it (python)
* For example: "$SPLUNK_HOME/bin/python" "$SPLUNK_HOME/etc/system/bin/$MY_SCRIPT"
* Note: If a path contains spaces, it must be quoted. The example above
  handles the case where SPLUNK_HOME contains a space

scriptSearchFilters = [1|0]
* OPTIONAL - Only set this to 1 to call the script to add search filters.
* 0 disables (default)

[cacheTiming]
* Use these settings to adjust how long Splunk will use the answers returned
  from script functions before calling them again.

userLoginTTL = <time range string>
* Timeout for the userLogin script function.
* These return values are cached on a per-user basis.
* The default is '0' (no caching)

getUserInfoTTL = <time range string>
* Timeout for the getUserInfo script function.
* These return values are cached on a per-user basis.
* The default is '10s'

getUsersTTL = <time range string>
* Timeout for the getUsers script function.
* There is only one global getUsers cache (it is not tied to a
  specific user).
* The default is '10s'

* All timeouts can be expressed in seconds or as a search-like time range
* Examples include '30' (30 seconds), '2mins' (2 minutes), '24h' (24 hours), etc.
* You can opt to use no caching for a particular function by setting the
  value to '0'
  * Be aware that this can severely hinder performance as a result of heavy
    script invocation
* Choosing the correct values for cache timing involves a tradeoff between
  new information latency and general performance
  * High values yield better performance from calling the script less, but
    introduces a latency in picking up changes
  * Low values will pick up changes in your external auth system more
    quickly, but may slow down performance due to increased script
    invocations

#####################
# Settings for Splunk Authentication mode
#####################

[splunk_auth]
* Settings for Splunk's internal authentication system.

minPasswordLength = <positive integer>
* Specifies the minimum permitted password length in characters when
  passwords are set or modified. 
* Defaults to 8. Any value less than 1 will be ignored.
* This setting is optional.
* Password modification attempts which do not meet this requirement will be
* explicitly rejected.

minPasswordUppercase = <positive integer>
* Specifies the minimum permitted uppercase characters when passwords are set or modified.
* Defaults to 0.
* Splunk software ignores negative values.
* This setting is optional.
* Password modification attempts which do not meet this requirement will be
* explicitly rejected.

minPasswordLowercase = <positive integer>
* Specifies the minimum permitted lowercase characters when passwords are set or modified.
* Defaults to 0.
* Splunk software ignores negative values.
* This setting is optional.
* Password modification attempts which do not meet this requirement will be
* explicitly rejected.

minPasswordDigit = <positive integer>
* Specifies the minimum permitted digit or number characters when passwords are set or modified.
* Defaults to 0.
* Splunk software ignores negative values.
* This setting is optional.
* Password modification attempts which do not meet this requirement will be
* explicitly rejected.

minPasswordSpecial = <positive integer>
* Specifies the minimum permitted special characters when passwords are set or modified.
* The semicolon character ':' is not allowed.
* Defaults to 0.
* Splunk software ignores negative values.
* This setting is optional.
* Password modification attempts which do not meet this requirement will be
* explicitly rejected.

expirePasswordDays = <positive integer>
* Specifies the number of days before the password expires after a reset.
* Minimum value: 0
* Maximum value: 3650
* Default: 90
* Splunk software ignores negative values.
* This setting is optional.

expireAlertDays = <positive integer>
* Specifies the number of days to issue alerts before password expires.
* Minimum value: 0
* Maximum value: 120
* Default: 15
* Splunk software ignores negative values.
* This setting is optional.
* Alert appears in splunkd.log.

expireUserAccounts = <boolean>
* Specifies whether password expiration is enabled.
* Defaults to false (user passwords do not expire).
* This setting is optional.

forceWeakPasswordChange = <boolean>
* Specifies whether users must change a weak password.
* Defaults to false (users can keep weak password).
* This setting is optional.

lockoutUsers = <boolean>
* Specifies whether locking out users is enabled.
* Defaults to true (users will be locked out on incorrect logins).
* This setting is optional.
* If you enable this setting on members of a search head cluster, user lockout 
  state applies only per SHC member, not to the entire cluster.

lockoutMins = <positive integer>
* The number of minutes that a user is locked out after entering an incorrect 
  password more than 'lockoutAttempts' times in 'lockoutThresholdMins' minutes.
* Any value less than 1 will be ignored.
* Minimum value: 1
* Maximum value: 1440
* Default: 30
* This setting is optional.
* If you enable this setting on members of a search head cluster, user lockout 
  state applies only per SHC member, not to the entire cluster.

lockoutAttempts = <positive integer>
* The number of unsuccessful login attempts that can occur before a user is locked out.
* The unsuccessful login attempts must occur within 'lockoutThresholdMins' minutes.
* Any value less than 1 will be ignored.
* Minimum value: 1
* Maximum value: 64
* Default: 5
* This setting is optional.
* If you enable this setting on members of a search head cluster, user lockout 
  state applies only per SHC member, not to the entire cluster.

lockoutThresholdMins = <positive integer>
* Specifies the number of minutes that must pass from the time of the first failed 
  login before the failed login attempt counter resets.
* Any value less than 1 will be ignored.
* Minimum value: 1
* Maximum value: 120
* Default: 5
* This setting is optional.
* If you enable this setting on members of a search head cluster, user lockout 
  state applies only per SHC member, not to the entire cluster.

enablePasswordHistory = <boolean>
* Specifies whether password history is enabled.
* Defaults to false.
* When set to true, Splunk software maintains a history of passwords
  that have been used previously.
* This setting is optional.

passwordHistoryCount = <positive integer>
* The number of passwords that are stored in history. If password
  history is enabled, on password change, user is not allowed to pick an
  old password.
* Minimum value: 1
* Maximum value: 128
* Default: 24
* This setting is optional.

constantLoginTime = <number>
* The amount of time, in seconds, that the authentication manager
* waits before returning any kind of response to a login request.
* When you set this setting, login will be guaranteed to take the
* amount of time you specify. If necessary, the authentication manager
* adds a delay to the actual response time to keep this guarantee.
* This setting is optional.
* Minimum value: 0 (Disables login time guarantee)
* Maximum value: 5.0
* Default: 0

verboseLoginFailMsg = <boolean>
* Specifies whether or not the login failure message explains
  the failure reason.
* When set to true, Splunk software displays a message on login
  along with the failure reason.
* When set to false, Splunk software displays a generic failure
  message without a specific failure reason.
* This setting is optional.
* Default: true

#####################
# SAML settings
#####################

[<saml-authSettings-key>]
* Follow this stanza name with the attribute/value pairs listed below.
* The <authSettings-key> must be one of the values listed in the
* authSettings attribute, specified above in the [authentication] stanza.

fqdn = <string>
* OPTIONAL
* The fully qualified domain name where this splunk instance is running.
* If this value is not specified, Splunk will default to the value specified
  in server.conf.
* If this value is specified and 'http://' or 'https://' prefix is not
  present, splunk will use the ssl setting for splunkweb.
* Splunk will use this information to populate the 'assertionConsumerServiceUrl'.

redirectPort = <port number>
* OPTIONAL
* The port where SAML responses will be sent. Typically, this is the
  web port.
* If internal port redirection is needed, set this port and the
  'assertionconsumerServiceUrl' in the AuthNRequest will contain this port
  instead of the splunkweb port.
* To prevent any port information to be appended in the
  'assertionConsumerServiceUrl' attribute, set this to 0.

idpSSOUrl = <url>
* REQUIRED
* The protocol endpoint on the IDP (Identity Provider) where the
  AuthNRequests should be sent.
* SAML requests will fail if this information is missing.

idpAttributeQueryUrl = <url>
* OPTIONAL
* The protocol endpoint on the IDP (Identity Provider) where the attribute
  query requests should be sent.
* Attribute queries can be used to get the latest 'role' information,
  if there is support for Attribute queries on the IDP.
* When this setting is absent, Splunk will cache the role information from the saml
  assertion and use it to run saved searches.

idpCertPath = <Pathname>
* OPTIONAL
* This setting is required if 'signedAssertion' is set to true.
* This value is relative to $SPLUNK_HOME/etc/auth/idpCerts.
* The value for this setting can be the name of the certificate file or a directory.
* If it is empty, Splunk will automatically verify with certificates in all subdirectories
  present in $SPLUNK_HOME/etc/auth/idpCerts.
* If the saml response is to be verified with a IDP (Identity Provider) certificate that
  is self signed, then this setting holds the filename of the certificate.
* If the saml response is to be verified with a certificate that is a part of a
  certificate chain(root, intermediate(s), leaf), create a subdirectory and place the
  certificate chain as files in the subdirectory.
* If there are multiple end certificates, create a subdirectory such that, one subdirectory
  holds one certificate chain.
* If multiple such certificate chains are present, the assertion is considered verified,
  if validation succeeds with any certifcate chain.
* The file names within a certificate chain should be such that root certificate is alphabetically
  before the intermediate which is alphabetically before of the end cert.
  ex. cert_1.pem has the root, cert_2.pem has the first intermediate cert, cert_3.pem has the second
      intermediate certificate and cert_4.pem has the end certificate.

idpSLOUrl = <url>
* OPTIONAL
* The protocol endpoint on the IDP (Identity Provider) where a SP
  (Service Provider) initiated Single logout request should be sent.

errorUrl = <url>
* OPTIONAL
* The url to be displayed for a SAML error. Errors may be due to
  erroneous or incomplete configuration in either the IDP or Splunk.
  This url can be absolute or relative. Absolute url should follow pattern 
  <protocol>:[//]<host> e.g. https://www.external-site.com.
  Relative urls should start with '/'. A relative url will show up as an 
  internal link of the splunk instance, e.g. https://splunkhost:port/relativeUrlWithSlash

errorUrlLabel = <string>
* OPTIONAL
* Label or title of the content pointed to by errorUrl.

entityId = <string>
* REQUIRED
* The entity id for SP connection as configured on the IDP.

issuerId = <string>
* REQUIRED
* The unique identifier of the identity provider.
  The value of this setting corresponds to attribute "entityID" of
  "EntityDescriptor" node in IdP metadata document.
* If you configure SAML using IdP metadata, this field will be extracted from
  the metadata.
* If you configure SAML manually, then you must configure this setting.
* When Splunk software tries to verify the SAML response, the issuerId
  specified here must match the 'Issuer' field in the SAML response. Otherwise,
  validation of the SAML response will fail.

signAuthnRequest = [ true | false ]
* OPTIONAL
* This tells Splunk whether to sign AuthNRequests.
* Defaults to true.

signedAssertion = [true|false]
* OPTIONAL
* This tells Splunk if the SAML assertion has been signed by the IDP
* If set to false, Splunk will not verify the signature of the assertion
  using the certificate of the IDP.
* Currently, we accept only signed assertions.
* Defaults to true.

attributeQuerySoapPassword = <password>
* OPTIONAL
* This setting is required if 'attributeQueryUrl' is specified.
* Attribute query requests are made using SOAP using basic authentication
* The password to be used when making an attribute query request.
* This string will obfuscated upon splunkd startup.

attributeQuerySoapUsername = <string>
* OPTIONAL
* This setting is required if 'attributeQueryUrl' is specified.
* Attribute Query requests are made using SOAP using basic authentication
* The username to be used when making an attribute query request.

attributeQueryRequestSigned = [ true | false ]
* OPTIONAL
* Specifies whether to sign attribute query requests.
* Defaults to true

attributeQueryResponseSigned = [ true | false ]
* OPTIONAL
* Specifies whether attribute query responses are signed.
* If set to false, Splunk will not verify the signature in the response
  using the certificate of the IDP.
* Defaults to true.

redirectAfterLogoutToUrl = <url>
* OPTIONAL
* The user will be redirected to this url after logging out of Splunk.
* If this is not specified and a idpSLO is also missing, the user will be
  redirected to splunk.com after logout.

defaultRoleIfMissing = <splunk role>
* OPTIONAL
* If the IDP does not return any AD groups or splunk roles as a part of the
  assertion, we will use this value if provided.

skipAttributeQueryRequestForUsers = <comma separated list of users>
* OPTIONAL
* To skip attribute query requests being sent to the IDP for certain users,
  add them here.
* By default, attribute query requests will be skipped for local users.
* For non-local users, use this in conjunction with 'defaultRoleIfMissing'.

maxAttributeQueryThreads = <int>
* OPTIONAL
* Defaults to 2, max is 10
* Number of threads to use to make attribute query requests.
* Changes to this will require a restart to take effect.

maxAttributeQueryQueueSize = <int>
* OPTIONAL
* Defaults to 50
* The number of attribute query requests to queue, set to 0 for infinite
  size.
* Changes to this will require a restart to take effect.

attributeQueryTTL = <ttl in seconds>
* OPTIONAL
* Determines the time for which Splunk will cache the user and role
  information.
* Once the ttl expires, Splunk will make an attribute query request to
  retrieve the role information.
* Default ttl if not specified, is 3600 seconds.

allowSslCompression = [ true | false ]
* OPTIONAL
* If set to true, the server will allow clients to negotiate SSL-layer 
  data compression.
* If not set, defaults to the setting in server.conf.

cipherSuite = <cipher suite string>
* OPTIONAL
* If set, Splunk uses the specified cipher string for the HTTP server.
* If not set, defaults to the setting in server.conf.
* Attribute query requests might fail if the IDP requires a relaxed
  ciphersuite.
* Use "openssl s_client -cipher 'TLSv1+HIGH:@STRENGTH' -host <IDP host> -port 443" 
  to determine if splunk can connect to the IDP

sslVersions = <versions_list>
* OPTIONAL
* Comma-separated list of SSL versions to support.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2"
* If not set, defaults to the setting in server.conf.

sslCommonNameToCheck = <commonName>
* OPTIONAL
* If this value is set, and 'sslVerifyServerCert' is set to true,
  splunkd will limit most outbound HTTPS connections to hosts which use
  a cert with this common name.
* If not set, Splunk uses the setting specified in server.conf.

sslAltNameToCheck = <alternateName1>, <alternateName2>, ...
* OPTIONAL
* If this value is set, and 'sslVerifyServerCert' is set to true,
  splunkd will also be willing to verify certificates which have a so-called
  "Subject Alternate Name" that matches any of the alternate names in this
  list.
* If not set, Splunk uses the setting specified in server.conf.

ecdhCurveName = <string>
* DEPRECATED; use 'ecdhCurves' instead.
* ECDH curve to use for ECDH key negotiation.
* If not set, Splunk uses the setting specified in server.conf.

ecdhCurves = <comma separated list of ec curves>
* ECDH curves to use for ECDH key negotiation.
* The curves should be specified in the order of preference.
* The client sends these curves as a part of Client Hello.
* The server supports only the curves specified in the list.
* We only support named curves specified by their SHORT names.
  (see struct ASN1_OBJECT in asn1.h)
* The list of valid named curves by their short/long names can be obtained
  by executing this command:
  $SPLUNK_HOME/bin/splunk cmd openssl ecparam -list_curves
* Default is empty string.
* e.g. ecdhCurves = prime256v1,secp384r1,secp521r1
* If not set, Splunk uses the setting specified in server.conf.

clientCert = <path>
* Full path to the client certificate PEM format file.
* Certificates are auto-generated upon first starting Splunk.
* You may replace the auto-generated certificate with your own.
* Default is $SPLUNK_HOME/etc/auth/server.pem.
* If not set, Splunk uses the setting specified in
  server.conf/[sslConfig]/serverCert.

sslKeysfile = <filename>
* DEPRECATED; use 'clientCert' instead.
* File is in the directory specified by 'caPath' (see below).
* Default is server.pem.

sslPassword = <password>
* Optional server certificate password.
* If unset, Splunk uses the setting specified in server.conf.
* Default is password.

sslKeysfilePassword = <password>
* DEPRECATED; use 'sslPassword' instead.

caCertFile = <filename>
* OPTIONAL
* Public key of the signing authority.
* Default is cacert.pem.
* If not set, Splunk uses the setting specified in server.conf.

caPath = <path>
* DEPRECATED; use absolute paths for all certificate files.
* If certificate files given by other settings in this stanza are not absolute
  paths, then they will be relative to this path.
* Default is $SPLUNK_HOME/etc/auth.

sslVerifyServerCert = <bool>
* OPTIONAL
* Used by distributed search: when making a search request to another
  server in the search cluster.
* If not set, Splunk uses the setting specified in server.conf.

blacklistedAutoMappedRoles = <comma separated list of roles>
* OPTIONAL
* Comma separated list of splunk roles that should be blacklisted
  from being auto-mapped by splunk from the IDP Response.

blacklistedUsers = <comma separated list of user names>
* OPTIONAL
* Comma separated list of user names from the IDP response to be
  blacklisted by splunk platform.

nameIdFormat = <string>
* OPTIONAL
* If supported by IDP, while making SAML Authentication request this value can
  be used to specify the format of the Subject returned in SAML Assertion.

ssoBinding = <string>
* OPTIONAL
* This is the binding that will be used when making a SP-initiated saml request.
* Acceptable options are 'HTTPPost' and 'HTTPRedirect'
* Defaults to 'HTTPPost'
* This binding must match the one configured on the IDP.

sloBinding = <string>
* OPTIONAL
* This is the binding that will be used when making a logout request or sending a logout
* response to complete the logout workflow.
* Acceptable options are 'HTTPPost' and 'HTTPRedirect'
* Defaults to 'HTTPPost'
* This binding must match the one configured on the IDP.

signatureAlgorithm = RSA-SHA1 | RSA-SHA256
* OPTIONAL
* Defaults to RSA-SHA1.
* Specifies the signature algorithm that will be used for outbound SAML messages,
  for example, SP-initiated SAML request.
* This setting only used when 'signAuthnRequest' is set to 'true'.
* This setting is applicable for both HTTP POST and HTTP Redirect binding.
* RSA-SHA1 corresponds to 'http://www.w3.org/2000/09/xmldsig#rsa-sha1'.
* RSA-SHA256 corresponds to 'http://www.w3.org/2001/04/xmldsig-more#rsa-sha256'.
* This will be sent as a part of 'sigAlg'.
* For improved security, set it to 'RSA-SHA256'.

inboundSignatureAlgorithm = RSA-SHA1;RSA-SHA256
* Allows only SAML responses that are signed using any one of the specified
  algorithms.
* This setting is applicable for both HTTP POST and HTTP Redirect binding.
* Provide a semicolon-separated list of signature algorithms for the SAML responses
  that you want Splunk Web to accept. Splunk software rejects any SAML responses
  that are not signed by the specified algorithms.
* For improved security, set it to 'RSA-SHA256'.
* OPTIONAL
* Defaults to 'RSA-SHA1;RSA-SHA256'.

replicateCertificates = <boolean>
* OPTIONAL
* Enabled by default, IdP certificate files will be replicated across search head cluster setup.
* If disabled, IdP certificate files needs to be replicated manually across SHC or else
  verification of SAML signed assertions will fail.
* This setting will have no effect if search head clustering is disabled.

allowPartialSignatures = <boolean>
* OPTIONAL
* When enabled, the Splunk authentication system only requires the SAML assertion block to be
  signed (but not necessarily the entire SAML response).
* When disabled, the entire SAML response must be signed for the login to succeed.
* Defaults to 'true'

#####################
# Map roles
#####################

[roleMap_<saml-authSettings-key>]
* The mapping of Splunk roles to SAML groups for the SAML stanza specified
  by <authSettings-key>
* If a SAML group is not explicitly mapped to a Splunk role, but has
  same name as a valid Splunk role then for ease of configuration, it is
  auto-mapped to that Splunk role.
* Follow this stanza name with several Role-to-Group(s) mappings as defined
  below.

<Splunk RoleName> = <SAML group string>
* Maps a Splunk role (from authorize.conf) to SAML groups
* This SAML group list is semicolon delimited (no spaces).
* List several of these attribute value pairs to map several Splunk roles to
  SAML Groups.
* If role mapping is not specified, Splunk expects Splunk roles in the
  assertion and attribute query response returned from the IDP.

#####################
# SAML User Roles Map
#####################

[userToRoleMap_<saml-authSettings-key>]
* The mapping of SAML user to Splunk roles, realname and email,
  for the SAML stanza specified by <authSettings-key>
* Follow this stanza name with several User-to-Role::Realname::Email mappings
  as defined below.
* The stanza is used only when the IDP does not support Attribute Query Request

<SAML User> = <Splunk Roles string>::<Realname>::<Email>
* Maps a SAML user to Splunk role(from authorize.conf), Realname and Email
* The Splunk Roles string is semicolon delimited (no spaces).
* The Splunk Roles string, Realname and Email are :: delimited (no spaces).

#####################
# Authentication Response Attribute Map
#####################

[authenticationResponseAttrMap_SAML]
* Splunk expects email, real name and roles to be returned as SAML
  Attributes in SAML assertion. This stanza can be used to map attribute names
  to what Splunk expects. These are optional settings and are only needed for
  certain IDPs.

role = <string>
* OPTIONAL
* Attribute name to be used as role in SAML Assertion.
* Default is "role"

realName = <string>
* OPTIONAL
* Attribute name to be used as realName in SAML Assertion.
* Default is "realName"

mail = <string>
* OPTIONAL
* Attribute name to be used as email in SAML Assertion.
* Default is "mail"

#####################
# Settings for Proxy SSO mode
#####################

[roleMap_proxySSO]

* The mapping of Splunk roles to groups passed in headers from proxy server.
* If a group is not explicitly mapped to a Splunk role, but has
  same name as a valid Splunk role then for ease of configuration, it is
  auto-mapped to that Splunk role.
* Follow this stanza name with several Role-to-Group(s) mappings as defined
  below.

<Splunk RoleName> = <Group string>
* Maps a Splunk role (from authorize.conf) to groups
* This group list is semicolon delimited (no spaces).
* List several of these attribute value pairs to map several Splunk roles to
  Groups
* If role mapping is not specified, user is logged in with default User role.

[userToRoleMap_proxySSO]
* The mapping of ProxySSO user to Splunk roles
* Follow this stanza name with several User-to-Role(s) mappings as defined
  below.

<ProxySSO User> = <Splunk Roles string>
* Maps a ProxySSO user to Splunk role (from authorize.conf)
* This Splunk Role list is semicolon delimited (no spaces).

[proxysso-authsettings-key]
* Follow this stanza name with the attribute/value pairs listed below.

defaultRoleIfMissing = <splunk role>
* OPTIONAL
* If splunk roles cannot be determined based on role mapping, use default configured
* splunk role.

blacklistedAutoMappedRoles = <comma separated list of roles>
* OPTIONAL
* Comma separated list of splunk roles that should be blacklisted
  from being auto-mapped by splunk from the proxy server headers.

blacklistedUsers = <comma separated list of user names>
* OPTIONAL
* Comma separated list of user names from the proxy server headers to be
  blacklisted by splunk platform.

#####################
# Secret Storage
#####################

[secrets]

disabled = <bool>
* Toggles integration with platform-provided secret storage facilities.
* Defaults to false if Common Criteria mode is enabled.
* Defaults to true if Common Criteria mode is disabled.
* NOTE: Splunk plans to submit Splunk Enterprise for Common Criteria
  evaluation. Splunk does not support using the product in Common
  Criteria mode until it has been certified by NIAP. See the "Securing
  Splunk Enterprise" manual for information on the status of Common
  Criteria certification.

filename = <filename>
* Designates a Python script that integrates with platform-provided
  secret storage facilities, like the GNOME keyring.
* <filename> should be the name of a Python script located in one of the
  following directories:
    $SPLUNK_HOME/etc/apps/*/bin
    $SPLUNK_HOME/etc/system/bin
    $SPLUNK_HOME/etc/searchscripts
* <filename> should be a pure basename; it should contain no path separators.
* <filename> should end with a .py file extension.

namespace = <string>
* Use an instance-specific string as a namespace within secret storage.
* When using the GNOME keyring, this namespace is used as a keyring name.
* If multiple Splunk instances must store separate sets of secrets within the
  same storage backend, this value should be customized to be unique for each
  Splunk instance.
* Defaults to "splunk".

#####################
# Duo MFA vendor settings
#####################
[<duo-externalTwoFactorAuthSettings-key>]
* <duo-externalTwoFactorAuthSettings-key> must be the value listed in the
  externalTwoFactorAuthSettings attribute, specified above in the [authentication]
  stanza.
* This stanza contains Duo specific multifactor authentication settings and will be
  activated only when externalTwoFactorAuthVendor is Duo.
* All the below attributes except appSecretKey would be provided by Duo.

apiHostname = <string>
* REQUIRED
* Duo's API endpoint which performs the actual multifactor authentication.
* e.g. apiHostname = api-xyz.duosecurity.com

integrationKey = <string>
* REQUIRED
* Duo's integration key for splunk. Must be of size = 20.
* Integration key will be obfuscated before being saved here for security.

secretKey = <string>
* REQUIRED
* Duo's secret key for splunk. Must be of size = 40.
* Secret key will be obfuscated before being saved here for security.

appSecretKey = <string>
* REQUIRED
* Splunk application specific secret key which should be random and locally generated.
* Must be atleast of size = 40 or longer.
* This secret key would not be shared with Duo.
* Application secret key will be obfuscated before being saved here for security.

failOpen = <bool>
* OPTIONAL
* Defaults to false if not set.
* If set to true, Splunk will bypass Duo multifactor authentication when the service is
  unavailable.

timeout = <int>
* OPTIONAL
* It determines the connection timeout in seconds for the outbound duo HTTPS connection.
* If not set, Splunk will use its default HTTPS connection timeout which is 12 seconds.

sslVersions = <versions_list>
* OPTIONAL
* Comma-separated list of SSL versions to support for incoming connections.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* If not set, Splunk uses the sslVersions provided in server.conf

cipherSuite = <cipher suite string>
* OPTIONAL
* If set, Splunk uses the specified cipher string for the HTTP server.
* If not set, Splunk uses the cipher string provided in server.conf

ecdhCurves = <comma separated list of ec curves>
* OPTIONAL
* ECDH curves to use for ECDH key negotiation.
* If not set, Splunk uses the ecdh curve names provided in server.conf

sslVerifyServerCert = <bool>
* OPTIONAL
* Defaults to false if not set.
* If this is set to true, you should make sure that the server that is
  being connected to is a valid one (authenticated). Both the common
  name and the alternate name of the server are then checked for a
  match if they are specified in this configuration file.  A
  certificiate is considered verified if either is matched.

sslCommonNameToCheck = <commonName1>, <commonName2>, ...
* OPTIONAL
* Not set by default.
* If this value is set, Splunk will limit outbound duo HTTPS connections
  to host which use a cert with one of the listed common names.
* sslVerifyServerCert must be set to true for this setting to work.

sslAltNameToCheck =  <alternateName1>, <alternateName2>, ...
* OPTIONAL
* Not set by default.
* If this value is set, Splunk will limit outbound duo HTTPS connections
  to host which use a cert with one of the listed alternate names.
* sslVerifyServerCert must be set to true for this setting to work.

sslRootCAPath = <path>
* OPTIONAL
* Not set by default.
* The <path> must refer to full path of a PEM format file containing one or more
  root CA certificates concatenated together.
* This Root CA must match the CA in the certificate chain of the SSL certificate
  returned by duo server.

useClientSSLCompression = <bool>
* OPTIONAL
* If set to true on client side, compression is enabled between the server and client
  as long as the server also supports it.
* If not set, Splunk uses the client SSL compression setting provided in server.conf

#####################
# RSA MFA vendor settings
#####################
[<rsa-externalTwoFactorAuthSettings-key>]
* <rsa-externalTwoFactorAuthSettings-key> must be the value listed in the
  externalTwoFactorAuthSettings attribute, specified above in the [authentication]
  stanza.
* This stanza contains RSA specific multifactor authentication settings and will be
  activated only when externalTwoFactorAuthVendor is RSA.
* All the below attributes can be obtained from RSA Authentication Manager 8.2 SP1.


authManagerUrl = <string>
* REQUIRED
* URL of REST endpoint of RSA Authentication Manager
* Splunk will send authentication requests to this URL. 
* URL should be https based. Splunk will not support communication over http.

accessKey = <string>
* REQUIRED
* Access key needed by Splunk to communicate with RSA Authentication Manager. 

clientId = <string>
* REQUIRED
* Agent name created on RSA Authentication Manager is clientId.

failOpen = <bool>
* OPTIONAL
* If true, allow login in case authentication server is unavailable.
* Default: false.

timeout = <int>
* OPTIONAL
* It determines the connection timeout in seconds for the outbound HTTPS connection.
* Default: 5.

messageOnError = <string>
* OPTIONAL
* Message that will be shown to user in case of login failure.
* You can specify contact of admin or link to diagnostic page.

sslVersions = <versions_list>
* OPTIONAL
* Comma-separated list of SSL versions to support for incoming connections.
* The versions available are "ssl3", "tls1.0", "tls1.1", and "tls1.2".
* If not set, Splunk uses the 'sslVersions' specified in server.conf
* Default: tls1.2

cipherSuite = <cipher suite string>
* OPTIONAL
* If set, Splunk uses the specified cipher string for the HTTP server.
* If not set, Splunk uses the 'cipherSuite' specified in server.conf

ecdhCurves = <comma separated list of ec curves>
* OPTIONAL
* ECDH curves to use for ECDH key negotiation.
* If not set, Splunk uses the 'ecdhCurves' specified in server.conf

sslVerifyServerCert = <bool>
* OPTIONAL
* If this is set to true, you should make sure that the server that is
  being connected to is a valid one (authenticated). Both the common
  name and the alternate name of the server are then checked for a
  match if they are specified in this configuration file.  A
  certificiate is considered verified if either is matched.
* Default: true.

sslCommonNameToCheck = <commonName1>, <commonName2>, ...
* OPTIONAL
* Not set by default.
* If this value is set, Splunk will limit outbound RSA HTTPS connections
  to host which use a cert with one of the listed common names.
* 'sslVerifyServerCert' must be set to true for this setting to work.

sslAltNameToCheck =  <alternateName1>, <alternateName2>, ...
* OPTIONAL
* Not set by default.
* If this value is set, Splunk will limit outbound RSA HTTPS connections
  to host which use a cert with one of the listed alternate names.
* 'sslVerifyServerCert' must be set to true for this setting to work.

sslRootCAPath = <path>
* REQUIRED
* Not set by default.
* The <path> must refer to full path of a PEM format file containing one or more
  root CA certificates concatenated together.
* This Root CA must match the CA in the certificate chain of the SSL certificate
  returned by RSA server.

sslVersionsForClient = <versions_list>
* OPTIONAL
* Comma-separated list of SSL versions to support for outgoing HTTP connections.
* If not set, Splunk uses the 'sslVersionsForClient' specified in server.conf
* Default: tls1.2

replicateCertificates = <boolean>
* OPTIONAL
* If enabled, RSA certificate files will be replicated across search head cluster setup.
* If disabled, RSA certificate files need to be replicated manually across SHC or else
  2FA verification will fail.
* This setting will have no effect if search head clustering is disabled.
* Default: true

enableMfaAuthRest = <boolean>
* Determines whether or not splunkd requires RSA two-factor authentication
  against REST endpoints.
* When two-factor authentication is enabled for REST endpoints, either you
  must log in to the Splunk instance with a valid RSA passcode, or requests
  to those endpoints must include a valid token in the following format,
  for example: "curl -k -u <username>:<password>:<token> -X GET <resource>"
* If set to "true", splunkd requires RSA REST two-factor authentication.
* If set to "false", splunkd does not require REST two-factor authentication.
* Optional.
* Default: false
