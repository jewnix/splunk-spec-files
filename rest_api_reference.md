# Splunk REST API Reference (version 10.2)

Source: https://help.splunk.com/en/splunk-enterprise/rest-api-reference/10.2/

## Endpoint Groups

- [Access](#access) (26 endpoints)
- [Application](#application) (8 endpoints)
- [Cluster](#cluster) (70 endpoints)
- [Configuration](#configuration) (2 endpoints)
- [Deployment](#deployment) (24 endpoints)
- [Federated Search](#federated-search) (10 endpoints)
- [Input](#input) (53 endpoints)
- [Introspection](#introspection) (41 endpoints)
- [Knowledge](#knowledge) (38 endpoints)
- [Kv Store](#kv-store) (13 endpoints)
- [License](#license) (14 endpoints)
- [Metrics Catalog](#metrics-catalog) (5 endpoints)
- [Output](#output) (9 endpoints)
- [Search](#search) (50 endpoints)
- [System](#system) (10 endpoints)
- [Workload Management](#workload-management) (10 endpoints)

---

## Access

### `/services/authentication/providers/LDAP`

Access or create LDAP authentication strategies on a server in your deployment.

#### GET

Access LDAP configurations strategies.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `strategy` | Name of LDAP configuration strategy |  |

#### POST

Create an LDAP strategy.

### `/services/authentication/providers/LDAP/{LDAP_strategy_name}`

Access, update, or delete the {LDAP_strategy_name} strategy.

#### POST

Update an existing LDAP strategy.

#### DELETE

Delete an existing LDAP strategy.

### `/services/authentication/providers/LDAP/{LDAP_strategy_name}/enable`

#### POST

Enable the {LDAP_strategy_name} LDAP strategy.

### `/services/authentication/providers/LDAP/{LDAP_strategy_name}/disable`

#### POST

Disable the {LDAP_strategy_name} LDAP strategy.

### `/services/admin/metrics-reload/_reload`

Use this endpoint to reload the metrics processor after updating a metrics-related configuration.

#### POST

Reload the metrics processor.

### `/services/admin/replicate-SAML-certs`

Replicate SAML IdP certificates across a search head cluster.

#### POST

Usage details

### `/services/authentication/providers/SAML`

Access and create SAML configurations.

#### GET

Access SAML configurations.

#### POST

Create a new SAML configuration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `allowSslCompression` | Indicates whether ssl data compression is enabled. |  |
| `attributeAliasMail` | Specifies which SAML attribute is mapped to 'email'. Defaults to 'email'. |  |
| `attributeAliasRealName` | Specifies which SAML attribute maps to 'realName'. Defaults to realName . |  |
| `attributeAliasRole` | Specifies which SAML attribute maps to role . Defaults to role . |  |
| `attributeQueryRequestSigned` | Indicates whether Attribute Queries should be signed. |  |
| `attributeQueryResponseSigned` | Indicates whether Attribute Query responses should be signed. |  |
| `attributeQuerySoapPassword` | Credentials for making Attribute Query using SOAP over HTTP. |  |
| `attributeQuerySoapUsername` | Credentials for making Attribute Query using SOAP over HTTP. |  |
| `attributeQueryTTL` | ttl (time to live) for the Attribute Query credentials cache. |  |
| `blacklistedAutoMappedRoles` | Comma separated list of Splunk roles that should be blacklisted from being auto-mapped from the IDP Response. |  |
| `blacklistedUsers` | Comma separated list of user names from the IDP response to be blacklisted by Splunk software. |  |
| `caCertFile` | File path for CA certificate. For example, /home/user123/saml-install/etc/auth/server.pem |  |
| `cipherSuite` | Ciphersuite for making Attribute Queries using ssl. For example, TLSv1+HIGH:@STRENGTH . |  |
| `defaultRoleIfMissing` | Default role to use if no role is returned in a SAML response. |  |
| `ecdhCurves` | EC curves for ECDH/ECDHE key exchange - ssl setting. |  |
| `entityId` | Required . Unique id preconfigured by the IdP. |  |
| `errorUrL` | URL to display for a SAML error. Errors may be due to incorrect or incomplete configuration in either the IDP or the Splunk deployment. |  |
| `errorUrlLabel` | Label or title of the content to which errorUrl points. Defaults to Click here to resolve SAML error. . |  |
| `fqdn` | Load balancer url. |  |
| `idpAttributeQueryUrl` | IdP attribute query url where SAML attribute queries are sent. |  |
| `idpCertPath` | Path for IdP certificate. |  |
| `idpMetadataFile` | Full path to idpMetadata on disk. Used to retrieve IdP information such as idpSLOUrl, idpSSOUrl, and signing certificate. |  |
| `idpSLOUrl` | IdP sso url where SAML SSO requests are sent. |  |
| `idpSSOUrl` | Required . IdP SSO url where SAML SLO requests are sent. |  |
| `nameIdFormat` | Specifies how subject is identified in SAML Assertion. Defaults to CODE Copy urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified Override it when using Azure AD as an IDP and set it to CODE Copy urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress |  |
| `redirectAfterLogoutToUrl` | Redirect URL after user logout If no SLO URL is configured. |  |
| `redirectPort` | Port where SAML responses are sent. Typically, this is the web port. Set this port if internal port redirection is needed. The assertionconsumerServiceUrl in the AuthNRequest uses the set port instead of the splunkweb port. To prevent any port information being appended to the assertionConsumerServiceUrl , set to 0 . |  |
| `signAuthnRequest` | Indicates whether to sign authentication requests. |  |
| `signatureAlgorithm` | Applicable only for redirect binding. Indicates the signature algorithm used for a SP-initiated SAML request when signedAuthnRequest is set to true . Possible values are: RSA-SHA1 (default) corresponds to http://www.w3.org/2000/09/xmldsig#rsa-sha1 RSA-SHA256 corresponds to http://www.w3.org/2001/04/xmldsig-more#rsa-sha256 |  |
| `signedAssertion` | Indicates whether to sign SAML assertions. |  |
| `skipAttributeQueryRequestForUsers` | Used in conjunction with defaultRoleIFMissing . Indicates whether to skip Attribute Queries for some users. |  |
| `sloBinding` | Binding used when making a logout request or sending a logout response to complete the logout workflow. Possible values are HTTPPost (default) and HTTPRedirect . This binding must match the binding configured on the IDP. |  |
| `sslAltNameToCheck` | Alternate name to check in the peer certificate. |  |
| `sslCommonNameToCheck` | Common name to check in the peer certificate. |  |
| `sslKeysfile` | Location of service provider private key. |  |
| `sslKeysfilePassword` | SSL password. |  |
| `sslVerifyServerCert` | Indicates whether to verify peer certificate. |  |
| `sslVersions` | SSL versions. |  |
| `ssoBinding` | Binding used when making a SP-initiated SAML request. Possible values are HTTPPost (default) and HTTPRedirect . This binding must match the binding configured on the IDP. |  |

### `/services/authentication/providers/SAML/{stanza_name}`

#### GET

Access a SAML configuration.

#### POST

Update a SAML configuration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `allowSslCompression` | Indicates whether ssl data compression is enabled. |  |
| `attributeAliasMail` | Specifies which SAML attribute is mapped to 'email'. Defaults to 'email'. |  |
| `attributeAliasRealName` | Specifies which SAML attribute maps to 'realName'. Defaults to realName . |  |
| `attributeAliasRole` | Specifies which SAML attribute maps to role . Defaults to role . |  |
| `attributeQueryRequestSigned` | Indicates whether Attribute Queries should be signed. |  |
| `attributeQueryResponseSigned` | Indicates whether Attribute Query responses should be signed. |  |
| `attributeQuerySoapPassword` | Credentials for making Attribute Query using SOAP over HTTP. |  |
| `attributeQuerySoapUsername` | Credentials for making Attribute Query using SOAP over HTTP. |  |
| `attributeQueryTTL` | ttl (time to live) for the Attribute Query credentials cache. |  |
| `blacklistedAutoMappedRoles` | Comma separated list of Splunk roles that should be blacklisted from being auto-mapped from the IDP Response. |  |
| `blacklistedUsers` | Comma separated list of user names from the IDP response to be blacklisted by Splunk software. |  |
| `caCertFile` | File path for CA certificate. For example, /home/user123/saml-install/etc/auth/server.pem |  |
| `cipherSuite` | Ciphersuite for making Attribute Queries using ssl. For example, TLSv1+HIGH:@STRENGTH . |  |
| `defaultRoleIfMissing` | Default role to use if no role is returned in a SAML response. |  |
| `ecdhCurves` | EC curves for ECDH/ECDHE key exchange - ssl setting. |  |
| `entityId` | Required . Unique id preconfigured by the IdP. |  |
| `errorUrL` | URL to display for a SAML error. Errors may be due to incorrect or incomplete configuration in either the IDP or the Splunk deployment. |  |
| `errorUrlLabel` | Label or title of the content to which errorUrl points. Defaults to Click here to resolve SAML error. . |  |
| `fqdn` | Load balancer url. |  |
| `idpAttributeQueryUrl` | IdP attribute query url where SAML attribute queries are sent. |  |
| `idpCertPath` | Path for IdP certificate. |  |
| `idpSLOUrl` | IdP sso url where SAML SSO requests are sent. |  |
| `idpSSOUrl` | Required . IdP SSO url where SAML SLO requests are sent. |  |
| `nameIdFormat` | Specifies how subject is identified in SAML Assertion. Defaults to CODE Copy urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified Override it when using Azure AD as an IDP and set it to CODE Copy urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress |  |
| `redirectAfterLogoutToUrl` | Redirect URL after user logout If no SLO URL is configured. |  |
| `redirectPort` | Port where SAML responses are sent. Typically, this is the web port. Set this port if internal port redirection is needed. The assertionconsumerServiceUrl in the AuthNRequest uses the set port instead of the splunkweb port. To prevent any port information being appended to the assertionConsumerServiceUrl , set to 0 . |  |
| `signAuthnRequest` | Indicates whether to sign authentication requests. |  |
| `signatureAlgorithm` | Applicable only for redirect binding. Indicates the signature algorithm used for a SP-initiated SAML request when signedAuthnRequest is set to true . Possible values are: RSA-SHA1 (default) corresponds to http://www.w3.org/2000/09/xmldsig#rsa-sha1 RSA-SHA256 corresponds to http://www.w3.org/2001/04/xmldsig-more#rsa-sha256 |  |
| `signedAssertion` | Indicates whether to sign SAML assertions. |  |
| `skipAttributeQueryRequestForUsers` | Used in conjunction with defaultRoleIFMissing . Indicates whether to skip Attribute Queries for some users. |  |
| `sloBinding` | Binding used when making a logout request or sending a logout response to complete the logout workflow. Possible values are HTTPPost (default) and HTTPRedirect . This binding must match the binding configured on the IDP. |  |
| `sslAltNameToCheck` | Alternate name to check in the peer certificate. |  |
| `sslCommonNameToCheck` | Common name to check in the peer certificate. |  |
| `sslKeysfile` | Location of service provider private key. |  |
| `sslKeysfilePassword` | SSL password. |  |
| `sslVerifyServerCert` | Indicates whether to verify peer certificate. |  |
| `sslVersions` | SSL versions. |  |
| `ssoBinding` | Binding used when making a SP-initiated SAML request. Possible values are HTTPPost (default) and HTTPRedirect . This binding must match the binding configured on the IDP. |  |

### `/services/authentication/providers/SAML/{stanza_name}/enable`

#### POST

Enable a SAML strategy.

### `/services/authentication/providers/SAML/{stanza_name}/disable`

#### POST

Delete a SAML strategy.

### `/services/auth/login`

#### POST

Get a session ID for use in subsequent API calls that require authentication. Optionally, use cookie-based authentication or multifactor authentication.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `cookie` | Boolean, only used value is 1. | To use cookie-based REST auth, pass in cookie=1 . Cookies will only be returned if the cookie parameter is passed in with the value of 1. |
| `password` | String | Required . Current username password. |
| `passcode` | String | Required for users with RSA multifactor authentication . The passcode associated with RSA multifactor authentication. This is a combination of the user's RSA token and PIN. |
| `username` | String | Required . Authenticated session owner name. |

### `/services/authentication/current-context`

Get the authenticated session owner username.

#### GET

Get user information for the current context.

### `/services/authentication/httpauth-tokens`

List currently active session IDs and users.

#### GET

List currently active session IDs/users.

### `/services/authentication/httpauth-tokens/{name}`

#### DELETE

Delete the session associated with this session ID.

#### GET

Get session information.

### `/services/authentication/users`

#### GET

List current users.

#### POST

Create a user.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `createrole` | Boolean | Flag to indicate that a new role should be created for the user. If set to "true", the new role user-<name> is created and assigned to the user. The <name> portion of the new role matches the name parameter value passed in with this POST request. If set to "false", at least one existing role must be specified using the roles parameter for the POST request. Defaults to "false". |
| `defaultApp` | String | User default app. Overrides the default app inherited from the user roles. |
| `email` | String | User email address. |
| `force-change-pass` | Boolean | Force user to change password indication: true = Force password change. false = Do not force password change. |
| `password` | String | User login password. |
| `realname` | String | Full user name. |
| `restart_background_jobs` | Boolean | Restart background search job that has not completed when Splunk restarts indication: true = Restart job. false = Do not restart job. |
| `roles` | String | Role to assign to this user. To assign multiple roles, pass in each role using a separate roles parameter value. For example, -d roles="role1", -d roles="role2" . At least one existing role is required if you are not using the createrole parameter to create a new role for the user. If you are using createrole to create a new role, you can optionally use this parameter to specify additional roles to assign to the user. |
| `tz` | String | User timezone. |

### `/services/authentication/users/{name}`

Access and update user information or delete the {name} > user.

#### DELETE

Remove the specified user from the system.

#### GET

Return information for the specified user.

#### POST

Update the specified user.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `defaultApp` | String | User default app. This overrides the default app inherited from the user roles. |
| `email` | String | User email address. |
| `force-change-pass` | Boolean | Indicates whether to force user password change. true = Force password change. false = Do not force password change. |
| `oldpassword` | String | Old user login password. Only required if using the password parameter to change the current user's password. |
| `password` | String | Required . User login password. To change the user password, enter the new user login password here. To change the current user's password, also supply the old password in the oldpassword parameter. |
| `realname` | String | Full user name. |
| `restart_background_jobs` | Boolean | Indicates whether to restart background search job that has not completed when the Splunk deployment restarts. true = Restart job. false = Do not restart job. |
| `roles` | String | Role to assign to this user. To assign multiple roles, pass in each role using a separate roles parameter value. For example, -d roles="role1", -d roles="role2" . At least one existing role is required if you are not using the createrole parameter to create a new role for the user. If you are using createrole to create a new role, you can optionally use this parameter to specify additional roles to assign to the user. |
| `tz` | String | User timezone. |

### `/services/authorization/capabilities`

Access system capabilities.

#### GET

List system capabiilities.

### `/services/authorization/fieldfilters`

Create a field filter or get a list of field filters. See Protect PII, PHI, and other sensitive data with field filters in Securing Splunk Platform .

#### GET

List all field filters. To use GET with this endpoint, you must be a member of the admin, sc_admin, or power user role.

#### POST

Create a field filter. To use POST with this endpoint, you must be a member of the admin or sc_admin role.

### `/services/authorization/fieldfilters/{name}`

Access, create, or delete properties for the {name} field filter. See Protect PII, PHI, and other sensitive data with field filters in Securing Splunk Platform .

#### DELETE

Delete the specified field filter. To use DELETE with this endpoint, you must be a member of the admin or sc_admin role.

#### GET

Retrieve details about a specific field filter. To use GET with this endpoint, you must be a member of the admin, sc_admin, or power user role.

#### POST

Update the specified field filter with the field values provided. To use POST with this endpoint, you must be a member of the admin or sc_admin role.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.field` | The name of the field to filter for this action. Only one field can be specified per request. |  |
| `action.operator` | The operator for the action. Operators for actions are described as follows: null(): Removes the field value from results of searches to which this filter is applied. sha256(): Computes and returns the secure hash of the value of the field based on the FIPS-compliant SHA-256 (SHA-2 family) hash function. This hash is then used to replace the value of the field wherever it appears in results of searches to which this filter is applied. See Cryptographic functions in the Splunk Cloud Platform Search Reference . sha512(): Computes and returns the secure hash of the value of the field based on the FIPS-compliant SHA-512 (SHA-2 family) hash function. This hash is then used to replace the value of the field wherever it appears in results of searches to which this filter is applied. See Cryptographic functions in the Splunk Cloud Platform Search Reference . <string literal>: Replaces the fieldname value with the specified string wherever the field value appears in results of searches to which this filter is applied. A string literal is a sequence of characters enclosed in double quotation marks (" "). Use backslash ( \ ) to escape the \ and " characters in a string literal. For example, use \\ and \" . sed(<string literal>): For _raw fields. The sed expression acts on searches to which this filter is applied. The sed expression replaces strings in search results that are matched by a regular expression (s) or transliterates characters found in search results with corresponding characters provided by the sed expression (y). A string literal is a sequence of characters enclosed in double quotation marks (" "). Use backslash ( \ ) to escape the \ and " characters in a string literal. For example, use \\ and \" . |  |
| `description = <string>` | Stores a description of the field filter. |  |
| `"index": "One or more index names"` | Specifies an index name or a list of comma-separated index names of the target indexes you want to search that contain the data you want to protect. If an index is not specified, all indexes are searched. |  |
| `limit.key` | The key for the field filter limit, which limits the field filter to events with a specific target host, source, or sourcetype. You can specify only one value. If the limit key is empty, the field filter doesn't apply to events with a specific host, source, or sourcetype. Limit statements that include wildcards or the following operators are not supported: AND, OR. |  |
| `limit.value` | The value for the limit, which is a sequence of characters enclosed in double quotation marks ( " ) that represents the name of one or more hosts, sources, or source types. The limit value can be a value or a list of comma-separated values for the specified limit. |  |
| `"roleExemptions": [ list of exempted roles ]` | A list of field filters from which each role is exempt. If a role is exempt from a field filter, the field filter is not run at search time for any users holding this role. Roles inherit all field filter exemptions from imported roles. You can't remove inherited field filter exemptions. |  |

### `/services/authorization/grantable_capabilities`

Get a list of all capabilities that the current user can grant.

#### GET

List capabilities that the current user can grant.

### `/services/authorization/roles`

#### GET

List all roles and the permissions for each role.

#### POST

Create a user role.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `capabilities` | String | List of capabilities assigned to role. To send multiple capabilities, send this argument multiple times. Roles inherit all capabilities from imported roles. |
| `cumulativeRTSrchJobsQuota` | Number | Maximum number of concurrently running real-time searches that all members of this role can have. Note : If a user belongs to multiple roles then the user first consumes searches from the roles with the largest cumulative search quota. When the quota of a role is completely used up then roles with lower quotas are examined. |
| `cumulativeSrchJobsQuota` | Number | Maximum number of concurrently running searches for all role members. Warning message logged when limit is reached. Note : If a user belongs to multiple roles then the user first consumes searches from the roles with the largest cumulative search quota. When the quota of a role is completely used up then roles with lower quotas are examined. |
| `defaultApp` | String | Specify the folder name of the default app to use for this role. A user-specific default app overrides this. |
| `imported_roles` | String | Specify a role to import attributes from. To import multiple roles, specify them separately. By default a role imports no other roles. Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is the value with the broadest permissions. Default roles admin can_delete power user You can specify additional roles created. |
| `name required` | String | Required . The name of the user role to create. |
| `rtSrchJobsQuota` | Number | Specify the maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit. |
| `srchDiskQuota` | Number | Specifies the maximum disk space in MB that can be used by a user's search jobs. For example, a value of 100 limits this role to 100 MB total. |
| `srchFilter` | String | Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify. In the case that a user has multiple roles with different search filters, they are combined with an OR. The search string can include search fields and the following terms. source host index eventtype sourcetype * OR AND Example: "host=web* OR source=/var/log/*" Note: You can also use the srchIndexesAllowed and srchIndexesDefault parameters to limit the search on indexes. |
| `srchIndexesAllowed` | String | Index that this role has permissions to search. Pass this argument once for each index that you want to specify. These may be wildcarded, but the index name must begin with an underscore to match internal indexes. Search indexes available by default include the following. All internal indexes All non-internal indexes _audit _blocksignature _internal _thefishbucket history main You can also specify other search indexes added to the server. |
| `srchIndexesDefault` | String | For this role, indexes to search when no index is specified. These indexes can be wildcarded, with the exception that '*' does not match internal indexes. To match internal indexes, start with '_'. All internal indexes are represented by '_*'. A user with this role can search other indexes using "index= " For example, "index=special_index". Search indexes available by default include the following. All internal indexes All non-internal indexes _audit _blocksignature _internal _thefishbucket history main other search indexes added to the server |
| `srchJobsQuota` | Number | The maximum number of concurrent searches a user with this role is allowed to run. For users with multiple roles, the maximum quota value among all of the roles applies. |
| `srchTimeWin` | Number | Maximum time span of a search, in seconds. By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to '0', as the 'admin' role does. |

### `/services/authorization/roles/{name}`

Access, create, or delete properties for the {name} role.

#### DELETE

Delete the specified role.

#### GET

Access the specified role.

#### POST

Update the specified role.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `capabilities` | String | List of capabilities assigned to this role. |
| `cumulativeRTSrchJobsQuota` | Number | Maximum number of concurrently running real-time searches for all role members. A warning message is logged when this limit is reached. |
| `cumulativeSrchJobsQuota` | Number | Maximum number of concurrently running searches for all role members. A warning message is logged when this limit is reached. |
| `defaultApp` | String | The folder name for the app to use as the default app for this role. A user-specific default app overrides this. |
| `imported_capabilities` | String | List of capabilities assigned to the role that were made available from imported roles. |
| `imported_roles` | String | Add an imported role one at a time. Importing other roles imports all aspects of that role, such as capabilities and allowed indexes to search. In combining multiple roles, the effective value for each attribute is value with the broadest permissions. |
| `imported_rtSrchJobsQuota` | String | The maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit. imported_rtSrchJObsQuota specifies the quota imported from other roles. |
| `imported_srchDiskQuota` | String | The maximum disk space in MB that can be used by a user's search jobs. For example, 100 limits this role to 100 MB total. imported_rtSrchJObsQuota specifies the quota imported from other roles. |
| `imported_srchFilter` | String | Search string, imported from other roles, that restricts the scope of searches run by this role. Search results for this role show only events that also match this search string. When a user has multiple roles with different search filters, they are combined with an OR . |
| `imported_srchIndexesAllowed` | String | A list of indexes, imported from other roles, that this role has permissions to search. |
| `imported_srchIndexesDefault` | String | A list of indexes, imported from other roles, that this role defaults to when no index is specified in a search. |
| `imported_srchJobsQuota` | String | The maximum number of historical searches for this role that are imported from other roles. |
| `imported_srchTimeWin` | String | Maximum time span of a search, in seconds. 0 indicates searches are not limited to any specific time window. imported_srchTimeWin specifies the limit from imported roles. |
| `rtSrchJobsQuota` | Number | The maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit. |
| `srchDiskQuota` | Number | The maximum disk space in MB that can be used by a user's search jobs. For example, 100 limits this role to 100 MB total. |
| `srchFilter` | String | Search string that restricts the scope of searches run by this role. Search results for this role show only events that also match this search string. When a user has multiple roles with different search filters, they are combined with an OR . |
| `srchIndexesAllowed` | String | A list of indexes this role has permissions to search. |
| `srchIndexesDefault` | String | List of search indexes that default to this role when no index is specified. |
| `srchIndexesDisallowed` | String | A list of indexes that this role does not have permission to search on or delete. |
| `srchJobsQuota` | Number | The maximum number of concurrent real-time search jobs for this role. This count is independent from the normal search jobs limit. |
| `srchTimeWin` | Number | Maximum time span of a search, in seconds. 0 indicates searches are not limited to any specific time window. |

### `/services/authorization/tokens`

#### GET

List information on tokens.

#### POST

Change the status of one or more tokens.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `audience` | String | The purpose for the token. Can be up to 256 characters. |
| `expires_on` | String | The time that the token expires. Can be either of an absolute time (ex.: 2019-02-09T07:35:00+07:00 ) or a relative time (ex.: +90d ). This time cannot be in the past. Note : If you specify not_before in addition to expires_on , not_before cannot be after expires_on .. |
| `not_before` | String | The time that the token becomes valid. Can be an absolute time or a relative time. This time cannot be in the past. Note : If you specify not_before in addition to expires_on , not_before cannot be after expires_on .. |

### `/services/authorization/tokens/{name}`

#### DELETE

Delete a token for the specified user.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `id` | The ID of the token you want to delete. Optional. If not specified, then all tokens that belong to {username} are deleted. |  |

#### POST

Create a token for the specified username.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `audience` | String | The purpose for the token. Can be up to 256 characters. |
| `expires_on` | String | The time that the token expires. Can be either of an absolute time (ex.: 2019-02-09T07:35:00+07:00 ) or a relative time (ex.: +90d ). This time cannot be in the past. Note : If you specify not_before in addition to expires_on , not_before cannot be after expires_on .. |
| `not_before` | String | The time that the token becomes valid. Can be an absolute time or a relative time. This time cannot be in the past. Note : If you specify not_before in addition to expires_on , not_before cannot be after expires_on .. |

### `/services/storage/passwords`

Create or update user credentials, or list credentials for all users.

#### GET

List available credentials.

#### POST

Create/update new credentials.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `password` | String | Required . Credentials user password. |
| `realm` | String | Credentials realm. |

### `/services/storage/passwords/{name}`

Update, delete, or list credentials for the {name} user.

#### DELETE

Delete the specified user credentials.

#### GET

Access the specified user credentials.

#### POST

Update the specified user credentials.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `password` | String | User password credential. |

---

## Application

### `/services/apps/appinstall (deprecated)`

Install or update an application.

#### POST

Install or update an application from a local file or URL.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `update` | Boolean | Indicates whether to update installed app. true = update existing app, overwriting the existing app folder. false = [Default] install new app. |

### `/services/apps/apptemplates`

#### GET

List installed app templates.

### `/services/apps/apptemplates/{name}`

#### GET

Get the {name} app template descriptor.

### `/services/apps/local`

#### GET

List installed apps and properties.

#### POST

Create an app.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `auth` | String | Splunkbase session token for operations like install and update that require login. Use auth or session when installing or updating an app through Splunkbase. |
| `author` | String | For apps posted to Splunkbase, use your Splunk account username. For internal apps, include your name and contact information. |
| `configured` | Boolean | Custom setup complete indication: true = Custom app setup complete. false = Custom app setup not complete. |
| `explicit_appname` | String | Custom app name. Overrides name when installing an app from a file where filename is set to true . See also filename . |
| `filename` | Boolean | Indicates whether to use the name value as the app source location. true indicates that name is a path to a file to install. false indicates that name is the literal app name and that the app is created from Splunkbase using a template. |
| `label` | String | App name displayed in Splunk Web, from five to eighty characters excluding the prefix "Splunk for". |
| `session` | String | Login session token for installing or updating an app on Splunkbase. Alternatively, use auth . |
| `template` | Enum | App template to use when creating the app" barebones - [Default] Basic app framework. sample_app - Example views and searches. Any custom app template. |
| `update` | Boolean | File-based update indication: true specifies that filename should be used to update an existing app. If not specified, update defaults to false , which indicates that filename should not be used to update an existing app. |
| `version` | String | App version. |
| `visible` | Boolean | Indicates whether the app is visible and navigable from Splunk Web. true = App is visible and navigable. false = App is not visible or navigable. |

### `/services/apps/local/{name}`

#### DELETE

Delete the {name} app.

#### GET

List information about the {name} app.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `refresh` | Boolean | Indicates whether to reload any objects associated with the {name} app indication: true = Reload objects. false = Do not reload objects. |

#### POST

Update the {name} app properties. Append /enable or /disable to enable or disable the app. See Enable and disable endpoint for more information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `author` | String | For apps posted to Splunkbase, use your Splunk account username. For internal apps, use your full name and contact information. |
| `check_for_updates` | Boolean | Check for updates indicator. true = Check Splunkbase for app updates. false = Do not check Splunkbase for app updates. |
| `configured` | Boolean | Custom setup completion indicator. true = Custom app setup complete. false = Custom app setup not complete. |
| `label` | String | App name displayed in Splunk Web, from five to 80 characters and excluding the prefix "Splunk For". |
| `version` | String | App version. |
| `visible` | Boolean | Indicates whether app is visible and navigable from Splunk Web. true = App is visible and navigable. false = App is not visible and navigable. |

### `/services/apps/local/{name}/package`

#### GET

Archive the {name}.spl app.

### `/services/apps/local/{name}/setup`

Get the {name} app setup information.

#### GET

Get setup information for the {name} app.

### `/services/apps/local/{name}/update`

#### GET

Get {name} app eai:acl information.

---

## Cluster

### `/services/cluster/config`

Access cluster node configuration details.

#### GET

List cluster node configuration.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cxn_timeout` | Low-level timeout, in seconds, for establishing connection between cluster nodes. Defaults to 60 seconds. |  |
| `disabled` | Indicates if this node is disabled. |  |
| `forwarderdata_rcv_port` | The port from which to receive data from a forwarder. |  |
| `forwarderdata_use_ssl` | Indicates whether to use SSL when receiving data from a forwarder. |  |
| `heartbeat_period` | Only valid for peer nodes in a cluster. The time, in seconds, that a peer attempts to send a heartbeat to the manager |  |
| `heartbeat_timeout` | Only valid for the manager node in a cluster configuration. The time, in seconds, before a manager considers a peer down. Once a peer is down, the manager initiates steps to replicate buckets from the dead peer to its live peers. Defaults to 60 seconds. |  |
| `manager_uri` | Valid only for nodes configured as a peer or searchhead. URI of the cluster manager to which this node connects. |  |
| `max_peer_build_load` | The number of jobs that a peer can have in progress at any time that make the bucket searchable. |  |
| `max_peer_rep_load` | Maximum number of replications that can be ongoing as a target. |  |
| `mode` | Valid values: (manager | peer | searchhead | disabled) Defaults to disabled. Sets operational mode for this cluster node. Only one manager may exist per cluster. |  |
| `ping_flag` | For internal use to facilitate communication between the manager and peers. |  |
| `quiet_period` | The time, in seconds, that a manager waits for peers to add themselves to the cluster. |  |
| `rcv_timeout` | Low-level timeout, in seconds, for receiving data between cluster nodes. Defaults to 60 seconds. |  |
| `register_forwarder_address` | Not used. Reserved for future use. |  |
| `register_replication_address` | Valid only for nodes configured as peers. The address on which a peer is available for accepting replication data. This is useful in the cases where a peer host machine has multiple interfaces and only one of them can be reached by another splunkd instance. |  |
| `register_search_address` | IP address that advertises this indexer to search heads. |  |
| `rep_cxn_timeout` | Low-level timeout, in seconds, for establishing a connection for replicating data. |  |
| `rep_max_rcv_timeout` | Maximum cumulative time, in seconds, for receiving acknowledgement data from peers. Defaults to 600s. |  |
| `rep_max_send_timeout` | Maximum time, in seconds, for sending replication slice data between cluster nodes. Defaults to 600s. |  |
| `rep_rcv_timeout` | Low-level timeout, in seconds, for receiving data between cluster nodes. |  |
| `rep_send_timeout` | Low-level timeout, in seconds, for sending replication data between cluster nodes. Defaults to 5 seconds. |  |
| `replication_factor` | Only valid for nodes configured as a manager. Determines how many copies of raw data are created in the cluster. This could be less than the number of cluster peers. Must be greater than 0 and greater than or equal to the search factor. Defaults to 3. |  |
| `replication_port` | TCP port to listen for replicated data from another cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `restart_timeout` | Only valid for nodes configured as a manager. The amount of time, in seconds, the manager waits for a peer to come back when the peer is restarted (to avoid the overhead of trying to fix the buckets that were on the peer). Defaults to 600 seconds. Note: This only works if the peer is restarted from Splunk Web. |  |
| `search_factor` | Only valid for nodes configured as a manager. Determines how many searchable copies of each bucket to maintain. Must be less than or equal to replication_factor and greater than 0. Defaults to 2. |  |
| `secret` | Secret shared among the nodes in the cluster to prevent any arbitrary node from connecting to the cluster. If a peer or searchhead is not configured with the same secret as the manager, it is not able to communicate with the manager. Corresponds to pass4SymmKey setting in server.conf . |  |
| `send_timeout` | Low-level timeout, in seconds, for sending data between cluster nodes. Defaults to 60 seconds. |  |
| `summary_replication` | Boolean indicator of whether summary replication is on or off. A true value means that it is turned on. |  |

### `/services/cluster/config/config`

Manage cluster node configuration details.

#### GET

List cluster node configuration.

#### POST

Manage configuration details.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `available_sites` | N/A | Sets the various sites that are recognized for this manager. Valid values include site1 to site64 . |
| `cluster_label` | String | Label for this cluster. |
| `cxn_timeout` | Number | Low-level timeout, in seconds, for establishing connection between cluster nodes. Defaults to 60 seconds. |
| `heartbeat_period` | Number | Only valid for peer nodes in a cluster. Time, in seconds, that a peer attempts to send a heartbeat to the manager |
| `heartbeat_timeout` | Number | Only valid for the manager node in a cluster configuration. Time, in seconds, before a manager considers a peer down. Once a peer is down, the manager initiates steps to replicate buckets from the dead peer to its live peers. Defaults to 60 seconds. |
| `manager_uri` | URI | Valid only for nodes configured as a peer or searchhead. URI of the cluster manager to which this node connects. |
| `max_peer_build_load` | Number | The number of jobs that a peer can have in progress at any time that make the bucket searchable. |
| `max_peer_rep_load` | Number | Maximum number of replications that can be ongoing as a target. |
| `mode` | See description. | Required. Valid values: (manager \| peer \| searchhead \| disabled) Defaults to disabled. Sets operational mode for this cluster node. Only one manager may exist per cluster. |
| `multisite` | Boolean | Enable or disable the multisite feature for this cluster. |
| `notify_scan_period` | Non-zero number | Controls the frequency that the indexer scans summary folders for summary updates. Only used when summary_replication is enabled on the manager. Defaults to 10 seconds. |
| `ping_flag` | N/A | For internal use to facilitate communication between the manager and peers. |
| `quiet_period` | Number | The time, in seconds, that a manager waits for peers to add themselves to the cluster. |
| `rcv_timeout` | Number | Low-level timeout, in seconds, for receiving data between cluster nodes. Defaults to 60 seconds. |
| `register_forwarder_address` | N/A | Reserved for future use. |
| `register_replication_address` | See description. | Valid only for nodes configured as peers. The address on which a peer is available for accepting replication data. This is useful in the cases where a peer host machine has multiple interfaces and only one of them can be reached by another splunkd instance. |
| `register_search_address` | N/A | IP address that advertises this indexer to search heads. |
| `rep_cxn_timeout` | Number | Low-level timeout, in seconds, for establishing a connection for replicating data. |
| `rep_max_rcv_timeout` | Number | Maximum cumulative time, in seconds, for receiving acknowledgement data from peers. Defaults to 600s. |
| `rep_max_send_timeout` | Number | Maximum time, in seconds, for sending replication slice data between cluster nodes. Defaults to 600s. |
| `rep_rcv_timeout` | Number | Low-level timeout, in seconds, for receiving data between cluster nodes. |
| `rep_send_timeout` | Number | Low-level timeout, in seconds, for sending replication data between cluster nodes. Defaults to 5 seconds. |
| `replication_factor` | Number | Only valid for nodes configured as a manager. Determines how many copies of raw data are created in the cluster. This could be less than the number of cluster peers. Must be greater than 0 and greater than or equal to the search factor. Defaults to 3. |
| `replication_port` | Number | TCP port to listen for replicated data from another cluster member. |
| `replication_use_ssl` | Number | Indicates whether to use SSL when sending replication data. |
| `restart_timeout` | Number | Only valid for nodes configured as a manager. The amount of time, in seconds, the manager waits for a peer to come back when the peer is restarted (to avoid the overhead of trying to fix the buckets that were on the peer). Defaults to 600 seconds. Note: This only works if the peer is restarted from Splunk Web. |
| `search_factor` | Number | Only valid for nodes configured as a manager. Determines how many searchable copies of each bucket to maintain. Must be less than or equal to replication_factor and greater than 0. Defaults to 2. |
| `secret` | N/A | Secret shared among the nodes in the cluster to prevent any arbitrary node from connecting to the cluster. If a peer or searchhead is not configured with the same secret as the manager, it is not able to communicate with the manager. Corresponds to pass4SymmKey setting in server.conf . |
| `send_timeout` | Number | Low-level timeout, in seconds, for sending data between cluster nodes. Defaults to 60 seconds. |
| `site` | N/A | Site ID for peer/searchhead indexer. Valid values include site1 to site64 . |
| `site_replication_factor` | Number | Replication factor for a multisite configuration. |
| `site_search_factor` | Number | Search factor for a multisite configuration. |
| `summary_replication` | Boolean | Enable or disable summary replication. |
| `use_batch_mask_changes` | Boolean | Only valid for mode=manager .Specifies if the manager should process bucket mask changes in batch or inidividually one by one. Defaults to true. Set to false when there are 6.1 peers in the cluster for backwards compatibility. |

### `/services/cluster/manager/buckets`

Provides bucket configuration information for a cluster manager node.

#### GET

List cluster manager node bucket configuration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `index` | String | Index name. |
| `status` | String | Bucket state. Available options are StreamingSource StreamingTarget Complete StreamingError PendingTruncate Bucket is scheduled to truncate. PendingDiscard Bucket is scheduled to discard. NonStreamingTarget |
| `search_state` | String | Bucket search state. Available options are Searchable Unsearchable PendingSearchable Bucket scheduled to become searchable by transferring or building tsidx files. PendingUnsearchable Bucket is scheduled to become unsearchable. SearchablePendingMask Primary change is scheduled or in progress. |
| `replication_count` | Number | Use <, >, != or = with numbers to indicate filtering values. |
| `search_count` | Number | Use <, >, != or = with numbers to indicate filtering values. |
| `bucket_size` | Number | Use <, >, != or = with numbers to indicate filtering values. |
| `frozen` | Boolean true | false | Return frozen buckets or non-frozen buckets. |
| `has_primary` | Boolean true | false | Return buckets with primaries or without primaries. |
| `meets_multisite_replication_count` | Boolean true | false | Return buckets that meet cluster replication policy or buckets that do not meet cluster replication policy. |
| `meets_multisite_search_count` | Boolean true | false | Return buckets that meet cluster search policy or buckets that do not meet cluster search policy. |
| `multisite_bucket` | Boolean true | false | Return buckets created in multisite mode or buckets not created in multisite mode. |
| `origin_site` | String | Site of the indexer where buckets were created. |
| `standalone` | Boolean true | false | Use true or 1 to return standalone buckets. Use false or 0 to return clustered buckets. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `bucket_size` | Indicates the size, in bytes, of the bucket. |  |
| `constrain_to_origin_site` | Flag indicating this particular bucket is a clustered pre-multisite bucket. Such buckets are replicated only within their origin site. |  |
| `frozen` | Indicates if the bucket is frozen. |  |
| `index` | Name of the index to which the bucket belongs. |  |
| `origin_site` | Where the bucket originated. |  |
| `peers` | Lists information about buckets on peers to this manager. |  |
| `primaries_by_site` | Primary peer (GIUD). |  |
| `rep_count_by_site` | Number of buckets. |  |
| `search_count_by_site` | Number of searchable buckets. |  |
| `service_after_time` | Bucket service is deferred until after this time. |  |
| `standalone` | Indicates if the bucket was created on the peer before the peer entered into a cluster configuration with this manager. |  |

### `/services/cluster/manager/buckets/{name}`

Access bucket configuration information.

#### GET

List bucket configuration information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `bucket_size` | Indicates the size, in bytes, of the bucket. |  |
| `constrain_to_origin_site` | Flag indicating this particular bucket is a clustered pre-multisite bucket. Such buckets are replicated only within their origin site. |  |
| `frozen` | Indicates if the bucket is frozen. |  |
| `index` | Name of the index to which the bucket belongs. |  |
| `origin_site` | Where the bucket originated. |  |
| `peers` | Lists information about buckets on peers to this manager. |  |
| `primaries_by_site` | Primary peer (GIUD). |  |
| `rep_count_by_site` | Number of buckets. |  |
| `search_count_by_site` | Number of searchable buckets. |  |
| `service_after_time` | Bucket service is deferred until after this time. |  |
| `standalone` | Indicates if the bucket was created on the peer before the peer entered into a cluster configuration with this manager. |  |

### `/services/cluster/manager/buckets/{bucket_id}/fix`

Add the specified bucket to the fix list.

#### POST

Add this bucket to the fix list.

### `/services/cluster/manager/buckets/{bucket_id}/fix_corrupt_bucket`

Trigger a corruption fixup of a clustered non-SmartStore-enabled bucket.

#### POST

Trigger a corruption fixup for this bucket.

### `/services/cluster/manager/buckets/{bucket_id}/freeze`

Set the bucket's state to frozen. The frozen state may not persist after a cluster manager restart unless one of the peers has set the frozen state. A POST to this endpoint does not set the bucket's state to frozen on peers.

#### POST

Set this bucket's state to frozen.

### `/services/cluster/manager/buckets/{bucket_id}/remove_all`

Delete all copies of the specified bucket.

#### POST

Delete all copies of the specified bucket.

### `/services/cluster/manager/buckets/{bucket_id}/remove_from_peer`

Deletes the copy of this bucket from specified peer.

#### POST

Delete this bucket from specified peer. Set bucket state to frozen

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `peer (required)` | GUID | Peer GUID |

### `/services/cluster/manager/control/control/prune_index`

Clean up excess bucket copies across an index.

#### POST

Clean up excess bucket copies across an index.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `index` | Optional. The index from which to remove excess bucket copies. If not specified, the POST operation clears excess bucket copies across all indexes. |  |

### `/services/cluster/manager/control/control/rebalance_primaries`

Rebalance primary bucket copies across peers. For more information, see Rebalance the indexer cluster primary buckets in Managing Indexers and Clusters of Indexers .

#### POST

Rebalance primary buckets across all peers of this manager.

### `/services/cluster/manager/control/control/remove_peers`

Remove one or more peers.

#### POST

Remove one or more peers.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `peers Required` | String | One or more comma-separated peer GUIDs. |

### `/services/cluster/manager/control/control/resync_bucket_from_peer`

This endpoint resets the state of a specified bucket based on the current state of the bucket at a peer.

#### POST

Reset bucket state based on the current state of the bucket at a peer.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `bucket_id` | String | N/A |
| `peer` | GUID | N/A |

### `/services/cluster/manager/control/control/roll-hot-buckets`

This endpoint forces a specified bucket in an indexer cluster to roll from hot to warm. Pass the bucket id (bid) to the manager node. The manager instructs the origin peer for that bucket to roll its copy. In turn, the origin peer tells all the replicating peers to roll their copies

#### POST

Force a bucket to roll from hot to warm.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `bucket_id` | String | N/A |

### `/services/cluster/manager/control/control/rolling_upgrade_finalize`

Finalizes an indexer cluster rolling upgrade.

#### POST

Finalizes an indexer cluster rolling upgrade.

### `/services/cluster/manager/control/control/rolling_upgrade_init`

Initializes an indexer cluster rolling upgrade.

#### POST

Initializes an indexer cluster rolling upgrade.

### `/services/cluster/manager/control/default/abort_restart`

Aborts an ongoing restart of an indexer cluster.

#### POST

Abort an ongoing restart of an indexer cluster.

### `/services/cluster/manager/control/default/apply`

Pushes a bundle.

#### POST

Push a bundle.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `skip-validation` | Boolean | False |
| `ignore_identical_bundle` | Boolean | True |

### `/services/cluster/manager/control/default/cancel_bundle_push`

Cancels and resets the bundle push operation. Use this endpoint when the cluster manager does not receive a validation response from the cluster peer due to an error. For more information, see Configuration bundle issues .

#### POST

Cancel and reset the bundle push operation.

### `/services/cluster/manager/control/default/maintenance`

Put the cluster manager into maintenance mode.

#### POST

Toggle maintenance mode.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `mode` | Boolean | Enable or disable maintenance mode on the cluster manager. |

### `/services/cluster/manager/control/default/rollback`

Roll a bundle back to the previously active bundle.

#### POST

Roll back a bundle.

### `/services/cluster/manager/control/default/validate_bundle`

Tests if the bundle in etc/manager-apps passes validation. Optionally, tests if the bundle will trigger an indexer restart.

#### POST

Validate a bundle.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `check-restart` | Boolean | False |

### `/services/cluster/manager/fixup`

Access a list of buckets on a specific fixup priority level. Bucket fixups are processed in order of priority level. See Request parameters below for priority level details.

#### GET

List buckets on the specified fixup level.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `level` | String | Required . Fixup priority level. Use one of the following level values, listed in order of priority. corruption : Corrupted buckets. streaming : Hot buckets that need to be rolled or have their size committed. data_safety : Buckets without at least two rawdata copies. generation : Buckets without a primary copy. replication_factor : Buckets without replication factor number of copies. search_factor : Buckets without search factor number of copies. checksum_sync : Level for syncing a bucket's delete files across all peers that have this bucket. Syncing is determined based on the checksum of all of the delete files. |
| `index` | String | Optional. Index name. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `id` | Bucket id. |  |
| `reason` | Initial or latest reason for the bucket being on this fixup level. |  |
| `timestamp` | Timestamp for initial bucket addition to fixup list or latest bucket check. |  |

### `/services/cluster/manager/generation`

Access current generation cluster manager information and create a cluster generation.

#### GET

List peer nodes participating in the current generation for this manager.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The ID for the current generation for this manager. |  |
| `generation_peers` | Lists the peers for this generation of the cluster. |  |
| `pending_generation_id` | The next generation ID used by the manager when committing a new generation. This value is useful for debugging. |  |
| `pending_last_attempt` | The timestamp of the last attempt to commit to the pending generation ID (if ever). |  |
| `pending_last_reason` | The reason why this peer failed to commit to the pending generation. This parameter is EMPTY if no such attempt was made. |  |

#### POST

Create a cluster generation.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String |  |
| `generation_poll_interval` | Number |  |
| `label` | String |  |
| `mgmt_port` | String |  |
| `register_search_address` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The ID for the current generation for this manager. |  |
| `generation_peers` | Lists the peers for this generation of the cluster. |  |
| `pending_generation_id` | The next generation ID used by the manager when committing a new generation. This value is useful for debugging. |  |
| `pending_last_attempt` | The timestamp of the last attempt to commit to the pending generation ID (if ever). |  |
| `pending_last_reason` | The reason why this peer failed to commit to the pending generation. This parameter is EMPTY if no such attempt was made. |  |
| `replication_factor_met` | Indicates if the replication factor was met for the cluster. |  |
| `search_factor_met` | Indicates if the search factor was met for the cluster. |  |
| `was_forced` | Indicates next generation was forcibly committed. |  |

### `/services/cluster/manager/generation/{name}`

Access information about a peer node participating in the current generation for the specified search head GUID.

#### GET

List peer node information of the specified search head GUID.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The ID of the current generation for this manager. |  |
| `generation_peers` | Lists the peers for this generation of the cluster. |  |
| `pending_generation_id` | The next generation ID used by the manager when committing a new generation. This value is useful for debugging. |  |
| `pending_last_attempt` | The timestamp of the last attempt to commit to the pending generation ID (if ever). |  |
| `pending_last_reason` | The reason why this peer failed to commit to the pending generation. This parameter is EMPTY if no such attempt was made. |  |

#### POST

Create a new generation for the specified search head GUID.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `generation_poll_interval` | Number | How often, in seconds, the searchhead polls the manager for generation information. Defaults to 60 seconds. |
| `label` | String | Server name for the search head specified by {name}. |
| `mgmt_port` | String | The managment port of searchhead node in a cluster upon which you are creating a new generation. |
| `register_search_address` | String | The address on which a peer node is available as search head. This is useful when a host machine has multiple interfaces and only one of them can be reached by another splunkd instance. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The ID for the current generation for this manager. |  |
| `generation_peers` | Lists the peers for this generation of the cluster. |  |
| `pending_generation_id` | The next generation ID used by the manager when committing a new generation. This value is useful for debugging. |  |
| `pending_last_attempt` | The timestamp of the last attempt to commit to the pending generation ID (if ever). |  |
| `pending_last_reason` | The reason why this peer failed to commit to the pending generation. This parameter is EMPTY if no such attempt was made. |  |
| `replication_factor_met` | Indicates if the replication factor was met for the cluster. |  |
| `search_factor_met` | Indicates if the search factor was met for the cluster. |  |
| `was_forced` | Indicates next generation was forcibly committed. |  |

### `/services/cluster/manager/ha_active_status`

Used by the load balancers to check the high availability mode of a given cluster manager.

#### GET

Checks the high availability mode of a given cluster manager.

### `/services/cluster/manager/health`

Performs health checks to determine the cluster health and search impact, prior to a rolling upgrade of the indexer cluster.

#### GET

Get indexer cluster health check results.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `all_data_is_searchable` | Boolean | Indicates if all data in the cluster is searchable. |
| `all_peers_are_up` | Boolean | Indicate if all peers are strictly in the Up status. |
| `cm_version_is_compatible` | Boolean | Indicates if any cluster peers are running a Splunk Enterprise version greater than or equal to the cluster manager's version. |
| `multisite` | Boolean | Indicates if multisite is enabled. |
| `no_fixups_in_progress` | Boolean | Indicates if there does not exist buckets with bucket state NonStreamingTarget , or bucket search states PendingSearchable or SearchablePendingMask . |
| `pre_flight_check` | Boolean | Indicates if the health check prior to a rolling upgrade was successful. This value is true only if the cluster passed all health checks. |
| `replication_factor_met` | Boolean | Only valid for mode=manager and multisite=false. Indicates whether the replication factor is met. If true, the cluster has at least replication_factor number of raw data copies in the cluster. |
| `search_factor_met` | Boolean | Only valid for mode=manager and multisite=false. Indicates whether the search factor is met. If true, the cluster has at least search_factor number of raw data copies in the cluster. |
| `site_replication_factor_met` | Boolean | Only valid for mode=manager and multisite=true. Indicates whether the site replication factor is met. If true, the cluster has at least replication_factor number of raw data copies in the cluster. |
| `site_search_factor_met` | Boolean | Only valid for mode=manager and multisite=true. Indicates whether the site search factor is met. If true, the cluster has at least site_search_factor number of raw data copies in the cluster. |
| `splunk_version_peer_count` | String | Lists the number of cluster peers running each Splunk Enterprise version. |

### `/services/cluster/manager/indexes`

Access cluster index information.

#### GET

List cluster indices.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `buckets_with_excess_copies` | Number of distinct buckets that have one or more excess replication copies. |  |
| `buckets_with_excess_searchable_copies` | Number of distinct buckets that have one or more excess searchable copies. |  |
| `index_size` | Size of the index |  |
| `is_searchable` | When every bucket in the index has a primary, the index is considered "searchable". |  |
| `non_site_aware_buckets_in_site_aware_cluster` | Number of buckets created when the cluster was not in a multisite config. (Included only when the cluster is in multisite config.) |  |
| `num_buckets` | Total number of distinct buckets. |  |
| `replicated_copies_tracker` | Displays how many distinct buckets have X number of copies. One of the following options. actual_copies_per_slot Number of buckets with X copies. expected_total_per_slot Expected number of buckets with X copies. |  |
| `searchable_copies_tracker` | Displays how many distinct buckets have X number of searchable copies. One of the following options. actual_copies_per_slot Number of buckets with X searchable copies. expected_total_per_slot Expected number of buckets with X searchable copies. |  |
| `sort_order` | Used by UI. |  |
| `total_excess_bucket_copies` | Total number of excess copies for all buckets. |  |
| `total_excess_searchable_copies` | Total number of excess searchable copies for all buckets. |  |

### `/services/cluster/manager/indexes/{name}`

Access specific cluster index information.

#### GET

List {name} index information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `buckets_with_excess_copies` | Number of distinct buckets that have one or more excess replication copies. |  |
| `buckets_with_excess_searchable_copies` | Number of distinct buckets that have one or more excess searchable copies. |  |
| `index_size` | Size of the index |  |
| `is_searchable` | When every bucket in the index has a primary, the index is considered "searchable". |  |
| `non_site_aware_buckets_in_site_aware_cluster` | Number of buckets created when the cluster was not in a multisite config. (Included only when the cluster is in multisite config.) |  |
| `num_buckets` | Total number of distinct buckets. Displays how many distinct buckets have X number of copies. One of the following options. actual_copies_per_slot Number of buckets with X copies. expected_total_per_slot Expected number of buckets with X copies. |  |
| `searchable_copies_tracker` | Displays how many distinct buckets have X number of searchable copies. One of the following options. actual_copies_per_slot Number of buckets with X searchable copies. expected_total_per_slot Expected number of buckets with X searchable copies. |  |
| `sort_order` | Used by UI. |  |
| `total_excess_bucket_copies` | Total number of excess copies for all buckets. |  |
| `total_excess_searchable_copies` | Total number of excess searchable copies for all buckets. |  |

### `/services/cluster/manager/info`

Access information about cluster manager node.

#### GET

List cluster manager node details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_bundle` | Provides information about the active bundle for this manager. |  |
| `apply_bundle_status` | Status of bundle application operations including validation, reload, dry-run reload, and rolling restart progress. |  |
| `backup_and_restore_primaries` | If true, indicates that the primary bucket backup and restoration is turned on during maintenance. |  |
| `controlled_rolling_restart_flag` | If true, indicates that the cluster is in controlled rolling restart mode, which is a shutdown-based rolling restart. |  |
| `eai:acl` | Returns the endpoint's External Admin Interface Access Control List information. |  |
| `indexing_ready_flag` | If true, indicates if the cluster is ready for indexing. |  |
| `initialized_flag` | If true, indicates if the cluster is initialized. |  |
| `label` | The name for the manager. Displayed in the Splunk Web manager page. |  |
| `last_check_restart_bundle_result` | If true, indicates if the last bundle validation check determined that a restart is required. |  |
| `last_dry_run_bundle` | Information about the most recent dry-run bundle that was used for testing configuration changes. |  |
| `last_validated_bundle` | Information about the last bundle that successfully completed validation. |  |
| `latest_bundle` | The most recent information reflecting any changes made to the manager-apps configuration bundle. In steady state, this is equal to active_bundle . If it is not equal, then pushing the latest bundle to all peers is in process (or needs to be started). |  |
| `maintenance_mode` | If true, indicates that the cluster is in maintenance mode. |  |
| `multisite` | If true, indicates that multisite clustering is turned on. |  |
| `previous_active_bundle` | Information about the most recently active bundle. This information is used for rollback scenarios. |  |
| `primaries_backup_status` | Status of primary bucket backup operations. |  |
| `quiet_period_flag` | If true, indicates that the cluster is in quiet period. The cluster is in a quiet period if the configured time has not elapsed or if Splunk platform is currently adding a peer. |  |
| `rolling_restart_flag` | If true, indicates that a rolling restart is currently in progress. |  |
| `rolling_restart_or_upgrade` | If true, indicates that a rolling restart and/or an upgrade operation is active. |  |
| `service_ready_flag` | If true, indicates that the cluster manager is ready to provide services. |  |
| `start_time` | Timestamp corresponding to the creation of the manager. |  |
| `summary_replication` | If true, indicates that summary replication is turned on. |  |

### `/services/cluster/manager/peers`

Access cluster manager peers.

#### GET

List cluster manager peers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_bundle_id` | The ID of the configuration bundle currently being used by the manager. |  |
| `apply_bundle_status` | Bundle status enumeration. |  |
| `base_generation_id` | The initial bundle generation ID recognized by this peer. Any searches from previous generations fail. The initial bundle generation ID is created when a peer first comes online, restarts, or recontacts the manager. |  |
| `bucket_count` | Count of the number of buckets on this peer, across all indexes. |  |
| `bucket_count_by_index` | Count of the number of buckets by index on this peer. |  |
| `delayed_buckets_to_discard` | List of bucket IDs waiting to be discarded on this peer. |  |
| `fixup_set` | The set of buckets that need repair once you take the peer offline. |  |
| `heartbeat_started` | Flag indicating if this peer has started heartbeating. |  |
| `host_port_pair` | The host and port advertised to peers for the data replication channel. Can be either of the form IP:port or hostname:port. |  |
| `is_searchable` | Flag indicating if this peer belongs to the current committed generation and is searchable. |  |
| `label` | The name for the peer. Displayed on the manager page. |  |
| `last_heartbeat` | Timestamp for last heartbeat recieved from the peer. |  |
| `latest_bundle_id` | The ID of the configuration bundle this peer is using. |  |
| `pending_job_count` | Used by the manager to keep track of pending jobs requested by the manager to this peer. |  |
| `primary_count` | Number of buckets for which the peer is primary in its local site, or the number of buckets that return search results from same site as the peer. |  |
| `primary_count_remote` | Number of buckets for which the peer is primary that are not in its local site. |  |
| `replication_count` | Number of replications this peer is part of, as either source or target. |  |
| `replication_port` | TCP port to listen for replicated data from another cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `search_state_counter` | Lists the number of buckets on the peer for each search state for the bucket. Possible values for search state include: Searchable Unsearchable |  |
| `site` | To which site the peer belongs. |  |
| `status` | Indicates the status of the peer. Valid values are: Up Pending AutomaticDetention ManualDetention-PortsEnabled ManualDetention Restarting ShuttingDown ReassigningPrimaries Decommissioning GracefulShutdown Stopped Down BatchAdding |  |
| `status_counter` | Lists the number of buckets on the peer for each bucket status. Possible values for bucket status: Complete: complete (warm/cold) bucket NonStreamingTarget: target of replication for already completed (warm/cold) bucket PendingTruncate: bucket pending truncation PendingDiscard: bucket pending discard Standalone: bucket that is not replicated StreamingError: copy of streaming bucket where some error was encountered StreamingSource: streaming hot bucket on source side StreamingTarget: streaming hot bucket copy on target side Unset: uninitialized |  |

### `/services/cluster/manager/peers/{name}`

Access specified peer.

#### GET

Get {name} peer information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `list_buckets` | Boolean | Indicates whether to list the buckets for the peers to this manager. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_bundle_id` | The ID of the configuration bundle currently being used by the manager. |  |
| `apply_bundle_status` | Bundle status enumeration. |  |
| `base_generation_id` | The initial bundle generation ID recognized by this peer. Any searches from previous generations fail. The initial bundle generation ID is created when a peer first comes online, restarts, or recontacts the manager. |  |
| `bucket_count` | Count of the number of buckets on this peer, across all indexes. |  |
| `bucket_count_by_index` | Count of the number of buckets by index on this peer. |  |
| `delayed_buckets_to_discard` | List of bucket IDs waiting to be discarded on this peer. |  |
| `fixup_set` | The set of buckets that need repair once you take the peer offline. |  |
| `heartbeat_started` | Flag indicating if this peer has started heartbeating. |  |
| `host_port_pair` | The host and port advertised to peers for the data replication channel. Can be either of the form IP:port or hostname:port. |  |
| `is_searchable` | Flag indicating if this peer belongs to the current committed generation and is searchable. |  |
| `label` | The name for the peer. Displayed on the Splunk Web manager page. |  |
| `last_heartbeat` | Timestamp for last heartbeat recieved from the peer. |  |
| `latest_bundle_id` | The ID of the configuration bundle this peer is using. |  |
| `pending_job_count` | Used by the manager to keep track of pending jobs requested by the manager to this peer. |  |
| `primary_count` | Number of buckets for which the peer is primary in its local site, or the number of buckets that return search results from same site as the peer. |  |
| `primary_count_remote` | Number of buckets for which the peer is primary that are not in its local site. |  |
| `replication_count` | Number of replications this peer is part of, as either source or target. |  |
| `replication_port` | TCP port to listen for replicated data from another cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `search_state_counter` | Lists the number of buckets on the peer for each search state for the bucket. Possible values for search state include: Searchable Unsearchable |  |
| `site` | To which site the peer belongs. |  |
| `splunk_version` | The version of Splunk that the peer is running. This will be of the form X.Y.Z where X is the major version, Y is the minor version, and Z is the maintenance version. |  |
| `status` | Indicates the status of the peer. Valid values are: Up Pending AutomaticDetention ManualDetention-PortsEnabled ManualDetention Restarting ShuttingDown ReassigningPrimaries Decommissioning GracefulShutdown Stopped Down BatchAdding |  |
| `status_counter` | Lists the number of buckets on the peer for each bucket status. Possible values for bucket status: Complete: complete (warm/cold) bucket NonStreamingTarget: target of replication for already completed (warm/cold) bucket PendingTruncate: bucket pending truncation PendingDiscard: bucket pending discard Standalone: bucket that is not replicated StreamingError: copy of streaming bucket where some error was encountered StreamingSource: streaming hot bucket on source side StreamingTarget: streaming hot bucket copy on target side Unset: uninitialized |  |

### `/services/cluster/manager/redundancy`

Display the details of all cluster managers participating in cluster manager redundancy, and switch the HA state of the cluster managers.

#### GET

Display the details of all cluster managers participating in cluster manager redundancy.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_bundle_id` | The active bundle ID of the cluster, as set in the given cluster manager. |  |
| `generation_id` | The last committed generation ID of the cluster, as known to the given cluster manager. |  |
| `ha_mode` | The high availability mode of the given cluster manager. |  |
| `last_heartbeat` | The timestamp of the last heartbeat received from the given cluster manager. This is only applicable for the standby cluster managers. For the active cluster manager, this is set to 0. For standby cluster managers, this field reflects the valid timestamp, denoting the last time the active manager received a heartbeat from this standby cluster manager. |  |
| `manager_switchover_mode` | The switchover mode set in the given cluster manager. |  |
| `peers_count` | The number of indexer peers known to to the given cluster manager. |  |
| `server_name` | The configured server name of the given cluster manager. |  |
| `uri` | The management URI of the given cluster manager. |  |

#### POST

Switch the high availability state of the cluster managers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `ha_mode` | The resultant high availability mode of the given cluster manager after the mode change request completion. |  |

### `/services/cluster/manager/sites`

Access cluster site information.

#### GET

List available cluster sites.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `peers` | Peers list of host:port and server name. |  |

### `/services/cluster/manager/sites/{name}`

Access specific cluster site information.

#### GET

List the {name} cluster site information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `peers` | Site peer reference, for each peer. Possible values include the following. host_port_pair Peer port number. server_name Peer server name. |  |

### `/services/cluster/manager/status`

Endpoint to get the status of a rolling restart.

#### GET

Get the status of a rolling restart.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `decommission_force_timeout` | The amount of time, in seconds, the cluster manager will wait for a peer in primary decommission status to finish primary reassignment and restart, during a searchable rolling restart with timeouts. Only valid for rolling_restart=searchable_force . Default value is 180. Max accepted value is 1800. |  |
| `maintenance_mode` | Indicates if the cluster is in maintenance mode. Happens during rolling restart, bundle push, and other maintenance activities. |  |
| `messages` | Array of messages from server. |  |
| `multisite` | Indicates if multisite is enabled for this manager. Make sure you set site parameters on the peers if you set this to true. Defaults to false. |  |
| `peers` | Object containing all the peers in the cluster. For each peer, the label, site and status are provided. |  |
| `restart_inactivity_timeout` | The amount of time, in seconds, that the manager waits for a peer to restart and rejoin the cluster before it considers the restart a failure and proceeds to restart other peers. A value of zero (0) means that the manager waits indefinitely for a peer to restart. Only valid for rolling_restart=searchable_force . Default is 600secs. |  |
| `restart_progress` | Object containing lists of peers in "done", "failed", "in_progress" and "to_be_restarted" state. |  |
| `rolling_restart_flag` | Boolean that indicates if there is a rolling restart in progress. |  |
| `rolling_restart_or_upgrade` | Boolean that indicates if there is a rolling restart or rolling upgrade in progress. |  |
| `searchable_rolling` | Boolean that indicates if a searchable rolling restart/upgrade in progress. |  |
| `service_ready_flag` | Boolean that indicates if the cluster is ready. |  |

### `/services/cluster/searchhead/generation`

Access peer information in a cluster searchhead.

#### GET

List peers available to a cluster searchhead.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The current generation ID for this searchhead, which is part of a cluster configuration. The search head uses this information to determine which buckets to search across. |  |
| `generation_peers` | List of peer nodes for the current generation in the cluster configuration for this searchhead. |  |

### `/services/cluster/searchhead/generation/{name}`

Access peer of the manager URI.

#### GET

Get {name} searchhead generation ID and generation peers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | The current generation ID for this searchhead, which is part of a cluster configuration. The search head uses this information to determine which buckets to search across. |  |
| `generation_peers` | List of peer nodes for the current generation in the cluster configuration for this searchhead. |  |

### `/services/cluster/searchhead/searchheadconfig`

Access cluster searchhead node configuration.

#### GET

List this cluster search head node configuration.

#### POST

Configure this server as a cluster searchhead node.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `secret` | String | Required . Secret shared among the nodes in the cluster to prevent any arbitrary node from connecting to the cluster. If a peer or searchhead is not configured with the same secret as the manager, it is not able to communicate with the manager. Corresponds to pass4SymmKey setting in server.conf. |

### `/services/cluster/searchhead/searchheadconfig/{name}`

Manage node in a cluster.

#### DELETE

Remove node from cluster.

#### GET

List cluster search head node configuration.

#### POST

Update cluster search head node configuration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `manager_uri` | String | The URI of the manager node in the cluster for which this searchhead is configured. |
| `secret` | String | Secret shared among the nodes in the cluster to prevent any arbitrary node from connecting to the cluster. If a peer or searchhead is not configured with the same secret as the manager, it is not able to communicate with the manager. Corresponds to pass4SymmKey setting in server.conf. |

### `/services/cluster/peer/buckets`

Access cluster peers bucket configuration.

#### GET

List cluster peers bucket configuration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | String | The generation ID for this peer. For each generation, the manager server in a cluster configuration assigns generation IDs. A generation identifies which copies of a cluster's buckets are primary and therefore can participate in a search. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `checksum` | Used internally to identify this bucket. |  |
| `earliest_time` | Indicates the time of the earliest event in this bucket. |  |
| `generation_id` | The generation ID for this peer. |  |
| `generations` | A sparse list of generation id to bucket primacy for the given peer. |  |
| `latest_time` | Indicates the time for the latest event in this bucket. |  |
| `search_state` | Indicates if the bucket is searchable or unsearchable . |  |
| `status` | Indicates the status of this bucket. One of the following values. Complete The copy of this bucket contains the full complement of information. StreamingSource The copy of this bucket is sending data to peer nodes for replication. StreamingTarget The copy of this bucket is receiving replicated data. NonStreamingTarget This copy of a warm bucket replication is in progress. Once replication is complete, the status changes to Complete. StreamingError The copy of this bucket encountered errors while streaming data. PendingTruncate The manager asked the peer to truncate this copy of the bucket to a certain size and is waiting for confirmation. PendingDiscard The manager asked the peer to discard this copy of the bucket (for whatever reason, and is waiting for confirmation. Standalone A bucket in the cluster that is not replicated. |  |

### `/services/cluster/peer/buckets/{name}`

Manage peer buckets.

#### DELETE

Remove specified bucket from peer node.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `bucket_id` | String | Required . The identifier for the bucket to remove. |

#### GET

List peer specified bucket information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `generation_id` | String | The generation ID for this peer. For each generation, the manager server in a cluster configuration assigns generation IDs. A generation identifies which copies of a cluster's buckets are primary and therefore can participate in a search. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `checksum` | Used internally to identify this bucket. |  |
| `earliest_time` | Indicates the time of the earliest event in this bucket. |  |
| `generation_id` | The generation ID for this peer. |  |
| `generations` | A sparse list of generation id to bucket primacy for the given peer. |  |
| `latest_time` | Indicates the time for the latest event in this bucket. |  |
| `search_state` | Indicates if the bucket is Searchable or Unsearchable . |  |
| `status` | Indicates the status of this bucket. One of the following values. Complete The copy of this bucket contains the full complement of information. StreamingSource The copy of this bucket is sending data to peer nodes for replication. StreamingTarget The copy of this bucket is receiving replicated data. NonStreamingTarget This copy of a warm bucket replication is in progress. Once replication is complete, the status changes to Complete. StreamingError The copy of this bucket encountered errors while streaming data. PendingTruncate The manager asked the peer to truncate this copy of the bucket to a certain size and is waiting for confirmation. PendingDiscard The manager asked the peer to discard this copy of the bucket (for whatever reason, and is waiting for confirmation. Standalone A bucket in the cluster that is not replicated. |  |

### `/services/cluster/peer/control/control/decommission`

Endpoint to decommission an indexer cluster peer node.

#### POST

Decommission a peer node.

### `/services/cluster/peer/control/control/re-add-peer`

Set the peer to re-add itself to the manager. This syncs the peer's state, including its in-memory bucket state, to the manager. By default, this resets the peer's primary bucket copies and the manager reassigns them across the cluster. To keep the peer's existing primary bucket copies, use the optional clearMasks=false parameter.

#### POST

Re-add the cluster indexer to the cluster manager.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `clearMasks` | Boolean. Use true or false . | true |

### `/services/cluster/peer/control/control/set_manual_detention`

If you have Splunk Enterprise, you can use this endpoint to put the peer node in manual detention mode or take the peer out of this mode. In manual detention, the peer does not serve as a replication target. Detention helps slow the growth of disk usage on the peer.

#### POST

Adjust cluster peer detention mode.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `manual_detention` | Use one of the following values. off : Default . Remove the indexer from the detention state. on : Put the indexer in manual detention mode. Close the TCP, UDP, and HTTP Event Collector data ports. Closing the ports causes most external data indexing to stop during detention. on_ports_enabled : Put the indexer in manual detention mode. Do not close the TCP, UDP, or HTTP Event Collector data ports. The peer continues to index data during detention. | Enable or disable manual detention. Opt to close data ports or leave them open when manual detention is enabled. |

### `/services/cluster/peer/info`

Access cluster peer node information.

#### GET

List peer information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_bundle` | Current bundle being used by this peer. |  |
| `base_generation_id` | The initial bundle generation ID recognized by this peer. Any searches from previous generations fail. The initial bundle generation ID is created when a peer first comes online, restarts, or recontacts the manager. |  |
| `invalid_bundle_ids` | List of bundle ids with validation errors in the peer. |  |
| `is_registered` | Indicates if this peer is registered with the manager in the cluster. |  |
| `last_heartbeat_attempt` | Timestamp for the last attempt to contact the manager. |  |
| `latest_bundle` | Lists information about the most recent bundle downloaded from the manager. |  |
| `restart_state` | Indicates whether the peer needs to be restarted to enable its cluster configuration. |  |
| `status` | Indicates the status of the peer. One of the following values. Up Down Pending Detention Restarting DecommAwaitingPeer DecommFixingBuckets Decommissioned |  |

### `/services/replication/configuration/health`

Access configuration replication health statistics for a search head cluster.

#### GET

Access the configuration replication health statistics for a search head cluster.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `bookmark` | Boolean | Use this parameter with a GET request on the captain. Set to 1 to list the most recent changesets that members pulled from the captain. A timestamp is also returned for each changeset. |
| `check_share_baseline` | Boolean | Set to 1 to check for a shared baseline among members. This parameter can be used with a request on any member, including the captain. |
| `unpublished` | Boolean | Set to 1 to check for unpublished changes on members. Use this parameter with a request on a member to check if the member has any changes that have not been pushed to the captain. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `[server_name]` | For each [server_name] member, a changeset and timestamp are shown, indicating when the [server_name] member last pulled this set of configuration changes from the captain. |  |

### `/services/replication/configuration/quarantined-assets`

Access information about quarantined lookups in a search head cluster.

#### GET

Access information about quarantined lookups in a search head cluster.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `assetName` | The name of the quarantined CSV lookup. |  |
| `quarantined_at_host` | The URL of the search head cluster member on which the lookup is quarantined. |  |
| `quarantined_at` | Seconds since epoch. |  |
| `lookup_size` | The size of the quarantined lookup in Bytes. |  |

### `/services/shcluster/captain/artifacts`

Provides list of artifacts and replicas currently managed by the captain across a searchhead cluster.

#### GET

Lists searchhead cluster artifacts and replicas.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `remote_sids` | Bool | Required . Set this to true to return the searches that the captain is seeing. Will include adhoc searches on remote members. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `artifact_size` | Artifact size, in bytes. |  |
| `origin_guid` | Guid of the origin peer where this artifact was created/search was run. |  |
| `peers` | Lists information about replicas of this artifact on members of this searchhead cluster. |  |
| `service_after_time` | Artifact service/fixup is deferred until after this time. |  |

### `/services/shcluster/captain/artifacts/{name}`

Get artifact information for a specific artifact.

#### GET

Get artifact information, size, replicas and earliest service time.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `artifact_size` | Artifact size, in bytes. |  |
| `origin_guid` | Guid of the origin peer where this artifact was created. |  |
| `peers` | Lists information about artifacts on members of this captain. |  |
| `service_after_time` | Artifact service is deferred until after this time. |  |

### `/services/shcluster/captain/control/default/restart`

Endpoint to initiate rolling restart of a search head cluster.

#### POST

Initiates rolling restart of a search head cluster

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `searchable` | Boolean | Maintain high search availability during a rolling restart. |
| `force` | Boolean | Override health check failures to continue searchable rolling restart. |
| `decommission_search_jobs_wait_secs` | Integer | Maximum time in secs that searchable rolling restart waits for existing searches to finish. Default: 180 secs. |

### `/services/shcluster/captain/control/control/rotate-splunk-secret`

Rotates the splunk.secret file on all nodes of a search head cluster.

#### POST

Rotates the splunk.secret file on all nodes of a search head cluster.

### `/services/shcluster/captain/control/control/upgrade-init`

Initializes a search head cluster rolling upgrade.

#### POST

Initializes a search head cluster rolling upgrade.

### `/services/shcluster/captain/control/control/upgrade-finalize`

Finishes a search head cluster rolling upgrade.

#### POST

Finishes a search head cluster rolling upgrade.

### `/services/shcluster/captain/info`

Access information about searchhead cluster captain node.

#### GET

List searchhead cluster captain node details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `elected_captain` | Time when the current captain was elected |  |
| `id` | Id of this SH cluster. This is used as the unique identifier for the Search Head Cluster in bundle replication and acceleration summary management. |  |
| `initialized_flag` | Indicates if the searchhead cluster is initialized. |  |
| `label` | The name for the captain. Displayed on the Splunk Web manager page. |  |
| `maintenance_mode` | Indicates if the cluster is in maintenance mode. |  |
| `min_peers_joined_flag` | Flag to indicate if more then replication_factor peers have joined the cluster. |  |
| `peer_scheme_host_port` | URI of the current captain. |  |
| `rolling_restart_flag` | Indicates whether the captain is restarting the members in a searchhead cluster. |  |
| `service_ready_flag` | Indicates whether the captain is ready to begin servicing, based on whether it is initialized. |  |
| `start_time` | Timestamp corresponding to the creation of the captain. |  |

### `/services/shcluster/captain/jobs`

List running and recently finished jobs for all cluster members.

#### GET

List running and recently finished jobs for this cluster.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `ATTEMPT_[n]` | dispatch_time - The UTC time of dispatch for the job errormsg - If the job failed, capturing the reason for failure peer - GUID of the member that the job was sent to sid - the search id of this attempt success - a boolean for success/failure of the job |  |
| `job_state` | Job State can be SCHEDULED / DISPATCHED / COMPLETED . A SCHEDULED job has been received by the captain from the scheduler to schedule. A DISPATCHED job has started to run on a remote member. A COMPLETED job has finished running on the remote member. |  |
| `saved_search` | The name of the saved-search from the associated savedsearches.conf file. |  |
| `savedsearchtype` | The scheduler manages three kinds of scheduled jobs, regular savedsearch for both realtime and historical, autosummary report acceleration build searches, and tsidx tsidx build searches. |  |
| `search_app` | The application in which the savedsearch was created. |  |
| `search_owner` | The owner of the saved search. |  |

### `/services/shcluster/captain/jobs/{name}`

#### GET

Get running and recently finished jobs for {name} cluster.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `ATTEMPT_[n]` | dispatch_time - The UTC time of dispatch for the job errormsg - If the job failed, capturing the reason for failure peer - GUID of the member that the job was sent to sid - the search id of this attempt success - a boolean for success/failure of the job |  |
| `job_state` | Job State can be SCHEDULED / DISPATCHED / COMPLETED . A SCHEDULED job has been received by the captain from the scheduler to schedule. A DISPATCHED job has started to run on a remote member. A COMPLETED job has finished running on the remote member. |  |
| `saved_search` | The name of the saved-search from the associated savedsearches.conf file. |  |
| `savedsearchtype` | The scheduler manages three kinds of scheduled jobs, regular savedsearch for both realtime and historical, autosummary report acceleration build searches, and tsidx tsidx build searches. |  |
| `search_app` | The application in which the savedsearch was created. |  |
| `search_owner` | The owner of the saved search. |  |

### `/services/shcluster/captain/members`

Lists the search head cluster members.

#### GET

List cluster members.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `adhoc_searchhead` | Flag to indicate if this member does not run scheduled searches. |  |
| `advertise_restart_required` | Flag to indicate if this peer advertised that it needed a restart. |  |
| `artifact_count` | Number of artifacts on this peer |  |
| `delayed_artifacts_to_discard` | List of artifacts waiting to be deleted from this peer. |  |
| `fixup_set` | N/A |  |
| `host_port_pair` | The host and management port advertised by this peer. |  |
| `kv_store_host_port` | Host and port of the kv store instance of this member. |  |
| `label` | The name for this member. Displayed on the Splunk Web manager page. |  |
| `last_heartbeat` | Timestamp for last heartbeat recieved from the peer |  |
| `peer_scheme_host_port` | URI of the current captain. |  |
| `pending_job_count` | Used by the captain to keep track of pending jobs requested by the captain to this member. |  |
| `replication_count` | Number of replications this peer is part of, as either source or target. |  |
| `replication_port` | TCP port to listen for replicated data from another cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `site` | N/A |  |
| `status` | Indicates the status of the member. Possible values are the following. Up Pending AutomaticDetention ManualDetention-PortsEnabled ManualDetention Restarting ShuttingDown ReassigningPrimaries Decommissioning GracefulShutdown Stopped Down BatchAdding |  |
| `status_counter` | Lists the number of buckets on the peer for each bucket status. Possible values are the following. Complete Complete (warm/cold) bucket NonStreamingTarget Target of replication for already completed (warm/cold) bucket PendingTruncate Bucket pending truncation PendingDiscard Bucket pending discard Standalone Bucket that is not replicated StreamingError Copy of streaming bucket where some error was encountered StreamingSource Streaming hot bucket on source side StreamingTarget Streaming hot bucket copy on target side Unset Uninitialized |  |

### `/services/shcluster/captain/members/{name}`

Get information about the {name} searchhead cluster member.

#### GET

Get information about the {name} searchhead cluster member.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `adhoc_searchhead` | Flag to indicate if this member does not run scheduled searches. |  |
| `advertise_restart_required` | Flag to indicate if this peer advertised that it needed a restart. |  |
| `artifact_count` | Number of artifacts on this peer. |  |
| `delayed_artifacts_to_discard` | List of artifacts waiting to be deleted from this peer. |  |
| `fixup_set` | N/A |  |
| `host_port_pair` | The host and management port advertised by this peer. |  |
| `kv_store_host_port` | Host and port of the kv store instance of this member. |  |
| `label` | The name for this member. Displayed on the Splunk Web manager page. |  |
| `last_heartbeat` | Timestamp for last heartbeat recieved from the peer |  |
| `peer_scheme_host_port` | URI of the current captain. |  |
| `pending_job_count` | Used by the manager to keep track of pending jobs requested by the manager to this peer. |  |
| `replication_count` | Number of replications this peer is part of, as either source or target. |  |
| `replication_port` | TCP port to listen for replicated data from another cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `site` | N/A |  |
| `status` | Indicates the status of the member. Possible values are the following. Up Pending AutomaticDetention ManualDetention-PortsEnabled ManualDetention Restarting ShuttingDown ReassigningPrimaries Decommissioning GracefulShutdown Stopped Down BatchAdding |  |
| `status_counter` | Lists the number of buckets on the peer for each bucket status. Possible values are the following. Complete Complete (warm/cold) bucket NonStreamingTarget Target of replication for already completed (warm/cold) bucket PendingTruncate Bucket pending truncation PendingDiscard Bucket pending discard Standalone Bucket that is not replicated StreamingError Copy of streaming bucket where some error was encountered StreamingSource Streaming hot bucket on source side StreamingTarget Streaming hot bucket copy on target side Unset Uninitialized |  |

### `/services/shcluster/config`

List search head cluster node configuration.

#### GET

List search head cluster node configuration.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cxn_timeout` | Low-level timeout, in seconds, for establishing connection between searchhead cluster nodes. Defaults to 60 seconds. |  |
| `disabled` | Indicates if this node is disabled. |  |
| `heartbeat_period` | Only valid for member nodes in a searchhead cluster. The time, in seconds, that a member attempts to send a heartbeat to the captain |  |
| `heartbeat_timeout` | Only valid for the captain node in a searchhead cluster configuration. The time, in seconds, before a captain considers a member down. Once a member is down, the captain initiates steps to replicate artifacts from the dead member to its live members. Defaults to 60 seconds. |  |
| `id` | Id of the SH cluster this member is a part of. |  |
| `max_peer_rep_load` | Maximum number of replications that can be ongoing as a target. |  |
| `mode` | Valid values: (disabled, member, captain, dynamic_captain) Defaults to disabled. Multiple values are permitted. Sets operational mode for this searchhead cluster node. Only one captain may exist per searchhead cluster. |  |
| `percent_peers_to_restart` | Percentage of peers to restart at the same time when doing a rolling restart. |  |
| `ping_flag` | For internal use to facilitate communication between the captain and members. |  |
| `quiet_period` | The time, in seconds, that a captain waits for members to add themselves to the searchhead cluster. |  |
| `rcv_timeout` | Low-level timeout, in seconds, for receiving data between searchhead cluster nodes. Defaults to 60 seconds. |  |
| `register_replication_address` | Valid only for nodes configured as members. The address on which a member is available for accepting replication data. This is useful in the cases where a member host machine has multiple interfaces and only one of them can be reached by another splunkd instance. |  |
| `rep_cxn_timeout` | Low-level timeout, in seconds, for establishing a connection for replicating data. |  |
| `rep_max_rcv_timeout` | Maximum cumulative time, in seconds, for receiving acknowledgement data from members. Defaults to 600s. |  |
| `rep_max_send_timeout` | Maximum time, in seconds, for sending replication slice data between searchhead cluster nodes. Defaults to 600s. |  |
| `rep_rcv_timeout` | Low-level timeout, in seconds, for receiving data between searchhead cluster nodes. |  |
| `rep_send_timeout` | Low-level timeout, in seconds, for sending replication data between searchhead cluster nodes. Defaults to 5 seconds. |  |
| `replication_factor` | Only valid for nodes configured as a captain. Determines how many copies of raw data are created in the searchhead cluster. This could be less than the number of searchhead cluster members. Must be greater than 0 and greater than or equal to the search factor. Defaults to 3. |  |
| `replication_port` | TCP port to listen for replicated data from another searchhead cluster member. |  |
| `replication_use_ssl` | Indicates whether to use SSL when sending replication data. |  |
| `restart_timeout` | Only valid for nodes configured as a captain. The amount of time, in seconds, the captain waits for a member to come back when the member is restarted (to avoid the overhead of trying to fix the artifacts that were on the member). Defaults to 600 seconds. Note: This only works if the member is restarted from Splunk Web. |  |
| `secret` | Secret shared among the nodes in the searchhead cluster to prevent any arbitrary node from connecting to the searchhead cluster. If a member or searchhead is not configured with the same secret as the captain, it is not able to communicate with the captain. Corresponds to pass4SymmKey setting in server.conf . |  |
| `send_timeout` | Low-level timeout, in seconds, for sending data between searchhead cluster nodes. Defaults to 60 seconds. |  |

### `/services/shcluster/config/config`

Configure search head cluster members.

#### POST

Configure search head cluster members.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `rolling_restart` | String | Sets the mode for search head cluster rolling restart. Options include: restart : Initiates a rolling restart in classic mode (no guarantee of search continuity). searchable : Initiates a rolling restart with minimum search interruption. |
| `decommission_search_jobs_wait_secs` | Integer | Specifies the amount of time, in seconds, that a search head cluster member waits for existing searches to complete before restarting. Default: 180 secs. |
| `manual_detention` | Use one of the following values: off : Default. Remove the target search head from the detention state. on : Put the target search head in manual detention mode. | Specifies whether to put the cluster member in manual detention. |
| `target_uri` | String | Specifies the target node you want to put in manual detention. |

### `/services/shcluster/member/artifacts`

Manage searchhead cluster member artifact configuration.

#### GET

List searchhead cluster members artifact configuration.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | Indicates the status of this artifact. Possible values are as follows. Complete The copy of this artifact contains the full complement of information. StreamingSource The copy of this artifact is sending data to member nodes for replication. StreamingTarget The copy of this artifact is receiving replicated data. NonStreamingTarget This copy of a warm artifact replication is in progress. Once replication is complete, the status changes to Complete. StreamingError The copy of this artifact encountered errors while streaming data. PendingTruncate The captain asked the member to truncate this copy of the artifact to a certain size and is waiting for confirmation. PendingDiscard The captain asked the member to discard this copy of the artifact and is waiting for confirmation. Standalone An artifact in the searchhead cluster that is not replicated. |  |

### `/services/shcluster/member/artifacts/{name}`

Get {name} member artifact configuration.

#### GET

List {name} member artifact information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | Indicates the status of this artifact. Possible values are as follows. Complete The copy of this artifact contains the full complement of information. StreamingSource The copy of this artifact is sending data to member nodes for replication. StreamingTarget The copy of this artifact is receiving replicated data. NonStreamingTarget This copy of a warm artifact replication is in progress. Once replication is complete, the status changes to Complete. StreamingError The copy of this artifact encountered errors while streaming data. PendingTruncate The captain asked the member to truncate this copy of the artifact to a certain size and is waiting for confirmation. PendingDiscard The captain asked the member to discard this copy of the artifact and is waiting for confirmation. Standalone An artifact in the searchhead cluster that is not replicated. |  |

### `/services/shcluster/member/control/control/set_manual_detention`

Put the search head cluster member in manual detention mode or take the search head cluster member out of this mode. When a search head cluster member is in manual detention, it does not accept new search jobs, including both scheduled and ad-hoc searches. Existing search jobs run to completion. It also participates in cluster administration operations with the exception of artifact replication.

#### POST

Adjust search head manual detention mode.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `manual_detention` | Use one of the following values. off : Default . Remove the search head from the detention state. on : Put the search head in manual detention mode. | Enable or disable manual detention. |

### `/services/shcluster/member/consensus`

Get latest cluster configuration from the raft consensus protocol.

#### GET

Get latest cluster configuration from the raft consensus protocol.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `configuration_id` | Unique id for this configuration. |  |
| `servers_list` | Comma-separated list of members that are part of the cluster. Each member is listed as scheme://host:port |  |

### `/services/shcluster/member/info`

Access searchhead cluster member node information.

#### GET

List member information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `active_historical_search_count` | Number of currently running historical searches. |  |
| `active_realtime_search_count` | Number of currently running realtime searches. |  |
| `adhoc_searchhead` | Flag that indicates if this member can run scheduled searches. |  |
| `is_registered` | Indicates if this member is registered with the searchhead cluster captain. |  |
| `last_heartbeat_attempt` | Timestamp for the last attempt to contact the captain. |  |
| `maintenance_mode` | N/A |  |
| `peer_load_stats_gla_15m` | Number of scheduled searches run in the last 15 minutes. |  |
| `peer_load_stats_gla_1m` | Number of scheduled searches run in the last one minute. |  |
| `peer_load_stats_gla_5m` | Number of scheduled searches run in the last five minutes. |  |
| `peer_load_stats_max_runtime` | N/A |  |
| `peer_load_stats_num_autosummary` | N/A |  |
| `peer_load_stats_num_historical` | N/A |  |
| `peer_load_stats_num_realtime` | N/A |  |
| `peer_load_stats_num_running` | N/A |  |
| `peer_load_stats_total_runtime` | N/A |  |
| `restart_state` | Indicates whether the member needs to be restarted to enable its searchhead cluster configuration. |  |
| `status` | Indicates the status of the member. Possible values are as follows. Up Pending AutomaticDetention ManualDetention Restarting ShuttingDown ReassigningPrimaries Decommissioning GracefulShutdown Down |  |

### `/services/shcluster/status`

Performs health checks to determine search head cluster health status, prior to a rolling upgrade or rolling restart.

#### GET

Get search head cluster health status information .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `advanced` | Boolean | Lists search head cluster status information in a verbose manner. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Captain` | decommission_search_jobs_wait_secs | Integer |
| `Member` | label | String |

### `/services/upgrade/shc/recovery`

Return search head cluster to ready state after automated rolling upgrade failure.

#### POST

Return SHC to ready state after automated rolling upgrade failure.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | String | Status of HTTP request. For example, "succeeded" or "failed" |

### `/services/upgrade/shc/status`

Check the status of an automated search head cluster rolling upgrade.

#### GET

Check the status of automated SHC rolling upgrade.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `upgrade status` | String | Status of automated rollling upgrade for entire clutser. |
| `peers_to_upgrade` | Number | The total number of cluster members to upgrade. |
| `overall_peers_upgraded` | Number | The number of cluster members upgraded at present. |
| `overall_peers_upgraded_percentage` | Number | The percentage of total cluster members upgraded at present. |
| `status` | String | Upgrade status of the individual cluster member. |
| `last_modified` | String | Date and time the individual cluster member was modified. |

### `/services/upgrade/shc/upgrade`

Initiate an automated rolling upgrade of a search head cluster.

#### POST

Initiate automated SHC rolling upgrade.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | String | Status of HTTP request. For example, "succeeded" or "failed". |

---

## Configuration

### `/services/configs/conf-{file}`

Access and update a .conf configuration file.

#### GET

List {file} configuration file stanzas.

#### POST

Add stanza to {file} configuration file.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `<variable>` | String | Arbritrary number of key/value pairs. |

### `/services/configs/conf-{file}/{stanza}`

#### DELETE

Delete {stanza} in {file} configuration file.

#### GET

Get {stanza} in {file} configuration file.

#### POST

Update or add property to {stanza} in {file} configuration file.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `<variable>` | String | Arbitrary number of key/value pairs to update. |

---

## Deployment

### `/services/deployment/client`

List deployment client configuration and status.

#### GET

Get deployment client list with enabled status, server class, and host and port number of each.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Disabled status: 0 = Enabled 1 = Disabled |  |
| `serverClasses` | List of member server classes for app download authorization. |  |
| `targetUri` | Host and port number ( <host>:<port> ). |  |

### `/services/deployment/client/config`

#### GET

Get deployment client enabled status, server class for app distribution, and host and port number.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Disabled status: 0 = Enabled 1 = Disabled |  |
| `serverClasses` | List of member server classes for app download authorization. |  |
| `targetUri` | Host and port number ( <host>:<port> ). |  |

### `/services/deployment/client/config/listIsDisabled`

#### GET

Get deployment client disabled status.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Disabled status: 0 = Enabled 1 = Disabled |  |

### `/services/deployment/client/config/reload`

Access information on reloading the named client.

#### POST

Access client reload information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `200` | Endpoint returned successfully. |  |
| `400` | Request error. See response body for details. |  |
| `401` | Authentication failure: must pass valid credentials with request. |  |
| `403` | Insufficient permissions to access resource. |  |
| `404` | Specified resoruce does not exist. |  |
| `409` | Request error: this operation is invalid for this item. See response body for details. |  |
| `500` | Internal server error. See response body for details. |  |

### `/services/deployment/client/{name}/reload`

Restart and reload the {name} deployment client.

#### POST

Restart and reload {name} deployment client.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Disabled status: 0 = Enabled 1 = Disabled |  |
| `serverClasses` | List of member server classes for app download authorization. |  |
| `targetUri` | Host and port number ( <host>:<port> ). |  |

### `/services/deployment/server/applications`

List distributed apps.

#### GET

List distributed apps, including distributed state information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `clientId` | String |  |
| `hasDeploymentError` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `archive` | Disk location of the archived version of the app. |  |
| `clientId` | Deployment client ID associated with the app, an MD5 hash value of serialized (catenated) client attributes. |  |
| `hasDeploymentError` | Indicates deployment fault status on at least one deployment client: 0 = Do not include apps with a deployment fault indication. 1 = Include apps with a deployment fault indication. |  |
| `loadtime` | Last deployment server app loaded or reloaded date and time. An application not mapped to serverclasses is not loaded so loadtime is 0 . |  |
| `restartSplunkWeb` | Restart Splunk Web indication: 0 = Do not restart Splunk Web. 1 = Restart Splunk Web. |  |
| `restartSplunkd` | Restart splunkd indication: 0 = Do not restart splunkd. 1 = Restart splunkd. |  |
| `serverclasses` | List of server classes associated with the application. |  |
| `size` | Size on disk of the compressed app (bundle), in bytes. |  |
| `stateOnClient` | App enablement status: 0 = Not enabled. 1 = Enabled. |  |

### `/services/deployment/server/applications/{name}`

Get or update distribution information for {name} app.

#### GET

Get {name} app distribution information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `archive` | Disk location of archived version of the app. |  |
| `clientId` | Deployment client ID associated with the app, an MD5 hash value of serialized (catenated) client attributes. |  |
| `hasDeploymentError` | Indicates deployment fault status on at least one deployment client: 0 = Do not include apps with a deployment fault indication. 1 = Include apps with a deployment fault indication. |  |
| `loadtime` | Last deployment server app loaded or reloaded date and time. An application not mapped to serverclasses is not loaded so loadtime is 0 . |  |
| `restartSplunkWeb` | Restart Splunk Web indication: 0 = Do not restart Splunk Web. 1 = Restart Splunk Web. |  |
| `restartSplunkd` | Restart splunkd indication: 0 = Do not restart splunkd. 1 = Restart splunkd. |  |
| `serverclasses` | List of server classes associated with the application. |  |
| `size` | Size on disk of the compressed app (bundle), in bytes. |  |
| `stateOnClient` | App enablement status: 0 = Not enabled. 1 = Enabled. |  |

#### POST

Update {name} app distribution information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blacklist.*` | String |  |
| `continueMatching` | Boolean |  |
| `deinstall` | Boolean |  |
| `filterType` | Enum |  |
| `machineTypesFilter` | String |  |
| `repositoryLocation` | String |  |
| `restartSplunkWeb` | Boolean |  |
| `restartSplunkd` | Boolean |  |
| `serverclass` | String |  |
| `stateOnClient` | Enum |  |
| `targetRepositoryLocation` | String |  |
| `tmpFolder` | String |  |
| `unmap` | Boolean |  |
| `whitelist.*` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `archive` | Specifies the location of the compressed version ( bundle ) of the app. |  |
| `blacklist.*` | Regular expressions used to exclude, when mapping this application to a client. If a client matches any of the blacklist regular expressions, it does not receive the application. The * is replaced by an integral ordinal number. |  |
| `continueMatching` | If true, configuration lookups continue matching server classes, beyond the first match. If false, only the first match is used. |  |
| `filterType` | blacklist) Determines the order of execution of filters. If filterType is whitelist, all whitelist filters are applied first, followed by blacklist filters. If filterType is blacklist, all blacklist filters are applied first, followed by whitelist filters. See description for the filterType POST parameter for more information. |  |
| `loadtime` | Specifies the date and time the application was last loaded (or reloaded) by the deployment server. An application not mapped to any serverclasses does not get loaded, thus its loadtime attribute is 0; in epoch terms, which is 01 Jan 1970 at midnight GMT. |  |
| `machineTypesFilter` | List of filters to be used in Boolean and logic with whitelist and blacklist filters. |  |
| `repositoryLocation` | The location on the deployment server to store the content that is to be deployed for this server class. |  |
| `restartSplunkWeb` | Indicates whether to restart Splunk Web. |  |
| `restartSplunkd` | Indicates whether to restart splunkd. |  |
| `serverclass` | The name of the server class to which the application is mapped. |  |
| `serverclasses` | List of server classes associated with the application. |  |
| `size` | Indicates in bytes the size on disk of the compressed version ( bundle ) of the application. |  |
| `stateOnClient` | Specifies whether the deployment client is enabled or disabled. |  |
| `targetRepositoryLocation` | The location on the deployment client to install the apps defined for this Deployment Server. If unset, or set to empty, the repositoryLocation path is used. |  |
| `tmpFolder` | Working folder used by deployment server. |  |
| `whitelist.*` | Regular expressions used to accept, when mapping this application to a client. If a client matches any of the whitelist regular expressions, it accepts the application. The * is replaced by an integral ordinal number. |  |

### `/services/deployment/server/clients`

Provides access to information about clients to a deployment server.

#### GET

Access information about clients to a deployment server.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action` | String |  |
| `application` | String |  |
| `hasDeploymentError` | Boolean | False |
| `maxPhonehome_latency_to_avgInterval_ratio` | Number |  |
| `minLatestPhonehomeTime` | Number |  |
| `minPhonehome_latency_to_avgInterval_ratio` | Number |  |
| `serverclasses` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `applications` | List of applications deployed to the deployment client. |  |
| `averagePhoneHomeInterval` | The average phone home interval, in seconds. |  |
| `build` | The build number for the Splunk instance on the deployment client. |  |
| `dns` | The DNS lookup name of the deployment client server. |  |
| `guid` | Identifier for the deployment server client. |  |
| `hasDeploymentError` | Specifies whether to check for clients with a deployment error. |  |
| `hostname` | The host name of the deployment client server. |  |
| `id` | ID for the client based on client name and IP address. |  |
| `ip` | The IP address of the client to the deployment server. |  |
| `lastPhoneHomeTime` | The last time the deployment client phones home to the deployment server, in epoch time. |  |
| `mgmt` | The managment port for the deployment client. |  |
| `minLatestPhonehomeTime` | Specifies in epoch seconds the minimum latency for a client to contact the deployment server. |  |
| `minPhonehome_latency_to_avgInterval_ratio` | The minimum value specified for the ratio of the phone home latency to the average phone home interval. |  |
| `serverclasses` | List of server classes for the deployment client. |  |
| `utsname` | Machine type for the deployment server client. |  |

### `/services/deployment/server/clients/countClients_by_machineType`

Access information about deployment clients to this server according to the machine type of the client.

#### GET

List the count of deployment clients for this server by machine type.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `counts` | The list of machine types for this deployment client, showing the count of each machine type. |  |

### `/services/deployment/server/clients/countRecentDownloads`

Access the count of the number of downloads from this client to the deployment server during the last specified time period.

#### GET

Return the count of the number of downloads from this client to the deployment server during the last specified time period.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `maxAgeSecs required` | Number |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `count` | The number of recent downloads. |  |

### `/services/deployment/server/clients/{name}`

Get client information or remove a client.

#### DELETE

Remove the specified client from the deployment server registry. The next time the client "phones home" the record is re-created.

#### GET

Lists information about the named client to the deployment server.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `application` | String |  |
| `hasDeploymentError` | Boolean |  |
| `maxPhonehome_latency_to_avgInterval_ratio` | Number |  |
| `minLatestPhonehomeTime` | Number |  |
| `minPhonehome_latency_to_avgInterval_ratio` | Number |  |
| `serverclasses` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `application` | The name of the application specified to filter the results of this call. |  |
| `applications` | List of applications deployed to the deployment client. |  |
| `averagePhoneHomeInterval` | The average phone home interval, in seconds. |  |
| `build` | The build number for the Splunk instance on the deployment client. |  |
| `dns` | The DNS lookup name of the deployment client server. |  |
| `guid` | Identifier for the deployment server client. |  |
| `hasDeploymentError` | Specifies whether to check for clients with a deployment error. |  |
| `hostname` | The host name of the deployment client server. |  |
| `id` | ID for the client based on client name and IP address. |  |
| `ip` | The IP address of the client to the deployment server. |  |
| `lastPhoneHomeTime` | The last time the deployment client phones home to the deployment server, in epoch time. |  |
| `maxPhonehome_latency_to_avgInterval_ratio` | The maximum value specified for the ratio of the phone home latency to the average phone home interval. |  |
| `mgmt` | The managment port for the deployment client. |  |
| `minLatestPhonehomeTime` | Specifies in epoch seconds the minimum latency for a client to contact the deployment server. |  |
| `minPhonehome_latency_to_avgInterval_ratio` | The minimum value specified for the ratio of the phone home latency to the average phone home interval. |  |
| `serverClasses` | The list of server classes to which the client belongs. |  |
| `serverclasses` | List of server classes for the deployment client. |  |
| `utsname` | Machine type for the deployment server client. |  |

### `/services/deployment/server/config`

#### POST

List configuration information for all deployment servers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `currentDownloads` | The number of current downloads for this deployment server. |  |
| `disabled` | Indicates whether the deployment server is disabled. |  |
| `loadTime` | The time, in epoch seconds, the serverclass for this server was loaded. |  |
| `repositoryLocation` | The location on the deployment server to store the content that is to be deployed. |  |
| `whitelist.0` | Lists the contents of whitelist.0. |  |

### `/services/deployment/server/config/attributesUnsupportedInUI`

#### GET

Lists deployment server attributes that cannot be configured from Splunk Web.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `property` | The attribute that cannot be configured from Splunk Web. |  |
| `reason` | The reason an attribute cannot be configured from Splunk Web. |  |
| `stanza` | In Splunk Enterprise, the stanza in serverclass.conf that lists deployment server attributes that cannot be configured from Splunk Web. |  |

### `/services/deployment/server/config/listIsDisabled`

Access deployment server enablement status.

#### GET

Access deployment server enablement status.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the deployment server is disabled. |  |

### `/services/deployment/server/serverclasses`

Access information about server classes.

#### GET

List server classes for this deployment server.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `blacklist-size` | The number of entires in the blacklist for this serverclass. |  |
| `clientId` | ID of deployment client for this server class. |  |
| `currentDownloads` | Number of applications currently downloaded. |  |
| `hasDeploymentError` | Indicates whether the serverclass has at least one deployment error. |  |
| `loadTime` | The time, in epoch seconds, this serverclass was loaded. |  |
| `machineTypesFilter` | List of filters to be used in Boolean and logic with whitelist and blacklist filters. |  |
| `repositoryList` | List of applications stored at the location specified by repositoryLocation. |  |
| `repositoryLocation` | The location on the deployment server to store the content that is to be deployed for this server class. |  |
| `restartSplunkWeb` | Indicates whether to restart Splunk Web. |  |
| `restartSplunkd` | Indicates whether to restart splunkd. |  |
| `stateOnClient` | Indicates whether this server class is enabled or disabled. |  |
| `whitelist-size` | Specifies the number of entries in the whitelist for this server class. |  |
| `whitelist.0` | List of servers for whitelist.0 for this server class. |  |

#### POST

Create a server class.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String |  |
| `blacklist.*` | String |  |
| `continueMatching` | Boolen |  |
| `filterType` | Enum |  |
| `machineTypesFilter` | String |  |
| `repositoryLocation` | String |  |
| `restartSplunkWeb` | Boolean |  |
| `restartSplunkd` | Boolean |  |
| `stateOnClient` | Enum |  |
| `targetRepositoryLocation` | String |  |
| `tmpFolder` | String |  |
| `whitelist.*` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `blacklist-size` | The number of entries in the blacklist for this serverclass. |  |
| `blacklist.*` | Regular expressions used to exclude for this server class. If a client matches any of the blacklist regular expressions, it is not included in the server class. The * is replaced by an integral ordinal number. |  |
| `continueMatching` | If true, configuration lookups continue matching server classes, beyond the first match. If false, only the first match is used. |  |
| `currentDownloads` | Number of applications currently downloaded. |  |
| `filterType` | blacklist) Determines the order of execution of filters. If filterType is whitelist, all whitelist filters are applied first, followed by blacklist filters. If filterType is blacklist, all blacklist filters are applied first, followed by whitelist filters. See description for the filterType POST parameter for more information. |  |
| `loadTime` | The time, in epoch seconds, this serverclass was loaded. |  |
| `machineTypesFilter` | List of filters to be used in Boolean and logic with whitelist and blacklist filters. |  |
| `repositoryList` | List of applications stored at the location specified by repositoryLocation. |  |
| `repositoryLocation` | The location on the deployment server to store the content that is to be deployed for this server class. |  |
| `restartSplunkWeb` | Indicates whether to restart Splunk Web. |  |
| `restartSplunkd` | Indicates whether to restart splunkd. |  |
| `stateOnClient` | Specifies whether the deployment client is enabled or disabled. |  |
| `targetRepositoryLocation` | The location on the deployment client to install the apps defined for this Deployment Server. If unset, or set to empty, the repositoryLocation path is used. That is, defaults to: $SPLUNK_HOME/etc/apps (the live configuration directory for a Splunk deployment. Useful only with complex (for example, tiered) deployment strategies. |  |
| `tmpFolder` | Working folder used by deployment server. Defaults to $SPLUNK_HOME/var/run/tmp |  |
| `whitelist-size` | Specifies the number of entries in the whitelist for this server class. |  |
| `whitelist.*` | Regular expressions used to accept for this server class. If a client matches any of the whitelist regular expressions, it is included in the server class. The * is replaced by an integral ordinal number. |  |

### `/services/deployment/server/serverclasses/rename`

Rename a server class.

#### POST

Specify a new name for a server class.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `newName required` | String |  |
| `oldName required` | String |  |

### `/services/deployment/server/serverclasses/{name}`

Manage the {name} serverclass.

#### DELETE

Remove the specfied server class from this deployment server.

#### GET

List information about the named server class.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `clientId` | String |  |
| `hasDeploymentError` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `blacklist-size` | Specifies the size of the blacklist for the named server class. |  |
| `clientId` | ID of deployment client for this server class. |  |
| `currentDownloads` | The number of entires in the blacklist for this serverclass. |  |
| `hasDeploymentError` | Indicates whether the serverclass has at least one deployment error. |  |
| `loadTime` | The time, in epoch seconds, this serverclass was loaded. |  |
| `machineTypesFilter` | List of filters to be used in Boolean and logic with whitelist and blacklist filters. |  |
| `repositoryList` | List of applications stored at the location specified by repositoryLocation. |  |
| `repositoryLocation` | The location on the deployment server to store the content that is to be deployed for this server class. |  |
| `restartSplunkWeb` | Indicates whether to restart Splunk Web. |  |
| `restartSplunkd` | Indicates whether to restart splunkd. |  |
| `stateOnClient` | Indicates whether this server class is enabled or disabled. |  |
| `whitelist-size` | Specifies the number of entries in the whitelist for this server class. |  |
| `whitelist.0` | List of servers for whitelist.0 for this server class. |  |

#### POST

Update the named server class.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blacklist.*` | String |  |
| `continueMatching` | Boolen |  |
| `filterType` | Enum |  |
| `machineTypesFilter` | String |  |
| `repositoryLocation` | String |  |
| `restartSplunkWeb` | Boolean |  |
| `restartSplunkd` | Boolean |  |
| `stateOnClient` | Enum |  |
| `targetRepositoryLocation` | String |  |
| `tmpFolder` | String |  |
| `whitelist.*` | String |  |

### `/services/search/distributed/bundle/replication/config`

Provides information on knowledge bundle replication configuration on a search head.

#### GET

List knowledge bundle replication configuration settings.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `concerningReplicatedFileSize` | A warning will be logged if the bundle lookup size exceeds this value |  |
| `connectionTimeout` | Timeout value for establishing connection between search head and indexer |  |
| `maxBundleSize` | Maximum allowable bundle size |  |
| `receiveTimeout` | Timeout value for receiving data between search head and indexer |  |
| `replicationPeriod` | Period during which the replicationThread checks whether bundle replication is required |  |
| `replicationPolicy` | Bundle replication policy in use |  |
| `sendTimeout` | Timeout value for sending data between search head and indexer |  |
| `statusQueueSize` | Size of the cycles maintained in memory and available through the cycles endpoint |  |

### `/services/search/distributed/bundle/replication/cycles`

Provides information and status for knowledge bundle replication cycles on a search head.

#### GET

List information and status for knowledge bundle replication cycles..

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `latest` | Boolean | Optional. If set to true , information about only the latest cycle is returned. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `bundle_id` | Knowledge bundle unique identifier composed of hostname-creation_time |  |
| `current_bundle` | Path to active knowledge bundle on disk |  |
| `current_repl_start_time` | Start time of current replication cycle |  |
| `cycle_id` | Bundle replication cycle unique identifier |  |
| `delta_path` | Path to the delta knowledge bundle on disk, if a delta was created |  |
| `is_repl_in_progress` | Boolean to indicate whether the replication cycle is in progress or completed |  |
| `peers_status` | Entry for each peer with peer_name and replication state for each peer |  |
| `replicationPolicy` | Bundle replication policy in use |  |

### `/services/search/distributed/bundle-replication-files`

Access information for the most recent distributed search bundle.

#### GET

List distributed search bundle replication files.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `checksum` | Common checksum for entities in the bundle. |  |
| `filename` | Bundle file name |  |
| `location` | Bundle file path |  |
| `size` | Bundle size, in bytes |  |
| `timestamp` | Bundle creation timestamp. |  |

### `/services/search/distributed/bundle-replication-files/{name}`

Get {name} bundle replication file information.

#### GET

List information about the specified bundle replication file. For {name} , specify the checksum for the file.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `force_list_all` | Boolean |  |

### `/services/search/distributed/config`

#### GET

Lists the configuration options for the distributed search system.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `autoAddServers` | [Deprecated] |  |
| `blacklistNames` | List of filenames that match the blacklist pattern, and are not replicated. |  |
| `blacklistURLs` | List of URLs that are blacklisted, and thus is not replicated. |  |
| `checkTimedOutServersFrequency` | Rechecks servers at the specified frequency (in seconds). If this is set to 0, then no recheck occurs. Defaults to 60. This attribute is ONLY relevant if removeTimedOutServers is set to true . If removeTimedOutServers is false , this attribute is ignored. |  |
| `connectionTimeout` | Connection timeout. |  |
| `disabled` | Indicates if the distributed search is disabled. |  |
| `dist_search_enabled` | Indicates if the distributed search is enabled. |  |
| `heartbeatFrequency` | [Deprecated] |  |
| `heartbeatMcastAddr` | [Deprecated] |  |
| `heartbeatPort` | [Deprecated] |  |
| `receiveTimeout` | Amount of time in seconds to use as a timeout while trying to read/receive data from a search peer. |  |
| `removedTimedOutServers` | If true, removes a server connection that cannot be made within serverTimeout. If false, every call to that server attempts to connect. This may result in a slow user interface. |  |
| `sendTimeout` | Send timeout. |  |
| `serverTimeout` | [Deprecated] Refer to connectionTimeout , sendTimeout , and receiveTimeout . |  |
| `servers` | The initial list of servers. If operating completely in autoAddServers mode (discovering all servers), there is no need to list any servers here. |  |
| `shareBundles` | Indicates whether this server uses bundle replication to share search time configuration with search peers. If set to false, the search head assumes that the search peers can access the correct bundles using an NFS share and have correctly configured the options listed under: "SEARCH HEAD BUNDLE MOUNTING OPTIONS." |  |
| `skipOurselves` | [Deprecated] |  |
| `statusTimeout` | Set connection timeout when gathering a search peer's basic info (/services/server/info). Read/write timeouts are automatically set to twice this value. |  |
| `ttl` | [Deprecated] |  |

### `/services/search/distributed/peers`

#### GET

Get configured search peers to which this search head is configured to distribute searches. This includes configured but disabled search peers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `build` | The Splunk build number for this peer. |  |
| `bundle_versions` | The IDs of the bundles (of this search head) that the peer has. The IDs are sorted from latest to earliest. |  |
| `disabled` | Indicates if the peer is disabled. |  |
| `guid` | GUID of the peer. |  |
| `is_https` | Inidcates if the management port is using SSL. |  |
| `licenseSignature` | The license signature. |  |
| `peerName` | The Splunk server name of the peer. |  |
| `peerType` | Specifies whether the peer is configured or discovered. |  |
| `replicationStatus` | The status of bundle replication to this peer. Can be any of the following values: Initial In progress Failed Successful Mounted |  |
| `status` | The status of the peer. Can be one of the following values: Up Down Blacklisted Not a Splunk server Free Splunk server Authentication Failed Duplicate License Duplicate Servername Inconsistent bundles |  |
| `status_details` | Details of any errors encountered in the last heartbeat period. |  |
| `version` | The Splunk software version string this peer is running. |  |

#### POST

Add a new distributed search peer.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `remotePassword` | String | ✓ |
| `remoteUsername` | String | ✓ |

### `/services/search/distributed/peers/{name}`

Manage distributed peer servers. A search peer is defined as a Splunk server to which another Splunk server distributes searches. The Splunk server where the search request originates is referred to as the search head.

#### POST

Update a peer server.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `remotePassword` | String | ✓ |
| `remoteUsername` | String | ✓ |

---

## Federated Search

### `/services/data/federated/settings/general`

Use this endpoint to review the general settings for your Splunk platform deployment implementation of Federated Search for Splunk and change those settings as necessary. For an overview of Federated Search for Splunk, see About Federated Search for Splunk in Federated Search .

#### GET

Provides the current general federated search settings for your Splunk platform deployment.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether federated search functionality is turned on for your Splunk platform deployment. If disabled = false , federated search functionality is turned on for your deployment. If disabled = true , federated search functionality is turned off for your deployment. Defaults to false . |  |
| `transparent_mode` | Specifies whether transparent mode federated search functionality is turned on for your Splunk platform deployment. If set to true , transparent mode is turned on, which means federated search users on your deployment can run federated searches over transparent mode federated providers as well as standard mode federated providers. If set to false , transparent mode is turned off, which means federated search users on your deployment can run federated searches only over standard mode federated providers. Defaults to true . |  |
| `controlCommandsFeatureEnabled` | Specifies whether a federated search head can send a federated search action, such as a search cancellation, to federated providers. Does not support search pause. Defaults to true . |  |
| `controlCommandsMaxThreads` | The maximum number of threads that can run a federated search action, such as a search cancellation, from a federated search head, on federated providers. Does not support search pause. Defaults to 5 . |  |
| `controlCommandsMaxTimeThreshold` | The maximum number of seconds that a federated search head waits for the completion of a federated search action such as a search cancellation. Does not support search pause. Defaults to 5 . |  |
| `heartbeatEnabled` | Specifies whether the federated search heartbeat mechanism is running. The heartbeat mechanism monitors the remote federated providers. If it detects problems with the federated providers the heartbeat mechanism can tell you what is wrong and take actions. Defaults to true . |  |
| `max_preview_generation_duration` | The maximum amount of time, in seconds, that the search head can spend to generate search result previews. When this limit is reached by a federated search, preview preview generation is halted, but the search continues gathering results until it completes and displays the final result set. A setting of 0 means that the preview generation duration of federated searches is unlimited. Defaults to 0 . |  |
| `needs_consent` | When set to true , needs_consent causes a checkbox to appear in the UI for federated provider definitions and index assignment to roles. This checkbox requires that users acknowledge that federated providers and federated index permissions can be set up in a manner detrimental to regulatory compliance. When set to false , needs_consent hides this checkbox. Defaults to true . |  |
| `proxyBundlesTTL` | Specifies the time to live in seconds of a proxy bundle on the remote search head after the last time it was used by a search. Defaults to 172800 seconds, or 2 days. |  |
| `remoteEventsDownloadRetryCountMax` | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the maximum number of event download retries that the federated search head can make before it reports an event download failure. Related to remoteEventsDownloadRetryTimeoutMs . Defaults to 20 event download retries. |  |
| `remoteEventsDownloadRetryTimeoutMs` | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the interval, in milliseconds, between retries of a failed event download from a federated provider. Related to remoteEventsDownloadRetryCountMax . Defaults to 1000 . |  |
| `verbose_mode` | Specifies whether federated searches can be run in verbose mode. A setting of false restricts the ability of federated searches to run in verbose mode, while allowing federated searches to run in fast or smart mode. In transparent mode, a setting of false means that Splunk software runs only the local portion of a verbose mode federated search. In standard mode, a setting of false terminates verbose mode federated searches without displaying their results. Defaults to true . |  |

#### POST

Updates general federated search settings. Can be used to turn federated search functionality on or off for a Splunk platform deployment.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean | When set to false , disabled specifies that federated search functionality is turned on for your Splunk platform deployment. When set to true , disabled specifies that federated search functionality is turned off for your Splunk platform deployment. Defaults to false . |
| `transparent_mode` | Boolean | When set to true , transparent_mode specifies that transparent mode federated search functionality is turned on for your Splunk platform deployment, which means that federated search users on your deployment can run federated searches over transparent mode federated providers as well as standard mode federated providers. When set to false , transparent_mode specifies that transparent mode federated search functionality is turned off for your Splunk platform deployment, which means that federated search users on your deployment can run federated searches only over standard mode federated providers. Defaults to true . Note: After turning on or off transparent mode, you must call _reload by running the following HTTP POST request; otherwise the change won't take effect: curl -k -u admin:changeme -X POST https://localhost:management-port/services/configs/conf-federated/_reload |
| `controlCommandsFeatureEnabled` | Boolean | Specifies whether a federated search head can send a federated search action, such as a search cancellation, to federated providers. Does not support search pause. Defaults to true . Change this setting only when instructed to do so by Splunk Support. |
| `controlCommandsMaxThreads` | Number | The maximum number of threads that can run a federated search action, such as a search cancellation, from a federated search head, on federated providers. Does not support search pause. Defaults to 5 . Change this setting only when instructed to do so by Splunk Support. |
| `controlCommandsMaxTimeThreshold` | Number | The maximum number of seconds that a federated search head waits for the completion of a federated search action such as a search cancellation. Does not support search pause. Defaults to 5 . Change this setting only when instructed to do so by Splunk Support. |
| `heartbeatEnabled` | Boolean | Specifies whether the federated search heartbeat mechanism is running. The heartbeat mechanism monitors the remote federated providers. If it detects problems with the federated providers the heartbeat mechanism can tell you what is wrong and take actions. Defaults to true . Change this setting only when instructed to do so by Splunk Support. |
| `max_preview_generation_duration` | Number | The maximum amount of time, in seconds, that the search head can spend to generate search result previews. When this limit is reached by a federated search, preview preview generation is halted, but the search continues gathering results until it completes and displays the final result set. A setting of 0 means that the preview generation duration of federated searches is unlimited. Defaults to 0 . Change the value of this setting to a number above zero if you find that your federated searches are terminated because their preview generation duration exceeds a timeout set by another component in your network, such as an elastic load balancer (ELB). For example, if you have an ELB that times out your searches after 60 seconds, set max_preview_generation_duration to 55 . |
| `needs_consent` | Boolean | When set to true , needs_consent causes a checkbox to appear in the UI for federated provider definitions and index assignment to roles. This checkbox requires that users acknowledge that federated providers and federated index permissions can be set up in a manner detrimental to regulatory compliance. When set to false , needs_consent hides this checkbox. Defaults to true . Change this setting only when instructed to do so by Splunk Support. |
| `proxyBundlesTTL` | Number | Specifies the time to live in seconds of a proxy bundle on the remote search head after the last time it was used by a search. Defaults to 172800 seconds, or 2 days. Change this setting only when instructed to do so by Splunk Support. |
| `remoteEventsDownloadRetryCountMax` | Number | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the maximum number of event download retries that the federated search head can make before it reports an event download failure. Related to remoteEventsDownloadRetryTimeoutMs . Defaults to 20 event download retries. Change this setting only when instructed to do so by Splunk Support. |
| `remoteEventsDownloadRetryTimeoutMs` | Number | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the interval, in milliseconds, between retries of a failed event download from a federated provider. Related to remoteEventsDownloadRetryCountMax . Defaults to 1000 . Change this setting only when instructed to do so by Splunk Support. |
| `verbose_mode` | Boolean | Specifies whether federated searches can be run in verbose mode. A setting of false restricts the ability of federated searches to run in verbose mode, while allowing federated searches to run in fast or smart mode. In transparent mode, a setting of false means that Splunk software runs only the local portion of a verbose mode federated search. In standard mode, a setting of false terminates verbose mode federated searches without displaying their results. Defaults to true . Change this setting only when instructed to do so by Splunk Support. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether federated search functionality is turned on for your Splunk platform deployment. If disabled = false , federated search functionality is turned on for your deployment. If disabled = true , federated search functionality is turned off for your deployment. Defaults to false . |  |
| `transparent_mode` | Specifies whether transparent mode federated search functionality is turned on for your Splunk platform deployment. If set to true , transparent mode is turned on, which means federated search users on your deployment can run federated searches over transparent mode federated providers as well as standard mode federated providers. If set to false , transparent mode is turned off, which means federated search users on your deployment can run federated searches only over standard mode federated providers. Defaults to true . |  |
| `controlCommandsFeatureEnabled` | Specifies whether a federated search head can send a federated search action, such as a search cancellation, to federated providers. Does not support search pause. Defaults to true . |  |
| `controlCommandsMaxThreads` | The maximum number of threads that can run a federated search action, such as a search cancellation, from a federated search head, on federated providers. Does not support search pause. Defaults to 5 . |  |
| `controlCommandsMaxTimeThreshold` | The maximum number of seconds that a federated search head waits for the completion of a federated search action such as a search cancellation. Does not support search pause. Defaults to 5 . |  |
| `heartbeatEnabled` | Specifies whether the federated search heartbeat mechanism is running. The heartbeat mechanism monitors the remote federated providers. If it detects problems with the federated providers the heartbeat mechanism can tell you what is wrong and take actions. Defaults to true . |  |
| `max_preview_generation_duration` | The maximum amount of time, in seconds, that the search head can spend to generate search result previews. When this limit is reached by a federated search, preview preview generation is halted, but the search continues gathering results until it completes and displays the final result set. A setting of 0 means that the preview generation duration of federated searches is unlimited. Defaults to 0 . |  |
| `needs_consent` | When set to true , needs_consent causes a checkbox to appear in the UI for federated provider definitions and index assignment to roles. This checkbox requires that users acknowledge that federated providers and federated index permissions can be set up in a manner detrimental to regulatory compliance. When set to false , needs_consent hides this checkbox. Defaults to true . |  |
| `proxyBundlesTTL` | Specifies the time to live in seconds of a proxy bundle on the remote search head after the last time it was used by a search. Defaults to 172800 seconds, or 2 days. |  |
| `remoteEventsDownloadRetryCountMax` | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the maximum number of event download retries that the federated search head can make before it reports an event download failure. Related to remoteEventsDownloadRetryTimeoutMs . Defaults to 20 event download retries. |  |
| `remoteEventsDownloadRetryTimeoutMs` | When you run a verbose-mode federated search, the federated search head downloads events from the federated provider. This setting provides the interval, in milliseconds, between retries of a failed event download from a federated provider. Related to remoteEventsDownloadRetryCountMax . Defaults to 1000 . |  |
| `verbose_mode` | Specifies whether federated searches can be run in verbose mode. A setting of false restricts the ability of federated searches to run in verbose mode, while allowing federated searches to run in fast or smart mode. In transparent mode, a setting of false means that Splunk software runs only the local portion of a verbose mode federated search. In standard mode, a setting of false terminates verbose mode federated searches without displaying their results. Defaults to true . |  |

### `/services/data/federated/provider`

Use this endpoint to get a list of federated providers and post new federated provider definitions. Some of these settings are exclusive to Federated Search for Splunk, while other settings are exclusive to Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform.

#### GET

Returns a list of federated providers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | Specifies the federated provider type. If you have a Splunk Enterprise deployment, you can set type only to splunk , indicating that the provider is for Federated Search for Splunk. If you have a Splunk Cloud Platform deployment, you can set type to either splunk or aws_s3 . A type = aws_s3 setting indicates the provider is for Federated Search for Amazon S3. Defaults to splunk . |
| `mode` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider runs federated searches in standard or transparent mode. For a detailed comparison of the standard and transparent modes of federated search, see About Federated Search for Splunk in Federated Search . Defaults to standard . |
| `appContext` | Applies only to Federated Search for Splunk providers | Specifies the Splunk application context for federated searches that are run over standard mode federated providers. The application context ensures that standard mode federated searches using this federated provider are limited to the knowledge objects that are associated with the named application. If mode = standard for this federated provider, appContext specifies an the folder name of an app that is installed on the remote search head of the federated provider. If mode = transparent for this federated provider, the federated provider ignores the appContext setting when you run federated searches over the provider. Transparent mode federated searches use the application context of the user running the search. Defaults to search . |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Specifies a 12-digit Amazon Web Services (AWS) account ID. |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of AWS Glue tables from which Federated Search for Amazon S3 can get metadata and data schemas. |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of the Amazon resource names (ARNs) for the AWS KMS keys that encrypt Amazon S3 data. |
| `aws_region` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Web Services (AWS) region of your Splunk Cloud Platform deployment. This setting is determined automatically by Splunk software. |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of Amazon S3 location paths that you can search with Federated Search for Amazon S3. |
| `database` | Applies only to Federated Search for Amazon S3 providers | Specifies the name of the AWS Glue Data Catalog database that contains the AWS Glue Data Catalog tables for the federated provider. |
| `data_catalog` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Resource Name (ARN) for the AWS Glue Data Catalog. The ARN points to an AWS account. |
| `hostPort` | Applies only to Federated Search for Splunk providers | Specifies the protocols required to connect to a federated provider. Usually follows this format <Host_Name>:<Service_Port_Number>. In some cases, an IP address is used instead of a host name. |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | Specifies the user name for a service account that has been set up on the federated provider for the purpose of facilitating secure federated searches. |
| `useFSHKnowledgeObjects` | Applies only to Federated Search for Splunk providers | Specifies whether the remote search head uses its own knowledge objects for federated searches, or if it uses knowledge objects that are bundle-replicated from the federated search head. The federated provider mode determines the required setting for useFSHKnowledgeObjects . When the federated provider has mode=standard , Splunk software always interprets useFSHKnowledgeObjects as being set to 0 or false , which means that the federated search can use a blend of local and remote knowledge objects. When the federated provider has mode=transparent , Splunk software always interprets useFSHKnowledgeObjects as being set to 1 or true , because transparent mode federated searches can use knowledge objects only from the federated search head. |
| `connectivityStatus` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider established a connection to your local deployment in its last attempt to do so. When connectivityStatus=valid , this federated provider was able to connect to your local deployment. When connectivityStatus=invalid , this federated provider was unable to connect to your local deployment. When connectivityStatus=unknown , the ability of the federated provider to check this connection has been turned off. This setting is for diagnostic purposes only and cannot be set or changed by users. |
| `disabled` | All providers | Specifies whether the federated provider is turned on or off. When a federated provider is turned off, the provider cannot return results for federated searches. |

#### POST

Creates a new federated provider definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | String |
| `mode` | Applies only to Federated Search for Splunk providers | String |
| `appContext` | Applies only to Federated Search for Splunk providers | String |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Number |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `database` | Applies only to Federated Search for Amazon S3 providers | String |
| `hostPort` | Applies only to Federated Search for Splunk providers | String |
| `password` | Applies only to Federated Search for Splunk providers | String |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | String |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | Specifies the federated provider type. If you have a Splunk Enterprise deployment, type only be set to splunk , indicating that the provider is for Federated Search for Splunk. If you have a Splunk Cloud Platform deployment, type can be set either to splunk or aws_s3 . A type = aws_s3 setting indicates the provider is for Federated Search for Amazon S3. Defaults to splunk . |
| `mode` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider runs federated searches in standard or transparent mode. For a detailed comparison of the standard and transparent modes of federated search, see About Federated Search for Splunk in Federated Search . Defaults to standard . |
| `appContext` | Applies only to Federated Search for Splunk providers | Specifies the Splunk application context for federated searches that are run over standard mode federated providers. The application context ensures that standard mode federated searches using this federated provider are limited to the knowledge objects that are associated with the named application. If mode = standard for this federated provider, appContext specifies an the folder name of an app that is installed on the remote search head of the federated provider. If mode = transparent for this federated provider, the federated provider ignores the appContext setting when you run federated searches over the provider. Transparent mode federated searches use the application context of the user running the search. Defaults to search . |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Specifies a 12-digit Amazon Web Services (AWS) account ID. |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of AWS Glue tables from which Federated Search for Amazon S3 can get metadata and data schemas. |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of the Amazon resource names (ARNs) for the AWS KMS keys that encrypt Amazon S3 data. |
| `aws_region` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Web Services (AWS) region of your Splunk Cloud Platform deployment. This setting is determined automatically by Splunk software. |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of Amazon S3 location paths that you can search with Federated Search for Amazon S3. |
| `database` | Applies only to Federated Search for Amazon S3 providers | Specifies the name of the AWS Glue Data Catalog database that contains the AWS Glue Data Catalog tables for the federated provider. |
| `data_catalog` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Resource Name (ARN) for the AWS Glue Data Catalog. The ARN points to an AWS account. Splunk software provides the value for this setting. |
| `hostPort` | Applies only to Federated Search for Splunk providers | Specifies the protocols required to connect to a federated provider. Usually follows this format <Host_Name>:<Service_Port_Number>. In some cases, an IP address is used instead of a host name. |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | Specifies the user name for a service account that has been set up on the federated provider for the purpose of facilitating secure federated searches. |
| `useFSHKnowledgeObjects` | Applies only to Federated Search for Splunk providers | Specifies whether the remote search head uses its own knowledge objects for federated searches, or if it uses knowledge objects that are bundle-replicated from the federated search head. The federated provider mode determines the required setting for useFSHKnowledgeObjects . When the federated provider has mode=standard , Splunk software always interprets useFSHKnowledgeObjects as being set to 0 or false , which means that the federated search can use a blend of local and remote knowledge objects. When the federated provider has mode=transparent , Splunk software always interprets useFSHKnowledgeObjects as being set to 1 or true , because transparent mode federated searches can use knowledge objects only from the federated search head. |
| `connectivityStatus` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider established a connection to your local deployment in its last attempt to do so. When connectivityStatus=valid , this federated provider was able to connect to your local deployment. When connectivityStatus=invalid , this federated provider was unable to connect to your local deployment. When connectivityStatus=unknown , the ability of the federated provider to check this connection has been turned off. This setting is for diagnostic purposes only and cannot be set or changed by users. |
| `disabled` | All providers | Specifies whether the federated provider is turned on or off. When a federated provider is turned off, the provider cannot return results for federated searches. |

### `/services/data/federated/provider/turnOffProvidersInBatch`

Use this endpoint to turn off groups of federated providers with one REST API call. This endpoint applies to federated providers for Federated Search for Splunk and Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform.

#### POST

Turns off all federated providers. Can also turn off all federated providers belonging to a specific federated search type .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | String |

### `/services/data/federated/provider/{federated_provider_name}`

Use this endpoint to:

#### GET

Returns a definition of a specific {federated_provider_name} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | Specifies the federated provider type. If you have a Splunk Enterprise deployment, you can set type only to splunk , indicating that the provider is for Federated Search for Splunk. If you have a Splunk Cloud Platform deployment, you can set type to either splunk or aws_s3 . A type = aws_s3 setting indicates the provider is for Federated Search for Amazon S3. Defaults to splunk . |
| `mode` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider runs federated searches in standard or transparent mode. For a detailed comparison of the standard and transparent modes of federated search, see About Federated Search for Splunk in Federated Search . Defaults to standard . |
| `appContext` | Applies only to Federated Search for Splunk providers | Specifies the Splunk application context for federated searches that are run over standard mode federated providers. The application context ensures that standard mode federated searches using this federated provider are limited to the knowledge objects that are associated with the named application. If mode = standard for this federated provider, appContext specifies an the folder name of an app that is installed on the remote search head of the federated provider. If mode = transparent for this federated provider, the federated provider ignores the appContext setting when you run federated searches over the provider. Transparent mode federated searches use the application context of the user running the search. Defaults to search . |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Specifies a 12-digit Amazon Web Services (AWS) account ID. |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of AWS Glue tables from which Federated Search for Amazon S3 can get metadata and data schemas. |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of the Amazon resource names (ARNs) for the AWS KMS keys that encrypt Amazon S3 data. |
| `aws_region` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Web Services (AWS) region of your Splunk Cloud Platform deployment. This setting is determined automatically by Splunk software. |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of Amazon S3 location paths that you can search with Federated Search for Amazon S3. |
| `database` | Applies only to Federated Search for Amazon S3 providers | Specifies the name of the AWS Glue Data Catalog database that contains the AWS Glue Data Catalog tables for the federated provider. |
| `data_catalog` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Resource Name (ARN) for the AWS Glue Data Catalog. The ARN points to an AWS account. |
| `hostPort` | Applies only to Federated Search for Splunk providers | Specifies the protocols required to connect to a federated provider. Usually follows this format <Host_Name>:<Service_Port_Number>. In some cases, an IP address is used instead of a host name. |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | Specifies the user name for a service account that has been set up on the federated provider for the purpose of facilitating secure federated searches. |
| `useFSHKnowledgeObjects` | Applies only to Federated Search for Splunk providers | Specifies whether the remote search head uses its own knowledge objects for federated searches, or if it uses knowledge objects that are bundle-replicated from the federated search head. The federated provider mode determines the required setting for useFSHKnowledgeObjects . When the federated provider has mode=standard , Splunk software always interprets useFSHKnowledgeObjects as being set to 0 or false , which means that the federated search can use a blend of local and remote knowledge objects. When the federated provider has mode=transparent , Splunk software always interprets useFSHKnowledgeObjects as being set to 1 or true , because transparent mode federated searches can use knowledge objects only from the federated search head. |
| `connectivityStatus` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider established a connection to your local deployment in its last attempt to do so. When connectivityStatus=valid , this federated provider was able to connect to your local deployment. When connectivityStatus=invalid , this federated provider was unable to connect to your local deployment. When connectivityStatus=unknown , the ability of the federated provider to check this connection has been turned off. This setting is for diagnostic purposes only and cannot be set or changed by users. |
| `disabled` | All providers | Specifies whether the federated provider is turned on or off. When a federated provider is turned off, the provider cannot return results for federated searches. |

#### POST

Updates a definition for a specific {federated_provider_name} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `appContext` | Applies only to Federated Search for Splunk providers | String |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Number |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | String |
| `hostPort` | Applies only to Federated Search for Splunk providers | String |
| `password` | Applies only to Federated Search for Splunk providers | String |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | String |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `type` | All providers | Specifies the federated provider type. If you have a Splunk Enterprise deployment, you can set type only to splunk , indicating that the provider is for Federated Search for Splunk. If you have a Splunk Cloud Platform deployment, you can set type to either splunk or aws_s3 . A type = aws_s3 setting indicates the provider is for Federated Search for Amazon S3. Defaults to splunk . |
| `mode` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider runs federated searches in standard or transparent mode. For a detailed comparison of the standard and transparent modes of federated search, see About Federated Search for Splunk in Federated Search . Defaults to standard . |
| `appContext` | Applies only to Federated Search for Splunk providers | Specifies the Splunk application context for federated searches that are run over standard mode federated providers. The application context ensures that standard mode federated searches using this federated provider are limited to the knowledge objects that are associated with the named application. If mode = standard for this federated provider, appContext specifies an the folder name of an app that is installed on the remote search head of the federated provider. If mode = transparent for this federated provider, the federated provider ignores the appContext setting when you run federated searches over the provider. Transparent mode federated searches use the application context of the user running the search. Defaults to search . |
| `aws_account_id` | Applies only to Federated Search for Amazon S3 providers | Specifies a 12-digit Amazon Web Services (AWS) account ID. |
| `aws_glue_tables_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of AWS Glue tables from which Federated Search for Amazon S3 can get metadata and data schemas. |
| `aws_kms_keys_arn_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of the Amazon resource names (ARNs) for the AWS KMS keys that encrypt Amazon S3 data. |
| `aws_region` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Web Services (AWS) region of your Splunk Cloud Platform deployment. This setting is determined automatically by Splunk software. |
| `aws_s3_paths_allowlist` | Applies only to Federated Search for Amazon S3 providers | Specifies a comma-separated list of Amazon S3 location paths that you can search with Federated Search for Amazon S3. |
| `database` | Applies only to Federated Search for Amazon S3 providers | Specifies the name of the AWS Glue Data Catalog database that contains the AWS Glue Data Catalog tables for the federated provider. |
| `data_catalog` | Applies only to Federated Search for Amazon S3 providers | Specifies the Amazon Resource Name (ARN) for the AWS Glue Data Catalog. The ARN points to an AWS account. Splunk software provides the value for this setting. |
| `hostPort` | Applies only to Federated Search for Splunk providers | Specifies the protocols required to connect to a federated provider. Usually follows this format <Host_Name>:<Service_Port_Number>. In some cases, an IP address is used instead of a host name. |
| `serviceAccount` | Applies only to Federated Search for Splunk providers | Specifies the user name for a service account that has been set up on the federated provider for the purpose of facilitating secure federated searches. |
| `useFSHKnowledgeObjects` | Applies only to Federated Search for Splunk providers | Specifies whether the remote search head uses its own knowledge objects for federated searches, or if it uses knowledge objects that are bundle-replicated from the federated search head. The federated provider mode determines the required setting for useFSHKnowledgeObjects . When the federated provider has mode=standard , Splunk software always interprets useFSHKnowledgeObjects as being set to 0 or false , which means that the federated search can use a blend of local and remote knowledge objects. When the federated provider has mode=transparent , Splunk software always interprets useFSHKnowledgeObjects as being set to 1 or true , because transparent mode federated searches can use knowledge objects only from the federated search head. |
| `connectivityStatus` | Applies only to Federated Search for Splunk providers | Specifies whether the federated provider established a connection to your local deployment in its last attempt to do so. When connectivityStatus=valid , this federated provider was able to connect to your local deployment. When connectivityStatus=invalid , this federated provider was unable to connect to your local deployment. When connectivityStatus=unknown , the ability of the federated provider to check this connection has been turned off. This setting is for diagnostic purposes only and cannot be set or changed by users. |
| `disabled` | All providers | Specifies whether the federated provider is turned on or off. When a federated provider is turned off, the provider cannot return results for federated searches. |

#### DELETE

Deletes a definition for a specific {federated_provider_name} .

### `/services/data/federated/provider/{federated_provider_name}/disable`

Use this endpoint to turn a specific federated provider off. When a federated provider is turned off, all federated indexes associated with that provider are not searchable in federated searches. This endpoint applies to federated providers for Federated Search for Splunk and for Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform deployments.

#### POST

Turn off a specific federated provider.

### `/services/data/federated/provider/{federated_provider_name}/enable`

Use this endpoint to turn a federated provider back on after you have turned it off. When a federated provider is turned on, all federated indexes associated with that provider can be searched in federated searches. This endpoint applies to federated providers for Federated Search for Splunk and federated providers for Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform deployments.

#### POST

Turns a specific federated index on.

### `/services/data/federated/index`

Use this endpoint to get a list of federated indexes and post new federated index definitions. Some of these federated index settings are exclusive to Federated Search for Splunk, while others are exclusive to Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform.

#### GET

Returns a list of federated indexes.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `federated.provider` | All federated indexes | Specifies the federated provider that contains the dataset to which this federated index maps. |
| `federated.dataset` | All federated indexes | Specifies the remote dataset on the federated.provider to which this federated index maps. Each federated index maps to only one dataset on a federated provider. The dataset is identified by its prefix and name, using the following syntax: <prefix>:<dataset_name> . If the federated.provider has type=splunk in its definition on federated.conf, the possible values for <prefix> are index , metricindex , savedsearch , lastjob , and datamodel . If the federated.provider has type=aws_s3 in its definition on federated.conf, the <prefix> must be set to aws_glue_table . |
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time field that acts like an event timestamp in the AWS Glue table to which this index maps. |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time format variable or custom time format variable string that matches the federated.timefield . |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | An alias for the federated.timefield that Splunk software converts into numeric UNIX time format at search time. Insert the federated.unixtimefield into federated searches that require numeric UNIX time field values, or when you want to see your time field in numeric UNIX time format in the search results. Defaults to _time . |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time-related fields in the AWS Glue table to which the index is mapped. Each field is a partition key for a partition time field level indicated by its order in the list. The first field is at the first level, the second field is at the second level, and so on. |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time format variables or custom time format strings that correspond to the fields in the federated.partition.time.fields list. The first variable corresponds to the first field name, the second variable corresponds to the second field name, and so on. |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time field types that correspond to the fields in the federated.partition.time.fields list. Possible values are String , Integer , and Date . |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the timezone that corresponds to the fields in the federated.partition.time.fields list. Possible values are canonical timezone names such as America/Los_Angeles . |

#### POST

Creates a new federated index definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `federated.provider` | All federated indexes | String |
| `federated.dataset` | All federated indexes | String |
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | String |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `federated.provider` | All federated indexes | Specifies the federated provider that contains the dataset to which this federated index maps. |
| `federated.dataset` | All federated indexes | Specifies the remote dataset on the federated.provider to which this federated index maps. Each federated index maps to only one dataset on a federated provider. The dataset is identified by its prefix and name, using the following syntax: <prefix>:<dataset_name> . If the federated.provider has type=splunk in its definition on federated.conf, the possible values for <prefix> are index , metricindex , savedsearch , lastjob , and datamodel . If the federated.provider has type=aws_s3 in its definition on federated.conf, the <prefix> must be set to aws_glue_table . |
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time field in the AWS Glue table to which this index maps that acts like an event timestamp. |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time format variable or custom time format variable string that matches the federated.timefield . |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | An alias for the federated.timefield that Splunk software converts into numeric UNIX time format at search time. Insert the federated.unixtimefield into federated searches that require numeric UNIX time field values, or when you want to see your time field in numeric UNIX time format in the search results. Defaults to _time . |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time-related fields in the AWS Glue table to which the index is mapped. Each field is a partition key for a partition time field level indicated by its order in the list. The first field is at the first level, the second field is at the second level, and so on. |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time format variables or custom time format strings that correspond to the fields in the federated.partition.time.fields list. The first variable corresponds to the first field name, the second variable corresponds to the second field name, and so on. |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time field types that correspond to the fields in the federated.partition.time.fields list. Possible values are String , Integer , and Date . |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the timezone that corresponds to the fields in the federated.partition.time.fields list. Possible values are canonical timezone names such as America/Los_Angeles . |

### `/services/data/federated/index/{federated_index_name}`

Use this endpoint to:

#### GET

Returns a definition of a specific {federated_index_name} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `federated.provider` | All federated indexes | Specifies the federated provider that contains the dataset to which this federated index maps. |
| `federated.dataset` | All federated indexes | Specifies the remote dataset on the federated.provider to which this federated index maps. Each federated index maps to only one dataset on a federated provider. The dataset is identified by its prefix and name, using the following syntax: <prefix>:<dataset_name> . If the federated.provider has type=splunk in its definition on federated.conf, the possible values for <prefix> are index , metricindex , savedsearch , lastjob , and datamodel . If the federated.provider has type=aws_s3 in its definition on federated.conf, the <prefix> must be set to aws_glue_table . |
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time field that acts like an event timestamp in the AWS Glue table to which this index maps. |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time format variable or custom time format variable string that matches the federated.timefield . |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | An alias for the federated.timefield that Splunk software converts into numeric UNIX time format at search time. Insert the federated.unixtimefield into federated searches that require numeric UNIX time field values, or when you want to see your time field in numeric UNIX time format in the search results. Defaults to _time . |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time-related fields in the AWS Glue table to which the index is mapped. Each field is a partition key for a partition time field level indicated by its order in the list. The first field is at the first level, the second field is at the second level, and so on. |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time format variables or custom time format strings that correspond to the fields in the federated.partition.time.fields list. The first variable corresponds to the first field name, the second variable corresponds to the second field name, and so on. |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time field types that correspond to the fields in the federated.partition.time.fields list. Possible values are String , Integer , and Date . |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the timezone that corresponds to the fields in the federated.partition.time.fields list. Possible values are canonical timezone names such as America/Los_Angeles . |

#### POST

Updates a definition for a specific {federated_index_name} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | String |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | String |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `federated.provider` | All federated indexes | Specifies the federated provider that contains the dataset to which this federated index maps. |
| `federated.dataset` | All federated indexes | Specifies the remote dataset on the federated.provider to which this federated index maps. Each federated index maps to only one dataset on a federated provider. The dataset is identified by its prefix and name, using the following syntax: <prefix>:<dataset_name> . If the federated.provider has type=splunk in its definition on federated.conf, the possible values for <prefix> are index , metricindex , savedsearch , lastjob , and datamodel . If the federated.provider has type=aws_s3 in its definition on federated.conf, the <prefix> must be set to aws_glue_table . |
| `federated.timefield` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time field in the AWS Glue table to which this index maps that acts like an event timestamp. |
| `federated.timeformat` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the time format variable or custom time format variable string that matches the federated.timefield . |
| `federated.unixtimefield` | Applies only to Federated Search for Amazon S3 federated indexes | An alias for the federated.timefield that Splunk software converts into numeric UNIX time format at search time. Insert the federated.unixtimefield into federated searches that require numeric UNIX time field values, or when you want to see your time field in numeric UNIX time format in the search results. Defaults to _time . |
| `federated.partition.time.fields` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time-related fields in the AWS Glue table to which the index is mapped. Each field is a partition key for a partition time field level indicated by its order in the list. The first field is at the first level, the second field is at the second level, and so on. |
| `federated.partition.time.formats` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time format variables or custom time format strings that correspond to the fields in the federated.partition.time.fields list. The first variable corresponds to the first field name, the second variable corresponds to the second field name, and so on. |
| `federated.partition.time.types` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies a comma-delimited list of time field types that correspond to the fields in the federated.partition.time.fields list. Possible values are String , Integer , and Date . |
| `federated.partition.time.tz` | Applies only to Federated Search for Amazon S3 federated indexes | Specifies the timezone that corresponds to the fields in the federated.partition.time.fields list. Possible values are canonical timezone names such as America/Los_Angeles . |

#### DELETE

Deletes a definition for a specific {federated_index_name} .

### `/services/data/federated/index/{federated_index_name}/disable`

Use this endpoint to turn a specific federated index off. When a federated index is turned off, that federated index is not searchable in federated searches. This endpoint applies to federated indexes for Federated Search for Splunk and for Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform deployments.

#### POST

Turn off a specific federated index.

### `/services/data/federated/index/{federated_index_name}/enable`

Use this endpoint to turn a federated index back on after you have turned it off. When a federated index is turned on, it can be searched in federated searches. This endpoint applies to federated indexes for Federated Search for Splunk and federated indexes for Federated Search for Amazon S3. Federated Search for Amazon S3 is available only for Splunk Cloud Platform deployments.

#### POST

Turns a specific federated index on.

---

## Input

### `/services/data/ingest/rfsdestinations`

Create/configure, get, or delete an S3 destination for ingest action.

#### DELETE

Deletes the S3 destination.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `path` | Path (bucket and folder) of the destination. |  |
| `remote.s3.access_key` | See indexes.conf . |  |
| `remote.s3.secret_key` | See indexes.conf . |  |
| `remote.s3.endpoint` | See indexes.conf . |  |
| `remote.s3.encryption` | See indexes.conf . |  |
| `remote.s3.kms.key_id:` | See indexes.conf . |  |
| `remote.s3.kms.auth_region` | See indexes.conf . |  |
| `remote.s3.signature_version` | See indexes.conf . |  |
| `remote.s3.supports_versioning` | See indexes.conf . |  |
| `remote.s3.url_version` | See indexes.conf . |  |
| `compression` | See outputs.conf . |  |
| `dropEventsOnUploadError` | See outputs.conf . |  |
| `batchTimeout` | See outputs.conf . |  |
| `batchSizeThresholdKB` | See outputs.conf . |  |
| `target` | When provided, the request will be proxied to the host specified here (optional). |  |

#### GET

Gets list of the s3 destination configuration values.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `path` | Path (bucket and folder) of the destination. |  |
| `remote.s3.access_key` | See indexes.conf . |  |
| `remote.s3.secret_key` | See indexes.conf . |  |
| `remote.s3.endpoint` | See indexes.conf . |  |
| `remote.s3.encryption` | See indexes.conf . |  |
| `remote.s3.kms.key_id:` | See indexes.conf . |  |
| `remote.s3.kms.auth_region` | See indexes.conf . |  |
| `remote.s3.signature_version` | See indexes.conf . |  |
| `remote.s3.supports_versioning` | See indexes.conf . |  |
| `remote.s3.url_version` | See indexes.conf . |  |
| `compression` | See outputs.conf . |  |
| `dropEventsOnUploadError` | See outputs.conf . |  |
| `batchTimeout` | See outputs.conf . |  |
| `batchSizeThresholdKB` | See outputs.conf . |  |
| `target` | When provided, the request will be proxied to the host specified here (optional). |  |

#### POST

Creates and configures the S3 destination.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `path` | (Required) Path (bucket and folder) of the destination. |  |
| `remote.s3.access_key` | (Optional) See indexes.conf . |  |
| `remote.s3.secret_key` | (Optional) See indexes.conf . |  |
| `remote.s3.endpoint` | (Optional) See indexes.conf . |  |
| `remote.s3.encryption` | (Optional) See indexes.conf . |  |
| `remote.s3.kms.key_id:` | (Optional) See indexes.conf . |  |
| `remote.s3.kms.auth_region` | (Optional) See indexes.conf . |  |
| `remote.s3.signature_version` | (Optional) See indexes.conf . |  |
| `remote.s3.supports_versioning` | (Optional) See indexes.conf . |  |
| `remote.s3.url_version` | (Optional) See indexes.conf . |  |
| `compression` | (Optional) See outputs.conf . |  |
| `dropEventsOnUploadError` | (Optional) See outputs.conf . |  |
| `batchTimeout` | (Optional) See outputs.conf . |  |
| `batchSizeThresholdKB` | (Optional) See outputs.conf . |  |
| `target` | (Optional) When provided, the request will be proxied to the host specified here. |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `path` | Path (bucket and folder) of the destination. |  |
| `remote.s3.access_key` | See indexes.conf . |  |
| `remote.s3.secret_key` | See indexes.conf . |  |
| `remote.s3.endpoint` | See indexes.conf . |  |
| `remote.s3.encryption` | See indexes.conf . |  |
| `remote.s3.kms.key_id:` | See indexes.conf . |  |
| `remote.s3.kms.auth_region` | See indexes.conf . |  |
| `remote.s3.signature_version` | See indexes.conf . |  |
| `remote.s3.supports_versioning` | See indexes.conf . |  |
| `remote.s3.url_version` | See indexes.conf . |  |
| `compression` | See outputs.conf . |  |
| `dropEventsOnUploadError` | See outputs.conf . |  |
| `batchTimeout` | See outputs.conf . |  |
| `batchSizeThresholdKB` | See outputs.conf . |  |
| `target` | When provided, the request will be proxied to the host specified here (optional). |  |

### `/services/data/ingest/rulesets`

Retrieve a list of your rulesets.

#### GET

Return a list of your deployed rulesets.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Sourcetype` | The sourcetype of the deployed ruleset. |  |
| `Rules` | The rules for your deployed ruleset. |  |

#### POST

Creates and updates a ruleset.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `Sourcetype` | The sourcetype of the deployed ruleset. |  |
| `Rules` | The rules for your deployed ruleset. |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Sourcetype` | The sourcetype of the deployed ruleset. |  |
| `Rules` | The rules for your deployed ruleset. |  |

### `/services/data/ingest/rulesets/{name}`

Retrieve a particular ruleset.

#### GET

Return a named deployed ruleset.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Sourcetype` | The sourcetype of the deployed ruleset. |  |
| `Rules` | The rules for your deployed ruleset. |  |

#### POST

Creates and updates a named ruleset.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `Match` | What your deployed ruleset matches. |  |
| `Action` | The action that your deployed ruleset does. |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Match` | What your deployed ruleset matches. |  |
| `Action` | The action that your deployed ruleset does. |  |

### `/services/data/ingest/rulesets/publish`

Publish ruleset changes on the indexer cluster manager.

#### POST

Push the ruleset changes into deployment.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Match` | What your deployed ruleset matches. |  |
| `Action` | The action that your deployed ruleset does. |  |

### `/services/data/inputs/ad`

Access and configure the active directory monitoring input.

#### GET

Get the current active directory monitoring configuration.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates whether this input is disabled. |  |
| `index` | The index in which to store the gathered data. If no value is present, sends data to the default index. |  |
| `monitorSubtree` | Indicates whether or not to monitor the subtrees of a given Active Directory tree path. |  |
| `startingNode` | Tells Splunk software where in the Active Directory directory tree to start monitoring. If not specified, Splunk software attempts to start at the root of the directory tree. The user as which you configure Splunk to run at installation determines where Splunk software starts monitoring. |  |
| `targetDc` | Fully qualified domain name of a valid, network-accessible Active Directory domain controller. If not specified, Splunk software obtains the local computer DC by default, and binds to its root Distinguished Name (DN). |  |

#### POST

Create or modify performance monitoring settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Boolean |  |
| `host` | String | Docs-W8R2-Std7 |
| `index` | String | default |
| `monitorSubtree` | Number |  |
| `printSchema` | Boolean |  |
| `source` | String |  |
| `sourcetype` | String |  |
| `startingNode` | String |  |
| `targetDc` | String |  |

### `/services/data/inputs/ad/{name}`

Manage {name} active directory monitoring.

#### DELETE

Delete the {name} Active Directory monitoring stanza.

#### GET

Gets the current configuration for the {name} Active Directory monitoring stanza.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates whether this input is disabled. |  |
| `index` | The index in which to store the gathered data. If no value is present, send data to the default index. |  |
| `monitorSubtree` | Indicates whether or not to monitor the subtrees of a given Active Directory tree path. |  |

#### POST

Update the {name} Active Directory monitoring stanza.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Boolean |  |
| `host` | String | Docs-W8R2-Std7 |
| `index` | String | default |
| `monitorSubtree required` | Number |  |
| `printSchema` | Boolean |  |
| `source` | String |  |
| `sourcetype` | String |  |
| `startingNode` | String |  |
| `targetDc` | String |  |

### `/services/data/inputs/all`

Access all inputs to the Splunk deployment. This includes any modular inputs that may be defined on the system.

#### GET

List all inputs, including modular inputs.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `common` | Boolean | Indicates whether to return only attributes common to all inputs. The common attributes are as follows. app disabled host index owner source sourcetype title updated |

### `/services/data/inputs/all/{name}`

Get information about the {name} input source.

#### GET

List details for the {name} input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `common` | Boolean | Indicates whether to return only attributes common to all inputs. These common attributes are as follows. app disabled host index owner source sourcetype title updated |

### `/services/data/inputs/http`

#### GET

Access global configuration information and a list of tokens

#### POST

Modify global configuration. Add and modify tokens.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `dedicatedIoThreads` | Number | 2 |
| `disabled` | Boolean | 1 |
| `enableSSL` | Boolean | 1 |
| `index` | String |  |
| `indexes` | String |  |
| `maxSockets` | Number | 0 |
| `maxThreads` | Number | 0 |
| `name required` | String |  |
| `port` | Number | 8088 |
| `source` | String |  |
| `sourcetype` | String |  |
| `useDeploymentServer` | Boolean | 0 (disabled) |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `dedicatedIoThreads` | Number of threads used by HTTP Input server. |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `enableSSL` | Enable SSL protocol for HTTP data input. 1 = SSL enabled, 0 = SSL disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `indexes` | Set of indexes allowed for events with this token. |  |
| `port` | HTTP data input IP port. |  |
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `source` | Default source for events with this token. |  |
| `sourcetype` | Default sourcetype for events with this token. |  |
| `useDeploymentServer` | Boolean | 0 (disabled) |

### `/services/data/inputs/http/{name}`

#### DELETE

Delete a token.

#### GET

Get token configuration details.

#### POST

Update token configuration information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean | 1 |
| `host` | String |  |
| `index` | String |  |
| `indexes` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |
| `useDeploymentServer` | Boolean | 0 (disabled) |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `source` | Source for events with this token. |  |
| `sourcetype` | Sourcetype for events with this token. |  |
| `token` | Token value for sending data to collector/event endpoint. |  |
| `useDeploymentServer` | Indicates whether the event collector input writes its configuration to a deployment server repository. When this setting is set to 1 (enabled), the input writes its configuration to the directory specified as repositoryLocation in serverclass.conf . Copy the full contents of the splunk_httpinput app directory to this directory for the configuration to work. When enabled, only the tokens defined in the splunk_httpinput app in this repository are viewable and editable on the API and the Data Inputs page in Splunk Web. When disabled, the input writes its configuration to $SPLUNK_HOME/etc/apps by default. Defaults to 0 (disabled). |  |

### `/services/data/inputs/http/{name}/disable`

Disable the {name} HTTP Event Collector token.

#### POST

Disable the {name} HTTP Event Collector token.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `source` | Default source for events with this token. |  |
| `sourcetype` | Default sourcetype for events with this token. |  |
| `token` | Token value for sending data to collector/event endpoint. |  |

### `/services/data/inputs/http/{name}/enable`

Enable the {name} HTTP Event Collector token.

#### POST

Enable the {name} HTTP Event Collector token.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `source` | Default source for events with this token. |  |
| `sourcetype` | Default sourcetype for events with this token. |  |
| `token` | Token value for sending data to collector/event endpoint. |  |

### `/services/data/inputs/http/{name}/rotate`

Regenerate the {name} token value.

#### POST

Regenerate the {name} token value.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `token` | Regenerated token value. |  |

### `/services/data/inputs/monitor`

Access monitor inputs.

#### GET

List enabled and disabled monitor inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_TCP_ROUTING` | List of TCP forwarding groups, as specified in outputs.conf . |  |
| `disabled` | Indicates if inputs monitoring is disabled. |  |
| `filecount` | Number of files monitored. |  |
| `host` | Name of the Splunk host for which inputs are monitored. |  |
| `index` | The index in which to store the gathered data. |  |
| `sourcetype` | Source type being monitored. The source type of an event is the format of the data input from which it originates, such as access_combined or cisco_syslog. The source type determines how Splunk software formats your data. |  |

#### POST

Create a new file or directory monitor input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blacklist` | String | Specify a regular expression for a file path. The file path that matches this regular expression is not indexed. |
| `check-index` | Boolean | If set to true, the index value is checked to ensure that it is the name of a valid index. |
| `check-path` | Boolean | If set to true, the name value is checked to ensure that it exists. |
| `crc-salt` | String | A string that modifies the file tracking identity for files in this input. The magic value "<SOURCE>" invokes special behavior (see admin documentation). |
| `disabled` | Boolean | Indicates if input monitoring is disabled. |
| `followTail` | Boolean | If set to true, files that are seen for the first time is read from the end. |
| `host` | String | The value to populate in the host field for events from this data input. |
| `host_regex` | String | Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group. |
| `host_segment` | Number | Use the specified slash-separate segment of the filepath as the host field value. |
| `ignore-older-than` | String | Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored. |
| `index` | String | Which index events from this input should be stored in. Defaults to default . |
| `recursive` | Boolean | Setting this to false prevents monitoring of any subdirectories encountered within this data input. |
| `rename-source` | String | The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs. |
| `sourcetype` | String | The value to populate in the sourcetype field for incoming events. |
| `time-before-close` | Number | When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data. |
| `whitelist` | String | Specify a regular expression for a file path. Only file paths that match this regular expression are indexed. |

### `/services/data/inputs/monitor/{name}`

Manage the {name} monitor input.

#### DELETE

Disable the named monitor data input and remove it from the configuration.

#### GET

List the properties of a single monitor data input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if inputs monitoring is disabled. |  |
| `filecount` | Number of files being monitored. |  |
| `host` | Name of the Splunk host for which inputs are monitored. |  |
| `index` | The index events from this input should be stored in. |  |

#### POST

Update properties of the named monitor input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blacklist` | String | Specify a regular expression for a file path. The file path that matches this regular expression is not indexed. |
| `check-index` | Boolean | If set to true, the "index" value is checked to ensure that it is the name of a valid index. |
| `check-path` | Boolean | If set to true, the "name" value is checked to ensure that it exists. |
| `crc-salt` | String | A string that modifies the file tracking identity for files in this input. The magic value "<SOURCE>" invokes special behavior (see admin documentation). |
| `disabled` | Boolean | Indicates if input monitoring is disabled. |
| `followTail` | Boolean | If set to true, files that are seen for the first time is read from the end. |
| `host` | String | The value to populate in the host field for events from this data input. |
| `host_regex` | String | Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group. |
| `host_segment` | Number | Use the specified slash-separate segment of the filepath as the host field value. |
| `ignore-older-than` | String | Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored. |
| `index` | String | Which index events from this input should be stored in. Defaults to default . |
| `recursive` | Boolean | Setting this to "false" prevents monitoring of any subdirectories encountered within this data input. |
| `rename-source` | String | The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs. |
| `sourcetype` | String | The value to populate in the sourcetype field for incoming events. |
| `time-before-close` | Number | When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data. |
| `whitelist` | String | Specify a regular expression for a file path. Only file paths that match this regular expression are indexed. |

### `/services/data/inputs/monitor/{name}/members`

List {name} monitor input files.

#### GET

List all files monitored under the named monitor input.

### `/services/data/inputs/oneshot`

Access oneshot inputs in progress or queue a file for immediate indexing.

#### GET

Access oneshot inputs in progress.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Bytes Indexed` | Total number of bytes read and sent to the pipeline for indexing during a oneshot input. This total includes the uncompressed byte count from a source file that is compressed on disk. |  |
| `Offset` | Current position in the source file, indicating how much of the file is read. For compressed source files, this offset represents the position in the compressed format. You can obtain the percentage of a source file read by calculating offset/size. |  |
| `Size` | Size of the source file, in bytes. You can obtain the percentage of a source file read by calculating offset/size. |  |
| `Sources Indexed` | Indicates the number of sources read from a file in a compressed format such as tar or zip. A value of 0 indicates the source file was not compressed. |  |
| `Spool Time` | Time that the request was made to read the source file. |  |

#### POST

Queue a file for immediate indexing.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `host` | String |  |
| `host_regex` | String |  |
| `host_segment` | Number |  |
| `index` | String |  |
| `rename-source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/oneshot/{name}`

Get information about the {name} one-shot input.

#### GET

Access information about the {name} in-progress oneshot input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Bytes Indexed` | Total number of bytes read and sent to the pipeline for indexing during a oneshot input. This total includes the uncompressed byte count from a source file that is compressed on disk. |  |
| `Offset` | Current position in the source file, indicating how much of the file is read. For compressed source files, this offset represents the position in the compressed format. You can obtain the percentage of a source file read by calculating offset/size. |  |
| `Size` | Size of the source file, in bytes. You can obtain the percentage of a source file read by calculating offset/size. |  |
| `Sources Indexed` | Indicates the number of sources read from a file in a compressed format such as tar or zip. A value of 0 indicates the source file was not compressed. |  |
| `Spool Time` | Time that the request was made to read the source file. |  |

### `/services/data/inputs/registry`

Access the Windows registry monitoring input.

#### GET

Get current registry monitoring configuration details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Indicates whether or not Splunk software should get a baseline of Registry events when it starts. Defaults to false. If true, the input captures a baseline for the specified hive when the input starts for the first time. |  |
| `disabled` | Indicats whether this input is disabled. |  |
| `hive` | Regular expression for Registry hives that this input should monitor for Registry access. Matches against the Registry key which was accessed. Events that contain hives that do not match the regular expression get filtered out. Events that contain hives that match the regular expression pass through. |  |
| `index` | Specifies the index that this input should send the data to. If no value is present, defaults to the default index. |  |
| `monitorSubnodes` | Indicates whether to monitor all Registry hives beneath the specified hive. |  |
| `proc` | Regular expression for processes this input should monitor for Registry access. It matches against the process name which performed the Registry access. Events generated by processes that do not match the regular expression get filtered out. Events generated by processes that match the regular expression pass through. |  |
| `type` | A regular expression that specifies the types of Registry events to monitor. |  |

#### POST

Creates new or modify existing registry monitoring settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Boolean |  |
| `hive` | String |  |
| `proc` | String |  |
| `type` | String |  |
| `disabled` | Boolean |  |
| `index` | String | default |
| `monitorSubnodes` | Boolean | True |

### `/services/data/inputs/registry/{name}`

Manage registry monitoring {name} stanza.

#### DELETE

Delete a registry monitoring configuration stanza.

#### GET

Gets current registry monitoring configuration stanza

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Indicates whether to get a baseline of Registry events when Splunk software starts. |  |
| `disabled` | Indicates if the input is disabled. |  |
| `hive` | Regular expression for Registry hives that this input should monitor for Registry access. Matches against the Registry key which was accessed. Events that contain hives that do not match the regular expression get filtered out. Events that contain hives that match the regular expression pass through. |  |
| `index` | Specifies the index that this input should send the data to. If no value is present, defaults to the default index. |  |
| `monitorSubnodes` | Indicates whether to monitor all Registry hives beneath the specified hive. |  |
| `proc` | Regular expression for processes this input should monitor for Registry access. It matches against the process name which performed the Registry access. Events generated by processes that do not match the regular expression get filtered out. Events generated by processes that match the regular expression pass through. |  |
| `type` | Regular expression that specifies the types of Registry events to monitor. |  |

#### POST

Modify the named registry monitoring stanza.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `baseline` | Number |  |
| `hive` | String |  |
| `proc` | String |  |
| `type` | String |  |
| `disabled` | Number |  |
| `index` | String | default |
| `monitorSubnodes` | Boolean | True |

### `/services/data/inputs/script`

Access scripted inputs.

#### GET

Get the configuration settings for scripted inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether the input script is disabled. |  |
| `endtime` | If available, the time when the script stopped executing. |  |
| `group` | The name of the inputstatus group, which is always "exec commands." |  |
| `host` | Host with which these data are identified. |  |
| `index` | Sets the index for events from this input. Defaults to the main index. |  |
| `interval` | An integer or cron schedule. Specifies how often to execute the specified script, in seconds or a valid cron schedule. For a cron schedule, the script is not executed on start-up. |  |
| `source` | The source key/field for events from this input. Defaults to the input file path. Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'. |  |
| `sourcetype` | Sets the sourcetype key/field for events from this input. If unset, Splunk software picks a source type based on various aspects of the data. There is no hard-coded default. For more information, see the documentation for the sourcetype parameter for the POST operation. |  |
| `starttime` | If available, the time the when the script was executed. |  |

#### POST

Configure scripted input settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `interval` | Number | 60.0 |
| `passAuth` | String |  |
| `rename-source` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/script/restart`

Allows for restarting scripted inputs.

#### POST

Causes a restart on a given scripted input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `script` | String |  |

### `/services/data/inputs/script/{name}`

Manage the {name} scripted input.

#### DELETE

Removes the {name} scripted input.

#### GET

Returns the configuration settings for the {name} scripted input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether the input script is disabled. |  |
| `group` | The name of the inputstatus group, which is always "exec commands." |  |
| `host` | Host these data are identified with. |  |
| `index` | Sets the index for events from this input. Defaults to the main index. |  |
| `interval` | An integer or cron schedule. Specifies how often to execute the specified script, in seconds or a valid cron schedule. For a cron schedule, the script is not executed on start-up. |  |

#### POST

Configures settings for the {name} scripted input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `interval` | Number | 60.0 |
| `passAuth` | String |  |
| `rename-source` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/tcp/cooked`

#### GET

Access information about all cooked TCP inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | The default value to fill in for events lacking a host value. |  |
| `index` | The index in which to store generated events. |  |

#### POST

Create a new container for managing cooked data.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `SSL` | Boolean |  |
| `connection_host` | Enum | dns |
| `disabled` | Boolean |  |
| `host` | String |  |
| `queue` | "parsingQueue" | "indexQueue" | "parsingQueue" |
| `restrictToHost` | String |  |

### `/services/data/inputs/tcp/cooked/{name}`

#### DELETE

Remove the cooked TCP inputs for port or host:port specified by {name} .

#### GET

Access information for the {name} cooked TCP input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | The default value to fill in for events lacking a host value. |  |
| `index` | The index in which to store generated events. |  |
| `restrictToHost` | Restrict incoming connections on this port to the specified host. |  |

#### POST

Update the container for managing cooked data.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `SSL` | Boolean |  |
| `connection_host` | Enum | ip |
| `disabled` | Boolean |  |
| `host` | String |  |
| `restrictToHost` | String |  |

### `/services/data/inputs/tcp/cooked/{name}/connections`

Get active connections to the {name} port.

#### GET

List active connections to the {name} port.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `connection` | Identifies the connection to port. |  |
| `servername` | Server name of forwarder connecting to this port. |  |

### `/services/data/inputs/tcp/raw`

#### GET

Get information about all raw TCP inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | The index in which to store generated events. |  |

#### POST

Create a new data input for accepting raw TCP data.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `connection_host` | Enum | dns |
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `name required` | String |  |
| `queue` | Enum |  |
| `rawTcpDoneTimeout` | Number |  |
| `restrictToHost` | String |  |
| `SSL` | Boolean |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/tcp/raw/{name}`

Manage raw inputs for the {name} host or port.

#### DELETE

Remove the raw inputs for port or host:port specified by {name}

#### GET

Returns information about raw TCP input port {name}.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `restrictToHost` | Restrict incoming connections on this port to the specified host. |  |

#### POST

Updates the container for managing raw data.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `SSL` | Boolean |  |
| `connection_host` | Enum | dns |
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `queue` | Enum |  |
| `rawTcpDoneTimeout` | Number |  |
| `restrictToHost` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/tcp/raw/{name}/connections`

Get active connections the {name} host or port.

#### GET

View all connections to the named data input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `connection` | IP address and port of the source connecting to this TCP input port. |  |
| `servername` | DNS name of the source connecting to this TCP input port. |  |

### `/services/data/inputs/tcp/splunktcptoken`

Manage receiver access using tokens.

#### GET

Return all configured tokens.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `token` | Token value. |  |

#### POST

Create a new token.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `token` | String | None |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `token` | Token value. |  |

### `/services/data/inputs/tcp/splunktcptoken/{name}`

Manage existing receiver tokens.

#### GET

Access token information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `token` | Token value. |  |

#### POST

Update the {name} token.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `token` | String | None |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `token` | Token value. |  |

#### DELETE

Delete the {name} token.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |
| `token` | Token value. |  |

### `/services/data/inputs/tcp/ssl`

Provides access to the SSL configuration of a Splunk server.

#### GET

Get SSL configuration details. There is only one SSL configuration for all input ports.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `cipherSuite` | Specifies list of acceptable ciphers to use in ssl. |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |

### `/services/data/inputs/tcp/ssl/{name}`

#### GET

Returns the SSL configuration for the host {name} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | [Deprecated] |  |
| `cipherSuite` | Specifies list of acceptable ciphers to use in ssl. |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |

#### POST

Configure SSL for the {name} host.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `password` | String |  |
| `requireClientCert` | Boolean |  |
| `rootCA` | String |  |
| `serverCert` | String |  |

### `/services/data/inputs/udp`

#### GET

List enabled and disabled UDP data inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |

#### POST

Create a new UDP data input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `connection_host` | Enum | ip |
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `no_appending_timestamp` | Boolean |  |
| `no_priority_stripping` | Boolean |  |
| `queue` | String |  |
| `restrictToHost` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/udp/{name}`

#### DELETE

Disable the named UDP data input and remove it from the configuration.

#### GET

List the properties of a single UDP data input port or host:port {name} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `_rcvbuf` | Socket receive buffer size (bytes). |  |
| `disabled` | Input disabled indicator: 0 = Input Not disabled, 1 = Input disabled. |  |
| `group` | Set to listenerports for listening ports. |  |
| `host` | Host from which the indexer gets data. |  |
| `index` | Index to store generated events. |  |

#### POST

Edit properties of the named UDP data input.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `connection_host` | Enum | ip |
| `disabled` | Boolean |  |
| `host` | String |  |
| `index` | String | default |
| `no_appending_timestamp` | Boolean |  |
| `no_priority_stripping` | Boolean |  |
| `queue` | String |  |
| `restrictToHost` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/data/inputs/udp/{name}/connections`

#### GET

List connections to the {name} host or port.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates whether the inputs are disabled. |  |
| `group` | Set to 'listenerports' for listening ports. |  |

### `/services/data/inputs/win-event-log-collections`

#### GET

Retrieve a list of configured event log collections.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `lookup_host` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the input is disabled. |  |
| `hosts` | Hosts you are monitoring. |  |
| `index` | Index to store data. If not specified defaults to the default index. |  |
| `logs` | List of event log channels to monitor. |  |

#### POST

Create or modify existing event log collection settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `hosts` | String |  |
| `index` | String | default |
| `logs` | String |  |
| `lookup_host` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the input is disabled. |  |
| `hosts` | Monitored hosts. |  |
| `index` | Index to store data. |  |
| `logs` | List of event log channels to monitor. |  |
| `lookup_host` | Host from which to monitor log events. |  |

### `/services/data/inputs/win-event-log-collections/{name}`

#### DELETE

Deletes an event log collection.

#### GET

Gets event log collection configurations.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `lookup_host` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the input is disabled. |  |
| `hosts` | Monitored hosts. |  |
| `index` | Index to store data. If not specified defaults to the default index. |  |
| `logs` | List of event log channels to monitor. |  |
| `lookup_host` | Host from which to monitor log events. |  |

#### POST

Modify an existing event log collection.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `hosts` | String |  |
| `index` | String | default |
| `logs` | String |  |
| `lookup_host` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the input is disabled. |  |
| `hosts` | Monitored hosts. |  |
| `index` | Index to store data. |  |
| `logs` | List of event log channels to monitor. |  |
| `lookup_host` | Host from which to monitor log events. |  |

### `/services/data/inputs/win-wmi-collections`

#### GET

Access configured WMI collections.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `class` | The WMI performance object class being monitored. |  |
| `disabled` | Indicates whther the input is disbled. |  |
| `fields` | The WMI performance counters being monitored. |  |
| `index` | The index to which you are sending input data. |  |
| `instances` | Instances of the WMI performance counter. |  |
| `interval` | The interval, in seconds, at which the WMI provider(s) are queried. |  |
| `server` | The server you are monitoring. |  |
| `wql` | The actual WQL query for monitoring the performance object. |  |

#### POST

Create or modify existing WMI collection settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `classes` | String |  |
| `disabled` | Number | 0 |
| `fields` | String | 1. * |
| `index` | String | default |
| `instances` | String | empty |
| `interval` | Number |  |
| `lookup_host` | String |  |
| `server` | String | localhost |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `classes` | A valid WMI class name. |  |
| `disabled` | Indicates if the input is disabled. |  |
| `fields` | Properties (fields) that you want to gather from the given class. |  |
| `index` | The index in which to store the gathered data. |  |
| `instances` | Instances of a given class for which data is gathered. |  |
| `interval` | The interval, in seconds, at which the WMI provider(s) is queried. |  |
| `lookup_host` | Host from which to monitor log events. |  |
| `server` | Servers from which to gather data. Used if you need to gather from more than a single machine. See also lookup_host. |  |
| `wql` | The actual WQL query for monitoring the performance object. |  |

### `/services/data/inputs/win-wmi-collections/{name}`

#### DELETE

Delete a given collection.

#### GET

Get information about a single collection.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `classes` | A valid WMI class name. |  |
| `disabled` | Indicates if the input is disabled. |  |
| `fields` | Properties (fields) that you want to gather from the given class. |  |
| `index` | The index in which to store the gathered data. |  |
| `instances` | Instances of a given class for which data is gathered. |  |
| `interval` | The interval, in seconds, at which the WMI provider(s) is queried. |  |
| `lookup_host` | Host from which to monitor log events. |  |
| `server` | Servers frpm which to gather data from. Used if you need to gather from more than a single machine. See also lookup_host. |  |
| `wql` | The actual WQL query for monitoring the performance object. |  |

#### POST

Modify a collection.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `classes` | String |  |
| `disabled` | Number |  |
| `fields` | String |  |
| `index` | String |  |
| `instances` | String |  |
| `interval` | Number |  |
| `lookup_host` | String |  |
| `server` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `classes` | A valid WMI class name. |  |
| `disabled` | Indicates if the input is disabled. |  |
| `fields` | Properties (fields) that you want to gather from the given class. |  |
| `index` | The index in which to store the gathered data. |  |
| `instances` | Instances of a given class for which data is gathered. |  |
| `interval` | The interval, in seconds, at which the WMI provider(s) are queried. |  |
| `lookup_host` | Host from which to monitor log events. |  |
| `server` | Servers from which to gather data. Used if you need to gather from more than a single machine. See also lookup_host. |  |
| `wql` | The actual WQL query for monitoring the performance object. |  |

### `/services/data/inputs/win-perfmon`

#### GET

Get current performance monitoring configuration details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `counters` | List of valid Performance Monitor counters. |  |
| `disabled` | Indicates whether the input is disabled. |  |
| `index` | The index that this input should send data to. If no value is present, send data to the default index. |  |
| `instances` | List of valid instances for a Performance Monitor counter. |  |
| `interval` | How often, in seconds, to poll for new data. |  |
| `nonmetric_counters` | List of valid Performance Monitor counters. |  |
| `object` | A valid Performance Monitor object as defined within Performance Monitor. |  |

#### POST

Update performance monitoring collection settings.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `counters` | String |  |
| `host` | String | Docs-W8R2-Std7 |
| `index` | String | default |
| `instances` | String |  |
| `interval` | Number |  |
| `name required` | String |  |
| `object` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `counters` | List of valid Performance Monitor counters. |  |
| `disabled` | Indicates whether the input is disabled. |  |
| `host` | Name of the host for the Windows Performance Monitor. |  |
| `index` | The index that this input should send data to. If no value is present, send data to the default index. |  |
| `instances` | List of valid instances for a Performance Monitor counter. |  |
| `interval` | How frequently, in seconds, to poll for new data. |  |
| `nonmetric_counters` | List of valid Performance Monitor counters. |  |
| `object` | A valid Performance Monitor object as defined within Performance Monitor. |  |
| `source` | Source for inputs. |  |
| `sourcetype` | Source type of the input. |  |

### `/services/data/inputs/win-perfmon/{name}`

#### DELETE

Delete a given monitoring stanza.

#### GET

Get settings for a given performance stanza.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `counters` | List of valid Performance Monitor counters. |  |
| `disabled` | Indicates whether the input is disabled. |  |
| `index` | The index that this input should send data to. If no value is present, send data to the default index. |  |
| `instances` | List of valid instances for a Performance Monitor counter. |  |
| `interval` | How often, in seconds, to poll for new data. |  |
| `nonmetric_counters` | List of valid Performance Monitor counters. |  |
| `object` | A valid Performance Monitor object as defined within Performance Monitor. |  |

#### POST

Modify an existing monitoring stanza.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `counters` | String |  |
| `host` | String | Docs-W8R2-Std7 |
| `index` | String | default |
| `instances` | String |  |
| `interval` | Number |  |
| `object` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `counters` | List of valid Performance Monitor counters. |  |
| `disabled` | Indicates whether the input is disabled. |  |
| `host` | Name of the host for the Windows Performance Monitor. |  |
| `index` | The index that this input should send data to. If no value is present, send data to the default index. |  |
| `instances` | List of valid instances for a Performance Monitor counter. |  |
| `interval` | How frequently, in seconds, to poll for new data. |  |
| `nonmetric_counters` | List of valid Performance Monitor counters. |  |
| `object` | A valid Performance Monitor object as defined within Performance Monitor, |  |
| `source` | Source for inputs. |  |
| `sourcetype` | Source type of the input. |  |

### `/services/data/modular-inputs`

Access currently defined modular inputs on the system.

#### GET

Get information about configured modular inputs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `endpoint` | Contains one or more <arg> elements, which define the parameters to an endpoint. |  |
| `streaming_mode` | Indicates the streaming mode for the modular input. Valid values are xml and simple . |  |
| `title` | The label for a modular input script. The title appears on the Data inputs manager page. |  |

### `/services/data/modular-inputs/{name}`

Get information about the {name} modular input.

#### GET

Get information about a modular input.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `endpoint` | Contains one or more <arg> elements, which define the parameters to an endpoint. |  |
| `streaming_mode` | Indicates the streaming mode for the modular input. Valid values are xml or simple (plain text). Contains one or more <arg> elements, which define the parameters to an endpoint. |  |
| `title` | The label for a modular input script. The label appears in the Data inputs manager page. |  |

### `/services/indexing/preview`

#### GET

Return a list of all data preview jobs.

#### POST

Create a preview data job for the specified source file, returning the preview data job ID.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `input.path` | String |  |
| `props.<props_attr>` | String |  |

### `/services/indexing/preview/{job_id}`

#### GET

Get props.conf file settings for a job.

### `/services/receivers/simple`

Allows for sending events to Splunk in an HTTP request.

#### POST

Create events from the contents contained in the HTTP body.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `<arbitrary_data>` | String |  |
| `host` | String |  |
| `host_regex` | String |  |
| `index` | String | default |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/receivers/stream`

#### POST

Create events from the stream of data following HTTP headers.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `<data_stream>` | String |  |
| `host` | String |  |
| `host_regex` | String |  |
| `index` | String |  |
| `source` | String |  |
| `sourcetype` | String |  |

### `/services/server/pipelinesets`

Provides information on the ingestion pipeline sets on an indexer.

#### GET

Query the status of pipeline sets.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `busiest_thread_name` | The name of the busiest pipeline thread within the pipeline set for past calculation period. |  |
| `dutycycle_ratio` | The dutycycle ratio of the busiest pipeline thread within the pipeline set for past calculation period. |  |
| `requests_last_period` | The number of ingestion requests processed by the pipeline set in the past calculation period. |  |
| `share` | The relative probability of selection of the pipeline set for the past calculation period. |  |

### `/services/services/collector`

Send events to HTTP Event Collector using the Splunk platform JSON event protocol.

#### POST

Send events to the HTTP Event Collector.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `channel` | See description | Required if useAck is enabled. Pass in the channel GUID as a string parameter or using the "x-splunk-request-channel" header. |
| `event` | string | Required. Event payload key-value. Value can be a string or a JSON object. JSON example: {"event": {"message":"Access log test message"}} String example: "event": "Access log test message." |
| `fields` | JSON object | Fields for indexing that do not occur in the event payload itself. You can use this parameter when you do not want particular fields to be included in the event data, but you need additional metadata for indexing and searching. Specify one or more additional fields to include for indexing with the event payload. For each field, use a key to specify the name and include one or more values. Specify multiple values in an array. In the following example, the "severity" field gets the value "INFO" and the "category" key gets both "foo" and "bar" values. JSON Copy -d {"event": "something happened", "fields": {"severity": "INFO", "category": ["foo", "bar"]}} -d {"event": "something happened", "fields": {"severity": "INFO", "category": ["foo", "bar"]}} |
| `host` | string | Host name. Specify with the host query string parameter. Sets a default for all events in the request. The default host name can be overridden. |
| `index` | string | Index name. Specify with the index query string parameter. Sets a default for all events in the request. The default index name can be overridden. |
| `source` | string | User-defined event source. Specify with the source query string parameter. Sets a default for all events in the request. The default source can be overridden. |
| `sourcetype` | string | User-defined event sourcetype. Specify with the sourcetype query string parameter. Sets a default for all events in the request. The default sourcetype can be overridden. |
| `time` | string or unsigned integer | Epoch-formatted time. Specify with the time query string parameter. Sets a default for all events in the request. The default time can be overridden. For more information about formatting, see Format events for HTTP Event Collector . |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `text` | Human readable status, same value as code . |  |
| `code` | Machine format status, same value as text . |  |
| `invalid-event-number` | When errors occur, indicates the zero-based index of first invalid event in an event sequence. |  |
| `ackId` | If useACK is enabled for the token, indicates the ackId to use for checking an indexer acknowledgement. |  |

### `/services/services/collector/ack`

#### GET

Get HTTP Event Collector event indexing status.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `channel` | See description | Required. Pass in the channel GUID as the channel string parameter or using the x-splunk-request-channel header. |
| `"acks"` | JSON object | Required. JSON object with an array of ack ID values. Include in the request payload. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `acks` | Contains the key/value pairs for each ACK ID requested. For each key in the "acks" object, a true value means the ACK ID's events were indexed. A false value means that indexing status is unknown. For example, an event may have an indexing delay long enough that it is no longer tracked. Here is an example response. {"acks" : { "0" : true, "1" : false, "2" : true, "3" : false}} |  |

### `/services/services/collector/mint`

Post MINT formatted data to the HTTP Event Collector. The authorization header contains the authorization scheme and application token. The HTTP POST body contains event data in the MINT payload format.

#### POST

Post MINT formatted data.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `host` | String | Host name. Specify with the host query string parameter. Sets a default for all events in the request. Can be overridden. |
| `index` | String | Index name. Specify with the index query string parameter. Sets a default for all events in the request. Can be overridden. |
| `source` | String | User-defined event source. Specify with the source query string parameter. Sets a default for all events in the request. The default source can be overridden. |
| `sourcetype` | string | User-defined event sourcetype. Specify with the sourcetype query string parameter. Sets a default for all events in the request. The default sourcetype can be overridden. |
| `time` | string or unsigned integer | Epoch-formatted time. Specify with the time query string parameter. Sets a default for all events in the request. The default time can be overridden. |

### `/services/services/collector/raw`

#### POST

Send raw data to the to the indexer queue. Requires a data channel GUID, provided as a custom HTTP header or request parameter.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `channel` | See description. | Required . Pass in the channel GUID as the channel string parameter or using the x-splunk-request-channel header. |
| `host` | String | Host name. Specify with the host query string parameter. Sets a default for all events in the request. Can be overridden. |
| `index` | String | Index name. Specify with the index query string parameter. Sets a default for all events in the request. Can be overridden. |
| `source` | String | User-defined event source. Specify with the source query string parameter. Sets a default for all events in the request. The default source can be overridden. |
| `sourcetype` | string | User-defined event sourcetype. Specify with the sourcetype query string parameter. Sets a default for all events in the request. The default sourcetype can be overridden. |
| `time` | string or unsigned integer | Epoch-formatted time. Specify with the time query string parameter. Sets a default for all events in the request. The default time can be overridden. |

---

## Introspection

### `/services/data/index-volumes`

Get information about the volume (logical drives) in use by the Splunk deployment.

#### GET

List the Splunk deployment volumes.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `max_size` | Maximum name volume size limit (MB): infinite = No maximum specified. |  |
| `total_size` | Total name volume capacity (MB). If max_size is infinite , this field is not listed. |  |

### `/services/data/index-volumes/{name}`

Get information about the {name} volume (logical drive).

#### GET

List {name} volume properties.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `max_size` | Maximum name volume size limit (MB). infinite = No maximum specified (i.e., 0, the default) |  |
| `total_size` | Total name volume capacity (MB). If max_size is infinite , this field is not listed. |  |

### `/services/data/indexes`

Create and manage data indexes.

#### GET

List the recognized indexes on the server.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `assureUTF8` | Indicates whether all data retreived from the index is proper UTF8. If enabled (set to True), degrades indexing performance. This is a global setting, not a per index setting. |  |
| `blockSignSize` | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. |  |
| `blockSignatureDatabase` | The index that stores block signatures of events. This is a global setting, not a per index setting. |  |
| `coldPath` | Filepath to the cold databases for the index. |  |
| `coldPath_expanded` | Absoute filepath to the cold databases. |  |
| `coldToFrozenDir` | Destination path for the frozen archive. Used as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory. Bucket freezing policy is as follows: New style buckets (4.2 and on): removes all files but the rawdata To thaw, run splunk rebuild <bucket dir> on the bucket, then move to the thawed directory Old style buckets (Pre-4.2): gzip all the .data and .tsidx files To thaw, unzip the zipped files and move the bucket into the thawed directory If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence. |  |
| `coldToFrozenScript` | Path to the archiving script. See the POST parameter description for details. |  |
| `compressRawdata` | This value is ignored. splunkd process always compresses raw data. |  |
| `currentDBSizeMB` | Total size, in MB, of data stored in the index. The total incudes data in the home, cold and thawed paths. |  |
| `defaultDatabase` | If no index destination information is available in the input data, the index shown here is the destination of such data. |  |
| `disabled` | Indicates if the index is disabled. |  |
| `enableRealtimeSearch` | Indicates if this is a real-time search. This is a global setting, not a per index setting. |  |
| `frozenTimePeriodInSecs` | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years). Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation. |  |
| `homePath` | An absolute path that contains the hot and warm buckets for the index. |  |
| `homePath_expanded` | An absolute filepath to the hot and warm buckets for the index. |  |
| `indexThreads` | Number of threads used for indexing. This is a global setting, not a per index setting. |  |
| `isInternal` | Indicates if this is an internal index (for example, _internal, _audit). |  |
| `isReady` | Indicates if the index is properly initialized. |  |
| `lastInitTime` | Last time the index processor was successfully initialized. This is a global setting, not a per index setting. |  |
| `maxConcurrentOptimizes` | The number of concurrent optimize processes that can run against a hot bucket. This number should be increased if instructed by Splunk Support. Typically the default value should suffice. |  |
| `maxDataSize` | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk software to autotune this parameter (recommended). Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto". A "high volume index" is typically one that gets over 10GB of data per day. "auto" sets the size to 750MB. "auto_high_volume" sets the size to 10GB on 64-bit, and 1GB on 32-bit systems. Although the maximum value you can set this is 1048576 MB, which corresponds to 1 TB, a reasonable number ranges anywhere from 100 - 50000. Any number outside this range should be approved by Splunk Support before proceeding. If you specify an invalid number or string, maxDataSize is auto-tuned. Note: The precise size of your warm buckets may vary from maxDataSize, due to post-processing and timing issues with the rolling policy. |  |
| `maxHotBuckets` | Maximum hot buckets that can exist per index. Defaults to 3. When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll. |  |
| `maxHotIdleSecs` | Maximum life, in seconds, of a hot bucket. Defaults to 0. A value of 0 turns off the idle check (equivalent to INFINITE idle time). If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. |  |
| `maxHotSpanSecs` | Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days). Note: If set too small, you can get an explosion of hot/warm buckets in the filesystem. The system sets a lower bound implicitly for this parameter at 3600, but this is an advanced parameter that should be set with care and understanding of the characteristics of your data. |  |
| `maxMemMB` | The amount of memory, in MB, allocated for indexing. This is a global setting, not a per index setting. |  |
| `maxMetaEntries` | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption. If set to 0, this setting is ignored (it is treated as infinite). If exceeded, a hot bucket is rolled to prevent further increase. If your buckets are rolling due to Strings.data hitting this limit, the culprit may be the punct field in your data. If you do not use punct, it may be best to simply disable this (see props.conf.spec in $SPLUNK_HOME/etc/system/README). There is a small time delta between when maximum is exceeded and bucket is rolled. This means a bucket may end up with epsilon more lines than specified, but this is not a major concern unless excess is significant. |  |
| `maxRunningProcessGroups` | Maximum number of processes that the indexer fires off at a time. This is a global setting, not a per index setting. |  |
| `maxTime` | ISO8601 timestamp of the newest event time in the index. |  |
| `maxTotalDataSizeMB` | The maximum size of an index, in MB. |  |
| `maxWarmDBCount` | The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times are moved to cold. |  |
| `memPoolMB` | Determines how much memory is given to the indexer memory pool. This is a global setting, not a per-index setting. |  |
| `minRawFileSyncSecs` | Can be either an integer (or "disable"). Some filesystems are very inefficient at performing sync operations, so only enable this if you are sure it is needed The integer sets how frequently splunkd forces a filesystem sync while compressing journal slices. During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files. If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete. |  |
| `minTime` | ISO8601 timestamp of the oldest event time in the index. |  |
| `partialServiceMetaPeriod` | Related to serviceMetaPeriod. By default it is turned off (zero). If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync'ed at serviceMetaPeriod. partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens. If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect. |  |
| `quarantineFutureSecs` | Events with timestamp of quarantineFutureSecs newer than "now" that are dropped into quarantine bucket. Defaults to 2592000 (30 days). This is a mechanism to prevent main hot buckets from being polluted with fringe events. |  |
| `quarantinePastSecs` | Events with timestamp of quarantinePastSecs older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events. |  |
| `rawChunkSizeBytes` | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. Note: rawChunkSizeBytes only specifies a target chunk size. The actual chunk size may be slightly larger by an amount proportional to an individual event size. Warning: This is an advanced parameter. Only change it if instructed to do so by Splunk Support. |  |
| `rotatePeriodInSecs` | Rotation period, in seconds, that specifies how frequently to check: If a new hot bucket needs to be created. If there are any cold buckets that should be frozen. If there are any buckets that need to be moved out hot and cold DBs, due to size constraints. |  |
| `serviceMetaPeriod` | Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds). You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path. |  |
| `summarize` | If true, leaves out certain index details, which provides a faster response. |  |
| `suppressBannerList` | List of indexes for which we suppress "index missing" warning banner messages. This is a global setting, not a per index setting. |  |
| `sync` | Specifies the number of events that trigger the indexer to sync events. This is a global setting, not a per index setting. |  |
| `syncMeta` | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures. Note: Do not change this parameter without the input of Splunk Support. |  |
| `thawedPath` | An absolute path that contains the thawed (resurrected) databases for the index. |  |
| `thawedPath_expanded` | Absolute filepath to the thawed (resurrected) databases. |  |
| `throttleCheckPeriod` | Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds). Note: Do not change this parameter without the input of Splunk Support. |  |
| `totalEventCount` | Total number of events in the index. |  |
| `tsidxDedupPostingsListMaxTermsLimit` | This setting is valid only when tsidxWritingLevel is at 4 or higher. This maximum term limit sets an upper bound on the number of terms kept inside an in-memory hash table that serves to improve tsidx compression. The tsidx optimizer uses the hash table to identify terms with identical postings lists. When the first instance of a term is received, its postings list is stored. When successive terms with identical postings lists are received, the tsidx optimizer makes them refer to the first instance of the postings list rather than creating and storing term postings list duplicates. Consider increasing this limit to improve compression for large tsidx files. For example, a tsidx file created with tsidxTargetSizeMB over 1500MB can contain a large number of terms with identical postings lists. Reducing this limit helps conserve memory consumed by optimization processes, at the cost of reduced tsidx compression. Set this limit to 0 to disable deduplicated postings list compression. This setting cannot exceed 1,073,741,824 (2 30 ). Defaults to 8,388,608 (2 23 ). |  |

#### POST

Create a new index.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blockSignSize` | Number | 0 |
| `bucketRebuildMemoryHint` | String | auto |
| `coldPath` | String |  |
| `coldToFrozenDir` | String |  |
| `coldToFrozenScript` | String |  |
| `compressRawdata` | Boolean | true |
| `enableOnlineBucketRepair` | Boolean | true |
| `frozenTimePeriodInSecs` | Number | 188697600 |
| `homePath` | String |  |
| `maxBloomBackfillBucketAge` | Number | 30d |
| `maxConcurrentOptimizes` | Number | 6 |
| `maxDataSize` | Number | auto |
| `maxHotBuckets` | Number | 3 |
| `maxHotIdleSecs` | Number | 0 |
| `maxHotSpanSecs` | Number | 7776000 |
| `maxMemMB` | Number | 5 |
| `maxMetaEntries` | Number | 1000000 |
| `maxTimeUnreplicatedNoAcks` | Number | 300 |
| `maxTimeUnreplicatedWithAcks` | Number | 60 |
| `maxTotalDataSizeMB` | Number | 500000 |
| `maxWarmDBCount` | Number | 300 |
| `minRawFileSyncSecs` | Number | disable |
| `minStreamGroupQueueSize` | Number | 2000 |
| `name required` | String |  |
| `partialServiceMetaPeriod` | Number | 0 |
| `processTrackerServiceInterval` | Number | 1 |
| `quarantineFutureSecs` | Number | 2592000 |
| `quarantinePastSecs` | Number | 77760000 |
| `rawChunkSizeBytes` | Number | 131072 |
| `repFactor` | String | 0 |
| `rotatePeriodInSecs` | Number | 60 |
| `serviceMetaPeriod` | Number | 25 |
| `syncMeta` | Boolean | true |
| `thawedPath` | String |  |
| `throttleCheckPeriod` | Number | 15 |
| `tstatsHomePath` | String |  |
| `warmToColdScript` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `assureUTF8` | Boolean value indicating wheter all data retreived from the index is proper UTF8. If enabled (set to True), degrades indexing performance Can only be set globally. |  |
| `blockSignSize` | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. |  |
| `blockSignatureDatabase` | The index that stores block signatures of events. This is a global setting, not a per index setting. |  |
| `bucketRebuildMemoryHint` | Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make. |  |
| `coldPath` | Filepath to the cold databases for the index. |  |
| `coldPath_expanded` | Absoute filepath to the cold databases. |  |
| `coldToFrozenDir` | Destination path for the frozen archive. Used as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory. Bucket freezing policy is as follows: New style buckets (4.2 and on): removes all files but the rawdata To thaw, run splunk rebuild <bucket dir> on the bucket, then move to the thawed directory Old style buckets (Pre-4.2): gzip all the .data and .tsidx files To thaw, unzip the zipped files and move the bucket into the thawed directory If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence. |  |
| `coldToFrozenScript` | Path to the archiving script. See the POST parameter description for details. |  |
| `compressRawdata` | This value is ignored. splunkd process always compresses raw data. |  |
| `currentDBSizeMB` | Total size, in MB, of data stored in the index. The total incudes data in the home, cold and thawed paths. |  |
| `defaultDatabase` | If no index destination information is available in the input data, the index shown here is the destination of such data. |  |
| `enableOnlineBucketRepair` | Indicates whether to run asynchronous "online fsck" bucket repair, which runs in a process concurrently with Splunk software. |  |
| `enableRealtimeSearch` | Indicates if this is a real-time search. This is a global setting, not a per index setting. |  |
| `frozenTimePeriodInSecs` | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years). Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation. |  |
| `homePath` | An absolute path that contains the hot and warm buckets for the index. |  |
| `homePath_expanded` | An absolute filepath to the hot and warm buckets for the index. |  |
| `indexThreads` | Number of threads used for indexing. This is a global setting, not a per index setting. |  |
| `isInternal` | Indicates if this is an internal index (for example, _internal, _audit). |  |
| `isReady` | Indicates if an index is properly initialized. |  |
| `lastInitTime` | Last time the index processor was successfully initialized. This is a global setting, not a per index setting. |  |
| `maxBloomBackfillBucketAge` | If a bucket (warm or cold) is older than this, Splunk software does not create (or re-create) its bloom filter. |  |
| `maxConcurrentOptimizes` | The number of concurrent optimize processes that can run against a hot bucket. This number should be increased if instructed by Splunk Support. Typically the default value should suffice. |  |
| `maxDataSize` | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk software to autotune this parameter (recommended). Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto". A "high volume index" is typically one that gets over 10GB of data per day. "auto" sets the size to 750MB. "auto_high_volume" sets the size to 10GB on 64-bit, and 1GB on 32-bit systems. Although the maximum value you can set this is 1048576 MB, which corresponds to 1 TB, a reasonable number ranges anywhere from 100 - 50000. Any number outside this range should be approved by Splunk Support before proceeding. If you specify an invalid number or string, maxDataSize is auto-tuned. Note: The precise size of your warm buckets may vary from maxDataSize, due to post-processing and timing issues with the rolling policy. |  |
| `maxHotBuckets` | Maximum hot buckets that can exist per index. Defaults to 3. When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll. |  |
| `maxHotIdleSecs` | Maximum life, in seconds, of a hot bucket. Defaults to 0. A value of 0 turns off the idle check (equivalent to INFINITE idle time). If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. |  |
| `maxHotSpanSecs` | Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days). Note: If set too small, you can get an explosion of hot/warm buckets in the filesystem. The system sets a lower bound implicitly for this parameter at 3600, but this is an advanced parameter that should be set with care and understanding of the characteristics of your data. |  |
| `maxMemMB` | The amount of memory, in MB, allocated for indexing. This is a global setting, not a per index setting. |  |
| `maxMetaEntries` | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption. If set to 0, this setting is ignored (it is treated as infinite). If exceeded, a hot bucket is rolled to prevent further increase. If your buckets are rolling due to Strings.data hitting this limit, the culprit may be the punct field in your data. If you do not use punct, it may be best to simply disable this (see props.conf.spec in $SPLUNK_HOME/etc/system/README). There is a small time delta between when maximum is exceeded and bucket is rolled. This means a bucket may end up with epsilon more lines than specified, but this is not a major concern unless excess is significant. |  |
| `maxTime` | ISO8601 timestamp of the newest event time in the index. |  |
| `maxTimeUnreplicatedNoAcks` | Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0. Note: this is an advanced parameter. Understand the consequences before changing. |  |
| `maxTimeUnreplicatedWithAcks` | Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering). Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza. To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647. |  |
| `maxTotalDataSizeMB` | The maximum size of an index, in MB. |  |
| `maxWarmDBCount` | The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times are moved to cold. |  |
| `memPoolMB` | Determines how much memory is given to the indexer memory pool. This is a global setting, not a per-index setting. |  |
| `minRawFileSyncSecs` | Can be either an integer (or "disable"). Some filesystems are very inefficient at performing sync operations, so only enable this if you are sure it is needed The integer sets how frequently splunkd forces a filesystem sync while compressing journal slices. During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files. If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete. |  |
| `minStreamGroupQueueSize` | Minimum size of the queue that stores events in memory before committing them to a tsidx file. |  |
| `minTime` | ISO8601 timestamp of the oldest event time in the index. |  |
| `partialServiceMetaPeriod` | Related to serviceMetaPeriod. By default it is turned off (zero). If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync'ed at serviceMetaPeriod. partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens. If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect. |  |
| `processTrackerServiceInterval` | How often, in seconds, the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. |  |
| `quarantineFutureSecs` | Events with timestamp of quarantineFutureSecs newer than "now" are dropped into quarantine bucket. Defaults to 2592000 (30 days). This is a mechanism to prevent main hot buckets from being polluted with fringe events. |  |
| `quarantinePastSecs` | Events with timestamp of quarantinePastSecs older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events. |  |
| `rawChunkSizeBytes` | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. Note: rawChunkSizeBytes only specifies a target chunk size. The actual chunk size may be slightly larger by an amount proportional to an individual event size. Warning: This is an advanced parameter. Only change it if instructed to do so by Splunk Support. |  |
| `repFactor` | Index replication control. This parameter applies to only clustering slaves. auto = Use the master index replication configuration value. 0 = Turn off replication for this index. |  |
| `rotatePeriodInSecs` | Rotation period, in seconds, that specifies how frequently to check: If a new hot bucket needs to be created. If there are any cold buckets that should be frozen. If there are any buckets that need to be moved out hot and cold DBs, due to size constraints. |  |
| `serviceMetaPeriod` | Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds). You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path. |  |
| `suppressBannerList` | List of indexes for which we suppress "index missing" warning banner messages. This is a global setting, not a per index setting. |  |
| `sync` | Specifies the number of events that trigger the indexer to sync events. This is a global setting, not a per index setting. |  |
| `syncMeta` | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures. Note: Do not change this parameter without the input of Splunk Support. |  |
| `thawedPath` | Filepath to the thawed (resurrected) databases for the index. |  |
| `thawedPath_expanded` | Absolute filepath to the thawed (resurrected) databases. |  |
| `throttleCheckPeriod` | Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds). Note: Do not change this parameter without the input of Splunk Support. |  |
| `totalEventCount` | Total number of events in the index. |  |
| `tsidxDedupPostingsListMaxTermsLimit` | This setting is valid only when tsidxWritingLevel is at 4 or higher. This maximum term limit sets an upper bound on the number of terms kept inside an in-memory hash table that serves to improve tsidx compression. The tsidx optimizer uses the hash table to identify terms with identical postings lists. When the first instance of a term is received, its postings list is stored. When successive terms with identical postings lists are received, the tsidx optimizer makes them refer to the first instance of the postings list rather than creating and storing term postings list duplicates. Consider increasing this limit to improve compression for large tsidx files. For example, a tsidx file created with tsidxTargetSizeMB over 1500MB can contain a large number of terms with identical postings lists. Reducing this limit helps conserve memory consumed by optimization processes, at the cost of reduced tsidx compression. Set this limit to 0 to disable deduplicated postings list compression. This setting cannot exceed 1,073,741,824 (2 30 ). Defaults to 8,388,608 (2 23 ). |  |
| `tstatsHomePath` | Location where datamodel acceleration TSIDX data for this index is stored. |  |
| `warmToColdScript` | Script to run when moving data from warm to cold. See input parameter description for details. |  |

### `/services/data/indexes/{name}`

Access, update, or delete the {name} index.

#### DELETE

Removes the {name} index and the data contained in it.

#### GET

Access information about the {name} index.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `summarize` | Boolean | false |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `assureUTF8` | Indicates whether all data retreived from the index is proper UTF8. If enabled (set to True), degrades indexing performance. This is a global setting, not a per index setting. |  |
| `blockSignSize` | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. |  |
| `blockSignatureDatabase` | The index that stores block signatures of events. This is a global setting, not a per index setting. |  |
| `bloomfilterTotalSizeKB` | Total size of all bloom filter files, in KB. |  |
| `coldPath` | Filepath to the cold databases for the index. |  |
| `coldPath_expanded` | Absoute filepath to the cold databases. |  |
| `coldToFrozenDir` | Destination path for the frozen archive. Used as an alternative to a coldToFrozenScript. Splunk software automatically puts frozen buckets in this directory. Bucket freezing policy is as follows: New style buckets (4.2 and on): removes all files but the rawdata To thaw, run splunk rebuild <bucket dir> on the bucket, then move to the thawed directory Old style buckets (Pre-4.2): gzip all the .data and .tsidx files To thaw, unzip the zipped files and move the bucket into the thawed directory If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence. |  |
| `coldToFrozenScript` | Path to the archiving script. See the POST parameter description for details. |  |
| `compressRawdata` | This value is ignored. splunkd process always compresses raw data. |  |
| `currentDBSizeMB` | Total size, in MB, of data stored in the index. The total incudes data in the home, cold and thawed paths. |  |
| `defaultDatabase` | If no index destination information is available in the input data, the index shown here is the destination of such data. |  |
| `disabled` | Indicates if the index is disabled. |  |
| `enableRealtimeSearch` | Indicates if this is a real-time search. This is a global setting, not a per index setting. |  |
| `frozenTimePeriodInSecs` | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years). Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation. |  |
| `homePath` | An absolute path that contains the hot and warm buckets for the index. |  |
| `homePath_expanded` | An absolute filepath to the hot and warm buckets for the index. |  |
| `indexThreads` | Number of threads used for indexing. This is a global setting, not a per index setting. |  |
| `isInternal` | Indicates if this is an internal index (for example, _internal, _audit). |  |
| `lastInitTime` | Last time the index processor was successfully initialized. This is a global setting, not a per index setting. |  |
| `maxConcurrentOptimizes` | The number of concurrent optimize processes that can run against a hot bucket. This number should be increased if instructed by Splunk Support. Typically the default value should suffice. |  |
| `maxDataSize` | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk software to autotune this parameter (recommended). Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto". A "high volume index" is typically one that gets over 10GB of data per day. "auto" sets the size to 750MB. "auto_high_volume" sets the size to 10GB on 64-bit, and 1GB on 32-bit systems. Although the maximum value you can set this is 1048576 MB, which corresponds to 1 TB, a reasonable number ranges anywhere from 100 - 50000. Any number outside this range should be approved by Splunk Support before proceeding. If you specify an invalid number or string, maxDataSize is auto-tuned. Note: The precise size of your warm buckets may vary from maxDataSize, due to post-processing and timing issues with the rolling policy. |  |
| `maxHotBuckets` | Maximum hot buckets that can exist per index. Defaults to 3. When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll. |  |
| `maxHotIdleSecs` | Maximum life, in seconds, of a hot bucket. Defaults to 0. A value of 0 turns off the idle check (equivalent to INFINITE idle time). If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. |  |
| `maxHotSpanSecs` | Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days). Note: If set too small, you can get an explosion of hot/warm buckets in the filesystem. The system sets a lower bound implicitly for this parameter at 3600, but this is an advanced parameter that should be set with care and understanding of the characteristics of your data. |  |
| `maxMemMB` | The amount of memory, in MB, allocated for indexing. This is a global setting, not a per index setting. |  |
| `maxMetaEntries` | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption. If set to 0, this setting is ignored (it is treated as infinite). If exceeded, a hot bucket is rolled to prevent further increase. If your buckets are rolling due to Strings.data hitting this limit, the culprit may be the punct field in your data. If you do not use punct, it may be best to simply disable this (see props.conf.spec in $SPLUNK_HOME/etc/system/README). There is a small time delta between when maximum is exceeded and bucket is rolled. This means a bucket may end up with epsilon more lines than specified, but this is not a major concern unless excess is significant. |  |
| `maxRunningProcessGroups` | Maximum number of processes that the indexer fires off at a time. This is a global setting, not a per index setting. |  |
| `maxTime` | UNIX timestamp of the newest event time in the index. |  |
| `maxTotalDataSizeMB` | The maximum size of an index, in MB. |  |
| `maxWarmDBCount` | Maximum number of warm buckets. |  |
| `memPoolMB` | Determines how much memory is given to the indexer memory pool. This is a global setting, not a per-index setting. |  |
| `minRawFileSyncSecs` | Can be either an integer (or "disable"). Some filesystems are very inefficient at performing sync operations, so only enable this if you are sure it is needed The integer sets how frequently splunkd forces a filesystem sync while compressing journal slices. During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files. If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete. |  |
| `minTime` | UNIX timestamp of the oldest event time in the index. |  |
| `numBloomfilters` | The number of bloom filters created for this index. |  |
| `numHotBuckets` | The number of hot buckets created for this index. |  |
| `numWarmBuckets` | The number of warm buckets created for this index. |  |
| `partialServiceMetaPeriod` | Related to serviceMetaPeriod. By default it is turned off (zero). If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync'ed at serviceMetaPeriod. partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens. If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect. |  |
| `quarantineFutureSecs` | Events with timestamp of quarantineFutureSecs newer than "now" that are dropped into quarantine bucket. Defaults to 2592000 (30 days). This is a mechanism to prevent main hot buckets from being polluted with fringe events. |  |
| `quarantinePastSecs` | Events with timestamp of quarantinePastSecs older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events. |  |
| `rawChunkSizeBytes` | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. Note: rawChunkSizeBytes only specifies a target chunk size. The actual chunk size may be slightly larger by an amount proportional to an individual event size. Warning: This is an advanced parameter. Only change it if instructed to do so by Splunk Support. |  |
| `rotatePeriodInSecs` | Rotation period, in seconds, that specifies how frequently to check: If a new hot bucket needs to be created. If there are any cold buckets that should be frozen. If there are any buckets that need to be moved out hot and cold DBs, due to size constraints. |  |
| `serviceMetaPeriod` | Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds). You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path. |  |
| `summarize` | If true, leaves out certain index details, which provides a faster response. |  |
| `suppressBannerList` | List of indexes for which we suppress "index missing" warning banner messages. This is a global setting, not a per index setting. |  |
| `sync` | Specifies the number of events that trigger the indexer to sync events. This is a global setting, not a per index setting. |  |
| `syncMeta` | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures. Note: Do not change this parameter without the input of Splunk Support. |  |
| `thawedPath` | An absolute path that contains the thawed (resurrected) databases for the index. |  |
| `thawedPath_expanded` | Absolute filepath to the thawed (resurrected) databases. |  |
| `throttleCheckPeriod` | Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds). Note: Do not change this parameter without the input of Splunk Support. |  |
| `totalEventCount` | Total number of events in the index. |  |
| `tsidxDedupPostingsListMaxTermsLimit` | This setting is valid only when tsidxWritingLevel is at 4 or higher. This maximum term limit sets an upper bound on the number of terms kept inside an in-memory hash table that serves to improve tsidx compression. The tsidx optimizer uses the hash table to identify terms with identical postings lists. When the first instance of a term is received, its postings list is stored. When successive terms with identical postings lists are received, the tsidx optimizer makes them refer to the first instance of the postings list rather than creating and storing term postings list duplicates. Consider increasing this limit to improve compression for large tsidx files. For example, a tsidx file created with tsidxTargetSizeMB over 1500MB can contain a large number of terms with identical postings lists. Reducing this limit helps conserve memory consumed by optimization processes, at the cost of reduced tsidx compression. Set this limit to 0 to disable deduplicated postings list compression. This setting cannot exceed 1,073,741,824 (2 30 ). Defaults to 8,388,608 (2 23 ). |  |

#### POST

Updates the {name} index.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `blockSignSize` | Number | 0 |
| `bucketRebuildMemoryHint` | String | auto |
| `coldToFrozenDir` | String |  |
| `coldToFrozenScript` | String |  |
| `compressRawdata` | Boolean | true |
| `enableOnlineBucketRepair` | Boolean | true |
| `frozenTimePeriodInSecs` | Number | 188697600 |
| `maxBloomBackfillBucketAge` | Number | 30d |
| `maxConcurrentOptimizes` | Number | 6 |
| `maxDataSize` | Number | auto |
| `maxHotBuckets` | Number | 3 |
| `maxHotIdleSecs` | Number | 0 |
| `maxHotSpanSecs` | Number | 7776000 |
| `maxMemMB` | Number | 5 |
| `maxMetaEntries` | Number | 1000000 |
| `maxTimeUnreplicatedNoAcks` | Number | 300 |
| `maxTimeUnreplicatedWithAcks` | Number | 60 |
| `maxTotalDataSizeMB` | Number | 500000 |
| `maxWarmDBCount` | Number | 300 |
| `minRawFileSyncSecs` | Number | disable |
| `minStreamGroupQueueSize` | Number | 2000 |
| `partialServiceMetaPeriod` | Number | 0 |
| `processTrackerServiceInterval` | Number | 1 |
| `quarantineFutureSecs` | Number | 2592000 |
| `quarantinePastSecs` | Number | 77760000 |
| `rawChunkSizeBytes` | Number | 131072 |
| `repFactor` | String | 0 |
| `rotatePeriodInSecs` | Number | 60 |
| `serviceMetaPeriod` | Number | 25 |
| `syncMeta` | Boolean | true |
| `throttleCheckPeriod` | Number | 15 |
| `tstatsHomePath` | String |  |
| `warmToColdScript` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `assureUTF8` | Boolean value indicating wheter all data retreived from the index is proper UTF8. If enabled (set to True), degrades indexing performance Can only be set globally. |  |
| `blockSignSize` | Controls how many events make up a block for block signatures. If this is set to 0, block signing is disabled for this index. A recommended value is 100. |  |
| `blockSignatureDatabase` | The index that stores block signatures of events. This is a global setting, not a per index setting. |  |
| `bucketRebuildMemoryHint` | Suggestion for the bucket rebuild process for the size of the time-series (tsidx) file to make. |  |
| `coldPath` | Filepath to the cold databases for the index. |  |
| `coldPath_expanded` | Absoute filepath to the cold databases. |  |
| `coldToFrozenDir` | Destination path for the frozen archive. Used as an alternative to a coldToFrozenScript. Splunk Enterprise automatically puts frozen buckets in this directory. Bucket freezing policy is as follows: New style buckets (4.2 and on): removes all files but the rawdata To thaw, run splunk rebuild <bucket dir> on the bucket, then move to the thawed directory Old style buckets (Pre-4.2): gzip all the .data and .tsidx files To thaw, gunzip the zipped files and move the bucket into the thawed directory If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence. |  |
| `coldToFrozenScript` | Path to the archiving script. See the POST parameter description for details. |  |
| `compressRawdata` | This value is ignored. splunkd process always compresses raw data. |  |
| `currentDBSizeMB` | Total size, in MB, of data stored in the index. The total incudes data in the home, cold and thawed paths. |  |
| `defaultDatabase` | If no index destination information is available in the input data, the index shown here is the destination of such data. |  |
| `enableOnlineBucketRepair` | Indicates whether to run asynchronous "online fsck" bucket repair, which runs in a process concurrently with Splunk software. |  |
| `enableRealtimeSearch` | Indicates if this is a real-time search. This is a global setting, not a per index setting. |  |
| `frozenTimePeriodInSecs` | Number of seconds after which indexed data rolls to frozen. Defaults to 188697600 (6 years). Freezing data means it is removed from the index. If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation. |  |
| `homePath` | An absolute path that contains the hot and warm buckets for the index. |  |
| `homePath_expanded` | An absolute filepath to the hot and warm buckets for the index. |  |
| `indexThreads` | Number of threads used for indexing. This is a global setting, not a per index setting. |  |
| `isInternal` | Indicates if this is an internal index (for example, _internal, _audit). |  |
| `lastInitTime` | Last time the index processor was successfully initialized. This is a global setting, not a per index setting. |  |
| `maxBloomBackfillBucketAge` | If a bucket (warm or cold) is older than this, Splunk Enterprise does not create (or re-create) its bloom filter. |  |
| `maxConcurrentOptimizes` | The number of concurrent optimize processes that can run against a hot bucket. This number should be increased if instructed by Splunk Support. Typically the default value should suffice. |  |
| `maxDataSize` | The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk software to autotune this parameter (recommended). Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto". A "high volume index" is typically one that gets over 10GB of data per day. "auto" sets the size to 750MB. "auto_high_volume" sets the size to 10GB on 64-bit, and 1GB on 32-bit systems. Although the maximum value you can set this is 1048576 MB, which corresponds to 1 TB, a reasonable number ranges anywhere from 100 - 50000. Any number outside this range should be approved by Splunk Support before proceeding. If you specify an invalid number or string, maxDataSize is auto-tuned. Note: The precise size of your warm buckets may vary from maxDataSize, due to post-processing and timing issues with the rolling policy. |  |
| `maxHotBuckets` | Maximum hot buckets that can exist per index. Defaults to 3. When maxHotBuckets is exceeded, Splunk software rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll. |  |
| `maxHotIdleSecs` | Maximum life, in seconds, of a hot bucket. Defaults to 0. A value of 0 turns off the idle check (equivalent to INFINITE idle time). If a hot bucket exceeds maxHotIdleSecs, Splunk software rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. |  |
| `maxHotSpanSecs` | Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days). Note: If set too small, you can get an explosion of hot/warm buckets in the filesystem. The system sets a lower bound implicitly for this parameter at 3600, but this is an advanced parameter that should be set with care and understanding of the characteristics of your data. |  |
| `maxMemMB` | The amount of memory, in MB, allocated for indexing. This is a global setting, not a per index setting. |  |
| `maxMetaEntries` | Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption. If set to 0, this setting is ignored (it is treated as infinite). If exceeded, a hot bucket is rolled to prevent further increase. If your buckets are rolling due to Strings.data hitting this limit, the culprit may be the punct field in your data. If you do not use punct, it may be best to simply disable this (see props.conf.spec in $SPLUNK_HOME/etc/system/README). There is a small time delta between when maximum is exceeded and bucket is rolled. This means a bucket may end up with epsilon more lines than specified, but this is not a major concern unless excess is significant. |  |
| `maxTime` | UNIX timestamp of the newest event time in the index. |  |
| `maxTimeUnreplicatedNoAcks` | Upper limit, in seconds, on how long an event can sit in raw slice. Applies only if replication is enabled for this index. Otherwise ignored. If there are any acknowledged events sharing this raw slice, this paramater does not apply. In this case, maxTimeUnreplicatedWithAcks applies. Highest legal value is 2147483647. To disable this parameter, set to 0. Note: this is an advanced parameter. Understand the consequences before changing. |  |
| `maxTimeUnreplicatedWithAcks` | Upper limit, in seconds, on how long events can sit unacknowledged in a raw slice. Applies only if you have enabled acks on forwarders and have replication enabled (with clustering). Note: This is an advanced parameter. Make sure you understand the settings on all forwarders before changing this. This number should not exceed ack timeout configured on any forwarder, and should actually be set to at most half of the minimum value of that timeout. You can find this setting in outputs.conf readTimeout setting under the tcpout stanza. To disable, set to 0, but this is NOT recommended. Highest legal value is 2147483647. |  |
| `maxTotalDataSizeMB` | The maximum size of an index, in MB. |  |
| `maxWarmDBCount` | The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times are moved to cold. |  |
| `memPoolMB` | Determines how much memory is given to the indexer memory pool. This is a global setting, not a per-index setting. |  |
| `minRawFileSyncSecs` | Can be either an integer (or "disable"). Some filesystems are very inefficient at performing sync operations, so only enable this if you are sure it is needed The integer sets how frequently splunkd forces a filesystem sync while compressing journal slices. During this period, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files. If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete. |  |
| `minStreamGroupQueueSize` | Minimum size of the queue that stores events in memory before committing them to a tsidx file. |  |
| `minTime` | UNIX timestamp of the oldest event time in the index. |  |
| `partialServiceMetaPeriod` | Related to serviceMetaPeriod. By default it is turned off (zero). If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file. Records that require full re-write are be sync'ed at serviceMetaPeriod. partialServiceMetaPeriod specifies, in seconds, how frequently it should sync. Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens. If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect. |  |
| `processTrackerServiceInterval` | How often, in seconds, the indexer checks the status of the child OS processes it launched to see if it can launch new processes for queued requests. |  |
| `quarantineFutureSecs` | Events with timestamp of quarantineFutureSecs newer than "now" are dropped into quarantine bucket. Defaults to 2592000 (30 days). This is a mechanism to prevent main hot buckets from being polluted with fringe events. |  |
| `quarantinePastSecs` | Events with timestamp of quarantinePastSecs older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days). This is a mechanism to prevent the main hot buckets from being polluted with fringe events. |  |
| `rawChunkSizeBytes` | Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, rawChunkSizeBytes is set to the default value. Note: rawChunkSizeBytes only specifies a target chunk size. The actual chunk size may be slightly larger by an amount proportional to an individual event size. Warning: This is an advanced parameter. Only change it if instructed to do so by Splunk Support. |  |
| `repFactor` | Index replication control. This parameter applies to only clustering slaves. auto = Use the master index replication configuration value. 0 = Turn off replication for this index. |  |
| `rotatePeriodInSecs` | Rotation period, in seconds, that specifies how frequently to check: If a new hot bucket needs to be created. If there are any cold buckets that should be frozen. If there are any buckets that need to be moved out hot and cold DBs, due to size constraints. |  |
| `serviceMetaPeriod` | Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds). You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path. |  |
| `suppressBannerList` | List of indexes for which we suppress "index missing" warning banner messages. This is a global setting, not a per index setting. |  |
| `sync` | Specifies the number of events that trigger the indexer to sync events. This is a global setting, not a per index setting. |  |
| `syncMeta` | When true, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures. Note: Do not change this parameter without the input of Splunk Support. |  |
| `thawedPath` | Filepath to the thawed (resurrected) databases for the index. |  |
| `thawedPath_expanded` | Absolute filepath to the thawed (resurrected) databases. |  |
| `throttleCheckPeriod` | Defines how frequently Splunk software checks for index throttling condition, in seconds. Defaults to 15 (seconds). Note: Do not change this parameter without the input of Splunk Support. |  |
| `totalEventCount` | Total number of events in the index. |  |
| `tsidxDedupPostingsListMaxTermsLimit` | This setting is valid only when tsidxWritingLevel is at 4 or higher. This maximum term limit sets an upper bound on the number of terms kept inside an in-memory hash table that serves to improve tsidx compression. The tsidx optimizer uses the hash table to identify terms with identical postings lists. When the first instance of a term is received, its postings list is stored. When successive terms with identical postings lists are received, the tsidx optimizer makes them refer to the first instance of the postings list rather than creating and storing term postings list duplicates. Consider increasing this limit to improve compression for large tsidx files. For example, a tsidx file created with tsidxTargetSizeMB over 1500MB can contain a large number of terms with identical postings lists. Reducing this limit helps conserve memory consumed by optimization processes, at the cost of reduced tsidx compression. Set this limit to 0 to disable deduplicated postings list compression. This setting cannot exceed 1,073,741,824 (2 30 ). Defaults to 8,388,608 (2 23 ). |  |
| `tstatsHomePath` | Location where datamodel acceleration TSIDX data for this index is stored. |  |
| `warmToColdScript` | Script to run when moving data from warm to cold. See input parameter description for details. |  |

### `/services/data/indexes-extended`

#### GET

List bucket attributes for all indexes.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `bucket_dirs` | (If total_size > 0) Lists the following attributes for each index bucket super-directory (home, cold, thawed): bucket_count (thawed and cold only), event_count, event_max_time, event_min_time, hot_bucket_count (home only), size, warm_bucket_count (home only). |  |
| `total_bucket_count` | (If total_size > 0 ) Number of index buckets. |  |
| `total_event_count` | (If total_size > 0 ) Number of events for index, excluding frozen events. Approximately equal to the event_count sum of all buckets. |  |
| `total_raw_size` | (If total_size > 0 ) Cumulative size (fractional MB) on disk of the <bucket>/rawdata/ directories of all buckets in this index, excluding frozen . |  |
| `total_size` | Size (fractional MB) on disk of this index. |  |

### `/services/data/indexes-extended/{name}`

#### GET

Get {name} bucket information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `bucket_dirs` | (If total_size > 0 ) Lists the following attributes for each index bucket super-directory (home, cold, thawed): bucket_count (thawed and cold only), event_count, event_max_time, event_min_time, hot_bucket_count (home only), size, warm_bucket_count (home only). |  |
| `total_bucket_count` | (If total_size > 0 ) Number of index buckets. |  |
| `total_event_count` | (If total_size > 0 ) Number of events for index, excluding frozen events. Approximately equal to the event_count sum of all buckets. |  |
| `total_row_size` | (If total_size > 0 ) Cumulative size (fractional MB) on disk of the <bucket>/rawdata/ directories of all buckets in this index, excluding frozen . |  |
| `total_size` | Size (fractional MB) on disk of this index. |  |

### `/services/data/summaries`

Get disk usage information about all summaries in an indexer.

#### GET

Gets current summary disk usage information.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `report_acceleration` | Optional. Use "report_acceleration=1" to access disk usage by report acceleration summary. |  |
| `data_model_acceleration` | Optional. Use "data_model_acceleration=1" to access disk usage by data model acceleration summary. |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `related_indexes` | Lists up to 10 indexes that contribute to this summary. |  |
| `related_indexes_count` | Provides total count of related indexes for this summary. |  |
| `search_head_guid` | GUID for the search head that created the summary data. |  |
| `total_bucket_count` | Number of buckets for this summary. |  |
| `total_size` | Total disk size for this summary, in MB. |  |
| `type` | Summary type, either "report_acceleration" or "data_model_acceleration" . |  |

### `/services/data/summaries/{summary_name}`

Get disk usage information about the {name} indexer summary.

#### GET

Get disk usage information for the {name} summary.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `related_indexes` | Lists up to 10 indexes that contribute to this summary. |  |
| `related_indexes_count` | Provides total count of related indexes for this summary. |  |
| `search_head_guid` | GUID for search head creating the summary data. |  |
| `total_bucket_count` | Number of buckets for this summary. |  |
| `total_size` | Total summary disk size in MB. |  |

### `/services/server/health/deployment`

Shows the overall health of a distributed deployment. The health of the deployment can be red, yellow, or green. The overall health of the deployment is based on the health of all features reporting to it.

#### GET

Get the health status of a distributed deployment.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `health` | String | Indicates the overall health of the deployment. Health status can be red, yellow, or green. |

### `/services/server/health/deployment/details`

Shows the overall health of the distributed deployment, as well as each feature node and its respective color.

#### GET

Get health status of distributed deployment features.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `health` | String | Indicates the color of the feature: red, yellow or green. The color of mid-level features defaults to the worst health status color of all features reporting to it. |
| `reason` | String | Descriptive string that explains the reason the indicator is non-green. |

### `/services/server/health/splunkd`

Shows the overall health of splunkd . The health of splunkd can be red, yellow, or green. The health of splunkd is based on the health of all features reporting to it.

#### GET

Get the health status of splunkd .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `health` | String | Indicates the overall health of splunkd . Health status can be red, yellow, or green. |

### `/services/server/health/splunkd/details`

Shows the overall health of the splunkd health status tree, as well as each feature node and its respective color. For unhealthy nodes (non-green), the output includes reasons, indicators, thresholds, messages, and so on.

#### GET

Get health status of splunkd features.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `health` | String | Indicate the color of the feature: red, yellow or green. The color of midlevel features is the worst color of all the features reporting to it. |
| `messages` | String | The last 50 messages from splunkd.log that might relate to the feature status change. Returned only if a feature color is not green. |
| `reasons` | String | Describes the indicator(s) that caused the feature's status to change to a non-green state. Returned only if a feature color is not green. |
| `due_to_stanza` | String | Indicates the stanza name in health.conf where the configuration for the non-green indicator exists. |
| `due_to_threshold` | String | Indicates the threshold because of which the color of the indicator is non-green. |
| `due_to_threshold_value` | Numeric | Indicates the value of the above threshold. |
| `indicator` | String | Name of the indicator because of which the feature is non-green. |
| `reason` | String | Descriptive string that explains the reason the indicator is non-green. |

### `/services/server/health-config`

Endpoint to configure the splunkd health report.

#### GET

List configuration information for the splunkd health report.

### `/services/server/health-config/{alert_action}`

Configure alert actions for the splunkd health report.

#### POST

Configure alert actions for the splunkd health report.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `alert_action:<action_name>` | String | Specify the alert action name. <action_name> can be one of the following: CODE Copy [email \| PagerDuty] [email \| PagerDuty] |
| `action.to` | String | Primary email address to use with the email alert action. |
| `action.cc` | String | CC email address to use with the email alert action. |
| `action.bcc` | String | BCC email address to use with the email alert action. |
| `action.integration_url_override` | String | Sets the <integration key> value for PagerDuty alert action. For example action.integration_url_override=78c3b6cf0a884a538410fe2812273b0b |
| `disabled` | Boolean | Enables/disables the alert action. Possible values are 0 and 1. A value of 1 disables the alert action. |

### `/services/server/health-config/{feature_name}`

Edit feature- and indicator-level settings for the splunkd health report.

#### POST

Edit feature- and indicator-level settings for the splunkd health report.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `alert.disabled` | Boolean | Possible values are 0 or 1. A value of 1 disables alerting for this feature. If alerting is disabled in the [health_reporter] stanza, alerting for this feature is disabled, regardless of the value set here. If the value is set to 1, alerting or all indicators is disabled. Default: 0 (enabled). |
| `alert.min_duration_sec` | Number | The minimum amount of time, in seconds, that the health status color must persist before an alert triggers. |
| `alert.threshold_color` | String | The health status color that triggers an alert. Possible values are yellow and red. Default: red. |
| `alert:<indicator_name>.disabled` | Number | Possible values are 0 or 1. A value of 1 disables alerting for this indicator. Default: 0 (enabled). |
| `alert:<indicator_name>.min_duration_sec` | Number | The minimum amount of time, in seconds, that the health status color must persist before an alert triggers for this indicator. |
| `alert:<indicator_name>.threshold_color` | String | The health status color that triggers an alert for this indicator. Possible values are yellow and red. Default: red. |
| `disable` | Boolean | Disables/enables reporting the health of the feature. Use disabled=1 to disable the feature. Use disabled=0 to enable the feature. |
| `distributed_disabled` | Boolean | Disables/enables reporting the health of the feature in the distributed health report Use disabled=1 to disable the feature. Use disabled=0 to enable the feature. |
| `feature:<feature_name>` | String | Specify the feature name. feature_name can be any supported feature listed in $SPLUNK_HOME/etc/system/default/health.conf. |
| `indicator:<indicator name>:<color>` | Number | The indicator threshold value that triggers a health status change to the specified color for the indicator. |

### `/services/server/info`

#### GET

Get Splunk instance information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `activeLicenseGroup` | Type of Splunk software license. CODE Copy Enterprise Forwarder Free Invalid Trial Enterprise Forwarder Free Invalid Trial |  |
| `addOns` | Names of active add-ons. |  |
| `build` | The build number for this Splunk instance version. |  |
| `cpu_arch` | The architecture type for the CPU hosting splunkd . The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `guid` | Globally unique identifier for this server. |  |
| `host` | Server name. |  |
| `host_fqdn` | host fully-qualified domain name. |  |
| `isFree` | Indicates if this server is running the Splunk instance under a free license. |  |
| `isTrial` | Indicates if this server is using a trial license. |  |
| `kv_store_status` | App KV store availability. |  |
| `license_labels` | Labels associated with the license used on this server. |  |
| `licenseKeys` | License key unique for each license. |  |
| `licenseSignature` | Hash signature for the license used on this server. |  |
| `licenseState` | Specifies the status of the license, which can be either OK or Expired. |  |
| `master_guid` | Globally unique identifier for this server. |  |
| `max_users` | Maximum number of users on the instance. |  |
| `mode` | Indicates whether the server is a dedicated forwarder. Possible values are: CODE Copy normal dedicated forwarder normal dedicated forwarder |  |
| `numberOfCores` | Server number of processor cores. The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `os_build` | Software build for the server os_version . The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `os_name` | Server operating system. The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `os_version` | Server operating system version. The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `physicalMemoryMB` | Server physical memory (MB). The value returned in the server/info response should be considered deprecated. Use server/sysinfo to access this response key and value instead. |  |
| `product_type` | Splunk software product type. One of the following values. CODE Copy enterprise hunk lite lite_free splunk enterprise hunk lite lite_free splunk |  |
| `rtsearch_enabled` | Indicates if real-time search is enabled for the instance on this server. |  |
| `server_roles` | Zero or more of the following possible server roles. CODE Copy indexer universal_forwarder heavyweight_forwarder lightweight_forwarder license_master license_slave cluster_master cluster_slave cluster_search_head deployment_server deployment_client search_head search_peer shc_captain shc_deployer shc_member indexer universal_forwarder heavyweight_forwarder lightweight_forwarder license_master license_slave cluster_master cluster_slave cluster_search_head deployment_server deployment_client search_head search_peer shc_captain shc_deployer shc_member See also: server/roles endpoint. |  |
| `serverName` | Server DNS domain name. |  |
| `startup_time` | Server platform start time, in seconds since January 1, 1970 ( UNIX epoch ). |  |
| `version` | Displays the Splunk platform version. |  |
| `versionControlEnabled` | Indicates whether the View version history option is enabled on the instance. A value of True means that the option is enabled. |  |

### `/services/server/introspection`

Access system introspection artifacts.

#### GET

List introspection resources.

### `/services/server/introspection/indexer`

Access the current indexer status.

#### GET

Get indexer status information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `average_KBps` | Average indexer throughput (kbps). |  |
| `reason` | Status explanation. For a normal status, returns . . The following examples show possible abnormal status reasons. CODE Copy "idx=<indexerName> Throttling indexer, too many tsidx files in bucket=<bucketName>. Is splunk-optimize working? If not, low disk space may be the cause." "idx=<indexerName> Throttling indexer, too many tsidx files in bucket=<bucketName>. Is splunk-optimize working? If not, low disk space may be the cause." CODE Copy "You are low in disk space on partition <partitionName>. Indexing is paused. Will resume when free disk space rises above <minFreeMB>." "You are low in disk space on partition <partitionName>. Indexing is paused. Will resume when free disk space rises above <minFreeMB>." |  |
| `status` | Current indexer status. One of the following values. normal throttled stopped |  |

### `/services/server/introspection/kvstore`

#### GET

List app KV store resources.

### `/services/server/introspection/kvstore/collectionstats`

#### GET

Get collection storage statistics.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `data` | Returns the following JSON document. count - Number of collection documents or objects. indexSizes - Key and size of every index on the collection. lastExtentSize - Size of last allocated extent. nindexes - Number of indexes on the collection. ns - Current collection namespace. numExtents - Number of contiguously allocated data file regions. paddingFactor - Amount of space added to each document. size - Collection records total size. storageSize - Collection document storage allocation. systemFlags - Collection flags that reflect internal server options. totalIndexSize - Size of all indexes. userFlags - Collection flags set by user. Note: Sizes are returned in MBs. For more information, see Performance Metrics . |  |

### `/services/server/introspection/kvstore/replicasetstats`

#### GET

Get the status of the replica set from the point of view of the current server.

### `/services/server/introspection/kvstore/serverstatus`

Get an overview of the database process state.

#### GET

Get an overview of the database process state.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `data` | Returns the following CDATA items. asserts - Number of database assertions since the server process started, for each of the following levels/types: regular warning msg user rollovers backgroundFlushing - Write to disk flush metrics: flushes - Number of times writes flushed. total_ms - Number of msec processes used to flush writes. average_ms - Relationship between flushes and total_ms , in msec. last_ms - Number of msec the last flush took. last_finished (date) - ISO time of last completed write flush operation. connections - Current incoming connections status and database availability: current - Number of active client connections. available - Number of unused connections available. totalCreated - Total number of connections created, including closed connections. cursors - [DEPRECATED] Current cursor and state. Use metrics , instead. dur - (Durability) Journaling-related operations and performance. Journaling must be enabled.: commits - Number of transactions written to the journal during the last group commit interval. journaledMB - Amount of data (MB) written to the journal during the last group commit interval. writeToDataFilesMB - Amount of data (MB) written from journal to data files during the last group commit interval. compression - Compression ratio of data written to journal: (journaled_size_of_data / uncompressed_size_of_data) commitsInWriteLock - Number of commits that occurred during a write lock. earlyCommits - Number of commits requested before scheduled group commit time. timeMs : Performance during various journaling phases. dt - Data collection interval (msec). prepLogBuffer - Time spend preparing to write to journal (msec). writeToJournal - Time spent writing to journal (msec). writeToDataFiles - Time spent writing to data files after journaling (msec). remapPrivateView - Time spent remapping copy-on-write memory mapped views (msec). extra_info - Platform-specific information: note - Platform-specific information. heap_usage_bytes - Total heap space size used by database (bytes). Applicable to *nix systems, only. page_faults - Total number of page faults that require disk operations. globalLock - Information about the current database lock state, historical lock status, and active clients: totalTime - Time since database started and globalLock creation (usec). lockTime - Time since database started that globalLock has been held (usec). currentQueue : Information about operations queued because of a lock. total - Total number of operations queued waiting on readers and writers locks. readers - Number of operations queued waiting for read lock. writers - Number of operations queued waiting for write lock. activeClients : Information about number and operation types of connected clients. total - Total number of readers and writers connections. readers - Number of connected clients performing read operations. writers - Number of connected clients performing write operations. host - Hostname and port number. indexCounters - Index usage counters: accesses - Number of times operations accessed indexes. hits - Number of times index accessed and returned from memory. misses - Number of attempts to access index not in memory. resets - Number of times index counters reset since database last started. missRatio - Ratio of hits to misses . localTime - ISO-formatted local time. locks - State and read/write use of global and database-specific locks: timeLockedMicros - Amount of time a lock existed, for all databases of this server instance (usec). timeAcquiringMicros - Amount of time operations spend waiting, for lock for all databases of this server instance (usec). admin : Lock use in the admin database. timeLockedMicros - Amount of time locks existed in the admin database context (usec). timeAcquiringMicros - Amount of time spent waiting to acquire a lock in the admin database context (usec). local : Lock use in the local database. timeLockedMicros - Amount of time locks existed in the local database context (usec). timeAcquiringMicros - Amount of time spent waiting to acquire a lock in the local database context (usec). search. <collection> : Locks used in each collection. timeLockedMicros - Amount of time locks exist in the collection context (usec). timeAcquiringMicros - Amount of time spent waiting to acquire a lock in the collection context (usec). mem - Memory usage: System architecture and memory usage metrics. bits - System address architecture: 32 or 64 bit architecture. resident - Amount of RAM currently used by the database process (MB). virtual - Amount of virtual memroy used (MB). supported : true = supports extended memory information, false = does not support extended memory information. mapped - Amount of mapped memory for database (MB). mappedWithJournal - Amount of mapped memory, including journaling memory (MB). Always twice the size of mapped . metrics - Current instance use and state: cursor : Cursor state and use. timedOut - Total number of cursors that have timed out since the server process started. open : - Information about open cursors. noTimeout - Number of open cursors with option set to prevent timeout after a period of inactivity. pinned - Number of pinned open cursors. total - Number of cursors maintained for clients, typically less than zero. document : Information about document access and modification patterns and data use. Compare these values to opcounters data, which track total number of operations. deleted - Total number of deleted documents. inserted - Total number of inserted documents. returned - Total number of documents returned by queries. updated - Total number of updated documents. getLastError : Information about getLastError use. wtime : getLastError operation counts with a specified write concern that wait for one or more members of a replica set to acknowledge the write operation. num - getLastError operation counts with a specified write concern that wait for one or more members of a replica set to acknowledge the write operation. totalMillis - Amount of time spent performing getLastError operations with write concern that wait for one or more members of a replica set to acknowledge the write operation (msec). wtimeouts - Number of times write concern operations timed out as a result of the wtimeout threshold to getLastError . operation : Counters for several types of update and query operations handled using special operation types. fastmod - Number of update operations that neither cause documents to grow nor require updates to the index. idhack - Number of queries that contain the _key field. scanAndOrder - Number of queries that return sorted numbers that cannot perform the sort operation using an index. queryExecutor : Data from the query execution system. scanned - Number of index items scanned during queries and query-plan evaluation. scannedObjects - Total number of documents scanned during the query. record : Data related to record allocation in the on-disk memory files. moves - Number of times documents move within the on-disk representation of the data set. Documents move as a result of operations that increase the size of the document beyond their allocated record size. repl : Metrics related to the ordered history of logical writes. apply : - Information about the application of ordered history of logical writes. batches : Information on the ordered history of logical writes application process on secondaries members of replica sets. num - Number of batches applied across all databases. totalMillis - Amount of time spent applying ordered history of logical write operations (msec). ops - Number of ordered history of logical write operations. buffer : Information to track the ordered history of logical write operations buffer. count - Number of operations on the ordered history of logical writes buffer. maxSizeBytes/ - Maximum size of the ordered history of logical writes buffer. sizeBytes - Current size of the contents of the ordered history of logical writes buffer. network : Network use information for the replication process. bytes - Amount of data read from the replication sync source (bytes). getmores : Information about queries for additional results from the ordered history of logical write operations cursor as part of the replication process. num - Number of queries for additional results from the ordered history of logical write operations, which are operations that request an additional set of operations from the replication sync source. totalMillis - Amount of time to collect data from queries for additional results from the ordered history of logical write operations (msec). ops - Number of operations read from the replication source. readersCreated - Number of queries for additional results from the ordered history of logical write operations processes created. preload : Information about replication pre-fetch. docs : Information about documents loaded into memory during replication pre-fetch. num - Number of documents loaded during replication pre-fetch. totalMillis - Amount of time spent loading documents as part of replication pre-fetch (msec). indexes : Information about index items loaded into memory during replication pre-fetch. num - Number of index entries loaded by members before updating documents as part of replication pre-fetch. totalMillis - Amount of time spent loading index entries as part of replication pre-fetch (msec). storage : Freelist behavior monitoring statistics. freelist : Freelist bucket behavior monitoring statistics. search : Freelist bucket behavior monitoring search statistics. bucketExhausted - Number of times bucket fully searched, requiring advance to next bucket. requests - Number of times the allocation function was called. scanned - Number of freelist bucket entries examined. ttl : Information about resource use of the ttl index process. deletedDocuments - Number of documents deleted from collections with a ttl index. passes - Number of times background process removes documents from collections with a ttl index. network - Network use and state: bytesIn - Amount of network traffic received by this database (bytes). bytesOut - Amount of network traffic sent from this database (bytes). numRequests - Number of distinct requests received by the server. ok - Command return status: 1 = Success, 0 = Failure. opcounters - Overview of database operations by type, similar to opcountersRepl : insert - Number of insert operations since instance started. query - Number of queries since instance started. update - Number of update operations since instance started. delete - Number of delete operations since instance started. getmore - Number of getmore operations since instance started. command - Number of commands issued since instance started. opcountersRepl - Overview of replication operations by type, similar to opcounters : insert - Number of replicated insert operations since instance started. query - Number of replicated queries since instance started. update - Number of replicated update operations since instance started. delete - Number of replicated delete operations since instance started. getmore - Number of replicated getmore operations since instance started. command - Number of replicated commands issued since instance started. pid - Process ID. recordStats - Page fault statistics: accessesNotInMemory - Number of times memory page accessed that was not resident in memory, for all databases. pageFaultExceptionsThrown - Number of page fault exceptions thrown when accessing data for all databases. admin : Admin database page fault statistics. accessesNotInMemory - Number of times memory page accessed that was not resident in memory, for the admin database. pageFaultExceptionsThrown - Number of page fault exceptions thrown when accessing data for the admin database. local : Local database page fault statistics. accessesNotInMemory - Number of times memory page accessed that was not resident in memory, for the local database. pageFaultExceptionsThrown - Number of page fault exceptions thrown when accessing data for the local database. search. <collection> : Search database page fault statistics. accessesNotInMemory - Number of times memory page accessed that was not resident in memory, for the search database. pageFaultExceptionsThrown - Number of page fault exceptions thrown when accessing data for the search database. uptime - Amount of time database process has been active (seconds). uptimeEstimate - Amount of time database process has been active as calculated from the internal, course-grained time keeping system (seconds). uptimeMillis - Amount of time database process has been active (msec). version - Version number (not used). writeBacksQueued - Write-backs queued status: true = write-backs queued, false = write-backs not queued. |  |

### `/services/server/introspection/search/dispatch`

Provides vital statistics for distributed search framework, including details on search peer performance.

#### GET

Enumerate scheduled search details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Bundle_Directory_Reaper_Average_Time(ms)` | Average time for dispatch reaper to walk search peer directory and reap obsolete bundles. |  |
| `Bundle_Directory_Reaper_Max_Time(ms)` | Maximum time for dispatch reaper to walk search peer directory and reap obsolete bundles. |  |
| `Compute_User_Search_Quota_Average_Time(ms)` | Average time for computing user search quota. |  |
| `Compute_User_Search_Quota_Max_Time(ms)` | Maximum time for computing user search quota. |  |
| `Dispatch_Directory_Reaper_Average_Time(ms)` | Average time for dispatch reaper to walk dispatch directory and reap stale artifacts. |  |
| `Dispatch_Directory_Reaper_Max_Time(ms)` | Maximum time for dispatch reaper to walk dispatch directory and reap stale artifacts. |  |
| `Search_StartUp_Time_Average_Time(ms)` | Average time for preprocessing before search startup. Counted from time search state is set to RUNNING . Startup time indicates that parsing is complete and the distributed search infrastructure is set up. At startup, the Splunk platform is ready to wait for responses from indexers. |  |
| `Search_StartUp_Time_Max_Time(ms)` | Maximum time for preprocessing before search startup. Counted from time search state is set to RUNNING . Startup time indicates that parsing is complete and the distributed search infrastructure is set up. At startup, the Splunk platform is ready to wait for responses from indexers. |  |

### `/services/server/introspection/search/dispatch/Bundle_Directory_Reaper`

Get average and maximum time for the dispatch reaper to walk the search peer directory and reap obsolete bundles.

#### GET

Enumerate routine distributed search method execution times for each peer.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Bundle_Directory_Reaper_Average_Time(ms)` | Average time for dispatch reaper to walk search peer directory and reap obsolete bundles. |  |
| `Bundle_Directory_Reaper_Max_Time(ms)` | Maximum time for dispatch reaper to walk search peer directory and reap obsolete bundles. |  |

### `/services/server/introspection/search/dispatch/Compute_User_Search_Quota`

Provides average and maximum time for computing user search quotas.

#### GET

Enumerate average and maximum time for user search quota computation.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Compute_User_Search_Quota_Average_Time(ms)` | Average time for computing user search quota. |  |
| `Compute_User_Search_Quota_Max_Time(ms)` | Maximum time for computing user search quota. |  |

### `/services/server/introspection/search/dispatch/Dispatch_Directory_Reaper`

#### GET

Show dispatch directory reaper times for reaping stale artifacts.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Dispatch_Directory_Reaper_Average_Time(ms)` | Average time for dispatch reaper to walk dispatch directory and reap stale artifacts. |  |
| `Dispatch_Directory_Reaper_Max_Time(ms)` | Maximum time for dispatch reaper to walk dispatch directory and reap stale artifacts. |  |

### `/services/server/introspection/search/dispatch/Search_StartUp_Time`

Get average and maximum time for search preprocessing before startup.

#### GET

Enumerate average and maximum time for search preprocessing before startup.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Search_StartUp_Time_Average_Time(ms)` | Average time for preprocessing before search startup. Counted from time search state is set to RUNNING . |  |
| `Search_StartUp_Time_Max_Time(ms)` | Maximum time for preprocessing before search startup. Counted from time search state is set to RUNNING . |  |

### `/services/server/introspection/search/distributed`

Get information about the search knowledge bundle replication, if the current instance is the search head. Provides details about maximum and average time to execute routine distributed search methods, including peer info, peer bundles list, and authentication token requests from search heads.

#### GET

Enumerate routine distributed search method execution times for each peer.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `Get_Authentication_Max_Time(ms)` | Maximum time for search head to get authentication from this peer. |  |
| `Get_Authentication_Mean_Time(ms)` | Average time for search head to get authentication from this peer. |  |
| `Get_BundleList_Max_Time(ms)` | Maximum time for search head to get bundle list from this peer. |  |
| `Get_ServerInfo_Max_Time(ms)` | Maximum time for search head to get server information back from this peer. |  |
| `Get_ServerInfo_Mean_Time(ms)` | Average time for search head to get server information back from this peer. |  |

### `/services/server/introspection/search/saved`

Access most recent scheduled search priority scores and score calculation adjustments.

#### GET

Enumerate scheduled search details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `final_score` | Most recent calculated priority score, based on adjustments and original score. |  |
| `orig_score` | A score based on a search's originally scheduled run time. |  |
| `owner` | Search scope or context owner. This could be a specific user or "nobody" for a search defined in an app or system-level scope. |  |
| `priority_no` | Most recent calculated priority number for this search. |  |
| `real_time_adj` | Real-time search priority adjustment. Real-time searches default to -80000 and continuous scheduled searches default to 0. This particular value is for internal purposes only and is subject to change. |  |
| `runtime_adj` | Calculated value based on average search runtime. |  |
| `skipped_adj` | Adjustment for number of times search has been skipped and search period. 0 means the search has not been skipped. |  |
| `window_adj` | Adjustment for remaining time in search run window. |  |

### `/services/server/status`

List server/status child resources.

#### GET

Enumerate server/status endpoints.

### `/services/server/status/dispatch-artifacts`

Access search job information.

#### GET

Get information about dispatched search jobs.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `count_realtime` | Jobs active in the immediate past observation period, not including historical jobs. |  |
| `count_scheduled` | Jobs active in the immediate past observation period, not including real-time jobs. |  |
| `count_summary` | Jobs active in the immediate past observation period, not including non-summary jobs. |  |
| `top_apps` | Top 15 apps in the past observation period, in app : count key-value pair format. |  |
| `top_named_searches` | Top 15 named searches in the past observation period, in savedSearchName : count key-value pair format. |  |
| `top_users` | Top 15 users in the past observation period, in username : count key-value pair format, with count as the number of app contexts for the user. |  |
| `total_count` | Number of dispatched search jobs since start-up. |  |

### `/services/server/status/fishbucket`

Access information about the private BTree database.

#### GET

Access private BTree database information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `key_count` | Number of file input records (keys) seen since start-up. |  |
| `total_size` | Total number of file input records (keys). |  |

### `/services/server/status/installed-file-integrity`

Check for system file irregularities.

#### GET

Check file integrity status.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `refresh` | Boolean | Set to true to perform a new file integrity check. Only one such check can be performed at a time. |
| `regex_filter` | PCRE regular expression | Specify a regular expression to filter results of the check. For example, use regex_filter=\.conf$ to filter results for configuration files. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `<empty>` | Indicates complete file integrity. No irregularities were found. |  |
| `access_failed` | The splunkd process does not have permissions to read the file. |  |
| `differs` | The installed file differs from the manifest file. |  |
| `missing` | The installed file was not found. |  |
| `read_failed` | The installed file comparison failed. |  |
| `other_open_failed` | A failure other than failure to access or read was encountered when trying to open the file. |  |

### `/services/server/status/limits/search-concurrency`

Access search concurrency metrics for a standalone Splunk Enterprise instance.

#### GET

Get search concurrency limits for a standalone Splunk Enterprise instance.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `max_auto_summary_searches` | Maximum number of auto summary searches. |  |
| `max_hist_scheduled_searches` | Maximum number of historical scheduled searches. |  |
| `max_hist_searches` | Maximum number of historical searches. |  |
| `max_rt_scheduled_searches` | Maximum number of scheduled searches. |  |
| `max_rt_searches` | Maximum number of real-time searches. |  |

### `/services/server/status/partitions-space`

#### GET

Get disk utilization information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `capacity` | Disk capacity (MB). |  |
| `free` | Disk free space (MB). |  |
| `fs_type` | File system type. Example values: Linux: ext2, ext3, ext4, qnx4 Solaris: ufs, zfs Windows: ntfs, fat32 AIX: jfs (not OS-specific) WORM: ISO9660, UDF13346 (not OS-specific); network-shared: SMB, CIFS, NFS (not OS-specific) Veritas: VxFS. |  |
| `mount_point` | Absolute path of the directory where this partition is mounted. |  |

### `/services/server/status/resource-usage`

Get current resource (CPU, RAM, VM, I/O, file handle) utilization for entire host, and per Splunk-related processes.

#### GET

Get resource utilization information.

### `/services/server/status/resource-usage/hostwide`

Access host-level dynamic CPU utilization and paging information.

#### GET

Get host-level, dynamic CPU utilization and paging information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cpu_arch` | CPU architecture |  |
| `cpu_count` | CPU count |  |
| `cpu_idle_pct` | Percentage of time CPU is idle. |  |
| `cpu_system_pct` | Percentage of time CPU is running in system mode. |  |
| `cpu_user_pct` | Percentage of time CPU is running in user mode. |  |
| `forks` | Cumulative number of forked processes since OS startup. |  |
| `mem` | Total physical memory available (MB) |  |
| `mem_used` | Total physical memory used (MB). This value represents the amount of actual physical memory minus the amount of physical memory currently available. This is the amount of physical memory that can be immediately reused without having to first write its contents to disk. On Unix, mem_used = CODE Copy total_phys_ram - (free_mem + buffer_mem + cached_mem) total_phys_ram - (free_mem + buffer_mem + cached_mem) On Windows, mem_used = CODE Copy (memoryStatus.ullTotalPhys - memoryStatus.ullAvailPhys) (memoryStatus.ullTotalPhys - memoryStatus.ullAvailPhys) See GlobalMemoryStatusEx function for more information. |  |
| `normalized_load_avg_1min` | Normalized load average of runnable_process_count across all cores (cumulative_load_avg / number_of_cores). This value is not reliable for a VM guest. |  |
| `os_build` | Software build for the os_version |  |
| `os_name` | Operating system name |  |
| `os_name_ext` | Extended operating system name |  |
| `os_version` | Operating system version |  |
| `pg_paged_out` | Cumulative VM page count paged since OS startup. Not available on Windows. |  |
| `pg_swapped_out` | Cumulative pages swapped out since OS startup. Not available on Windows. |  |
| `runnable_process_count` | Number of process running or in the runnable queue. Value reported as 1 on Windows except for Vista+ and XP/Win2003 English-only operating systems. |  |
| `splunk_version` | Currently installed Splunk software version |  |
| `swap` | Amount of disk allocated to swap (fractional MB) |  |
| `swap_used` | Swap space currently in use (fractional MB) |  |
| `virtual_cpu_count` | Virtual CPU count |  |

### `/services/server/status/resource-usage/iostats`

#### GET

Get disk I/O statistics.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `avg_service_ms` | Average time requests caused the CPU to be in use, in milliseconds. |  |
| `avg_total_ms` | Average queue + execution time for requests to be completed, in milliseconds. |  |
| `cpu_pct` | Percentage of time the CPU was servicing requests. |  |
| `device` | Device name (e.g., as listed under /dev on UNIX). |  |
| `fs_type` | Mounted device file system type. |  |
| `interval` | Interval over which sampling occurred, in seconds. |  |
| `mount_point` | Mount point(s) of the underlying device. |  |
| `reads_kb_ps` | Total number of kb read per second. |  |
| `reads_ps` | Number of read requests per second. |  |
| `writes_kb_ps` | Total number of kb written per second. |  |
| `writes_ps` | Number of write requests per second. |  |

### `/services/server/status/resource-usage/splunk-processes`

Access operating system resource utilization information.

#### GET

Get process operating system resource utilization information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `args` | Non-search process arguments. |  |
| `cpu_system_time` | Cumulative time this process has spent executing in kernel (incl. system calls). Extra field. |  |
| `cpu_user_time` | Cumulative time this process has spent executing in user space (incl. library functions). Extra field. |  |
| `elapsed` | Elapsed wall time, accurate to within the collection period . |  |
| `fd_used` | Number of currently open files used by this process. |  |
| `label` | Human-readable label for the saved search. |  |
| `mem_unshared_data_used` | Amount of heap and stack used. Not available on Windows. Extra field. |  |
| `mem_used` | Current amount of resident physical memory used (MB). (Usually far less deceiving than virtual memory because operating systems can be liberal with virtual memory size but never with resident memory size.) On Windows, mem_used is obtained by reading the WorkingSetSize property returned by the GetProcessMemoryInfo() function (see GetProcessMemoryInfo function and PROCESS_MEMORY_COUNTERS structure ). |  |
| `normalized_pct_cpu` | Percentage of CPU usage across all cores. 100% is equivalent to all CPU resources on the machine. |  |
| `page_faults` | Number of major page faults. Extra field. |  |
| `pct_cpu` | Percentage of CPU usage, relative to one core. 100% is equivalent to 1 core. |  |
| `pct_memory` | Percentage of physical memory used hostwide (( mem_used /available_host_memory) * 100). |  |
| `pid` | Process ID. |  |
| `ppid` | Parent process ID. Not available for all processes. |  |
| `process` | Process name. The .exe suffix is stripped on Windows operating systems. |  |
| `read_mb` | Amount of data read (MB), excluding cache reads. |  |
| `search_head` | Dispatching search head for processes running saved searches. |  |
| `search_props` | Search properties map of the following key value pairs. acceleration_id : Acceleration ID app : App name mode : One of the following search modes. historical historical batch RT RT indexed provenance : One of the following search sources. cli rest ui:<App>:<View> role : Splunk Enterprise platform role. Either head or peer . scan_count : Event scan count for running process. Available only in Linux systems. This property is offered experimentally and might be changed or removed in a future release. delta_scan_count : Delta event scan count for running process. Available only in Linux systems. This property is offered experimentally and might be changed or removed in a future release. sid : Search ID (SID). type : One of the following search types. ad-hoc datamodel acceleration other report acceleration scheduled summary indexing user : Splunk username who initiated the search |  |
| `status` | Status from the OS scheduler. Can be R (runnable or running), W (waiting), stopped, Z (zombie), or O (other). W includes voluntary sleep or blocking on I/O. O means status is knowable but does not fit into one of those categories. Not available on Windows. |  |
| `t_count` | Current number of threads. |  |
| `written_mb` | Amount of data written (MB), excluding canceled writes. |  |

### `/services/server/sysinfo`

Exposes relevant information about the resources and OS settings of the machine where Splunk Enterprise is running.

#### GET

Access server details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cpu_arch` | Server CPU architecture. |  |
| `numberOfCores` | Number of server processor cores. Not applicable if host is a VM guest. A value of 0 is returned if the number cannot be accessed and the access failure reason is logged to splunkd.log . |  |
| `numberOfVirtualCores` | Number of server virtual cores. |  |
| `os_build` | Software build for the server os_version . |  |
| `os_name` | Server operating system name. |  |
| `os_name_extended` | Server operating system name. |  |
| `os_version` | Server operating system version. |  |
| `physicalMemoryMB` | Server physical memory (MB). The same value is returned as the mem field from server/status/resource-usage/hostwide . A value of 0 is returned if the number cannot be accessed and the access failure reason is logged to splunkd.log . |  |
| `transparent_hugepages` | For Linux systems, includes the following THP status indicators. defrag effective_state enabled For non-Linux systems, effective_state is set to ok |  |
| `ulimits` | On all UNIX systems, lists settings for the following ulimits in place on splunkd at runtime. core_file_size cpu_time data_file_size data_segment_size nice open_files resident_memory_size stack_size user_processes virtual_address_space_size |  |

### `/services/services/saved/bookmarks/monitoring_console`

Add URLs that link to monitoring consoles of your other deployments. For example, if you're admin overseeing multiple separate Splunk deployments for different teams.

#### GET

List deployment bookmarks.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count` | Number | Number of bookmark URLs to list. |
| `offset` | Number | Lists bookmark URLs, offset from the first bookmark. |
| `search` | String | Items to search for, must be valid as SPL. |
| `sort_dir` | Enum | asc or desc; ascending or descending |
| `sort_key` | String | Key to sort on, must be existing key in the stanza |

#### POST

Add deployment bookmark URLs.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `url` | string | Full URL to the monitoring console of a different Splunk deployment. |

#### DELETE

Remove deployment bookmark URLs.

---

## Knowledge

### `/services/admin/summarization`

Get aggregated details about all accelerated data model summaries.

#### GET

Get a list of field:value pairs that provide details about accelerated data models and their summaries.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `search` | The data models, represented as search strings. |  |
| `summary.access_count` | The total number of times that the summary for each data model has been accessed. |  |
| `summary.access_time` | The last time that the summary of each data model was accessed. |  |
| `summary.average_time` | The average runtime of the past 48 summarization search jobs for this data model. |  |
| `summary.buckets` | The total number of buckets in the summaries of each data model. |  |
| `summary.buckets_size` | The total size of the buckets in the summaries of each data model. The size is reported in terms of megabytes (MB). |  |
| `summary.complete` | Reports whether or not the summaries for each data model are complete. |  |
| `summary.earliest_time` | The timestamp of the earliest event in the summaries for each data model. |  |
| `summary.id` | The ID of the data models being summarized. The format is DM_<app_name>_<data_model_ID> . |  |
| `summary.is_inprogress` | Indicates whether or not the summary build is currently in progress for each data model. |  |
| `summary.last_error` | Lists errors that were logged in the latest run (from last_sid ) of the summary creation search. |  |
| `summary.last_sid` | The SID of the latest creation search job for each data model summary. |  |
| `summary.latest_time` | The timestamp of the latest events in each data model summary. |  |
| `summary.latest_dispatch_time` | The timestamp of the latest summary creation search for each data model. |  |
| `summary.latest_run_duration` | The runtime of the latest summary creation search for each data model. |  |
| `summary.mod_time` | The last time each data model summary was modified. |  |
| `summary.p50` | The 50th percentile of summarization search runtimes for each data model. 50 percent of the summarization searches for a given data model had runtimes that were less than this value. |  |
| `summary.p90` | The 90th percentile of summarization search runtimes for each data model. 90 percent of the summarization searches for a given data model had runtimes that were less than this value. |  |
| `summary.run_stats` | The start and duration of all saved previous summarization search jobs, up to 100 jobs. |  |
| `summary.size` | The total size of each summary, in bytes. |  |
| `summary.time_range` | The range of time covered by each summary. |  |

### `/services/admin/summarization/tstats:DM_{app}_{data_model_ID}`

Review information about the summaries of a specific data model. Identify specific data models by providing their app short name and their data model ID.

#### GET

Get detailed information about the acceleration summaries of a specific datamodel. See statistics about data model usage and information about the latest summary creation run.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `app required` | string |  |
| `data model ID required` | string |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `search` | The data model, represented as a search string. |  |
| `summary.access_count` | The total number of times that the summary for this data model has been accessed. |  |
| `summary.access_time` | The last time that the summary of this data model was accessed. |  |
| `summary.average_time` | The average runtime of the past 48 summarization search jobs for this data model. |  |
| `summary.buckets` | The total number of buckets in the summary of this data model. |  |
| `summary.buckets_size` | The total size of the buckets in the summary of this data model. The size is reported in terms of megabytes (MB). |  |
| `summary.complete` | Reports whether or not the summary for the data model are complete. |  |
| `summary.earliest_time` | The timestamp of the earliest event in the summary for this data model. |  |
| `summary.id` | The ID of the data model being summarized. The format is DM_<app_name>_<data_model_ID> . |  |
| `summary.is_inprogress` | Indicates whether or not the data model summary build is currently in progress. |  |
| `summary.last_error` | Lists errors that were logged in the latest run (from last_sid ) of the summary creation search. |  |
| `summary.last_sid` | The SID of the latest data model summary creation search job. |  |
| `summary.latest_time` | The timestamp of the latest event in the data model summary. |  |
| `summary.latest_dispatch_time` | The timestamp of the latest summary creation search for the data model. |  |
| `summary.latest_run_duration` | The runtime of the latest summary creation search for the data model. |  |
| `summary.mod_time` | The last time the data model summary was modified. |  |
| `summary.p50` | The 50th percentile of summarization search runtimes for the data model. 50 percent of the summarization searches for this data model had runtimes that were less than this value. |  |
| `summary.p90` | The 90th percentile of summarization search runtimes for the data model. 90 percent of the summarization searches for this data model had runtimes that were less than this value. |  |
| `summary.run_stats` | The start and duration of all saved previous summarization search jobs, up to 100 jobs. |  |
| `summary.size` | The total size of the summary, in bytes. |  |
| `summary.time_range` | The range of time covered by the summary. |  |

### `/services/data/lookup-table-files`

#### GET

List lookup table files.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | The app for which the lookup table applies. |  |
| `eai:data` | The source path for the lookup staging area. The lookup table file is moved from here into $SPLUNK_HOME. |  |
| `eai:userName` | The Splunk user who created the lookup table. |  |

#### POST

Create a lookup table file by moving a file from the upload staging area into $SPLUNK_HOME.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:data required` | String |  |
| `name required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | The app for which the lookup table applies. |  |
| `eai:data` | The source path for the lookup staging area. The lookup table file is moved from here into $SPLUNK_HOME. |  |
| `eai:userName` | The Splunk user who created the lookup table. |  |

### `/services/data/lookup-table-files/{name}`

Manage the {name} lookup table file.

#### DELETE

Delete the named lookup table file.

#### GET

List a single lookup table file.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | The app for which the lookup table applies. |  |
| `eai:attributes` | Field control information. |  |
| `eai:data` | The source path for the lookup staging area. The lookup table file is moved from here into $SPLUNK_HOME. |  |
| `eai:userName` | The Splunk user who created the lookup table. |  |

#### POST

Modify a lookup table file by replacing it with a file from the upload staging area.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:data required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | The app for which the lookup table applies. |  |
| `eai:data` | The source path for the lookup staging area. The lookup table file is moved from here into $SPLUNK_HOME. |  |
| `eai:userName` | The Splunk user who created the lookup table. |  |

### `/services/data/props/calcfields`

#### GET

Returns information on calculated fields for this instance of your Splunk deployment.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The name of the calculated field, which includes the "EVAL-" prefix. |  |
| `field.name` | The name of the field which is being calculated with an EVAL expression. |  |
| `stanza` | The name of the stanza in props.conf that defines the calculated field. |  |
| `type` | The type of the calculated field. This is always EVAL. |  |
| `value` | The EVAL statement for the calculated field. |  |

#### POST

Create an eval expression defining a calculated field in props.conf.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String |  |
| `stanza required` | String |  |
| `value required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The name of the calculated field, which includes the "EVAL-" prefix. |  |
| `field.name` | The name of the field which is being calculated with an EVAL expression. |  |
| `stanza` | The name of the stanza in props.conf that defines the calculated field. |  |
| `type` | The type of the calculated field. This is always EVAL. |  |
| `value` | The EVAL statement for the calculated field. |  |

### `/services/data/props/calcfields/{name}`

Manage the {name} calculated field.

#### DELETE

Deletes the named calculated field.

#### GET

Access the named calculated field.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The name of the calculated field, which includes the "EVAL-" prefix. |  |
| `field.name` | The name of the field which is being calculated with an EVAL expression. |  |
| `stanza` | The name of the stanza in props.conf that defines the calculated field. |  |
| `type` | The type of the calculated field. This is always EVAL. |  |
| `value` | The EVAL statement for the calculated field. |  |

#### POST

Update the named calculated field.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `value` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The name of the calculated field, which includes the "EVAL-" prefix. |  |
| `field.name` | The name of the field which is being calculated with an EVAL expression. |  |
| `stanza` | The name of the stanza in props.conf that defines the calculated field. |  |
| `type` | The type of the calculated field. This is always EVAL. |  |
| `value` | The EVAL statement for the calculated field. |  |

### `/services/data/props/extractions`

#### GET

List field extractions.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field extraction applies. for example, the sourcetype or source that triggers this field extraction. The full name of the field extraction includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

#### POST

Create a new field extraction.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String |  |
| `stanza required` | String |  |
| `type required` | Enum |  |
| `value required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | Specifies the name of the stanza for the field extraction. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

### `/services/data/props/extractions/{name}`

#### DELETE

Delete the named field extraction.

#### GET

List a single field extraction.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field extraction applies. for example, the sourcetype or source that triggers this field extraction. The full name of the field extraction includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

#### POST

Modify the named field extraction.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `value required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | Specifies the name of the stanza for the field extraction. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

### `/services/data/props/fieldaliases`

Access or create field aliases.

#### GET

List field aliases.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `alias.*` | The user-specified part of the field alias name. The full name of the field alias includes this identifier as a suffix. |  |
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field alias applies, e.g. the sourcetype or source that causes this field alias to be applied. The full name of the field alias includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

#### POST

Create a new field alias.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `alias.*` | The user-specified part of the field alias name. The full name of the field alias includes this identifier as a suffix. |  |
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field alias applies, e.g. the sourcetype or source that causes this field alias to be applied. The full name of the field alias includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform. |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

### `/services/data/props/fieldaliases/{name}`

Manage the {name} field alias.

#### DELETE

Delete the named field alias.

#### GET

Access a field alias.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `alias.*` | The user-specified part of the field alias name. The full name of the field alias includes this identifier as a suffix. |  |
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field alias applies, e.g. the sourcetype or source that causes this field alias to be applied. The full name of the field alias includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform . |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

#### POST

Update a field alias.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `alias.*` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `alias.*` | The alias for a given field. For example, supply a value of "bar" for an argument "alias.foo" to alias "foo" to "bar". |  |
| `attribute` | Specifies the field extraction configuration. For example, REPORT-<name> or EXTRACT-<name>. |  |
| `stanza` | The props.conf stanza to which this field alias applies, e.g. the sourcetype or source that causes this field alias to be applied. The full name of the field alias includes this stanza name as a prefix. |  |
| `type` | Specifies the field extraction type, which can be either inline or uses transform. |  |
| `value` | If this is an EXTRACT-type field extraction, a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, a list of transforms.conf stanza names that define the field transformations to apply. |  |

### `/services/data/props/lookups`

Access or create automatic lookups.

#### GET

List automatic lookups.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, LOOKUP-my_lookup. |  |
| `overwrite` | If set to true, output fields are always overridden. If set to false, output fields are only written out if they do not already exist. |  |
| `stanza` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |
| `transform` | The transforms.conf stanza that defines the lookup to apply. |  |
| `type` | Specifies the field extraction type. For this endpoint, this is always LOOKUP |  |
| `value` | The transform stanza with the value for the lookup. |  |

#### POST

Create an automatic lookup.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `lookup.field.input.*` | String |  |
| `lookup.field.output.*` | String |  |
| `name required` | String |  |
| `overwrite required` | Boolean |  |
| `stanza required` | String |  |
| `transform required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, LOOKUP-my_lookup. |  |
| `lookup.field.input.*` | A column in the lookup table to match against. Supply a non-empty value if the corresponding field has a different name in your actual events. |  |
| `lookup.field.output.*` | A column in the lookup table to output. Supply a non-empty value if the field should have a different name in your actual events. |  |
| `overwrite` | If set to true, output fields are always overridden. If set to false, output fields are only written out if they do not already exist. |  |
| `stanza` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |
| `transform` | The transforms.conf stanza that defines the lookup to apply. |  |
| `type` | Specifies the field extraction type. For this endpoint, this is alwqys LOOKUP . |  |
| `value` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |

### `/services/data/props/lookups/{name}`

#### DELETE

Delete an automatic lookup.

#### GET

Access an automatic lookup.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, LOOKUP-my_lookup. |  |
| `overwrite` | If set to true, output fields are always overridden. If set to false, output fields are only written out if they do not already exist. |  |
| `stanza` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |
| `transform` | The transforms.conf stanza that defines the lookup to apply. |  |
| `type` | Specifies the field extraction type. For this endpoint, this is always LOOKUP . |  |
| `value` | The transform stanza with the value for the lookup. |  |

#### POST

Update an automatic lookup.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `lookup.field.input.*` | String |  |
| `lookup.field.output.*` | String |  |
| `overwrite required` | Boolean |  |
| `transform required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | Specifies the field extraction configuration. For example, LOOKUP-my_lookup. |  |
| `lookup.field.input.*` | A column in the lookup table to match against. Supply a non-empty value if the corresponding field has a different name in your actual events. |  |
| `lookup.field.output.*` | A column in the lookup table to output. Supply a non-empty value if the field should have a different name in your actual events. |  |
| `overwrite` | If set to true, output fields are always overridden. If set to false, output fields are only written out if they do not already exist. |  |
| `stanza` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |
| `transform` | The transforms.conf stanza that defines the lookup to apply. |  |
| `type` | Specifies the field extraction type. For this endpoint, this is alwqys LOOKUP . |  |
| `value` | The props.conf stanza to which this automatic lookup applies. For example, the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix. |  |

### `/services/data/props/sourcetype-rename`

Access or rename props.conf sourcetypes.

#### GET

List renamed sourcetypes.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The configuration key. |  |
| `stanza` | The sourcetype to rename, which is the name of a stanza in props.conf. |  |
| `type` | The value of the configuration key. |  |
| `value` | The new name for the sourcetype. |  |

#### POST

Rename a sourcetype.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String |  |
| `value required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The configuration key. |  |
| `stanza` | The sourcetype to rename, which is the name of a stanza in props.conf. |  |
| `type` | The value of the configuration key. |  |
| `value` | The new name for the sourcetype. |  |

### `/services/data/props/sourcetype-rename/{name}`

Access, delete, or update a sourcetype name.

#### DELETE

Restore the original sourcetype name for {name} .

#### GET

Access a specific renamed sourcetype.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The configuration key. |  |
| `stanza` | The sourcetype to rename, which is the name of a stanza in props.conf. |  |
| `type` | The value of the configuration key. |  |
| `value` | The new name for the sourcetype. |  |

#### POST

Update a renamed sourcetype name.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `value required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `attribute` | The configuration key. |  |
| `stanza` | The sourcetype to rename, which is the name of a stanza in props.conf. |  |
| `type` | The value of the configuration key. |  |
| `value` | The new name for the sourcetype. |  |

### `/services/data/transforms/extractions`

Access field extraction definitions.

#### GET

List field extractions.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if the field transformation is disabled. |  |
| `eai:appName` | The Splunk app for which the field extractions are defined. For example, the search app. |  |
| `eai:userName` | The name of the Splunk user who created the field extraction definitions. For example, the admin user. |  |

#### POST

Create a new field transformation.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Bool | True |
| `CLEAN_KEYS` | Boolean | True |
| `disabled` | Boolean |  |
| `FORMAT` | String |  |
| `KEEP_EMPTY_VALS` | Boolean | False |
| `MV_ADD` | Boolean | False |
| `name required` | String |  |
| `REGEX required` | String |  |
| `SOURCE_KEY required` | String | _raw |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: \\tREGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). \\tREGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if the field transformation is disabled. |  |
| `eai:appName` | The Splunk app for which the field extractions are defined. For example, the search app. |  |
| `eai:userName` | The name of the Splunk user who created the field extraction definitions. For example, the admin user. |  |

### `/services/data/transforms/extractions/{name}`

Access, delete, or update the {name} field extraction.

#### DELETE

Delete a field extraction.

#### GET

Access a specific field extraction.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if the field transformation is disabled. |  |
| `eai:appName` | The Splunk app for which the field extractions are defined. For example, the search app. |  |
| `eai:attributes` | Field control information. |  |
| `eai:userName` | The name of the Splunk user who created the field extraction definitions. For example, the admin user. |  |

#### POST

Update a field extraction.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `REGEX` | String |  |
| `SOURCE_KEY` | String | _raw |
| `CAN_OPTIMIZE` | Bool | True |
| `CLEAN_KEYS` | Boolean | True |
| `FORMAT` | String |  |
| `KEEP_EMPTY_VALS` | Boolean |  |
| `MV_ADD` | Boolean |  |
| `disabled` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: \\tREGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). \\tREGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if the field transformation is disabled. |  |
| `eai:appName` | The Splunk app for which the field extractions are defined. For example, the search app. |  |
| `eai:userName` | The name of the Splunk user who created the field extraction definitions. For example, the admin user. |  |

### `/services/data/transforms/lookups`

Access or create lookup definitions.

#### GET

List lookup definitions.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `getsize` | Boolean | false |
| `replicate_delta` | Boolean | false |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation for data/transforms/extractions. |  |
| `GETSIZE` | If enabled, returns the file size. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if this lookup is disabled. |  |
| `eai:appName` | The Splunk app for which the lookups are defined. For example, the search app. |  |
| `eai:userName` | The Splunk user for which the lookups are defined. |  |
| `external_cmd` | Provides the command and arguments to invoke to perform a lookup. Use this for external (or "scripted") lookups, where you interface with with an external script rather than a lookup table. This string is parsed like a shell command. The first argument is expected to be a python script located in: $SPLUNK_HOME/etc/<app_name>/bin (or ../etc/searchscripts) Presence of this field indicates that the lookup is external and command based. |  |
| `fields_list` | List of all fields that are supported by the external command. |  |
| `replicate_delta` | Indicates that only the changes to a CSV lookup table are replicated, rather than the entire lookup table. |  |
| `type` | Specifies the field extraction type. Can be either external or file. |  |

#### POST

Update a lookup definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `collection` | String | <empty> |
| `default_match` | String |  |
| `disabled` | Boolean |  |
| `external_cmd` | String |  |
| `external_type` | One of the following values: python executable geo kvstore | python |
| `fields_list` | String |  |
| `filename` | String |  |
| `max_matches` | Number |  |
| `max_offset_secs` | Number |  |
| `min_matches` | Number |  |
| `min_offset_secs` | Number |  |
| `replicate_delta` | Boolean | false |
| `time_field` | String |  |
| `time_format` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation for data/transforms/extractions. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `default_match` | If min_matches is greater than zero and Splunk software has less than min_matches for any given input, it provides this default_match value one or more times until the min_matches threshold is reached. |  |
| `disabled` | Specifies whether the lookup definition is disabled. |  |
| `eai:appName` | The Splunk app for which the lookups are defined. For example, the search app. |  |
| `eai:userName` | The Splunk user for which the lookups are defined. |  |
| `external_cmd` | Provides the command and arguments to invoke to perform a lookup. Use this for external (or "scripted") lookups, where you interface with with an external script rather than a lookup table. This string is parsed like a shell command. The first argument is expected to be a python script located in: $SPLUNK_HOME/etc/<app_name>/bin (or ../etc/searchscripts) Presence of this field indicates that the lookup is external and command based. |  |
| `fields_list` | List of all fields that are supported by the external command. Use this for external (or "scripted") lookups. |  |
| `filename` | The name of the static lookup table file. |  |
| `max_matches` | The maximum number of possible matches for each input lookup value. If the lookup is non-temporal (not time-bounded, meaning the time_field attribute is not specified), Splunk software uses the first <integer> entries, in file order. If the lookup is temporal, Splunk software uses the first <integer> entries in descending time order. Default = 100 if the lookup is not temporal, default = 1 if it is temporal. |  |
| `max_offset_secs` | For temporal lookups, this is the maximum time (in seconds) that the event timestamp can be later than the lookup entry time for a match to occur. |  |
| `min_matches` | The minimum number of possible matches for each input lookup value. |  |
| `min_offset_secs` | For temporal lookups, this is the maximum time (in seconds) that the event timestamp can be later than the lookup entry time for a match to occur. |  |
| `time_field` | For temporal lookups, this is the field in the lookup table that represents the timestamp. |  |
| `time_format` | For temporal lookups, this specifies the \\"strptime\\" format of the timestamp field. |  |
| `type` | Specifies the field extraction type. Can be either external or file. |  |

### `/services/data/transforms/lookups/{name}`

Manage the {name} lookup definition.

#### DELETE

Delete a specific lookup definition.

#### GET

Access a specific lookup definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `replicate_delta` | Boolean | false |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Indicates whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | Indicates whether Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation for data/transforms/extractions. |  |
| `KEEP_EMPTY_VALS` | Indicates whether Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | For index-time filed extractions. Specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | "If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `disabled` | Indicates if this lookup is disabled. |  |
| `eai:appName` | The Splunk software app for which the lookups are defined. For example, the search app. |  |
| `eai:attributes` | Field control information. |  |
| `eai:userName` | The Splunk user for which the lookups are defined. |  |
| `filename` | The name of the static lookup table file. |  |
| `replicate_delta` | Indicates that only the changes to a CSV lookup table are replicated, rather than the entire lookup table. |  |
| `type` | Specifies the field extraction type. Can be either external or file. |  |

#### POST

Update a lookup definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `collection` | String | <empty> |
| `default_match` | String |  |
| `disabled` | Boolean |  |
| `external_cmd` | String |  |
| `external_type` | One of the following values: python executable geo kvstore | python |
| `fields_list` | String |  |
| `filename` | String |  |
| `max_matches` | Number |  |
| `max_offset_secs` | Number |  |
| `min_matches` | Number |  |
| `min_offset_secs` | Number |  |
| `replicate_delta` | Boolean | false |
| `time_field` | String |  |
| `time_format` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `CAN_OPTIMIZE` | Controls whether Splunk software can optimize this extraction out (another way of saying the extraction is disabled). You might use this when you have field discovery turned off--it ensures that certain fields are always discovered. Splunk software only disables an extraction if it can determine that none of the fields identified by the extraction is ever needed for the successful evaluation of a search. |  |
| `CLEAN_KEYS` | If set to true, Splunk software "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores. |  |
| `DEFAULT_VALUE` | Optional attribute for index-time field extractions. Splunk software writes the specified value to DEST_KEY if the specified REGEX fails. |  |
| `DEST_KEY` | Valid for index-time field extractions, specifies where Splunk software stores the REGEX results. |  |
| `FORMAT` | This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time. This attribute specifies the format of the event, including any field names or values you want to add. For details, refer to the documentation for this parameter in the POST operation for data/transforms/extractions. |  |
| `KEEP_EMPTY_VALS` | If set to true, Splunk software preserves extracted fields with empty values. |  |
| `LOOKAHEAD` | Optional attribute for index-time filed extractions. specifies how many characters to search into an event. Defaults to 4096. You may want to increase this value if you have event line lengths that exceed 4096 characters (before linebreaking). |  |
| `MV_ADD` | If Splunk software extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded. |  |
| `REGEX` | The regular expression to operate on your data. This attribute is valid for both index-time and search-time field extractions: REGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below). REGEX is required for all index-time transforms. For details, see the documentation for this parameter in the POST operation. |  |
| `SOURCE_KEY` | The KEY to which Splunk software applies REGEX. |  |
| `WRITE_META` | Indicates whether to automatically write REGEX to metadata. This attribute is required for all index-time field extractions except for those where DEST_KEY = meta (see the description of the DEST_KEY attribute). Use instead of DEST_KEY = meta. |  |
| `default_match` | If min_matches is greater than zero and Splunk software has less than min_matches for any given input, it provides this default_match value one or more times until the min_matches threshold is reached. |  |
| `disabled` | Specifies whether the lookup definition is disabled. |  |
| `eai:appName` | The Splunk app for which the lookups are defined. For example, the search app. |  |
| `eai:userName` | The Splunk user for which the lookups are defined. |  |
| `external_cmd` | Provides the command and arguments to invoke to perform a lookup. Use this for external (or "scripted") lookups, where you interface with with an external script rather than a lookup table. This string is parsed like a shell command. The first argument is expected to be a python script located in: $SPLUNK_HOME/etc/<app_name>/bin (or ../etc/searchscripts) Presence of this field indicates that the lookup is external and command based. |  |
| `fields_list` | List of all fields that are supported by the external command. Use this for external (or "scripted") lookups. |  |
| `filename` | The name of the static lookup table file. |  |
| `max_matches` | The maximum number of possible matches for each input lookup value. |  |
| `max_offset_secs` | For temporal lookups, this is the maximum time (in seconds) that the event timestamp can be later than the lookup entry time for a match to occur. |  |
| `min_matches` | The minimum number of possible matches for each input lookup value. |  |
| `min_offset_secs` | For temporal lookups, this is the maximum time (in seconds) that the event timestamp can be later than the lookup entry time for a match to occur. |  |
| `time_field` | For temporal lookups, this is the field in the lookup table that represents the timestamp. |  |
| `time_format` | For temporal lookups, this specifies the "strptime" format of the timestamp field. |  |
| `type` | Specifies the field extraction type. Can be either external or file. |  |

### `/services/data/transforms/metric-schema`

Use this endpoint to configure ingest-time log-to-metrics transformations. Identify measurements and blacklist dimensions. Design transformations that target specific event schemas within a log.

#### GET

List existing log-to-metrics configurations.

#### POST

Configures ingest-time conversion of log events to metric data points.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `name required` | String | Required. Name of the metric-schema stanza in transforms.conf . |
| `field_name required` | String | Comma-separated list of measure fields to be extracted from a log line. |
| `blacklist_dimension optional` | String | Comma-separated list of dimension fields to be omitted when log events are converted to metric data points. |
| `metric_name_prefix optional` | String | Used when the events in a log have more than one schema, meaning that they have differing sets of measure fields and blacklist dimension fields. Takes the value of a field that is shared by all events in the log, and whose values correspond to the different event schemas. |

#### DELETE

Delete existing log-to-metrics configurations.

### `/services/data/transforms/statsdextractions`

Use this endpoint to configure dimension extraction from StatsD metrics.

#### POST

Configures dimension extraction from StatsD metrics.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `unique_transforms_stanza_name` | String | A unique name for this stanza. |
| `REGEX = <regular expression>` | String | A regular expression that defines how to match and extract dimensions from StatsD metrics data. Splunk supports a named capturing-group extraction format (?<diml>group)(?dim2>group) ... to provide dimension names for the corresponding values that are extracted. |
| `REMOVE_DIMS_FROM_METRIC_NAME= <Boolean>` | Boolean | Specifies whether unmatched segments of the StatsD dotted name segment are used as the metric_name . When true , dimension values are be removed from the measurement and the unmatched portion becomes the metric_name . The default value is true . When false , extracted dimension values are included in the metric_name . For example, a metric measurement name is "x.y.z". The regular expression matches "y" and "z". When REMOVE_DIMS_FROM_METRIC_NAME is true , metric_name is "x". When false , metric_name is "x.y.z". |

### `/services/data/ui/global-banner`

View or create a global banner.

#### GET

View a global banner.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `background_color` | Indicates the color of the banner. |  |
| `hyperlink` | The link included in the banner. |  |
| `hyperlink_text` | Display text for the link in the banner. |  |
| `message` | Banner notification text. |  |
| `visible` | Boolean value indicating whether the banner is visible. |  |

#### POST

Create a new global banner.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `background_color required` | String | blue |
| `hyperlink optional` | String |  |
| `hyperlink_text optional` | String |  |
| `message required` | String | sample text |
| `visible required` | Boolean | false |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `background_color` | Indicates the color of the banner. |  |
| `hyperlink` | The link included in the banner. |  |
| `hyperlink_text` | Display text for the link in the banner. |  |
| `message` | Banner notification text. |  |
| `visible` | Boolean value indicating whether the banner is visible. |  |

### `/services/data/ui/panels`

View, add, or edit dashboard panels.

#### GET

Access all the XML definitions for existing panels.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the panel. |  |
| `eai:data` | XML definition for the panel. |  |
| `eai:userName` | User who created the panel. |  |
| `label` | Panel label. |  |
| `panel.title` | Panel title. |  |
| `rootNode` | XML root node. |  |

#### POST

Create a new dashboard panel source XML definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:data` | XML document |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the panel. |  |
| `eai:data` | XML definition for the panel. |  |
| `eai:userName` | User who created the panel. |  |
| `label` | Panel label. |  |
| `panel.title` | Panel title. |  |
| `rootNode` | XML root node. |  |

### `/services/data/ui/views`

View or create a dashboard source XML definition.

#### GET

Access all the XML definitions for existing dashboards.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the dashboard. |  |
| `eai:data` | XML definition for the dashboard. |  |
| `eai:type` | User interface type. For dashboards, this type is view . |  |
| `eai:userName` | User who created the dashboard. |  |
| `isDashboard` | Boolean value indicating whether the knowledge object is a dashboard. |  |
| `isVisible` | Boolean value indicating whether the dashboard is visible. |  |
| `label` | Dashboard label. |  |
| `rootNode` | XML root node. |  |

#### POST

Create a new dashboard source XML definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:data` | XML document |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the dashboard. |  |
| `eai:data` | XML definition for the dashboard. |  |
| `eai:type` | User interface type. For dashboards, this type is view . |  |
| `eai:userName` | User who created the dashboard. |  |
| `isDashboard` | Boolean value indicating whether the knowledge object is a dashboard. |  |
| `isVisible` | Boolean value indicating whether the dashboard is visible. |  |
| `label` | Dashboard label. |  |
| `rootNode` | XML root node. |  |

### `/services/data/ui/views/{name}`

Access or update source XML for an existing dashboard.

#### GET

Access an existing dashboard XML definition.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the dashboard. |  |
| `eai:data` | XML definition for the dashboard. |  |
| `eai:type` | User interface type. For dashboards, this type is view . |  |
| `eai:userName` | User who created the dashboard. |  |
| `isDashboard` | Boolean value indicating whether the knowledge object is a dashboard. |  |
| `isVisible` | Boolean value indicating whether the dashboard is visible. |  |
| `label` | Dashboard label. |  |
| `rootNode` | XML root node. |  |

#### POST

Update a specific dashboard XML definition.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:changelog optional` | string |  |
| `eai:data` | XML document |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `eai:appName` | App context for the dashboard. |  |
| `eai:data` | XML definition for the dashboard. |  |
| `eai:type` | User interface type. For dashboards, this type is view . |  |
| `eai:userName` | User who created the dashboard. |  |
| `isDashboard` | Boolean value indicating whether the knowledge object is a dashboard. |  |
| `isVisible` | Boolean value indicating whether the dashboard is visible. |  |
| `label` | Dashboard label. |  |
| `rootNode` | XML root node. |  |

#### DELETE

Delete a specific dashboard.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `eai:changelog optional` | string |  |

### `/services/data/ui/views/{name}/history`

View the revision history of a {name} dashboard.

#### GET

Access revisions made to a {name} dashboard.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `with_message optional` | String |  |

### `/services/data/ui/views/{name}/revision`

View a specific revision of a {name} dashboard.

#### GET

Access a specific revision made to a {name} dashboard.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `revision_id required` | String |  |

### `/services/datamodel/acceleration/{name} (DEPRECATED)`

Get information about the {name} datamodel.

#### GET

Get information about a specific data model.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | Indicates if acceleration is enabled for this data model. |  |
| `acceleration.earliest_time` | The earliest time to dispatch the search. |  |
| `search` | Specifies the search to accelerate this data model. |  |

### `/services/datamodel/model`

Access or create data models.

#### GET

List data models on the server.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `concise` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | Indicates whether acceleration is enabled for the data model. |  |
| `concise` | Indicates whether to list a concise JSON description of the data model. |  |
| `displayName` | The name displayed for the data model in Splunk Web. |  |
| `eai:appName` | The Splunk app in which the data model was created. |  |
| `eai:userName` | The name of the user who created the data model. |  |

#### POST

Create a new data model.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | String |  |
| `Hunk data model acceleration settings` | See description |  |

### `/services/datamodel/model/{name}`

Access, delete, or update the {name} data model.

#### DELETE

Delete a specific data model.

#### GET

Access a specific data model.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `concise` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | Indicates whether acceleration is enabled for the data model. |  |
| `concise` | Indicates whether to list a concise JSON description of the data model. |  |
| `displayName` | The name displayed for the data model in Splunk Web. |  |
| `eai:appName` | The Splunk app in which the data model was created. |  |
| `eai:attributes` | Field control information. |  |
| `eai:userName` | The name of the Splunk user who created the data model. |  |

#### POST

Update a specific data model.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | String |  |
| `Hunk data model acceleration settings` | See description |  |
| `provisional` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `acceleration` | Indicates whether acceleration is enabled for the data model. |  |
| `concise` | Indicates whether to list a concise JSON description of the data model. |  |
| `displayName` | The name displayed for the data model in Splunk Web. |  |
| `eai:appName` | The Splunk app in which the data model was created. |  |
| `eai:attributes` | Field control information. |  |
| `eai:userName` | The name of the Splunk user who created the data model. |  |

### `/services/datamodel/pivot`

Access pivots that are based on named data models.

#### GET

Get information about a specific pivot.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `pivot_json` | String |  |
| `pivot_search` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `drilldown_search` | The search for running this pivot report using drilldown |  |
| `open_in_search` | Equivalent to search parameter, but listed more simply. |  |
| `pivot_json` | JSON specifying a pivot based on the named data model. |  |
| `pivot_search` | A pivot search command based on the named data model. |  |
| `search` | The search string for running the pivot report |  |
| `tstats_search` | The search for running this pivot report using tstats |  |

### `/services/saved/bookmarks/monitoring_console`

Add URLs that link to monitoring consoles of your other deployments. For example, if you're admin overseeing multiple separate Splunk deployments for different teams.

#### GET

List deployment bookmarks.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count` | Number | Number of bookmark URLs to list. |
| `offset` | Number | Lists bookmark URLs, offset from the first bookmark. |
| `search` | String | Items to search for, must be valid as SPL. |
| `sort_dir` | Enum | asc or desc; ascending or descending |
| `sort_key` | String | Key to sort on, must be existing key in the stanza |

#### POST

Add deployment bookmark URLs.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `url` | string | Full URL to the monitoring console of a different Splunk deployment. |

#### DELETE

Remove deployment bookmark URLs.

### `/services/saved/eventtypes`

Access or create an event type.

#### GET

Retrieve saved event types.

#### POST

Create an event type.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `search` | String |  |
| `disabled` | Boolean | 0 |
| `priority` | Number | 1 |
| `tags` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if this event type is disabled. |  |
| `eai:appName` | The Splunk app for which this event type applies. For example, the Splunk search app. |  |
| `eai:userName` | Splunk user name of the creator of this event type. For example, the Splunk admin user. |  |
| `priority` | The value used to determine the order in which the matching event types of an event are displayed. 1 is the highest priority. |  |
| `search` | Search terms for this event type. |  |
| `tags` | [Deprecated] Tags associated with this event type. Use tags.conf.spec file to assign tags to groups of events with related field values. |  |

### `/services/saved/eventtypes/{name}`

#### DELETE

Delete an event type.

#### GET

Access the {name} event type.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the event type is disabled. |  |
| `eai:appName` | The Splunk app for which this event type applies. For example, the Splunk search app. |  |
| `eai:attributes` | Field control information. |  |
| `eai:userName` | Splunk user name of the creator of this event type. For example, the Splunk admin user. |  |
| `priority` | The value used to determine the order in which the matching event types of an event are displayed. 1 is the highest priority. |  |
| `search` | Search terms for this event type. |  |
| `tags` | [Deprecated] Tags associated with this event type. Use the tags.conf.spec file to assign tags to groups of events with related field values. |  |

#### POST

Update an event type.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `search` | String |  |
| `disabled` | Boolean | 0 |
| `priority` | Number | 1 |
| `tags` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if this event type is disabled. |  |
| `eai:appName` | The Splunk app for which this event type applies. For example, the Splunk search app. |  |
| `eai:userName` | Splunk user name of the creator of this event type. For example, the Splunk admin user. |  |
| `priority` | The value used to determine the order in which the matching event types of an event are displayed. 1 is the highest priority. |  |
| `search` | Search terms for this event type. |  |
| `tags` | [Deprecated] Tags associated with this event type. Use tags.conf.spec file to assign tags to groups of events with related field values. |  |

### `/services/search/fields`

Access search field configurations.

#### GET

Get a list of fields registered for field configuration.

### `/services/search/fields/{field_name}`

Access the {field_name} field.

#### GET

Get information about the {field_name} field.

### `/services/search/fields/{field_name}/tags`

Access or update the tags associated with the {field_name} field.

#### GET

Get tags associated with the {field_name} field.

#### POST

Update tags associated with the {field_name} field.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `value` | String |  |
| `add` | String |  |
| `delete` | String |  |

### `/services/search/tags`

Access search time tags.

#### GET

List all search time tags.

### `/services/search/tags/{tag_name}`

Access, update, or delete {tag_name} values.

#### DELETE

Delete the tag and its associated field:value pair assignments.

#### GET

Returns a list of field:value pairs associated with the {tag_name} tag.

#### POST

Update the field:value pairs associated with the {tag_name} tag.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add` | String |  |
| `delete` | String |  |

---

## Kv Store

### `/services/kvstore/backup/create`

#### POST

Create a KV Store backup archive file.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `archiveName` | String | Specify a file name for the backup. |
| `appName` | String | Specify a target app for backup, rather than all of the KV Store. Only available if pointInTime is not set to true. |
| `collectionName` | String | Specify a target collection for backup, rather than all of the KV Store. Only available if pointInTime is not set to true. |
| `pointInTime` | Boolean | Defaults to false. To take a consistent backup, set it to true. Only available for single-instance deployments. |
| `cancel` | Boolean | Defaults to false. Set it to true to cancel an in-progress backup. Only available if pointInTime is set to true. |
| `parallelCollections` | Number | Defaults to 1. Raise the number to increase the number of collections to back up in parallel. Only available if pointInTime is set to true. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | Code 200 for success, and code 404 for failure. |  |

### `/services/kvstore/backup/restore`

#### POST

Extracts the KV Store backup archive file and restores the KV Store.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `archiveName` | String | Required . Specifies the name of the backup file. |
| `appName` | String | Specify a target app for backup, rather than all of the KV Store. Only available if pointInTime is not set to true. |
| `collectionName` | String | Specify a target collection for backup, rather than all of the KV Store. Only available if pointInTime is not set to true. |
| `pointInTime` | Boolean | Defaults to false. To restore from a backup taken with consistency, set it to true. |
| `cancel` | Boolean | Defaults to false. Set it to true to cancel an in-progress restore. Only available if pointInTime set to true. |
| `parallelCollections` | Number | Defaults to 1. Raise the number to increase the number of collections to restore in parallel, which speeds up the store. Only available if pointInTime set to true. |
| `insertionsWorkersPerCollection` | Number | Defaults to 1. Raise to increase the number of insertion workers per collection, which speeds up the restore. Only available if pointInTime set to true. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `status` | Code 200 for success, and code 404 for failure. |  |

### `/services/kvstore/control/maintenance`

#### POST

Toggle maintenance mode.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `mode` | Boolean | Required. Type true to enter maintenance mode. To exit, type false . |

### `/services/kvstore/status`

Access KV store status information for standalone or search head clustering (SHC) deployments. For SHC deployments, provides information on SHC members where KV Store is enabled and used for replication.

#### GET

Access KV store status information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `current` | Includes the following indicators for the machine making the GET request. backupRestoreStatus : Status for a KV Store backup in progress. One of the following values: Busy : Backup or restore in progress. Failed : Restore failed to extract an archive file. Ready : Ready to run a backup or restore. Shutdown : KV Store is in the process of shutting down. backupRestoreProgress : Counter that increments each time a collection finishes being backed up or restored. date : DateTime when this status was retrieved. datesec : Unix timestamp, equivalent to date disabled : If KV Store is disabled on the current member. 0 means enabled, 1 means disabled. guid : Instance ID of the current member. oplogEndTimestamp : Last recorded timestamp in the operations log. Last update in all KV Store collections. Compare this indicator to other instances to check if KV Store members are not up to date. oplogEndTimestampSec : Unix timestamp equivalent to oplogEndTimestamp oplogStartTimestamp : First recorded timestamp in the operations log. oplogStartTimestampSec : Unix timestamp equivalent to oplogStartTimestamp port : KV Store port replicaSet : Replica set name. Instance ID by default for standalone mode. Configured in server.conf for SHC. replicationStatus : In standalone mode, this is KV Store captain . Otherwise, one of the following values. Startup KV Store captain Non-captain KV Store member Recovering Initial Sync Unknown status Down Rollback Removed standalone : Indicates whether the machine making the request is a standalone member or SHC member. 1 indicates a standalone member. status : KV Store status. One of the following values. unknown disabled starting ready failed shuttingdown |  |
| `Enabled KV Store members` | Returned for SHC deployments. Lists the following values for SHC members where KV Store is enabled and used for replication. guid : Instance ID of the current member. hostAndPort : Address used for replication between KV Store members and for accessing members from splunkd . Can be configured in server.conf . |  |
| `members` | For KV Store members, lists the following indicators. configVersion : Version number that increases each time the KV Store cluster is updated. electionDate : DateTime for election. electionDateSec : Unix equivalent of electionDate hostAndPort : Address used for replication between KV Store members and for accessing members from splunkd . Can be configured in server.conf . lastHeartbeat : Last time the requesting member sent a heartbeat to this member. lastHeartbeatRecv : Last time this member replied on heartbeat. lastHeartbeatRecvSec : Unix equivalent of lastHeartbeatRecv lastHeartbeatSec : Unix equivalent of lastHeartbeat optimeDate : Last recorded timestamp for this member in the operations log. optimeDateSec : Unix equivalent of optimeDate pingMs : Latency (milliseconds for round trip. replicationStatus : In standalone mode, this is KV Store captain . Otherwise, one of the following values. Startup KV Store captain Non-captain KV Store member Recovering Initial Sync Unknown status Down Rollback Removed uptime : Number of seconds this member has been online. |  |

### `/services/shcluster/captain/kvmigrate/start`

#### POST

Start the migration.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `storageEngine` | String | Required. Name of target storage engine, wiredTiger or mmap . |
| `isDryRun` | Boolean | Type true to complete pre-flight checks and exit without migrating. Setting is false by default. |
| `maxRetries` | Number | Number of times to retry a failed migration, per member. |
| `clusterPerc` | Number | Percentage of peers to migrate. |
| `peersList` | String | Names of peers to migrate, listed with name and management port. For example: CODE Copy peersList="server1:8089,server2:8089,server3:8089" peersList="server1:8089,server2:8089,server3:8089" |

### `/services/shcluster/captain/kvmigrate/status`

#### GET

Check the status.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `clusterPerc` | Percentage of cluster members that have completed migration. |  |
| `migrationID` | ID number for the migration. |  |
| `migrationStartTime` | Timestamp that the migration began. |  |
| `peerRetryCount` | Number of times that the peer failed to migrate and retried. |  |
| `status` | Status of the migration. |  |
| `storageEngine` | Target storage engine. |  |

### `/services/shcluster/captain/kvmigrate/stop`

#### POST

Stop the migration.

### `/services/storage/collections/config`

#### GET

List all collections.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean indicating collection state. By default, the value is false , indicating that the collection is enabled. |  |
| `profilingEnabled` | Boolean indicating profiling status of slow-running operations. By default, this value is false , meaning that profiling is disabled. |  |
| `profilingThresholdMs` | Threshold for logging slow-running operations, in milliseconds. Applies only if profilingEnabled is true . |  |

#### POST

Create a collection.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `profilingEnabled` | Boolean | A collections.conf file property that affects profilingThresholdMs . Defaults to false . Enable profiling of slow-running operations by setting profilingEnabled to true . |
| `profilingThresholdMs` | Number | Threshold for logging slow-running operations, in milliseconds. Applies only if profilingEnabled is true . Defaults to 100 . Set to 0 to log all slow-running operations. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean indicating collection state. By default, the value is false , indicating that the collection is enabled. |  |
| `profilingEnabled` | Profiling status of slow-running operations, profilingThresholdMs . Defaults to false . |  |
| `profilingThresholdMs` | Threshold for logging slow-running operations, in milliseconds. Applies only if profilingEnabled is true . |  |

### `/services/storage/collections/config/{collection}`

Access, delete, or update a specific {collection} .

#### DELETE

Delete a specific {collection} .

#### GET

Access a specific {collection} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean indicating collection state. By default, the value is 0 , meaning that the collection is enabled. |  |
| `field.<fieldName>` | Field type. One of the following values. array number bool string cidr time |  |
| `accelerated_fields. <field_name>` | Field acceleration name and JSON definition. |  |
| `enforceTypes` | Boolean indicating if data types are enforced when inserting data into the collection. Defaults to false . |  |
| `profilingEnabled` | Profiling status of slow-running operations, affecting profilingThresholdMs . By default, the value is false , meaning that profiling is disabled. If true , profiling is enabled. |  |
| `profilingThresholdMs` | Threshold for logging slow-running operations, in milliseconds. Applies only if profilingEnabled is true . |  |
| `replicate` | Boolean indicating whether the collection is replicated on indexers. Defaults to false , meaning that this collection is not replicated, and lookups that depend on the collection will not be available. However, if you run a lookup command with local=true , local lookups will still be available. When true , this collection is replicated on indexers. |  |
| `replication_dump_maximum_file_size` | Indicates the maximum file size (in KB) for each dump file when replication_dump_strategy = auto . Defaults to 10240KB. If this value is larger than concerningReplicatedFileSize , which is set in the distsearch.conf file, the value of concerningReplicatedFileSize is used instead. KV Store does not pre-calculate the size of the records that will be written to disk, so the size of the resulting files can be affected by the max_rows_in_memory_per_dump setting in the limits.conf file. |  |
| `replication_dump_strategy` | One of the following two values. auto : Default. Dumps are stored in multiple files when the size of the collection exceeds the value of replication_dump_maximum_file_size . one_file : Dump files are stored in a single file. |  |

#### POST

Update a specific {collection} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `field.<fieldName>` | String | Field type. One of the following values. array number bool string cidr time |
| `accelerated_fields.<field_name>` | String, JSON (see description) | The name of a field acceleration (string) and its definition, in JSON key value format. For example, accelerated_fields.my_accel = {"id": 1} |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Collection state: true = disabled. false = [Default] enabled. |  |
| `field.<fieldName>` | Field type. One of the following values. array number bool string cidr time |  |
| `accelerated_fields.<field_name>` | The name of a field acceleration (string) and its definition, in JSON key value format. For example, accelerated_fields.my_accel = {"id": 1} |  |
| `profilingEnabled` | Profiling status of slow-running operations, affecting profilingThresholdMs . By default, the value is false , meaning that profiling is disabled. If true , profiling is enabled. |  |
| `profilingThresholdMs` | Threshold for logging slow-running operations, in milliseconds. Applies only if profilingEnabled is true . |  |
| `replicate` | Boolean indicating whether the collection is replicated on indexers. Defaults to false , meaning that this collection is not replicated, and lookups that depend on the collection will not be available. However, if you run a lookup command with local=true , local lookups will still be available. When true , this collection is replicated on indexers. |  |
| `replication_dump_maximum_file_size` | Indicates the maximum file size (in KB) for each dump file when replication_dump_strategy = auto . Defaults to 10240KB. If this value is larger than concerningReplicatedFileSize , which is set in the distsearch.conf file, the value of concerningReplicatedFileSize is used instead. KV Store does not pre-calculate the size of the records that will be written to disk, so the size of the resulting files can be affected by the max_rows_in_memory_per_dump setting in the limits.conf file. |  |
| `replication_dump_strategy` | One of the following two values. auto : Default. Dumps are stored in multiple files when the size of the collection exceeds the value of replication_dump_maximum_file_size . one_file : Dump files are stored in a single file. |  |

### `/services/storage/collections/data/{collection}`

#### DELETE

Delete items in the {collection} or delete an entire collection.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `query` | JSON object | Query JSON object. Conditional operators: $gt , $gte , $lt , $lte , and $ne Logical operators: $and , $or , and , $not (invert conditional operators) Examples: query={"title":"Item"} (Select all documents with property title that has value Item ) query={"price":{"$gt":5}} (Select all documents with price greater than 5 ) |

#### GET

Access a specific {collection} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `fields` | String | Comma-separated list of fields to include ( 1 ) or exclude ( 0 ). A fields value cannot contain both include and exclude specifications except for exclusion of the _key field. Examples: fields=firstname,surname (Include only firstname , surname , and _key fields) fields=firstname,surname,_key:0 (Include only the firstname and surname fields) fields=address:0 (Include all fields except the address field) |
| `shared` | Boolean | Defaults to false. Set to true to return records for the specified user as well as records for the nobody user. |
| `limit` | Number | Maximum number of items to return. For example, to return five items, use limit=5 . |
| `skip` | Number | Number of items to skip from the start. For example, to skip the first ten items, use skip=10 . |
| `sort` | String | Sort order. Examples: sort=surname (Sort by surname , ascending) sort=surname,firstname (Sort by surname , ascending, after firstname , ascending) sort=surname:-1,firstname:1 (Sort by surname , descending, after firstname , ascending sort=surname:1,first name (Sort by surname , ascending, after firstname , ascending |
| `query` | JSON object | Query JSON object. Conditional operators: $gt , $gte , $lt , $lte , and $ne Logical operators: $and , $or , and , $not (invert conditional operators) Examples: query={"title":"Item"} (Select all documents with property title that has value Item ) query={"price":{"$gt":5}} (Select all documents with price greater than 5 ) |

#### POST

Insert an item into the {collection} .

### `/services/storage/collections/data/{collection}/{key}`

#### DELETE

Delete a collection item.

#### GET

Access a collection item.

#### POST

Update a collection item.

### `/services/storage/collections/data/{collection}/batch_find`

Perform multiple queries in a batch.

#### POST

Perform multiple queries in a batch.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `fields` | String | Comma-separated list of fields to include ( 1 ) or exclude ( 0 ). A fields value cannot contain both include and exclude specifications except for exclusion of the _key field. Examples: fields=firstname,surname (Include only firstname , surname , and _key fields) fields=firstname,surname,_key:0 (Include only the firstname and surname fields. fields=address:0 (Include all fields except the address field) |
| `shared` | Boolean | Defaults to false. Set to true to return records for the specified user as well as records for the nobody user. |
| `limit` | Number | Maximum number of items to return. For example, to return five items, use limit=5 . |
| `skip` | Number | Number of items to skip from the start. For example, to skip the first ten items, use skip=10 . |
| `sort` | String | Sort order. Examples: sort=surname (Sort by surname , ascending) sort=surname,firstname (Sort by surname , ascending, after firstname , ascending) sort=surname:-1,firstname:1 (Sort by surname , descending, after firstname , ascending sort=surname:1,first name (Sort by surname , ascending, after firstname , ascending |
| `query` | JSON object | Query JSON object. Conditional operators: $gt , $gte , $lt , $lte , and $ne Logical operators: $and , $or , and , $not (invert conditional operators) Examples: query={"title":"Item"} (Select all documents with property title that has value Item ) query={"price":{"$gt":5}} (Select all documents with price greater than 5 ) |

### `/services/storage/collections/data/{collection}/batch_save`

Perform multiple save operations in a batch.

#### POST

Perform multiple save operations in a batch.

---

## License

### `/services/licenser/groups`

Provides access to the configuration of licenser groups.

#### GET

Lists all licenser groups.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `is_active` | Indicates if the license group is active. |  |
| `stack_ids` | The license stacks in the license group. |  |

### `/services/licenser/groups/{name}`

#### GET

List a specific licenser group.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `is_active` | Indicates if the license group is active. |  |
| `stack_ids` | The license stacks in the license group. |  |

#### POST

Activate a specific licenser group and deactivate the previously active one.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `is_active` | Boolean |  |

### `/services/licenser/licenses`

#### GET

List all licenses added.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `creation_time` | The creation time of this license, in Coordinated Universal Time (UTC). |  |
| `expiration_time` | The time this license expires, in Coordinated Universal Time (UTC). |  |
| `features` | The list of features and components enabled by this license. |  |
| `group_id` | The ID of the group to which this license belongs. |  |
| `label` | Plain text description of this license. |  |
| `license_hash` | Unique identifier for the license. The REST API uses this identifier to access this license. |  |
| `max_violations` | The maximum number of violations allowed during the specified window period ( window_period . Searching is disabled when max_violations is exceeded. |  |
| `quota` | Daily indexing quota, in bytes, for this license. |  |
| `sourcetypes` | The list of allowed sourcetypes for this list. You cannot use this license to index sourcetypes that are not present in this list. An empty list indicates all sourcetypes are allowed. |  |
| `stack_id` | The ID of the license stack to which this license belongs. |  |
| `status` | The status of a license can be either VALID or EXPIRED. |  |
| `type` | Provides any additional information about the type of this license. |  |
| `window_period` | The rolling period, in days, in which violations are aggregated. |  |

#### POST

Add a license entitlement to the current instance.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `payload` | string |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `creation_time` | The creation time of this license, in Coordinated Universal Time (UTC). |  |
| `expiration_time` | The time this license expires, in Coordinated Universal Time (UTC). |  |
| `features` | The list of features and components enabled by this license. |  |
| `group_id` | The ID of the group to which this license belongs. |  |
| `label` | Plain text description of this license. |  |
| `license_hash` | Unique identifier for the license. The REST API uses this identifier to access this license. |  |
| `max_violations` | The maximum number of violations allowed during the specified window period ( window_period . Searching is disabled when max_violations is exceeded. |  |
| `payload` | String representation of license, encoded in xml. |  |
| `quota` | Daily indexing quota, in bytes, for this license. |  |
| `sourcetypes` | The list of allowed sourcetypes for this list. You cannot use this license to index sourcetypes that are not present in this list. An empty list indicates all sourcetypes are allowed. |  |
| `stack_id` | The ID of the license stack to which this license belongs. |  |
| `status` | The status of a license can be either VALID or EXPIRED. |  |
| `type` | Provides any additional information about the type of this license. |  |
| `window_period` | The rolling period, in days, in which violations are aggregated. |  |

### `/services/licenser/licenses/{name}`

Access or delete the {name} license.

#### DELETE

Delete the license with a hash corresponding to {name}

#### GET

List license details.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `creation_time` | The creation time of this license, in Coordinated Universal Time (UTC). |  |
| `expiration_time` | The time this license expires, in Coordinated Universal Time (UTC). |  |
| `features` | The list of features and components enabled by this license. |  |
| `group_id` | The ID of the group to which this license belongs. |  |
| `label` | Plain text description of this license. |  |
| `license_hash` | Unique identifier for the license. The REST API uses this identifier to access this license. |  |
| `max_violations` | The maximum number of violations allowed during the specified window period ( window_period . Searching is disabled when max_violations is exceeded. |  |
| `quota` | Daily indexing quota, in bytes, for this license. |  |
| `sourcetypes` | The list of allowed sourcetypes for this list. You cannot use this license to index sourcetypes that are not present in this list. An empty list indicates all sourcetypes are allowed. |  |
| `stack_id` | The ID of the license stack to which this license belongs. |  |
| `status` | The status of a license can be either VALID or EXPIRED. |  |
| `type` | Provides any additional information about the type of this license. |  |
| `window_period` | The rolling period, in days, in which violations are aggregated. |  |

### `/services/licenser/localpeer`

Get license state information for the Splunk instance.

#### GET

Get license state information for the Splunk instance.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `add_ons` | List of add-ons resident on this instance, and add-on parameters. |  |
| `connection_timeout` | Instance connection timeout (seconds). |  |
| `features` | List of key-value pairs of the following features and their ENABLED/DISABLED status: Acceleration AdvancedSearchCommands AdvancedXML Alerting AllowDuplicateKeys Auth CanBeRemoteManager CustomRoles DeployClient DeployServer DistSearch FwdData GuestPass KVStore LDAPAuth LocalSearch MultisiteClustering NontableLookups RcvData RcvSearch ResetWarnings">DISABLED_DUE_TO_LICENSE</s:key> RollingWindowAlerts ScheduledAlerts ScheduledReports ScheduledSearch SearchheadPooling SigningProcessor SplunkWeb SyslogOutputProcessor UnisiteClustering |  |
| `last_manager_contact_attempt_time` | Time of last attempt to contact manager. |  |
| `last_manager_contact_success_time` | Time of last successful attempt to contact manager. |  |
| `last_trackerdb_service_time` | Time of last license servicing, tracking persistent store. |  |
| `license_keys` | List of license keys this instance is using. |  |
| `manager_guid` | Manager license GUID. |  |
| `manager_uri` | Manager license URI. |  |
| `receive_timeout` | Network layer receive timeout for communication to manager (seconds). |  |
| `send_timeout` | Network layer send timeout for communication to manager (seconds). |  |
| `peer_id` | This instance GUID. |  |
| `peer_label` | This instance server name. |  |
| `squash_threshold` | Threshold that enables source/host squashing of rows of usage data sent to manager periodically. |  |

### `/services/licenser/messages`

Access licenser messages.

#### GET

List all messages/alerts/persisted warnings for this node.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `category` | Indicates the category for the licenser message. The category can be any of the following: license_window pool_over_quota stack_over_quota orphan_peer pool_warning_count pool_violated_peer_count |  |
| `create_time` | The time the message was created in the system, expressed in Coordinated Universal time (UTC). |  |
| `pool_id` | The ID of the licesne pool to which the message applies. If a pool ID is not present, then the message in not applicable to a specific license pool. |  |
| `severity` | Indicates the severity of the message. The severity can be any of the following: INFO WARN ERROR |  |
| `peer_id` | The ID of the license peer to which the message applies. |  |
| `stack_id` | The ID of the license stack to which the message applies. If a stack ID is not present, thae the message is not applicable to a specific license stack. |  |

### `/services/licenser/messages/{name}`

Get the message with message ID {name} .

#### GET

List specific message whose msgId corresponds to {name} component.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `category` | Indicates the category for the licenser message. The category can be any of the following: license_window pool_over_quota stack_over_quota orphan_peer pool_warning_count pool_violated_peer_count |  |
| `create_time` | The time the message was created in the system, expressed in Coordinated Universal time (UTC). |  |
| `pool_id` | The ID of the licesne pool to which the message applies. If a pool ID is not present, then the message in not applicable to a specific license pool. |  |
| `severity` | Indicates the severity of the message. The severity can be any of the following: INFO WARN ERROR |  |
| `peer_id` | The ID of the license peer to which the message applies. |  |
| `stack_id` | The ID of the license stack to which the message applies. If a stack ID is not present, thae the message is not applicable to a specific license stack. |  |

### `/services/licenser/pools`

#### GET

Enumerate all pools.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `quota` | The byte quota of this license pool. MAX: maximum amount allowed by the license. You can only have one pool with MAX size in a stack. Number: the number of bytes allowed by this license. |  |
| `peers` | peerids that are members of this pool. Returned as a list in Atom format. See example below. |  |
| `peers_usage_bytes` | Usage, in bytes, of peers to this license. |  |
| `stack_id` | Stack ID of the stack corresponding to this pool. |  |
| `used_bytes` | Usage, in bytes, for this license pool. |  |

#### POST

Create a license pool.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `quota` | String |  |
| `peers` | String |  |
| `stack_id` | Enum |  |

### `/services/licenser/pools/{name}`

#### DELETE

Delete the specified pool.

#### GET

Lists details of the pool specified by {name}.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `quota` | The byte quota of this license pool. MAX: maximum amount allowed by the license. You can only have one pool with MAX size in a stack. Number: the number of bytes allowed by this license. |  |
| `peers` | peerids that are members of this pool. Returned as a list in Atom format. See example below. |  |
| `peers_usage_bytes` | Usage, in bytes, of peers to this license. |  |
| `stack_id` | Stack ID of the stack corresponding to this pool. |  |
| `used_bytes` | Usage, in bytes, for this license pool. |  |

#### POST

Edit properties of the pool specified by {name}.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `append_peers` | Boolean |  |
| `quota` | String |  |
| `peers` | String |  |

### `/services/licenser/peers`

#### GET

List all peers registered to this license manager.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `label` | Plain text name for the license peer. |  |
| `pool_ids` | License pools for which this license peer is a member. |  |
| `stack_ids` | License stacks for which this license peer is a member. |  |
| `warning_count` | Number of license warnings issued for this license peer. |  |

### `/services/licenser/peers/{name}`

#### GET

List attributes of the peer instance specified by {name}.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `label` | Plain text name for the license peer. |  |
| `pool_ids` | License pools for which this license peer is a member. |  |
| `stack_ids` | License stacks for which this license peer is a member. |  |
| `warning_count` | Number of license warnings issued for this license peer. |  |

### `/services/licenser/stacks`

#### GET

Enumerate all license stacks.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `label` | The name of this license stack. |  |
| `quota` | The byte quota of this license stack. This value is the sum of the byte quota for all the licenses in the license stack. |  |
| `type` | Any additional information about the type of this license stack. |  |

### `/services/licenser/stacks/{name}`

#### GET

Retrieve details of a specific license stack.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `label` | The name of this license stack. |  |
| `quota` | The byte quota of this license stack. This value is the sum of the byte quota for all the licenses in the license stack. |  |
| `type` | Any additional information about the type of this license stack. |  |

### `/services/licenser/usage`

#### GET

Enumerate license usage information from the last minute, since midnight server time.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `quota` | The byte quota of this license stack. This value is the sum of the byte quota for all the licenses in the active license group. |  |
| `peers_usage_bytes` | Peer usage bytes across all pools that are within the active license group. |  |

---

## Metrics Catalog

### `/services/catalog/metricstore/metrics`

Use this endpoint to list metric names.

#### GET

Returns metric names.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest` | String | Optional. A time string that specifies the earliest time for this search. Can be a relative or absolute time. The default value is -1d . |
| `filter` | String | Optional. A URL-encoded set of one or more key-value pairs, where keys correspond to metric fields such as index or dimension. For example, to specify a dimension named app , use filter=app . To specify two index names and values such as index=index1 and index=index2 , use index%3dindex1%26index%3dindex2 . |
| `latest` | String | Optional. A time string that specifies the latest time for this search. Can be a relative or absolute time. The default value is now . |
| `list_indexes` | Boolean | Optional. When set to true , the endpoint returns the index or indexes associated with each metric. The default value is false . |

### `/services/catalog/metricstore/dimensions`

Use this endpoint to list dimension names.

#### GET

Returns dimension names for a given metric.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest` | String | Optional. A time string that specifies the earliest time for this search. Can be a relative or absolute time. The default value is -1d . |
| `filter` | String | Optional. A URL-encoded set of one or more key-value pairs, where keys correspond to metric fields such as index or dimension. For example, to specify a dimension named os , use filter=os . To specify two index names and values such as index=index1 and index=index2 , use index%3dindex1%26index%3dindex2 . |
| `latest` | String | Optional. A time string that specifies the latest time for this search. Can be a relative or absolute time. The default value is now . |
| `metric_name` | String | Required. The name of a metric. |

### `/services/catalog/metricstore/dimensions/{dimension-name}/values`

Use this endpoint to list values for a given {dimension-name} .

#### GET

Returns values of a {dimension-name} for a given metric.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest` | String | Optional. A time string that specifies the earliest time for this search. Can be a relative or absolute time. The default value is -1d . |
| `filter` | String | Optional. A URL-encoded set of one or more key-value pairs, where keys correspond to metric fields such as index or dimension. For example, to specify a dimension named os , use filter=os . To specify two index names and values such as index=index1 and index=index2 , use index%3dindex1%26index%3dindex2 . |
| `latest` | String | Optional. A time string that specifies the latest time for this search. Can be a relative or absolute time. The default value is now . |
| `metric_name` | String | Required. The name of a metric. |

### `/services/catalog/metricstore/rollup`

Use this endpoint to retrieve lists of metric indexes and their rollup summaries and to create new rollup policies for a given metric index.

#### GET

Returns rollup summaries and the metric indexes with which they are associated.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `summaries` | A comma-separated list of the rollup summaries associated with the source metric index. Each summary configuration consists of a span and a rollup_index . The span is the interval by which the search head generates the aggregated rollup metric data points that make up the summary. The rollup_index is the target index for the rollup summary. The endpoint uses the following format when it lists summaries: <span_1>|<rollup_index_1>,<span_2>|<rollup_index_2>...<span_n>|<rollup_index_n> |  |

#### POST

Creates rollup policies for a specified metric index.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `summaries` | String | Required. Specify one or more rollup summaries, separated by commas. A rollup summary is a combination of a rollup period and a rollup metric index. The rollup period is the span. This time range string is the interval on which the search head generates the aggregated rollup metric data points that make up the summary. The rollup span is limited to the following values for minutes, hours, and days. Other time units are not allowed. m (minutes): 1,2,3,4,5,6,10,12,20,30,60 h (hours): 1,2,3,4,6,8,12,24 d (days): 1 The rollup index is the target index for the rollup summary. The endpoint uses the following format when it lists summaries: <span_1>\|<rollup_index_1>,<span_2>\|<rollup_index_2>...<span_n>\|<rollup_index_n> . Defaults to 1hr\|<name> . |
| `default_agg` | String | Optional . A list of aggregation functions, separated by # characters. Provides the set of aggregation functions that the rollup search uses when it aggregates the metric data points in the source metric index for a rollup summary. The defaultAggregation can be overruled for specific metrics by the aggregation.<metric_name> setting. This setting supports the following functions: avg , count , max , median , min , perc<int> , and sum . Defaults to avg . |
| `metric_list` | String | Optional . A comma-separated list of metric names. All of the listed metrics must appear in the source metric index identified by the name parameter. This list works in conjunction with the metric_list_type parameter to create a filter at the search head that allows certain metrics to be rolled up but not others. Defaults to empty string. |
| `metric_list_type` | [included | excluded] | Optional . Works in conjunction with the metric_list parameter to create a filter at the search head that allows certain metrics to be rolled up to the rollup summaries but not others. Defaults to excluded . Use included to indicate that the search head should filter out all available metrics from the set of metrics being rolled up to the rollup summaries, except for the metrics listed in metric_list parameter. Use excluded to indicate that the search head should roll up all available metrics to the rollup summaries except the metrics listed in metric_list parameter. |
| `dimension_list` | String | Optional . A comma-separated list of dimensions that appear in the source metric index identified by the name parameter. This list corresponds to the dimension_list_type parameter, which determines whether this set of dimensions is included or excluded from the aggregated rollup metrics that the search head generates for the rollup summary. Defaults to empty string. |
| `dimension_list_type` | [included | excluded] | Optional . Identifies whether the dimensions specified in the dimension_list parameter are included or excluded from the rollup metrics that are generated by the rollup policies for the rollup summaries. Defaults to excluded . Use included to indicate that the rollup metrics produced by the rollup policy filter out all dimensions except the dimensions listed in the dimension_list parameter. Use excluded to indicate that the rollup metrics produced by the rollup policy include all available dimensions except the dimensions in the dimension_list parameter. |
| `metric_overrides` | String | Optional . Provides a comma-separated list of exclusion rules for a set of rollup policies. Use this setting to override the default aggregation for one or more metrics. Each metric override pairs a metric name with one or more aggregation functions separated by # characters. Each metric override uses the following syntax: <metric_name>\|<aggregation_function_1>#<aggregation_function_2>#…<aggregation_function_n . Only the following aggregation functions are allowed: avg , count , max , median , min , perc<int> , and sum . Defaults to empty string. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `aggregation.<metric_name>` | Overrides the default aggregation or set of aggregations for the specified metric_name and gives it a different aggregation or set of aggregations instead. Defined by the metric_overrides argument. |  |
| `defaultAggregation` | The default aggregation methods for the rollup policy, separated by # characters. |  |
| `dimensionList` | Comma-separated list of dimensions to be included or excluded from the aggregations, depending on the value of dimensionListType . |  |
| `dimensionListType` | Indicates whether the dimensionList should be included or excluded from the rollup policy. |  |
| `metricList` | Comma-separated list of metrics to be included or excluded from the set of metrics rolled up to the summaries, depending on the value of dimensionListType |  |
| `metricListType` | Indicates whether the metricList should be included or excluded from the rollup policy. |  |
| `rollup.<summary number>.rollupIndex` | The target rollup index for a specific summary. Summaries are identified by the <summary number> . |  |
| `rollup.<summary number>.span` | The rollup span for a specific summary. Summaries are identified by the <summary number> . |  |

### `/services/catalog/metricstore/rollup/{index}`

Use this endpoint to:

#### GET

Returns a list of the rollup summaries associated with a specific source {index} .

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `summaries` | A comma-separated list of the rollup summaries associated with the source metric {index} . Each summary configuration consists of a span and a rollup_index . The span is the interval by which the search head generates the aggregated rollup metric data points that make up the summary. The rollup_index is the target index for the rollup summary. The endpoint uses the following format when it lists summaries: <span_1>|<rollup_index_1>,<span_2>|<rollup_index_2>...<span_n>|<rollup_index_n> |  |

#### POST

Updates a rollup policy for a specific source {index} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `default_agg` | String | Optional . A list of aggregation functions, separated by # characters. Provides the set of aggregation functions that the rollup search uses when it aggregates the metric data points in the source metric index for a rollup summary. The defaultAggregation can be overruled for specific metrics by the aggregation.<metric_name> setting. This setting supports the following functions: avg , count , max , median , min , perc<int> , and sum . Defaults to avg . |
| `metric_list` | String | Optional . A comma-separated list of metric names. All of the listed metrics must appear in the source metric index identified by the name parameter. This list works in conjunction with the metric_list_type parameter to create a filter at the search head that allows certain metrics to be rolled up but not others. Defaults to empty string. |
| `metric_list_type` | [included | excluded] | Optional . Works in conjunction with the metric_list parameter to create a filter at the search head that allows certain metrics to be rolled up to the rollup summaries but not others. Defaults to excluded . Use included to indicate that the search head should filter out all available metrics from the set of metrics being rolled up to the rollup summaries, except for the metrics listed in metric_list parameter. Use excluded to indicate that the search head should roll up all available metrics to the rollup summaries except the metrics listed in metric_list parameter. |
| `dimension_list` | string | Optional. A comma-separated list of dimensions that appear in the source index. This list corresponds to the dimension_list_type parameter, which determines whether this set of dimensions is included or excluded from the aggregated rollup metrics that the search head generates for the rollup summary. Defaults to empty string. |
| `dimension_list_type` | [included | excluded] | Optional . Identifies whether the dimensions specified in the dimension_list parameter are included or excluded from the rollup metrics that are generated by the rollup policies for the rollup summaries. Use included to indicate that the rollup metrics produced by the rollup policy filter out all dimensions except the dimensions listed in the dimension_list parameter. Use excluded to indicate that the rollup metrics produced by the rollup policy include all available dimensions except the dimensions in the dimension_list parameter. |
| `metric_overrides` | String | Optional . Provides a comma-separated list of exclusion rules for a set of rollup policies. Use this setting to override the default aggregation for one or more metrics. Each metric override pairs a metric name with one or more aggregation functions separated by # characters. Each metric override uses the following syntax: <metric_name>\|<aggregation_function_1>#<aggregation_function_2>#…<aggregation_function_n . Only the following aggregation functions are allowed: avg , count , max , median , min , perc<int> , and sum . Defaults to empty string. |
| `summaries` | String | Optional. Specify one or more rollup summaries, separated by commas. A rollup summary is a combination of a rollup period and a rollup metric index. The rollup period is the span. This time range string is the interval on which the search head generates the aggregated rollup metric data points that make up the summary. The rollup span is limited to the following values for minutes, hours, and days. Other time units are not allowed. m (minutes): 1,2,3,4,5,6,10,12,20,30,60 h (hours): 1,2,3,4,6,8,12,24 d (days): 1 The rollup index is the target index for the rollup summary. The endpoint uses the following format when it lists summaries: <span_1>\|<rollup_index_1>,<span_2>\|<rollup_index_2>...<span_n>\|<rollup_index_n> . |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `aggregation.<metric_name>` | Overrides the default aggregation or set of aggregations for the specified metric_name and gives it a different aggregation or set of aggregations instead. Defined by the metric_overrides argument. |  |
| `defaultAggregation` | The default aggregation methods for the rollup policy, separated by # characters. |  |
| `dimensionList` | Comma-separated list of dimensions to be included or excluded from the aggregations, depending on the value of dimensionListType . |  |
| `dimensionListType` | Indicates whether the dimensionList should be included or excluded from the rollup policy. |  |
| `metricList` | Comma-separated list of metrics to be included or excluded from the set of metrics rolled up to the summaries, depending on the value of dimensionListType |  |
| `metricListType` | Indicates whether the metricList should be included or excluded from the rollup policy. |  |
| `rollup.<summary number>.rollupIndex` | The target rollup index for a specific summary. Summaries are identified by the <summary number> . |  |
| `rollup.<summary number>.span` | The rollup span for a specific summary. Summaries are identified by the <summary number> . |  |

#### DELETE

Deletes a rollup policy for a specific source {index} .

---

## Output

### `/services/data/outputs/tcp/default`

Access to global tcpout properties.

#### GET

Returns the current tcpout properties.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `autoLB` | Specifies whether Auto Load balance method is used. |  |
| `defaultGroup` | Target group names. The forwarder sends all data to the specified groups. Starting with 4.2, this attribute is no longer required. |  |
| `disabled` | Indicates if tcpout settings are disabled. |  |
| `forwardedindex.0.whitelist` | Specifies 0th whitelist filter. forwardedindex.<n>.whitelist decides which events get forwarded based on the indexes they belong to. |  |
| `forwardedindex.1.blacklist` | Specifies 1st blacklist filter. forwardedindex.<n>.blacklist specifies index for which events are not forwarded. |  |
| `forwardedindex.2.whitelist` | Specifies 2nd whitelist filter. forwardedindex.<n>.whitelist decides which events get forwarded based on the indexes they belong to. |  |
| `forwardedindex.filter.disable` | Specifies whether filtering of forwarded data based on index is diasbled. |  |
| `indexAndForward` | Specifies whether to index all data locally, in addition to forwarding it. Defaults to false. This is known as an "index-and-forward" configuration. This attribute is only available for heavy forwarders. It is available only at the top level [tcpout] stanza in outputs.conf. It cannot be overridden in a target group. |  |
| `maxQueueSize` | Sets the maximum size of the forwarder output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true). See the parmeter description for the POST operation for more information. |  |

#### POST

Configure global tcpout properties.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `defaultGroup` | String |  |
| `disabled` | Boolean |  |
| `dropEventsOnQueueFull` | Number |  |
| `heartbeatFrequency` | Number |  |
| `indexAndForward` | Boolean |  |
| `maxQueueSize` | Number |  |
| `name required` | String |  |
| `sendCookedData` | Boolean |  |

### `/services/data/outputs/tcp/default/{name}`

Manage forwarder settings.

#### DELETE

Disable the default forwarding settings.

#### GET

Retrieve the named configuration.

#### POST

Configure global forwarding properties.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `defaultGroup` | String |  |
| `disabled` | Boolean |  |
| `dropEventsOnQueueFull` | Number |  |
| `heartbeatFrequency` | Number |  |
| `indexAndForward` | Boolean |  |
| `maxQueueSize` | Number |  |
| `sendCookedData` | Boolean |  |

### `/services/data/outputs/tcp/group`

Access to the configuration of a group of one or more data forwarding destinations.

#### GET

Get configuration information about target groups.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if tcpout is disabled for this group. |  |
| `method` | Specifies the type of output processor. Valid values: (tcpout | syslog) |  |
| `servers` | Servers included in this group. |  |

#### POST

Configure a group of one or more data forwarding destinations.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `compressed` | Boolean | false |
| `disabled` | Boolean | false |
| `dropEventsOnQueueFull` | Number | -1 |
| `heartbeatFrequency` | Number | 30 |
| `maxQueueSize` | Number | auto |
| `method` | Enum |  |
| `name required` | String |  |
| `sendCookedData` | Boolean | true |
| `servers required` | String |  |
| `token` | GUID |  |

### `/services/data/outputs/tcp/group/{name}`

Manage the {name} target group.

#### DELETE

Deletes the target group specified by {name}.

#### GET

Get configuration information about the target group specified by {name}.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `autoLB` | Indicates if the forwarder performs automatic load balancing. See the description for the autoLB parameter in POST data/outputs/tcp/group for details. |  |
| `disabled` | Indicates if tcpout is disabled for this group. |  |
| `method` | Specifies the type of output processor. Valid values: (tcpout | syslog) |  |
| `servers` | Servers included in this group. |  |

#### POST

Update the configuration of the target group.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `compressed` | Boolean | false |
| `disabled` | Boolean | false |
| `dropEventsOnQueueFull` | Number | -1 |
| `heartbeatFrequency` | Number | 30 |
| `maxQueueSize` | Number | auto |
| `method` | Enum |  |
| `sendCookedData` | Boolean | true |
| `servers required` | String |  |
| `token` | GUID |  |

### `/services/data/outputs/tcp/server`

Access data forwarding configurations.

#### GET

List existing forwarded servers.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `destHost` | DNS name of the destination server. |  |
| `destIp` | IP address of the destination server. |  |
| `destPort` | Port on which the destination server is listening. |  |
| `disabled` | Indicates if the outputs to the destination server is disabled. |  |
| `method` | The data distribution method used when two or more servers exist in the same forwarder group. Valid values: (clone | balance | autobalance) |  |
| `sourcePort` | Port on destination server where data is forwarded. |  |
| `status` | Indicates the status of the connection to the server. |  |

#### POST

Creates a new forwarder output.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `method` | Enum |  |
| `name required` | String |  |
| `sslAltNameToCheck` | String |  |
| `sslCertPath` | String |  |
| `sslCipher` | String |  |
| `sslCommonNameToCheck` | String |  |
| `sslPassword` | String |  |
| `sslRootCAPath` | String |  |
| `sslVerifyServerCert` | Boolean |  |

### `/services/data/outputs/tcp/server/{name}`

Manage the {name} forwarder.

#### DELETE

Deletes the configuration for the {name} forwarded server.

#### GET

Lists information for the {name} forwarded server.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Indicates if the outputs to the destination server is disabled. |  |
| `method` | The data distribution method used when two or more servers exist in the same forwarder group. Valid values: (clone | balance | autobalance) |  |

#### POST

Configures the forwarded server specified by {name} .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `method` | Enum |  |
| `sslAltNameToCheck` | String |  |
| `sslCertPath` | String |  |
| `sslCipher` | String |  |
| `sslCommonNameToCheck` | String |  |
| `sslPassword` | String |  |
| `sslRootCAPath` | String |  |
| `sslVerifyServerCert` | Boolean |  |

### `/services/data/outputs/tcp/server/{name}/allconnections`

#### GET

List current connections to the {name} forwarded server.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `destHost` | DNS name of the destination server. |  |
| `destIp` | IP address of the destination server. |  |
| `destPort` | Port on which the destination server is listening. |  |
| `sourcePort` | Port on destination server where data is forwarded. |  |
| `status` | Indicates the status of the connection to the server. |  |

### `/services/data/outputs/tcp/syslog`

Access the configuration of a forwarded server configured to provide data in standard syslog format.

#### GET

Provides access to syslog data forwarding configurations.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether global syslog configuration is disabled. |  |
| `server` | Specifies server:port where data is forwarded. |  |
| `type` | Specifies whether tcp or udp is used to forward data. If unspecified, udp is used. Valid values : (tcp | udp). |  |

#### POST

Configures a forwarder to send data in standard syslog format

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `name required` | String |  |
| `priority` | Number |  |
| `server` | String |  |
| `syslogSourceType` | String |  |
| `timestampformat` | String |  |
| `type` | String |  |

### `/services/data/outputs/tcp/syslog/{name}`

Manage configuration for the {name} forwarder.

#### DELETE

Deletes the configuration for the {name} forwarder.

#### GET

Returns configuration information for the {name} forwarder.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Specifies whether global syslog configuration is disabled. |  |
| `server` | Specifies server:port where data is forwarded. |  |
| `type` | Specifies whether tcp or udp is used to forward data. If unspecified, udp is used. Valid values : (tcp | udp). |  |

#### POST

Updates the configuration of the {name} forwarder.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |
| `priority` | Number |  |
| `server` | String |  |
| `syslogSourceType` | String |  |
| `timestampformat` | String |  |
| `type` | String |  |

---

## Search

### `/services/alerts/alert_actions`

Access alert actions.

#### GET

Access a list of alert actions.

### `/services/alerts/fired_alerts`

Access fired alerts.

#### GET

Access a fired alerts summary.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `triggered_alert_count` | Trigger count for this alert. |  |

### `/services/alerts/fired_alerts/{name}`

Access or delete the {name} triggered alert.

#### GET

List unexpired triggered instances of this alert.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `actions` | Any additional alert actions triggered by this alert. |  |
| `alert_type` | Indicates if the alert was historical or real-time. |  |
| `digest_mode` |  |  |
| `expiration_time_rendered` |  |  |
| `savedsearch_name` | Name of the saved search that triggered the alert. |  |
| `severity` | Indicates the severity level of an alert. Severity level ranges from Info, Low, Medium, High, and Critical. Default is Medium. Severity levels are informational in purpose and have no additional functionality. |  |
| `sid` | The search ID of the search that triggered the alert. |  |
| `trigger_time` | The time the alert was triggered. |  |
| `trigger_time_rendered` |  |  |
| `triggered_alerts` |  |  |

#### DELETE

Delete the record of this triggered alert.

### `/services/alerts/metric_alerts`

This endpoint lets you access and create streaming metric alerts.

#### GET

Access streaming metric alert configurations.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular metric alert. Valid values for action_name are: email logevent rss script webhook For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the metric alert configuration to which it is applied. |  |
| `condition` | Specifies an alert condition for one or more metric_name and aggregation pairs. The alert conditions can include multiple Boolean operators, eval functions, and metric aggregations. The Splunk software applies this evaluation to the results of the alert search on a regular interval. When the alert condition evaluates to 'true', the alert is triggered. Must reference at least one '<mstats_aggregation>(<metric_name>)' clause in single quotes. The condition can also reference dimensions specified in the groupby setting. |  |
| `filter` | Provides one or more Boolean expressions like <dimension_field>=<value> to define the search result dataset to monitor for the alert condition. Does not support subsearches, macros, tags, event types, or time modifiers such as 'earliest' or 'latest'. Combines with the metric_indexes setting to provide the complete search filter for the alert. |  |
| `groupby` | The list of dimension fields, delimited by comma, for the group-by clause of the alert search. This leads to multiple aggregation values, one per group, instead of one single value. |  |
| `label.<label-name>` | Arbitrary key-value pairs for labeling this alert. |  |
| `metric_indexes` | Specifies one or more metric indexes, delimited by comma. Combines with the filter setting to provide the complete search filter for the alert. |  |
| `splunk_ui.<label-name>` | An arbitrary key-value pair that is automatically generated by the Splunk software for its internal use only. Do not change it. |  |
| `trigger.expires` | Sets the period of time that a triggered alert record displays on the Triggered Alerts page. |  |
| `trigger.max_tracked` | Specifies the maximum number of instances of this alert that can display in the Triggered Alerts page. When this threshold is passed, the Splunk software removes the earliest instances from the Triggered Alerts page to honor this maximum number. |  |
| `trigger.suppress` | Specifies the suppression period to silence alert actions and notifications. The suppression period goes into effect when an alert is triggered. During this period, if the alert is triggered again, its actions do not happen and its notifications do not go out. When the period elapses, a subsequent triggering of the alert causes alert actions and notifications to take place as usual, and the alert is suppressed again. |  |

#### POST

Create a streaming metric alert.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.<action-name>` | Boolean | Indicates whether the <action_name> is enabled or disabled for a particular metric alert. Valid values for action_name are: email logevent rss script webhook For more information about the alert action options see the alert_actions.conf file. |
| `action.<action-name>.<parameter>` | String | Override the global setting defined for an <action-name> in the alert_actions.conf file with a new setting that is valid only for the metric alert configuration to which it is applied. |
| `condition required` | Boolean eval expression | Specifies an alert condition for one or more metric_name and aggregation pairs. You can set alert conditions that include multiple Boolean operators, eval functions, and metric aggregations. The Splunk software applies this evaluation to the results of the alert search on a regular interval. When the alert condition evaluates to 'true', the alert is triggered. Must reference at least one '<mstats_aggregation>(<metric_name>)' clause in single quotes. The condition can also reference dimensions specified in the groupby setting. |
| `filter` | String | Specify one or more Boolean expressions like <dimension_field>=<value> to define the search result dataset to monitor for an alert condition. Link multiple Boolean expressions with the AND operator. The filter does not support subsearches, macros, tags, event types, or time modifiers such as 'earliest' or 'latest'. This setting combines with the metric_indexes setting to provide the complete search filter for the alert. |
| `groupby` | String | Provide a list of dimension fields, delimited by comma, for the group-by clause of the alert search. This results in multiple aggregation values, one per group, instead of one aggregation value. |
| `label.<label-name>` | String | Provide an arbitrary key-value pair to label or tag this alert. This key-value pair is not used by the Splunk alerting framework. You can design applications that use the alert label when they call the `alerts/metric_alerts` endpoint. |
| `metric_indexes required` | String | Specify one or more metric indexes, delimited by comma. Combines with the filter setting to define the search result dataset that the alert monitors for the alert condition. |
| `name required` | String | Specify the name of the streaming metric alert. |
| `trigger.expires` | String | Set the period of time that a triggered alert record displays on the Triggered Alerts page. Use <positive integer><time-unit> , where <time_unit> can be 'm' for minutes, 'h' for hours, and 'd' for days. Set to 0 to make triggered alerts expire immediately so they do not appear on the Triggered Alerts page at all. Default is 24h. |
| `trigger.max_tracked` | Number | Specify the maximum number of instances of this alert that can display in the triggered alerts dashboard. When this threshold is passed, the Splunk software removes the earliest jinstances from the dashboard to honor this maximum number. Set to 0 to remove the cap. Defaults to 20. |
| `trigger.suppress` | String | Define the suppression period to silence alert actions and notifications. The suppression period goes into effect when an alert is triggered. During this period, if the alert is triggered again, its actions do not happen and its notifications do not go out. When the period elapses, a subsequent triggering of the alert causes alert actions and notifications to take place as usual, and the alert is suppressed again. Use <number> m to specify a timespan in minutes. Default is 0m. |

### `/services/alerts/metric_alerts/{alert_name}`

This endpoint lets you create, update, delete, enable, and disable streaming metric alerts.

#### GET

Access the named streaming metric alert.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular metric alert. Valid values for action_name are: email logevent rss script webhook For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the metric alert configuration to which it is applied. |  |
| `condition` | Specifies an alert condition for one or more metric_name and aggregation pairs. The alert conditions can include multiple Boolean operators, eval functions, and metric aggregations. The Splunk software applies this evaluation to the results of the alert search on a regular interval. When the alert condition evaluates to 'true', the alert is triggered. Must reference at least one '<mstats_aggregation>(<metric_name>)' clause in single quotes. The condition can also reference dimensions specified in the groupby setting. |  |
| `groupby` | The list of dimension fields, delimited by comma, for the group-by clause of the alert search. This leads to multiple aggregation values, one per group, instead of one single value. |  |
| `filter` | Provides one or more Boolean expressions like <dimension_field>=<value> to define the search result dataset to monitor for the alert condition. Does not support subsearches, macros, tags, event types, or time modifiers such as 'earliest' or 'latest'. Combines with the metric_indexes setting to provide the complete search filter for the alert. |  |
| `label.<label-name>` | Arbitrary key-value pairs for labeling this alert. |  |
| `metric_indexes` | Specifies one or more metric indexes, delimited by comma. Combines with the filter setting to provide the complete search filter for the alert. |  |
| `splunk_ui.<label-name>` | An arbitrary key-value pair that is automatically generated by the Splunk software for its internal use only. Do not change it. |  |
| `trigger.expires` | Sets the period of time that a triggered alert record displays on the Triggered Alerts page. |  |
| `trigger.max_tracked` | Specifies the maximum number of instances of this alert that can display in the Triggered Alerts page. When this threshold is passed, the Splunk software removes the earliest instances from the Triggered Alerts page to honor this maximum number. |  |
| `trigger.suppress` | Specifies the suppression period to silence alert actions and notifications. The suppression period goes into effect when an alert is triggered. During this period, if the alert is triggered again, its actions do not happen and its notifications do not go out. When the period elapses, a subsequent triggering of the alert causes alert actions and notifications to take place as usual, and the alert is suppressed again. |  |

#### POST

Update the named streaming metric alert.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.<action-name>` | Boolean | Indicates whether the <action_name> is enabled or disabled for a particular metric alert. Valid values for <action_name> are: email logevent rss script webhook For more information about the alert action options see the alert_actions.conf file. |
| `action.<action-name>.<parameter>` | String | Override the global setting defined for an <action-name> in the alert_actions.conf file with a new setting that is valid only for the metric alert configuration to which it is applied. |
| `condition required` | Boolean eval expression | Specifies an alert condition for one or more metric_name and aggregation pairs. You can set alert conditions that include multiple Boolean operators, eval functions, and metric aggregations. The Splunk software applies this evaluation to the results of the alert search on a regular interval. When the alert condition evaluates to 'true', the alert is triggered. Must reference at least one '<mstats_aggregation>(<metric_name>)' clause in single quotes. The condition can also reference dimensions specified in the groupby setting. |
| `groupby` | String | Provide a list of dimension fields, delimited by comma, for the group-by clause of the alert search. This results in multiple aggregation values, one per group, instead of one aggregation value. |
| `filter` | String | Specify one or more Boolean expressions like <dimension_field>=<value> to define the search result dataset to monitor for an alert condition. Link multiple Boolean expressions with the 'AND' operator. The filter does not support subsearches, macros, tags, event types, or time modifiers such as 'earliest' or 'latest'. This setting combines with the metric_indexes setting to provide the complete search filter for the alert. |
| `label.<label-name>` | String | Provide an arbitrary key-value pair to label or tag this alert. This key-value pair is not used by the Splunk alerting framework. You can design applications that use the alert label when they call the `alerts/metric_alerts` endpoint. |
| `metric_indexes required` | String | Specify one or more metric indexes, delimited by comma. Combines with the filter setting to define the search result dataset that the alert monitors for the alert condition. |
| `trigger.expires` | String | Set the period of time that a triggered alert record displays on the Triggered Alerts page. Use <positive integer><time-unit> , where <time_unit> can be 'm' for minutes, 'h' for hours, and 'd' for days. Set to 0 to make triggered alerts expire immediately so they do not appear on the Triggered Alerts page at all. Default is 24h. |
| `trigger.max_tracked` | Number | Specify the maximum number of instances of this alert that can display in the triggered alerts dashboard. When this threshold is passed, the Splunk software removes the earliest instances from the dashboard to honor this maximum number. Set to 0 to remove the cap. Defaults to 20. |
| `trigger.suppress` | String | Define the suppression period to silence alert actions and notifications. The suppression period goes into effect when an alert is triggered. During this period, if the alert is triggered again, its actions do not happen and its notifications do not go out. When the period elapses, a subsequent triggering of the alert causes alert actions and notifications to take place as usual, and the alert is suppressed again. Use <number> m to specify a timespan in minutes. Default is 0m. |

#### DELETE

Deletes the named metric alert.

### `/services/data/commands`

Access Python search commands.

#### GET

Access Python search commands.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `changes_colorder` | Indicates whether the script output should be used to change the column ordering of the fields. |  |
| `disabled` | Indicates if the command is disabled. |  |
| `enableheader` | Indicate whether or not your script is expecting header information or not. Currently, the only thing in the header information is an auth token. If set to true the command expects as input a head section + '\ ' then the csv input. Note: Should be set to true if you use splunk.Intersplunk |  |
| `filename` | Name of script file for command. <stanza-name>.pl for perl. <stanza-name>.py for python. |  |
| `generates_timeorder` | If generating = false and streaming = true, indicates if the command changes the order of events w/respect to time. |  |
| `generating` | Indicates if the command generates new events. |  |
| `maxinputs` | Maximum number of events that can be passed to the command for each invocation. This limit cannot exceed the value of maxresultrows in limits.conf. 0 indicates no limit. Defaults to 50000. |  |
| `outputheader` | If true, the output of script should be a header section + blank line + csv output. If false, script output should be pure csv only. |  |
| `passauth` | If true, passes an authentication token on the start of input. |  |
| `required_fields` | A list of fields that this command may use. Informs previous commands that they should retain/extract these fields if possible. No error is generated if a field specified is missing. Defaults to '*'. |  |
| `requires_preop` | Indicates whether the command sequence specified by the streaming_preop key is required for proper execution or is it an optimization only. Default is false (stremaing_preop not required). |  |
| `retainsevents` | Indicates whether the command retains events (the way the sort/dedup/cluster commands do) or whether the command transforms them (the way the stats command does). |  |
| `streaming` | Indicates whether the command is streamable. |  |
| `supports_getinfo` | Indicates whether the command supports dynamic probing for settings (first argument invoked == __GETINFO__ or __EXECUTE__). |  |
| `supports_rawargs` | Indicates whether the command supports raw arguments being passed to it or if it uses parsed arguments (where quotes are stripped). |  |
| `type` | Specifies the type of command. The only valid value for this attribute is python . |  |

### `/services/data/commands/{name}`

Get information about the {name} python search command.

#### GET

Access search command information.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `changes_colorder` | Indicates whether the script output should be used to change the column ordering of the fields. |  |
| `disabled` | Indicates if the command is disabled. |  |
| `enableheader` | Indicate whether or not your script is expecting header information or not. Currently, the only thing in the header information is an auth token. If set to true the command expects as input a head section + '\ ' then the csv input. Note: Should be set to true if you use splunk.Intersplunk |  |
| `filename` | Name of script file for command. <stanza-name>.pl for perl. <stanza-name>.py for python. |  |
| `generates_timeorder` | If generating = false and streaming = true, indicates if the command changes the order of events w/respect to time. |  |
| `generating` | Indicates if the command generates new events. |  |
| `maxinputs` | Maximum number of events that can be passed to the command for each invocation. This limit cannot exceed the value of maxresultrows in limits.conf. 0 indicates no limit. Defaults to 50000. |  |
| `outputheader` | If true, the output of script should be a header section + blank line + csv output. If false, script output should be pure csv only. |  |
| `passauth` | If true, passes an authentication token on the start of input. |  |
| `required_fields` | A list of fields that this command may use. Informs previous commands that they should retain/extract these fields if possible. No error is generated if a field specified is missing. Defaults to '*'. |  |
| `requires_preop` | Indicates whether the command sequence specified by the streaming_preop key is required for proper execution or is it an optimization only. Default is false (stremaing_preop not required). |  |
| `retainsevents` | Indicates whether the command retains events (the way the sort/dedup/cluster commands do) or whether the command transforms them (the way the stats command does). |  |
| `streaming` | Indicates whether the command is streamable. |  |
| `supports_getinfo` | Indicates whether the command supports dynamic probing for settings (first argument invoked == __GETINFO__ or __EXECUTE__). |  |
| `supports_rawargs` | Indicates whether the command supports raw arguments being passed to it or if it uses parsed arguments (where quotes are stripped). |  |
| `type` | Specifies the type of command. The only valid value for this attribute is python . |  |

### `/services/saved/searches`

Access and create saved searches.

#### GET

Access saved search configurations.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time` | String |  |
| `latest_time` | String |  |
| `listDefaultActionArgs` | Boolean |  |
| `add_orphan_field` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular search. For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the search configuration to which it is applied. |  |
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here that is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments. Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. Note: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be referenced externally, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost." When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the global maximum number of search results to send when email.action is enabled. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.reportServerEnabled` | Not supported. |  |
| `action.email.reportServerURL` | Not supported. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `action.populate_lookup` | The state of the populate lookup action. |  |
| `action.populate_lookup.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.populate_lookup.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.populate_lookup.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.populate_lookup.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.populate_lookup.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.populate_lookup.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p] |  |
| `action.rss` | The state of the RSS action. |  |
| `action.rss.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.rss.hostname` | Sets the hostname used in the web link (url) sent in alert actions. |  |
| `action.rss.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.rss.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m. |  |
| `action.rss.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.rss.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.script` | The state of the script action. |  |
| `action.script.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.script.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.script.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.script.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. |  |
| `action.script.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.script.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.summary_index` | Specifies whether the summary index action is enabled for this search. |  |
| `action.summary_index._type"` | Specifies the data type of the summary index where the Splunk software saves the results of the scheduled search. Can be set to event or metric . |  |
| `action.summary_index.force_realtime_schedule` | By default, realtime_schedule is false for a report configured for summary indexing. When set to 1 or true , this setting overrides realtime_schedule . Setting this setting to true can cause gaps in summary data, as a realtime_schedule search is skipped if search concurrency limits are violated. |  |
| `action.summary_index.inline` | Determines whether to execute the summary indexing action as part of the scheduled search. Note: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always). |  |
| `action.summary_index.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.summary_index.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. |  |
| `action.summary_index.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.summary_index.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p. |  |
| `alert.digest_mode` | Indicates if alert actions are applied to the entire result set or to each individual result. |  |
| `alert.expires` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.managedBy` | Specifies the feature or component that created the alert. |  |
| `alert.severity` | The alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL |  |
| `alert.suppress` | Indicates whether alert suppression is enabled for this scheduled search. |  |
| `alert.suppress.fields` | List of fields to use when suppressing per-result alerts. Must be specified if the digest mode is disabled and suppression is enabled. |  |
| `alert.suppress.group_name` | Optional setting. Used to define an alert suppression group for a set of alerts that are running over identical or very similar datasets. Alert suppression groups can help you avoid getting multiple triggered alert notifications for the same data. |  |
| `alert.suppress.period` | Specifies the suppression period. Only valid if alert.suppress is enabled. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.track` | Specifies whether to track the actions triggered by this scheduled search. auto - (Default) Determine whether to apply alert tracking to this search, based on the tracking setting of each action. Do not track scheduled searches that always trigger actions. true - Force alert tracking for this search. Default. false - Disable alert tracking for this search. |  |
| `alert_comparator` | One of the following strings: greater than less than equal to rises by drops by rises by perc drops by perc Used with alert_threshold to trigger alert actions. |  |
| `alert_condition` | A conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition , do not set counttype, relation, or quantity. |  |
| `alert_threshold` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator ) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc" or "drops by perc." |  |
| `alert_type` | What to base the alert on, overridden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |  |
| `allow_skew` | Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 . Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |  |
| `auto_summarize` | Specifies whether the search scheduler should ensure that the data for this search is automatically summarized. |  |
| `auto_summarize.command` | A search template to use to construct the auto-summarization for the search. Do not change. |  |
| `auto_summarize.cron_schedule` | Cron schedule to use to probe or generate the summaries for this search |  |
| `auto_summarize.dispatch.<arg-name>` | Dispatch options that can be overridden when running the summary search. |  |
| `auto_summarize.max_concurrent` | The maximum number of concurrent instances of this auto summarizing search that the scheduler is allowed to run. |  |
| `auto_summarize.max_disabled_buckets` | The maximum number of buckets with suspended summarization before the summarization search is completely stopped and the summarization of the search is suspended for the value specified by the auto_summarize.suspend_period setting. |  |
| `auto_summarize.max_summary_ratio` | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. |  |
| `auto_summarize.max_summary_size` | The minimum summary size, in bytes, before testing whether the summarization is helpful. |  |
| `auto_summarize.max_time` | The maximum time, in seconds, that the auto-summarization search is allowed to run. |  |
| `auto_summarize.suspend_period` | The amount of time to suspend summarization of the search if the summarization is deemed unhelpful. |  |
| `auto_summarize.timespan` | Comma-delimited list of time ranges that each summarized chunk should span. Comprises the list of available summary ranges for which summaries would be available. Does not support 1w timespans. |  |
| `auto_summarize.workload_pool` | Sets the name of the workload pool that is used by the auto-summarization of this search. |  |
| `cron_schedule` | The cron schedule to run this search. For more information, refer to the description of this parameter in the POST endpoint. |  |
| `defer_scheduled_searchable_idxc` | Specifies whether to defer a continuous saved search during a searchable rolling restart or searchable rolling upgrade of an indexer cluster. |  |
| `disabled` | Indicates whether this saved search is disabled. |  |
| `dispatch.allow_partial_results` | Specifies whether the search job can proceed to provide partial results if a search peer fails. When set to false, the search job fails if a search peer providing results for the search job fails. |  |
| `dispatch.auto_cancel` | Specifies the amount of inactive time, in seconds, after which the search job is automatically canceled. |  |
| `dispatch.auto_pause` | Specifies the amount of inactive time, in seconds, after which the search job is automatically paused. |  |
| `dispatch.buckets` | The maximum number of timeline buckets. |  |
| `dispatch.earliest_time` | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.index_earliest` | Specifies the earliest index time for this search. Can be a relative or absolute time. |  |
| `dispatch.index_latest` | Specifies the latest index time for this saved search. Can be a relative or absolute time. |  |
| `dispatch.indexedRealtime` | Specifies whether to use 'indexed-realtime' mode when doing real-time searches. |  |
| `dispatch.indexedRealtimeMinSpan` | Specifies the minimum number of seconds to wait between component index searches. |  |
| `dispatch.indexedRealtimeOffset` | Specifies the number of seconds to wait for disk flushes to finish. |  |
| `dispatch.indexedRealtimeMinSpan` | Allows for a per-job override of the [search] indexed_realtime_default_span setting in limits.conf . The default for saved searches is "unset", falling back to the limits.conf setting. |  |
| `dispatch.latest_time` | A time string that specifies the latest time for the saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.lookups` | Indicates if lookups are enabled for this search. |  |
| `dispatch.max_count` | The maximum number of results before finalizing the search. |  |
| `dispatch.max_time` | Indicates the maximum amount of time (in seconds) before finalizing the search. |  |
| `dispatch.reduce_freq` | Specifies how frequently the MapReduce reduce phase runs on accumulated map values. |  |
| `dispatch.rt_backfill` | Specifies whether to do real-time window backfilling for scheduled real-time searches. |  |
| `dispatch.rt_maximum_span` | Sets the maximum number of seconds to search data that falls behind real time. |  |
| `dispatch.sample_ratio` | The integer value used to calculate the sample ratio. The formula is 1 / <integer> . |  |
| `dispatch.spawn_process` | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Specifies whether new search process is spawned when this saved search is executed. Searches against indexes must run in a separate process. |  |
| `dispatch.time_format` | Time format string that defines the time format for specifying the earliest and latest time. |  |
| `dispatch.ttl` | Indicates the time to live (ttl), in seconds, for the artifacts of the scheduled search, if no actions are triggered. |  |
| `dispatchAs` | When the saved search is dispatched using the "saved/searches/{name}/dispatch" endpoint, this setting controls what user that search is dispatched as. Only meaningful for shared saved searches. Can be set to owner or user . |  |
| `displayview` | Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |  |
| `durable.backfill_type` | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . |  |
| `durable.lag_time` | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.max_backfill_intervals` | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.track_time_type` | Indicates that a scheduled search is durable and specifies how the search tracks events. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |  |
| `earliest_time` | For scheduled searches display all the scheduled times starting from this time (not just the next run time). |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule |  |
| `is_visible` | Indicates if this saved search appears in the visible saved search list. |  |
| `latest_time` | For scheduled searches display all the scheduled times until this time (not just the next run time). |  |
| `listDefaultActionArgs` | List default values of actions.* , even though some of the actions may not be specified in the saved search. |  |
| `max_concurrent` | The maximum number of concurrent instances of this search the scheduler is allowed to run. |  |
| `next_scheduled_time` | Time when the scheduler runs this search again. |  |
| `orphan` | If add_orphan_field has been specified in the GET request, indicates whether the search is orphaned. |  |
| `qualifiedSearch` | The exact search string that the scheduler would run. |  |
| `realtime_schedule` | Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. See the POST parameter for this attribute for details. |  |
| `request.ui_dispatch_app` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `request.ui_dispatch_view` | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |  |
| `restart_on_searchpeer_add` | Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Note: The peer can be a newly added peer or a peer down and now available. |  |
| `run_n_times` | Runs this search exactly the specified number of times. Does not run the search again until the Splunk platform is restarted. |  |
| `run_on_startup` | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. This parameter should be set to 1 for scheduled searches that populate lookup tables. |  |
| `schedule_priority` | Indicates the scheduling priority of a specific search. One of the following values. CODE Copy [ default | higher | highest ] [ default | higher | highest ] default No scheduling priority increase. higher Scheduling priority is higher than other searches of the same scheduling tier. While there are four tiers of priority for scheduled searches, only the following are affected by this property: CODE Copy * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). highest Scheduling priority is higher than other searches regardless of scheduling tier. However, real-time-scheduled searches with priority = highest always have priority over continuous scheduled searches with priority = highest . This is the high-to-low priority order (where RTSS = real-time-scheduled search, CSS = continuous-scheduled search, d = default, h = higher, H = highest). CODE Copy RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) Changing the priority requires the search owner to have the edit_search_schedule_priority capability in order to make non-default settings. Defaults to default . For more details, see savedsearches.conf.spec . |  |
| `schedule_window` | Time window (in minutes) during which the search has lower priority. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. If set to auto , the scheduler prioritizes searches automatically. |  |
| `search` | Search expression to filter the response. The response matches field values against the search expression. For example: search=foo matches any object that has "foo" as a substring in a field. search=field_name%3Dfield_value restricts the match to a single field. URI-encoding is required in this example. |  |
| `vsid` | The viewstate id associated with the UI view listed in 'displayview'. Must match up to a stanza in viewstates.conf. |  |

#### POST

Create a saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Boolean | Enable or disable an alert action. See alert_actions.conf for available alert action types. action_name defaults to an empty string. |
| `action.<action_name>.<parameter>` |  | Use this syntax to configure action parameters. See alert_actions.conf for parameter options. |
| `action.summary_index._type"` | String | Specifies the data type of the summary index where the Splunk software saves the results of the scheduled search. Can be set to event or metric . |
| `action.summary_index.force_realtime_schedule` | Boolean | By default, realtime_schedule is false for a report configured for summary indexing. When set to 1 or True , this setting overrides realtime_schedule . Setting this setting to true can cause gaps in summary data, as a realtime_schedule search is skipped if search concurrency limits are violated. |
| `actions` | String | A comma-separated list of actions to enable. For example: rss,email |
| `alert.digest_mode` | Boolean | Specifies whether alert actions are applied to the entire result set or on each individual result. Defaults to 1. |
| `alert.expires` | Number | Valid values: [number][time-unit] Sets the period of time to show the alert in the dashboard. Defaults to 24h. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |
| `alert.severity` | Enum | Valid values: (1 \| 2 \| 3 \| 4 \| 5 \| 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN (default) 4 ERROR 5 SEVERE 6 FATAL |
| `alert.suppress` | Boolean | Indicates whether alert suppression is enabled for this scheduled search. |
| `alert.suppress.fields` | String | Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled. |
| `alert.suppress.group_name` | String | Optional setting. Used to define an alert suppression group for a set of alerts that are running over identical or very similar datasets. Alert suppression groups can help you avoid getting multiple triggered alert notifications for the same data. |
| `alert.suppress.period` | Number | Valid values: [number][time-unit] Specifies the suppression period. Only valid if alert.suppress is enabled. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |
| `alert.track` | String | Valid values: (true \| false \| auto) Specifies whether to track the actions triggered by this scheduled search. auto - Determine whether to apply alert tracking to this search, based on the tracking setting of each action. Do not track scheduled searches that always trigger actions. Default. true - Force alert tracking for this search. false - Disable alert tracking for this search. |
| `alert_comparator` | String | One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc. Used with alert_threshold to trigger alert actions. |
| `alert_condition` | String | Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition, do not set counttype, relation, or quantity. |
| `alert_threshold` | Number | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator ) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |
| `alert_type` | String | What to base the alert on, overridden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |
| `allow_skew` | 0 | <percentage> | <duration> | Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. Defaults to 0 (skew disabled). CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule' values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 . Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |
| `args.*` | String | Wildcard argument that accepts any saved search template argument, such as args.username=foobar when the search is search $username$. |
| `auto_summarize` | Boolean | Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0. |
| `auto_summarize.command` | String | An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details. Do not change unless you understand the architecture of saved search auto summarization. |
| `auto_summarize.cron_schedule` | String | Cron schedule that probes and generates the summaries for this saved search. The default value, */10 * * * * , corresponds to "every ten hours". |
| `auto_summarize.dispatch.earliest_time` | String | A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `auto_summarize.dispatch.latest_time` | String | A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `auto_summarize.dispatch.time_format` | String | Defines the time format used to specify the earliest and latest time. Defaults to %FT%T.%Q%:z |
| `auto_summarize.dispatch.ttl` | String | Valid values: Integer[p] Indicates the time to live (ttl), in seconds, for the artifacts of the summarization of the scheduled search. Defaults to 60. |
| `auto_summarize.max_concurrent` | Number | The maximum number of concurrent instances of this auto summarizing search that the scheduler is allowed to run. |
| `auto_summarize.max_disabled_buckets` | Number | The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2. |
| `auto_summarize.max_summary_ratio` | Number | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1. Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size. |
| `auto_summarize.max_summary_size` | Number | The minimum summary size, in bytes, before testing whether the summarization is helpful. The default value, 52428800 , is equivalent to 5MB. |
| `auto_summarize.max_time` | Number | The maximum time, in seconds, that the summary search is allowed to run. Defaults to 3600. Note: This is an approximate time. The summary search stops at clean bucket boundaries. |
| `auto_summarize.suspend_period` | String | The amount of time to suspend summarization of this search if the summarization is deemed unhelpful. Defaults to 24h. |
| `auto_summarize.timespan` | String | Comma-delimited list of time ranges that each summarized chunk should span. Comprises the list of available granularity levels for which summaries would be available. Does not support 1w timespans. For example, a timechart over the last month whose granularity is at the day level should set this to 1d . If you need the same data summarized at the hour level for weekly charts, use: 1h,1d . |
| `cron_schedule` | String | Valid values: cron string The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * * , which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. To reduce system load, schedule your searches so that they are staggered over time. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. |
| `disabled` | Boolean | Indicates whether the saved search is enabled. Defaults to 0. Disabled saved searches are not visible in Splunk Web. |
| `dispatch.*` | String | Wildcard argument that accepts any dispatch related argument. |
| `dispatch.allow_partial_results` | Boolean | Specifies whether the search job can proceed to provide partial results if a search peer fails. When set to false, the search job fails if a search peer providing results for the search job fails. |
| `dispatch.auto_cancel` | Number | Specifies the amount of inactive time, in seconds, after which the search job is automatically canceled. |
| `dispatch.auto_pause` | Number | Specifies the amount of inactive time, in seconds, after which the search job is automatically paused. |
| `dispatch.buckets` | Number | The maximum number of timeline buckets. Defaults to 0. |
| `dispatch.earliest_time` | String | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `dispatch.index_earliest` | String | A time string that specifies the earliest index time for this search. Can be a relative or absolute time. |
| `dispatch.index_latest` | String | A time string that specifies the latest index time for this saved search. Can be a relative or absolute time. |
| `dispatch.indexedRealtime` | Boolean | Indicates whether to used indexed-realtime mode when doing real-time searches. |
| `dispatch.indexedRealtimeOffset` | Number | Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf . Default for saved searches is "unset", falling back to limits.conf setting. |
| `dispatch.indexedRealtimeMinSpan` | Number | Allows for a per-job override of the [search] indexed_realtime_default_span setting in limits.conf . Default for saved searches is "unset", falling back to the limits.conf setting. |
| `dispatch.latest_time` | String | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `dispatch.lookups` | Boolean | Enables or disables the lookups for this search. Defaults to 1. |
| `dispatch.max_count` | Number | The maximum number of results before finalizing the search. Defaults to 500000. |
| `dispatch.max_time` | Number | Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0. |
| `dispatch.reduce_freq` | Number | Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10. |
| `dispatch.rt_backfill` | Boolean | Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0. |
| `dispatch.rt_maximum_span` | Number | Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf . Default for saved searches is "unset", falling back to the limits.conf setting. |
| `dispatch.sample_ratio` | Number | The integer value used to calculate the sample ratio. The formula is 1 / <integer> . |
| `dispatch.spawn_process` | Boolean | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Specifies whether to spawn a new search process when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process. |
| `dispatch.time_format` | String | A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z . |
| `dispatch.ttl` | Number | Valid values: Integer[p]. Defaults to 2p. Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered. If an action is triggered, the action ttl is used. If multiple actions are triggered, the maximum ttl is applied to the artifacts. To set the action ttl, refer to alert_actions.conf.spec . If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period. |
| `dispatchAs` | String | When the saved search is dispatched using the "saved/searches/{name}/dispatch" endpoint, this setting controls what user that search is dispatched as. Only meaningful for shared saved searches. Can be set to owner or user . |
| `displayview` | String | Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |
| `durable.backfill_type` | String | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . time_whole - The Splunk software schedules a single backfill search job with a time range that spans the combined time ranges of all failed scheduled search jobs. The time_whole setting can be applied only to searches that are streaming, where the results are raw events without additional aggregation. time_interval - The Splunk software schedules multiple backfill search jobs, one for each failed scheduled search job. The backfill jobs have time ranges that match those of the failed jobs. The time_interval setting can be applied to both streaming and non-streaming searches. auto - The Splunk software decides the backfill type by checking whether the search is streaming or not. If the search is streaming, the Splunk software uses the time_whole backfill type. Otherwise, it uses the time_interval backfill type. |
| `durable.lag_time` | Number | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |
| `durable.max_backfill_intervals` | Number | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |
| `durable.track_time_type` | String | Indicates that a scheduled search is durable and specifies how the search tracks events. A durable search is a search that tries to ensure the delivery of all results, even when the search process is slowed or stopped by runtime issues like rolling restarts, network bottlenecks, and even downed servers. Applies only to scheduled searches. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |
| `is_scheduled` | Boolean | Whether this search is to be run on a schedule |
| `is_visible` | Boolean | Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1. |
| `max_concurrent` | Number | The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1. |
| `next_scheduled_time` | String | Read-only attribute. Value ignored on POST. There are some old clients who still send this value |
| `qualifiedSearch` | String | Read-only attribute. Value ignored on POST. This value is computed during runtime. |
| `realtime_schedule` | Boolean | Controls the way the scheduler computes the next execution time of a scheduled search. Defaults to 1. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option. If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range. The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0). |
| `request.ui_dispatch_app` | String | Specifies a field used by Splunk Web to denote the app this search should be dispatched in. |
| `request.ui_dispatch_view` | String | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |
| `restart_on_searchpeer_add` | Boolean | Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1. Note: The peer can be a newly added peer or a peer down and now available. |
| `run_n_times` | Number | Runs this search exactly the specified number of times. Does not run the search again until the Splunk platform is restarted. |
| `run_on_startup` | Boolean | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set run_on_startup to 1 for scheduled searches that populate lookup tables. |
| `schedule_priority` | String | Configures the scheduling priority of a specific search. One of the following values. CODE Copy [ default \| higher \| highest ] [ default \| higher \| highest ] default No scheduling priority increase. higher Scheduling priority is higher than other searches of the same scheduling tier. While there are four tiers of priority for scheduled searches, only the following are affected by this property: CODE Copy * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). highest Scheduling priority is higher than other searches regardless of scheduling tier. However, real-time-scheduled searches with priority = highest always have priority over continuous scheduled searches with priority = highest . This is the high-to-low priority order (where RTSS = real-time-scheduled search, CSS = continuous-scheduled search, d = default, h = higher, H = highest). CODE Copy RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) Changing the priority requires the search owner to have the edit_search_schedule_priority capability in order to make non-default settings. Defaults to default . For more details, see savedsearches.conf.spec . |
| `schedule_window` | Number or auto | Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto . |
| `search` | String | Required . The search to save. |
| `vsid` | String | Defines the viewstate id associated with the UI view listed in 'displayview'. Must match up to a stanza in viewstates.conf. |
| `workload_pool` | String | Specifies the new workload pool where the existing running search will be placed. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular search. For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the search configuration to which it is applied. |  |
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments.< Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be referenced externally, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the global maximum number of search results to send when email.action is enabled. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportCIDFontList` | Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering. If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used. To skip loading any CID fonts, specify the empty string. Default value: "gb cns jp kor" |  |
| `action.email.reportIncludeSplunkLogo` | Indicates whether to include the Splunk logo with the report. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.reportServerEnabled` | Not supported. |  |
| `action.email.reportServerURL` | Not supported. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `action.email.width_sort_columns` | Indicates whether columns should be sorted from least wide to most wide, left to right. Only valid if format=text. |  |
| `action.populate_lookup` | Indicates the state of the populate lookup action. |  |
| `action.populate_lookup.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.populate_lookup.dest` | Lookup name of path of the lookup to populate. |  |
| `action.populate_lookup.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.populate_lookup.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.populate_lookup.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.populate_lookup.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.populate_lookup.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p] |  |
| `action.rss` | Indicates the state of the RSS action. |  |
| `action.rss.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.rss.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.rss.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.rss.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Valid values are Integer[m |s |h |d]. |  |
| `action.rss.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.rss.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.script` | Indicates the state of the script for this action. |  |
| `action.script.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.script.filename` | File name of the script to call. Required if script action is enabled |  |
| `action.script.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.script.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.script.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. |  |
| `action.script.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.script.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.summary_index` | Indicates the state of the summary index. |  |
| `action.summary_index._name` | Specifies the name of the summary index where the results of the scheduled search are saved. Defaults to "summary." |  |
| `action.summary_index.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.summary_index.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.summary_index.inline` | Determines whether to execute the summary indexing action as part of the scheduled search. Note: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always). |  |
| `action.summary_index.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.summary_index.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.summary_index.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.summary_index.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `actions` | Actions triggerd by this alert. |  |
| `alert.digest_mode` | Indicates if the alert actions are applied to the entire result set or to each individual result. |  |
| `alert.expires` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. Valid values: [number][time-unit] |  |
| `alert.severity` | Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL |  |
| `alert.suppress` | Indicates whether alert suppression is enabled for this schedules search. |  |
| `alert.suppress.fields` | Fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled. |  |
| `alert.suppress.period` | Specifies the suppresion period. Only valid if alert.supress is enabled. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.track` | Specifies whether to track the actions triggered by this scheduled search. auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. true - force alert tracking. false - disable alert tracking for this search. |  |
| `alert_comparator` | One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc |  |
| `alert_condition` | A conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition, do not set counttype, relation, or quantity. |  |
| `alert_threshold` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |  |
| `alert_type` | What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |  |
| `allow_skew` | 0 | <percentage> | <duration> Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 (which disables skew). Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |  |
| `args.*` | Wildcard argument that accepts any saved search template argument, such as args.username=foobar when the search is search $username$. |  |
| `auto_summarize` | Indicates whether the scheduler should ensure that the data for this search is automatically summarized. |  |
| `auto_summarize.command` | A search template that constructs the auto summarization for this search. Caution: Advanced feature. Do not change unless you understand the architecture of auto summarization of saved searches. |  |
| `auto_summarize.cron_schedule` | Cron schedule that probes and generates the summaries for this saved search. |  |
| `auto_summarize.dispatch.earliest_time` | A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time. |  |
| `auto_summarize.dispatch.latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. |  |
| `auto_summarize.dispatch.time_format` | Time format used to specify the earliest and latest times. |  |
| `auto_summarize.dispatch.ttl` | Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search. If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period. |  |
| `auto_summarize.max_disabled_buckets` | The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. |  |
| `auto_summarize.max_summary_ratio` | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size. |  |
| `auto_summarize.max_summary_size` | The minimum summary size, in bytes, before testing whether the summarization is helpful. |  |
| `auto_summarize.max_time` | Maximum time (in seconds) that the summary search is allowed to run. Note: This is an approximate time. The summary search stops at clean bucket boundaries. |  |
| `auto_summarize.suspend_period` | Time specifier indicating when to suspend summarization of this search if the summarization is deemed unhelpful. |  |
| `auto_summarize.timespan` | The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. For example a timechart over the last month whose granularity is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d. |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if this saved search is disabled. |  |
| `dispatch.*` | * represents any custom dispatch field. |  |
| `dispatch.buckets` | The maximum nuber of timeline buckets. |  |
| `dispatch.earliest_time` | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.indexedRealtime` | Indicates whether to used indexed-realtime mode when doing real-time searches. |  |
| `dispatch.latest_time` | A time string that specifies the latest time for the saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.lookups` | Indicates if lookups are enabled for this search. |  |
| `dispatch.max_count` | The maximum number of results before finalizing the search. |  |
| `dispatch.max_time` | Indicates the maximum amount of time (in seconds) before finalizing the search. |  |
| `dispatch.reduce_freq` | Specifies how frequently the MapReduce reduce phase runs on accumulated map values. |  |
| `dispatch.rt_backfill` | Indicates whether to back fill the real time window for this search. Parameter valid only if this is a real time search |  |
| `dispatch.spawn_process` | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Indicates whether a new search process spawns when this saved search is executed. |  |
| `dispatch.time_format` | Time format string that defines the time format for specifying the earliest and latest time. |  |
| `dispatch.ttl` | Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered. If an action is triggered, the action ttl is used. If multiple actions are triggered, the maximum ttl is applied to the artifacts. To set the action ttl, refer to alert_actions.conf.spec . If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period. |  |
| `displayview` | Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |  |
| `durable.backfill_type` | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . |  |
| `durable.lag_time` | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.max_backfill_intervals` | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.track_time_type` | Indicates that a scheduled search is durable and specifies how the search tracks events. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `is_visible` | Indicates if this saved search appears in the visible saved search list. |  |
| `max_concurrent` | The maximum number of concurrent instances of this search the scheduler is allowed to run. |  |
| `next_scheduled_time` | The time when the scheduler runs this search again. |  |
| `qualifiedSearch` | The exact search string that the scheduler would run. |  |
| `realtime_schedule` | Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option. If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range. The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0). |  |
| `request.ui_dispatch_app` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `request.ui_dispatch_view` | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |  |
| `restart_on_searchpeer_add` | Indicates whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Note: The peer can be a newly added peer or a peer down and now available. |  |
| `run_on_startup` | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Splunk recommends that you set run_on_startup to true for scheduled searches that populate lookup tables. |  |
| `schedule_window` | Time window (in minutes) during which the search has lower priority. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. If set to auto , the scheduler prioritizes searches automatically. |  |
| `search` | Search expression to filter the response. The response matches field values against the search expression. For example: search=foo matches any object that has "foo" as a substring in a field. search=field_name%3Dfield_value restricts the match to a single field. URI-encoding is required in this example. |  |
| `vsid` | The viewstate id associated with the UI view listed in 'displayview'. Matches to a stanza in viewstates.conf. |  |

### `/services/saved/searches/{name}`

Manage the {name} saved search.

#### DELETE

Delete the named saved search.

#### GET

Access the named saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time` | String |  |
| `latest_time` | String |  |
| `listDefaultActionArgs` | Boolean |  |
| `add_orphan_field` | Boolean |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular search. For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the search configuration to which it is applied. |  |
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here that is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments. Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. Note: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be referenced externally, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost." When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the global maximum number of search results to send when email.action is enabled. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.reportServerEnabled` | Not supported. |  |
| `action.email.reportServerURL` | Not supported. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `action.populate_lookup` | The state of the populate lookup action. |  |
| `action.populate_lookup.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.populate_lookup.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.populate_lookup.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.populate_lookup.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.populate_lookup.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.populate_lookup.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p] |  |
| `action.rss` | The state of the RSS action. |  |
| `action.rss.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.rss.hostname` | Sets the hostname used in the web link (url) sent in alert actions. |  |
| `action.rss.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.rss.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m. |  |
| `action.rss.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.rss.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.script` | The state of the script action. |  |
| `action.script.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.script.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.script.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.script.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. |  |
| `action.script.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.script.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.summary_index` | The state of the summary index action. |  |
| `action.summary_index._name` | Specifies the name of the summary index where the results of the scheduled search are saved. Defaults to "summary." |  |
| `action.summary_index._type"` | Specifies the data type of the summary index where the Splunk software saves the results of the scheduled search. Can be set to event or metric . |  |
| `action.summary_index.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.summary_index.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.summary_index.force_realtime_schedule` | By default, realtime_schedule is false for a report configured for summary indexing. When set to 1 or true , this setting overrides realtime_schedule . Setting this setting to true can cause gaps in summary data, as a realtime_schedule search is skipped if search concurrency limits are violated. |  |
| `action.summary_index.inline` | Determines whether to execute the summary indexing action as part of the scheduled search. Note: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always). |  |
| `action.summary_index.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.summary_index.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. |  |
| `action.summary_index.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.summary_index.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `alert.digest_mode` | Specifies whether alert actions are applied to the entire result set or to each individual result. |  |
| `alert.expires` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. |  |
| `alert.managedBy` | Specifies the feature or component that created the alert. |  |
| `alert.severity` | Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL |  |
| `alert.suppress` | Indicates whether alert suppression is enabled for this schedules search. |  |
| `alert.suppress.fields` | List of fields to use when suppressing per-result alerts. Must be specified if the digest mode is disabled and suppression is enabled. |  |
| `alert.suppress.group_name` | Optional setting. Used to define an alert suppression group for a set of alerts that are running over identical or very similar datasets. Alert suppression groups can help you avoid getting multiple triggered alert notifications for the same data. |  |
| `alert.suppress.period` | Specifies the suppression period. Only valid if alert.suppress is enabled. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.track` | Specifies whether to track the actions triggered by this scheduled search. auto - (Default) Determine whether to apply alert tracking to this search, based on the tracking setting of each action. Do not track scheduled searches that always trigger actions. true - Force alert tracking for this search. Default. false - Disable alert tracking for this search. |  |
| `alert_comparator` | One of the following strings: greater than less than equal to rises by drops by rises by perc drops by perc Used with alert_threshold to trigger alert actions. |  |
| `alert_condition` | A conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition , do not set counttype, relation, or quantity. |  |
| `alert_threshold` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator ) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to rises by perc" or "drops by perc." |  |
| `alert_type` | What to base the alert on, overridden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. Typically, reports return the "always" value, while alerts can return any other value. |  |
| `allow_skew` | 0 | <percentage> | <duration> Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 . Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |  |
| `auto_summarize` | Specifies whether the search scheduler should ensure that the data for this search is automatically summarized. |  |
| `auto_summarize.command` | A search template to use to construct the auto-summarization for the search. Do not change. |  |
| `auto_summarize.cron_schedule` | Cron schedule to use to probe or generate the summaries for this search |  |
| `auto_summarize.dispatch.<arg-name>` | Dispatch options that can be overridden when running the summary search. |  |
| `auto_summarize.max_concurrent` | The maximum number of concurrent instances of this auto summarizing search that the scheduler is allowed to run. |  |
| `auto_summarize.max_disabled_buckets` | The maximum number of buckets with suspended summarization before the summarization search is completely stopped and the summarization of the search is suspended for the value specified by the auto_summarize.suspend_period setting. |  |
| `auto_summarize.max_summary_ratio` | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. |  |
| `auto_summarize.max_summary_size` | The minimum summary size, in bytes, before testing whether the summarization is helpful. |  |
| `auto_summarize.max_time` | The maximum time, in seconds, that the auto-summarization search is allowed to run. |  |
| `auto_summarize.suspend_period` | The amount of time to suspend summarization of the search if the summarization is deemed unhelpful. |  |
| `auto_summarize.timespan` | Comma-delimited list of time ranges that each summarized chunk should span. Comprises the list of available summary ranges for which summaries would be available. Does not support 1w timespans. |  |
| `auto_summarize.workload_pool` | Sets the name of the workload pool that is used by the auto-summarization of this search. |  |
| `cron_schedule` | The cron schedule to run this search. For more information, refer to the description of this parameter in the POST endpoint. |  |
| `defer_scheduled_searchable_idxc` | Specifies whether to defer a continuous saved search during a searchable rolling restart or searchable rolling upgrade of an indexer cluster. |  |
| `disabled` | Indicates if this saved search is disabled. |  |
| `dispatch.allow_partial_results` | Specifies whether the search job can proceed to provide partial results if a search peer fails. When set to false, the search job fails if a search peer providing results for the search job fails. |  |
| `dispatch.auto_cancel` | Specifies the amount of inactive time, in seconds, after which the search job is automatically canceled. |  |
| `dispatch.auto_pause` | Specifies the amount of inactive time, in seconds, after which the search job is automatically paused. |  |
| `dispatch.buckets` | The maximum number of timeline buckets. |  |
| `dispatch.earliest_time` | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.index_earliest` | Specifies the earliest index time for this search. Can be a relative or absolute time. |  |
| `dispatch.index_latest` | Specifies the latest index time for this saved search. Can be a relative or absolute time. |  |
| `dispatch.indexedRealtime` | Specifies whether to use 'indexed-realtime' mode when doing real-time searches. |  |
| `dispatch.indexedRealtimeMinSpan` | Specifies the minimum number of seconds to wait between component index searches. |  |
| `dispatch.indexedRealtimeOffset` | Specifies the number of seconds to wait for disk flushes to finish. |  |
| `dispatch.indexedRealtimeMinSpan` | Allows for a per-job override of the [search] indexed_realtime_default_span setting in limits.conf . The default for saved searches is "unset", falling back to the limits.conf setting. |  |
| `dispatch.latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.lookups` | Indicates if lookups are enabled for this search. |  |
| `dispatch.max_count` | The maximum number of results before finalizing the search. |  |
| `dispatch.max_time` | Indicates the maximum amount of time (in seconds) before finalizing the search. |  |
| `dispatch.reduce_freq` | Specifies how frequently the MapReduce reduce phase runs on accumulated map values. |  |
| `dispatch.rt_backfill` | Specifies whether to do real-time window backfilling for scheduled real-time searches. |  |
| `dispatch.rt_maximum_span` | Sets the maximum number of seconds to search data that falls behind real time. |  |
| `dispatch.sample_ratio` | The integer value used to calculate the sample ratio. The formula is 1 / <integer> . |  |
| `dispatch.spawn_process` | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Indicates whether a new search process spawns when this saved search is executed. |  |
| `dispatch.time_format` | A time format string that defines the time format for specifying the earliest and latest time. |  |
| `dispatch.ttl` | Indicates the time to live (ttl), in seconds, for the artifacts of the scheduled search, if no actions are triggered. |  |
| `displayview` | Defines the default Splunk Web view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |  |
| `durable.backfill_type` | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . |  |
| `durable.lag_time` | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.max_backfill_intervals` | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.track_time_type` | Indicates that a scheduled search is durable and specifies how the search tracks events. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |  |
| `earliest_time` | For scheduled searches display all the scheduled times starting from this time. |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `is_visible` | Indicates if this saved search appears in the visible saved search list. |  |
| `latest_time` | For scheduled searches display all the scheduled times until this time (not just the next run time). |  |
| `listDefaultActionArgs` | List default values of actions.*, even though some of the actions may not be specified in the saved search. |  |
| `max_concurrent` | The maximum number of concurrent instances of this search the scheduler is allowed to run. |  |
| `next_scheduled_time` | The time when the scheduler runs this search again. |  |
| `orphan` | If the add_orphan_field parameter is passed in with the GET request, this field indicates whether the search is orphaned. |  |
| `qualifiedSearch` | The exact search command for this saved search. |  |
| `realtime_schedule` | Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. See the POST parameter for this attribute for details. |  |
| `request.ui_dispatch_app` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `request.ui_dispatch_view` | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |  |
| `restart_on_searchpeer_add` | Indicates whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Note: The peer can be a newly added peer or a peer down and now available. |  |
| `run_n_times` | Runs this search exactly the specified number of times. Does not run the search again until the Splunk platform is restarted. |  |
| `run_on_startup` | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Set run_on_startup to true for scheduled searches that populate lookup tables. |  |
| `schedule_priority` | Indicates the scheduling priority of a specific search. One of the following values. CODE Copy [ default | higher | highest ] [ default | higher | highest ] Raises the scheduling priority of the named search. default No scheduling priority increase. higher Scheduling priority is higher than other searches of the same scheduling tier. While there are four tiers of priority for scheduled searches, only the following are affected by this property: CODE Copy * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). * real-Time-Scheduled (realtime_schedule=1). * continuous-Scheduled (realtime_schedule=0). highest Scheduling priority is higher than other searches regardless of scheduling tier. However, real-time-scheduled searches with priority = highest always have priority over continuous scheduled searches with priority = highest . The high-to-low priority order (where RTSS = real-time-scheduled search, CODE Copy CSS = continuous-scheduled search, d = default, h = higher, H = highest) is: CSS = continuous-scheduled search, d = default, h = higher, H = highest) is: CODE Copy RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) RTSS(H) > CSS(H) > RTSS(h) > RTSS(d) > CSS(h) > CSS(d) Requires the search owner to have the edit_search_schedule_priority capability in order to make non-default settings. Defaults to default . For more details, see savedsearches.conf.spec . |  |
| `schedule_window` | Time window (in minutes) during which the search has lower priority. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. If set to auto , the scheduler determines the optimal time window automatically. |  |
| `search` | Search expression to filter the response. The response matches field values against the search expression. For example: search=foo matches any object that has "foo" as a substring in a field. search=field_name%3Dfield_value restricts the match to a single field. URI-encoding is required in this example. |  |
| `vsid` | Defines the viewstate id associated with the UI view listed in 'displayview'. Must match up to a stanza in viewstates.conf. |  |

#### POST

Update the named saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Boolean | Enable or disable an alert action. See alert_actions.conf for available alert action types. action_name defaults to the empty string. |
| `action.<action_name>.<parameter>` | String or Number | Use this syntax to configure action parameters. See alert_actions.conf for parameter options. |
| `action.summary_index._type"` | String | Specifies the data type of the summary index where the Splunk software saves the results of the scheduled search. Can be set to event or metric . |
| `action.summary_index.force_realtime_schedule` | Boolean | By default, realtime_schedule is false for a report configured for summary indexing. When set to 1 or True , this setting overrides realtime_schedule . Setting this setting to true can cause gaps in summary data, as a realtime_schedule search is skipped if search concurrency limits are violated. |
| `actions` | String | A comma-separated list of actions to enable. For example: rss,email |
| `alert.digest_mode` | Boolean | Specifies whether alert actions are applied to the entire result set or on each individual result. Defaults to 1 (true). |
| `alert.expires` | Number | Valid values: [number][time-unit] Sets the period of time to show the alert in the dashboard. Defaults to 24h. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |
| `alert.severity` | Enum | Valid values: (1 \| 2 \| 3 \| 4 \| 5 \| 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL Defaults to 3. |
| `alert.suppress` | Boolean | Indicates whether alert suppression is enabled for this scheduled search. |
| `alert.suppress.fields` | String | Comma delimited list of fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled. |
| `alert.suppress.group_name` | String | Optional setting. Used to define an alert suppression group for a set of alerts that are running over identical or very similar datasets. Alert suppression groups can help you avoid getting multiple triggered alert notifications for the same data. |
| `alert.suppress.period` | Number | Valid values: [number][time-unit] Specifies the suppression period. Only valid if alert.suppress is enabled. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |
| `alert.track` | Enum | Valid values: (true \| false \| auto) Specifies whether to track the actions triggered by this scheduled search. auto - Determine whether to apply alert tracking to this search, based on the tracking setting of each action. Do not track scheduled searches that always trigger actions. Default. true - Force alert tracking for this search. false - Disable alert tracking for this search. |
| `alert_comparator` | String | One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc. Used with alert_threshold to trigger alert actions. |
| `alert_condition` | String | Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition, do not set counttype, relation, or quantity. |
| `alert_threshold` | Number | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator ) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |
| `alert_type` | String | What to base the alert on, overridden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |
| `allow_skew` | 0 | <percentage> | <duration> | Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 . Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |
| `args.*` | String | Wildcard argument that accepts any saved search template argument, such as args.username=foobar when the search is search $username$. |
| `auto_summarize` | Boolean | Indicates whether the scheduler should ensure that the data for this search is automatically summarized. Defaults to 0. |
| `auto_summarize.command` | String | An auto summarization template for this search. See auto summarization options in savedsearches.conf for more details. Do not change unless you understand the architecture of saved search auto summarization. |
| `auto_summarize.cron_schedule` | String | Cron schedule that probes and generates the summaries for this saved search. The default value is */10 * * * * and corresponds to "every ten hours". |
| `auto_summarize.dispatch.earliest_time` | String | A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `auto_summarize.dispatch.latest_time` | String | A time string that specifies the latest time for summarizing this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `auto_summarize.dispatch.time_format` | String | Defines the time format that Splunk software uses to specify the earliest and latest time. Defaults to %FT%T.%Q%:z |
| `auto_summarize.dispatch.ttl` | String | Valid values: Integer[p]. Indicates the time to live (ttl), in seconds, for the artifacts of the summarization of the scheduled search. Defaults to 60. |
| `auto_summarize.max_disabled_buckets` | Number | The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. Defaults to 2. |
| `auto_summarize.max_summary_ratio` | Number | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Defaults to 0.1 Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size. |
| `auto_summarize.max_summary_size` | Number | The minimum summary size, in bytes, before testing whether the summarization is helpful. The default value is 52428800 and is equivalent to 5MB. |
| `auto_summarize.max_time` | Number | Maximum time (in seconds) that the summary search is allowed to run. Defaults to 3600. Note: This is an approximate time. The summary search stops at clean bucket boundaries. |
| `auto_summarize.suspend_period` | String | Time specifier indicating when to suspend summarization of this search if the summarization is deemed unhelpful. Defaults to 24h. |
| `auto_summarize.timespan` | String | Comma-delimited list of time ranges that each summarized chunk should span. Comprises the list of available granularity levels for which summaries would be available. Does not support 1w timespans. For example, a timechart over the last month whose granularity is at the day level should set this to 1d . If you need the same data summarized at the hour level for weekly charts, use: 1h,1d . |
| `cron_schedule` | String | Valid values: cron string The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. |
| `disabled` | Boolean | Indicates if the saved search is enabled. Defaults to 0. Disabled saved searches are not visible in Splunk Web. |
| `dispatch.*` | String | Wildcard argument that accepts any dispatch related argument. |
| `dispatch.allow_partial_results` | Boolean | Specifies whether the search job can proceed to provide partial results if a search peer fails. When set to false, the search job fails if a search peer providing results for the search job fails. |
| `dispatch.auto_cancel` | Number | Specifies the amount of inactive time, in seconds, after which the search job is automatically canceled. |
| `dispatch.auto_pause` | Number | Specifies the amount of inactive time, in seconds, after which the search job is automatically paused. |
| `dispatch.buckets` | Number | The maximum number of timeline buckets. Defaults to 0. |
| `dispatch.earliest_time` | String | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `dispatch.index_earliest` | String | A time string that specifies the earliest index time for this search. Can be a relative or absolute time. |
| `dispatch.index_latest` | String | A time string that specifies the latest index time for this saved search. Can be a relative or absolute time. |
| `dispatch.indexedRealtime` | Boolean | Indicates whether to used indexed-realtime mode when doing real-time searches. |
| `dispatch.indexedRealtimeOffset` | Integer | Allows for a per-job override of the [search] indexed_realtime_disk_sync_delay setting in limits.conf . Default for saved searches is "unset", falling back to limits.conf setting. |
| `dispatch.indexedRealtimeMinSpan` | Integer | Allows for a per-job override of the [search] indexed_realtime_default_span setting in limits.conf . Default for saved searches is "unset", falling back to the limits.conf setting. |
| `dispatch.latest_time` | String | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |
| `dispatch.lookups` | Boolean | Enables or disables the lookups for this search. Defaults to 1. |
| `dispatch.max_count` | Number | The maximum number of results before finalizing the search. Defaults to 500000. |
| `dispatch.max_time` | Number | Indicates the maximum amount of time (in seconds) before finalizing the search. Defaults to 0. |
| `dispatch.reduce_freq` | Number | Specifies, in seconds, how frequently the MapReduce reduce phase runs on accumulated map values. Defaults to 10. |
| `dispatch.rt_backfill` | Boolean | Whether to back fill the real time window for this search. Parameter valid only if this is a real time search. Defaults to 0. |
| `dispatch.rt_maximum_span` | Number | Allows for a per-job override of the [search] indexed_realtime_maximum_span setting in limits.conf . Default for saved searches is "unset", falling back to the limits.conf setting. |
| `dispatch.sample_ratio` | Number | The integer value used to calculate the sample ratio. The formula is 1 / <integer> . |
| `dispatch.spawn_process` | Boolean | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Specifies whether a new search process spawns when this saved search is executed. Defaults to 1. Searches against indexes must run in a separate process. |
| `dispatch.time_format` | String | A time format string that defines the time format for specifying the earliest and latest time. Defaults to %FT%T.%Q%:z |
| `dispatch.ttl` | Number | Valid values: Integer[p]. Defaults to 2p. Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered. If an action is triggered, the ttl changes to that action ttl. If multiple actions are triggered, the maximum ttl is applied to the artifacts. To set the action ttl, refer to alert_actions.conf.spec . If the integer is followed by the letter 'p', the ttl is handled as a multiple of the scheduled search period. |
| `dispatchAs` | String | When the saved search is dispatched using the "saved/searches/{name}/dispatch" endpoint, this setting controls what user that search is dispatched as. Only meaningful for shared saved searches. Can be set to owner or user . |
| `displayview` | String | Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |
| `durable.backfill_type` | String | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . time_whole - The Splunk software schedules a single backfill search job with a time range that spans the combined time ranges of all failed scheduled search jobs. The time_whole setting can be applied only to searches that are streaming, where the results are raw events without additional aggregation. time_interval - The Splunk software schedules multiple backfill search jobs, one for each failed scheduled search job. The backfill jobs have time ranges that match those of the failed jobs. The time_interval setting can be applied to both streaming and non-streaming searches. auto - The Splunk software decides the backfill type by checking whether the search is streaming or not. If the search is streaming, the Splunk software uses the time_whole backfill type. Otherwise, it uses the time_interval backfill type. |
| `durable.lag_time` | Number | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |
| `durable.max_backfill_intervals` | Number | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |
| `durable.track_time_type` | String | Indicates that a scheduled search is durable and specifies how the search tracks events. A durable search is a search that tries to ensure the delivery of all results, even when the search process is slowed or stopped by runtime issues like rolling restarts, network bottlenecks, and even downed servers. Applies only to scheduled searches. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |
| `is_scheduled` | Boolean | Whether this search is to be run on a schedule |
| `is_visible` | Boolean | Specifies whether this saved search should be listed in the visible saved search list. Defaults to 1. |
| `max_concurrent` | Number | The maximum number of concurrent instances of this search the scheduler is allowed to run. Defaults to 1. |
| `next_scheduled_time` | String | Read-only attribute. Value ignored on POST. There are some old clients who still send this value |
| `qualifiedSearch` | String | Read-only attribute. Value ignored on POST. The value is computed during runtime. |
| `realtime_schedule` | Boolean | Defaults to 1. Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option. If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range. The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0). |
| `request.ui_dispatch_app` | String | Specifies a field used by Splunk Web to denote the app this search should be dispatched in. |
| `request.ui_dispatch_view` | String | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |
| `restart_on_searchpeer_add` | Boolean | Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Defaults to 1. Note: The peer can be a newly added peer or a peer down and now available. |
| `run_n_times` | Number | Runs this search exactly the specified number of times. Does not run the search again until the Splunk platform is restarted. |
| `run_on_startup` | Boolean | Indicates whether this search runs at startup. If it does not run on startup, it runs at the next scheduled time. Defaults to 0. Set to 1 for scheduled searches that populate lookup tables. |
| `schedule_window` | Number or auto | Time window (in minutes) during which the search has lower priority. Defaults to 0. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. Set to auto to let the scheduler determine the optimal window value automatically. Requires the edit_search_schedule_window capability to override auto . |
| `search` | String | Required. The search to save. |
| `schedule_priority` | See description | Raises the scheduling priority of the named search. Use one of the following options. default No scheduling priority increase. higher Scheduling priority is higher than other searches of the same scheduling tier. While there are four tiers of priority for scheduled searches, only the following search types are affected by this property. real-time scheduled (realtime_schedule=1). continuous scheduled (realtime_schedule=0). highest Scheduling priority is higher than other searches regardless of scheduling tier. However, real-time-scheduled searches with priority = highest always have priority over continuous scheduled searches with priority = highest . Requires the search owner to have the edit_search_schedule_priority capability in order to make non-default settings. Defaults to default . For more details, see savedsearches.conf.spec . |
| `vsid` | String | Defines the viewstate id associated with the UI view listed in 'displayview'. Must match up to a stanza in viewstates.conf. |
| `workload_pool` | String | Specifies the new workload pool where the existing running search will be placed. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.<action_name>` | Indicates whether the <action_name> is enabled or disabled for a particular search. For more information about the alert action options see the alert_actions.conf file. |  |
| `action.<action_name>.<parameter>` | Overrides the setting defined for an action in the alert_actions.conf file with a new setting that is valid only for the search configuration to which it is applied. |  |
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments.< Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be referenced externally, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the global maximum number of search results to send when email.action is enabled. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportCIDFontList` | Space-separated list. Specifies the set (and load order) of CID fonts for handling Simplified Chinese(gb), Traditional Chinese(cns), Japanese(jp), and Korean(kor) in Integrated PDF Rendering. If multiple fonts provide a glyph for a given character code, the glyph from the first font specified in the list is used. To skip loading any CID fonts, specify the empty string. Default value: "gb cns jp kor" |  |
| `action.email.reportIncludeSplunkLogo` | Indicates whether to include the Splunk logo with the report. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.reportServerEnabled` | Not supported. |  |
| `action.email.reportServerURL` | Not supported. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `action.email.width_sort_columns` | Indicates whether columns should be sorted from least wide to most wide, left to right. Only valid if format=text. |  |
| `action.populate_lookup` | Indicates the state of the populate lookup action. |  |
| `action.populate_lookup.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.populate_lookup.dest` | Lookup name of path of the lookup to populate. |  |
| `action.populate_lookup.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.populate_lookup.maxresults` | The maximum number of search results sent using alerts. |  |
| `action.populate_lookup.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.populate_lookup.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.populate_lookup.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p] |  |
| `action.rss` | Indicates the state of the RSS action. |  |
| `action.rss.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.rss.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.rss.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.rss.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Valid values are Integer[m |s |h |d]. |  |
| `action.rss.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.rss.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.script` | Indicates the state of the script for this action. |  |
| `action.script.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.script.filename` | File name of the script to call. Required if script action is enabled |  |
| `action.script.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.script.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.script.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. |  |
| `action.script.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.script.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `action.summary_index` | Indicates the state of the summary index. |  |
| `action.summary_index._name` | Specifies the name of the summary index where the results of the scheduled search are saved. Defaults to "summary." |  |
| `action.summary_index.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.summary_index.hostname` | Sets the hostname used in the web link (url) sent in alert actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) See action.email.hostname for details. |  |
| `action.summary_index.inline` | Determines whether to execute the summary indexing action as part of the scheduled search. Note: This option is considered only if the summary index action is enabled and is always executed (in other words, if counttype = always). |  |
| `action.summary_index.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.summary_index.maxtime` | Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m. Valid values are: Integer[m|s|h|d] |  |
| `action.summary_index.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.summary_index.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p. If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are: Integer[p] |  |
| `actions` | Actions triggerd by this alert. |  |
| `alert.digest_mode` | Indicates if the alert actions are applied to the entire result set or to each individual result. |  |
| `alert.expires` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. Valid values: [number][time-unit] |  |
| `alert.severity` | Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL |  |
| `alert.suppress` | Indicates whether alert suppression is enabled for this schedules search. |  |
| `alert.suppress.fields` | Fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled. |  |
| `alert.suppress.period` | Specifies the suppresion period. Only valid if alert.supress is enabled. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.track` | Specifies whether to track the actions triggered by this scheduled search. auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. true - force alert tracking. false - disable alert tracking for this search. |  |
| `alert_comparator` | One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc |  |
| `alert_condition` | A conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition, do not set counttype, relation, or quantity. |  |
| `alert_threshold` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |  |
| `alert_type` | What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |  |
| `allow_skew` | 0 | <percentage> | <duration> Allows the search scheduler to distribute scheduled searches randomly and more evenly over their specified search periods. CAUTION: This setting does not require adjusting in most use cases. Check with an admin before making any updates. When set to a non-zero value for searches with the following cron_schedule values, the search scheduler randomly skews the second, minute, and hour on which the search runs. CODE Copy * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). * * * * * Every minute. */M * * * * Every M minutes (M > 0). 0 * * * * Every hour. 0 */H * * * Every H hours (H > 0). 0 0 * * * Every day (at midnight). When set to a non-zero value for a search that has any other cron_schedule setting, the search scheduler can randomly skew only the second on which the search runs. The amount of skew for a specific search remains constant between edits of the search. A value of 0 disallows skew. 0 is the default setting. Percentage <int> followed by % specifies the maximum amount of time to skew as a percentage of the scheduled search period. Duration <int><unit> specifies a maximum duration. The <unit> can be omitted only when the <int> is 0 (which disables skew). Valid duration units: m min minute mins minutes h hr hour hrs hours d day days Examples CODE Copy 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum 100% (for an every-5-minute search) = 5 minutes maximum 50% (for an every-minute search) = 30 seconds maximum 5m = 5 minutes maximum 1h = 1 hour maximum |  |
| `args.*` | Wildcard argument that accepts any saved search template argument, such as args.username=foobar when the search is search $username$. |  |
| `auto_summarize` | Indicates whether the scheduler should ensure that the data for this search is automatically summarized. |  |
| `auto_summarize.command` | A search template that constructs the auto summarization for this search. Caution: Advanced feature. Do not change unless you understand the architecture of auto summarization of saved searches. |  |
| `auto_summarize.cron_schedule` | Cron schedule that probes and generates the summaries for this saved search. |  |
| `auto_summarize.dispatch.earliest_time` | A time string that specifies the earliest time for summarizing this search. Can be a relative or absolute time. |  |
| `auto_summarize.dispatch.latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. |  |
| `auto_summarize.dispatch.time_format` | Time format used to specify the earliest and latest times. |  |
| `auto_summarize.dispatch.ttl` | Indicates the time to live (in seconds) for the artifacts of the summarization of the scheduled search. If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period. |  |
| `auto_summarize.max_disabled_buckets` | The maximum number of buckets with the suspended summarization before the summarization search is completely stopped, and the summarization of the search is suspended for auto_summarize.suspend_period. |  |
| `auto_summarize.max_summary_ratio` | The maximum ratio of summary_size/bucket_size, which specifies when to stop summarization and deem it unhelpful for a bucket. Note: The test is only performed if the summary size is larger than auto_summarize.max_summary_size. |  |
| `auto_summarize.max_summary_size` | The minimum summary size, in bytes, before testing whether the summarization is helpful. |  |
| `auto_summarize.max_time` | Maximum time (in seconds) that the summary search is allowed to run. Note: This is an approximate time. The summary search stops at clean bucket boundaries. |  |
| `auto_summarize.suspend_period` | Time specifier indicating when to suspend summarization of this search if the summarization is deemed unhelpful. |  |
| `auto_summarize.timespan` | The list of time ranges that each summarized chunk should span. This comprises the list of available granularity levels for which summaries would be available. For example a timechart over the last month whose granularity is at the day level should set this to 1d. If you need the same data summarized at the hour level for weekly charts, use: 1h,1d. |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if this saved search is disabled. |  |
| `dispatch.*` | * represents any custom dispatch field. |  |
| `dispatch.buckets` | The maximum nuber of timeline buckets. |  |
| `dispatch.earliest_time` | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.indexedRealtime` | Indicates whether to used indexed-realtime mode when doing real-time searches. |  |
| `dispatch.latest_time` | A time string that specifies the latest time for the saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.lookups` | Indicates if lookups are enabled for this search. |  |
| `dispatch.max_count` | The maximum number of results before finalizing the search. |  |
| `dispatch.max_time` | Indicates the maximum amount of time (in seconds) before finalizing the search. |  |
| `dispatch.reduce_freq` | Specifies how frequently the MapReduce reduce phase runs on accumulated map values. |  |
| `dispatch.rt_backfill` | Indicates whether to back fill the real time window for this search. Parameter valid only if this is a real time search |  |
| `dispatch.spawn_process` | This parameter is deprecated and will be removed in a future release. Do not use this parameter. Indicates whether a new search process spawns when this saved search is executed. |  |
| `dispatch.time_format` | Time format string that defines the time format for specifying the earliest and latest time. |  |
| `dispatch.ttl` | Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no actions are triggered. If an action is triggered, the action ttl is used. If multiple actions are triggered, the maximum ttl is applied to the artifacts. To set the action ttl, refer to alert_actions.conf.spec . If the integer is followed by the letter 'p', the ttl is interpreted as a multiple of the scheduled search period. |  |
| `displayview` | Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions. |  |
| `durable.backfill_type` | Specifies how the Splunk software backfills the lost search results of failed scheduled search jobs. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . Valid values are auto , time_interval , and time_whole . |  |
| `durable.lag_time` | Specifies the search time delay, in seconds, that a durable search uses to catch events that are ingested or indexed late. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.max_backfill_intervals` | Specifies the maximum number of cron intervals (previous scheduled search jobs) that the Splunk software can attempt to backfill for this search, when those jobs have incomplete events. Applies only to scheduled searches that have a valid setting other than none for durable.track_time_type . |  |
| `durable.track_time_type` | Indicates that a scheduled search is durable and specifies how the search tracks events. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `is_visible` | Indicates if this saved search appears in the visible saved search list. |  |
| `max_concurrent` | The maximum number of concurrent instances of this search the scheduler is allowed to run. |  |
| `next_scheduled_time` | The time when the scheduler runs this search again. |  |
| `qualifiedSearch` | The exact search string that the scheduler would run. |  |
| `realtime_schedule` | Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option. If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range. The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0). |  |
| `request.ui_dispatch_app` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `request.ui_dispatch_view` | Specifies a field used by Splunk Web to denote the view this search should be displayed in. |  |
| `restart_on_searchpeer_add` | Indicates whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Note: The peer can be a newly added peer or a peer down and now available. |  |
| `run_on_startup` | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Splunk recommends that you set run_on_startup to true for scheduled searches that populate lookup tables. |  |
| `schedule_window` | Time window (in minutes) during which the search has lower priority. The scheduler can give higher priority to more critical searches during this window. The window must be smaller than the search period. If set to auto , the scheduler prioritizes searches automatically. |  |
| `search` | Search expression to filter the response. The response matches field values against the search expression. For example: search=foo matches any object that has "foo" as a substring in a field. search=field_name%3Dfield_value restricts the match to a single field. URI-encoding is required in this example. |  |
| `vsid` | The viewstate id associated with the UI view listed in 'displayview'. Matches to a stanza in viewstates.conf. |  |

### `/services/saved/searches/{name}/acknowledge`

Acknowledge the {name} saved search alert suppression.

#### POST

Acknowledge the {name} saved search alert suppression and resume alerting.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `key` | String |  |

### `/services/saved/searches/{name}/dispatch`

Dispatch the {name} saved search.

#### POST

Dispatch the {name} saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `args.*` |  |  |
| `dispatchAs` | String | "owner" \| "user" |
| `dispatch.*` | String |  |
| `dispatch.adhoc_search_level` | String |  |
| `dispatch.now` | Boolean |  |
| `force_dispatch` | Boolean |  |
| `now` | String |  |
| `replay_speed` | Number greater than 0 |  |
| `replay_et` | Time modifier string |  |
| `replay_lt` | Time modifier string. |  |
| `trigger_actions` | Boolean |  |

### `/services/saved/searches/{name}/history`

List available search jobs created from the {name} saved search.

#### GET

List available search jobs created from the {name} saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `savedsearch` | String triplet consisting of user:app:search_name . The triplet constitutes a unique identifier for accessing saved search history. Passing in this parameter can help you work around saved search access limitations in search head clustered deployments. As an example, the following parameter triplet represents an admin user, the search app context, and a search named Splunk errors last 24 hours . CODE Copy savedsearch=admin:search:Splunk%20errors%20last%2024%20hours savedsearch=admin:search:Splunk%20errors%20last%2024%20hours |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `durableTrackTime` | The durable cursor timestamp for the search job, expressed in UNIX Epoch time notation (elapsed time since 1/1/1970). If durableTrackType=_indextime , this timestamp is associated with the indexed timestamp of the events returned by the job. If durableTrackType=_time , this timestamp is associated with the event timestamp of the events returned by the job. |  |
| `durableTrackType` | Indicates that a scheduled search is durable and specifies how the search tracks events. A value of _time means the durable search tracks each event by its event timestamp , based on time information included in the event. A value of _indextime means the durable search tracks each event by its indexed timestamp. The search is not durable if this setting is unset or is set to none . |  |
| `earliest_time` | The earliest time a search job is configured to start. |  |
| `isDone` | Indicates if the search has completed. |  |
| `isFinalized` | Indicates if the search was finalized (stopped before completion). |  |
| `isRealTimeSearch` | Indicates if the search is a real time search. |  |
| `isSaved` | Indicates if the search is saved indefinitely. |  |
| `isScheduled` | Indicates if the search is a scheduled search. |  |
| `isZombie` | Indicates if the process running the search is dead, but with the search not finished. |  |
| `latest_time` | The latest time a search job is configured to start. |  |
| `listDefaultActionArgs` | List default values of actions.*, even though some of the actions may not be specified in the saved search. |  |
| `ttl` | The time to live, or time before the search job expires after it completes. |  |

### `/services/saved/searches/{name}/reschedule`

Set {name} scheduled saved search to start at a specific time and then run on its schedule thereafter.

#### POST

Define a new start time for a scheduled saved search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `schedule_time` | Timestamp |  |

### `/services/saved/searches/{name}/scheduled_times`

Get the {name} saved search scheduled time.

#### GET

Access {name} saved search scheduled time.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time required` | String |  |
| `latest_time required` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here that is encrypted on the next platform restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.summary_index` | The state of the summary index action. |  |
| `action.summary_index._name` | Specifies the name of the summary index where the results of the scheduled search are saved. Defaults to "summary." |  |
| `actions` | Actions triggered by this alert. |  |
| `alert.digest_mode` | Indicates if alert actions are applied to the entire result set or to each individual result. |  |
| `alert.expires` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.severity` | Valid values: (1 | 2 | 3 | 4 | 5 | 6) Sets the alert severity level. Valid values are: 1 DEBUG 2 INFO 3 WARN 4 ERROR 5 SEVERE 6 FATAL |  |
| `alert.suppress` | Indicates whether alert suppression is enabled for this schedules search. |  |
| `alert.suppress.fields` | Fields to use for suppression when doing per result alerting. Required if suppression is turned on and per result alerting is enabled. |  |
| `alert.suppress.period` | Specifies the suppression period. Only valid if alert.supress is enabled. Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `alert.track` | Specifies whether to track the actions triggered by this scheduled search. auto - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions. true - force alert tracking. false - disable alert tracking for this search. |  |
| `alert_comparator` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |  |
| `alert_condition` | A conditional search that is evaluated against the results of the saved search. Defaults to an empty string. Alerts are triggered if the specified search yields a non-empty search result list. Note: If you specify an alert_condition, do not set counttype, relation, or quantity. |  |
| `alert_threshold` | Valid values are: Integer[%] Specifies the value to compare (see alert_comparator) before triggering the alert actions. If expressed as a percentage, indicates value to use when alert_comparator is set to "rises by perc" or "drops by perc." |  |
| `alert_type` | What to base the alert on, overridden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources. |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if this saved search is disabled. |  |
| `dispatch.buckets` | The maximum number of timeline buckets. |  |
| `dispatch.earliest_time` | A time string that specifies the earliest time for this search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `dispatch.lookups` | Indicates if lookups are enabled for this search. |  |
| `dispatch.max_count` | The maximum number of results before finalizing the search. |  |
| `dispatch.max_time` | Indicates the maximum amount of time (in seconds) before finalizing the search |  |
| `earliest_time` | For scheduled searches display all the scheduled times starting from this time. |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `is_visible` | Indicates if this saved search appears in the visible saved search list. |  |
| `latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `listDefaultActionArgs` | List default values of actions.*, even though some of the actions may not be specified in the saved search. |  |
| `max_concurrent` | The maximum number of concurrent instances of this search the scheduler is allowed to run. |  |
| `next_scheduled_time` | The time when the scheduler runs this search again. |  |
| `qualifiedSearch` | The exact search command for this saved search. |  |
| `realtime_schedule` | Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time. If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler load. Use continuous scheduling whenever you enable the summary index option. If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range. The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0). |  |
| `request.ui_dispatch_app` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `request.ui_dispatch_view` | A field used by Splunk Web to denote the app this search should be dispatched in. |  |
| `restart_on_searchpeer_add` | Indicates whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search. Note: The peer can be a newly added peer or a peer down and now available. |  |
| `run_on_startup` | Indicates whether this search runs on startup. If it does not run on startup, it runs at the next scheduled time. Splunk recommends that you set run_on_startup to true for scheduled searches that populate lookup tables. |  |
| `scheduled_times` | The times when the scheduler runs the search. |  |
| `search` | Search expression to filter the response. The response matches field values against the search expression. For example: search=foo matches any object that has "foo" as a substring in a field. search=field_name%3Dfield_value restricts the match to a single field. URI-encoding is required in this example. |  |
| `vsid` | The viewstate id associated with the Splunk Web view listed in 'displayview'. Matches to a stanza in viewstates.conf. |  |

### `/services/saved/searches/{name}/suppress`

Get the {name} saved search alert suppression state.

#### GET

Get the {name} saved search alert suppression state.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `expiration` | String |  |
| `key` |  |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time` | For scheduled searches display all the scheduled times starting from this time. |  |
| `expiration` | Sets the period of time to show the alert in the dashboard. Defaults to 24h. Uses [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour. |  |
| `latest_time` | A time string that specifies the latest time for this saved search. Can be a relative or absolute time. If this value is an absolute time, use the dispatch.time_format to format the value. |  |
| `listDefaultActionArgs` | List default values of actions.*, even though some of the actions may not be specified in the saved search. |  |
| `suppressed` | Indicates if alert suppression is enabled for this search. |  |
| `suppressionKey` | A combination of all the values of the suppression fields (or the combinations MD5), if fields were specified. |  |

### `/services/scheduled/views`

Access views scheduled for PDF delivery. Scheduled views are dummy noop scheduled saved searches that email a PDF of a dashboard.

#### GET

List all scheduled view objects.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.email` | Indicates the state of the email action. |  |
| `action.email.pdfview` | Name of the view to send as a PDF. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether the search results are included in the email. The results can be attached or inline. |  |
| `action.email.to` | List of recipient email addresses. Required if the email alert action is enabled. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `cron_schedule` | The cron schedule to use for delivering the view. Scheduled views are dummy/noop scheduled saved searches that email a pdf version of a view For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. |  |
| `disabled` | Indicates if the scheduled view is disabled. |  |
| `is_scheduled` | Indicates if PDF delivery of this view is scheduled. |  |
| `next_scheduled_time` | The next time when the view is delivered. |  |

### `/services/scheduled/views/{name}`

Manage the {name} scheduled view.

#### DELETE

Delete a scheduled view.

#### GET

Access a scheduled view.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.email` | Indicates the sate of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here and it is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | "BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments.< Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be externally referenced, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the global maximum number of search results to send when email.action is enabled. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled. |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies the email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if the saved search for this view is disabled. |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `next_scheduled_time` | The next time when the view is delivered. |  |

#### POST

Update a scheduled view.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action.email.to required` | String |  |
| `action.email*` | String |  |
| `cron_schedule required` | String |  |
| `disabled` | Boolean | 0 |
| `is_scheduled required` | Boolean |  |
| `next_scheduled_time` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.email` | Indicates the status of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here that is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments.< Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct an externally referencable url, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled. |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if the saved search for this view is disabled. |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `next_scheduled_time` | The next time when the view is delivered. |  |

### `/services/scheduled/views/{name}/dispatch`

Dispatch the scheduled search associated with the {name} scheduled view.

#### POST

Dispatch the scheduled search associated with the {name} scheduled view.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `args.*` | String |  |
| `dispatch.*` | String |  |
| `dispatch.now` | Boolean |  |
| `force_dispatch` | Boolean |  |
| `now` | String |  |
| `trigger_actions` | Boolean |  |

### `/services/scheduled/views/{name}/history`

List search jobs used to render the {name} scheduled view.

#### GET

List search jobs used to render the {name} scheduled view.

### `/services/scheduled/views/{name}/reschedule`

Schedule the {name} view PDF delivery.

#### POST

Schedule the {name} view PDF delivery.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `schedule_time` | String |  |

### `/services/scheduled/views/{name}/scheduled_times`

Get scheduled view times.

#### GET

Get scheduled view times.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time` | String |  |
| `latest_time` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `action.email` | Indicates the state of the email action. |  |
| `action.email.auth_password` | The password to use when authenticating with the SMTP server. Normally this value is set when editing the email settings, however you can set a clear text password here that is encrypted on the next restart. Defaults to empty string. |  |
| `action.email.auth_username` | The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string. Note: Your SMTP server might reject unauthenticated emails. |  |
| `action.email.bcc` | BCC email address to use if action.email is enabled. |  |
| `action.email.cc` | CC email address to use if action.email is enabled. |  |
| `action.email.command` | The search command (or pipeline) which is responsible for executing the action. Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$. |  |
| `action.email.format` | Specify the format of text in the email. This value also applies to any attachments.< Valid values: (plain | html | raw | csv) |  |
| `action.email.from` | Email address from which the email action originates. |  |
| `action.email.hostname` | Sets the hostname used in the web link (url) sent in email actions. This value accepts two forms: hostname (for example, splunkserver, splunkserver.example.com) protocol://hostname:port (for example, http://splunkserver:8000 , https://splunkserver.example.com:443 ) When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url. When this value begins with ' http://' , it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct a url that can be externally referenced, such as SSO environments, other proxies, or when the server hostname is not generally resolvable. Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used. |  |
| `action.email.inline` | Indicates whether the search results are contained in the body of the email. Results can be either inline or attached to an email. See action.email.sendresults. |  |
| `action.email.mailserver` | Set the address of the MTA server to be used to send the emails. Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf). |  |
| `action.email.maxresults` | Sets the maximum number of search results sent using alerts. |  |
| `action.email.maxtime` | Specifies the maximum amount of time the execution of an email action takes before the action is aborted. |  |
| `action.email.pdfview` | The name of the view to deliver if sendpdf is enabled. |  |
| `action.email.preprocess_results` | Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing). Usually the preprocessing consists of filtering out unwanted internal fields. |  |
| `action.email.reportPaperOrientation` | Specifies the paper orientation: portrait or landscape. |  |
| `action.email.reportPaperSize` | Specifies the paper size for PDFs. Defaults to letter. Valid values: (letter | legal | ledger | a2 | a3 | a4 | a5) |  |
| `action.email.reportServerEnabled` | Not supported. |  |
| `action.email.reportServerURL` | Not supported. |  |
| `action.email.sendpdf` | Indicates whether to create and send the results as a PDF. |  |
| `action.email.sendresults` | Indicates whether to attach the search results in the email. Results can be either attached or inline. See action.email.inline. |  |
| `action.email.subject` | Specifies an email subject. Defaults to SplunkAlert-<savedsearchname>. |  |
| `action.email.to` | List of recipient email addresses. Required if this search is scheduled and the email alert action is enabled. |  |
| `action.email.track_alert` | Indicates whether the execution of this action signifies a trackable alert. |  |
| `action.email.ttl` | Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows <Integer>, int is the number of scheduled periods. Defaults to 86400 (24 hours). If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf. Valid values are Integer[p]. |  |
| `action.email.use_ssl` | Indicates whether to use SSL when communicating with the SMTP server. |  |
| `action.email.use_tls` | Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls). |  |
| `action.email.width_sort_columns` | Indicates whether columns should be sorted from least wide to most wide, left to right. Only valid if format=text. |  |
| `cron_schedule` | The cron schedule to execute this search. For example: */5 * * * * causes the search to execute every 5 minutes. cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43. Splunk recommends that you schedule your searches so that they are staggered over time. This reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes. Valid values: cron string |  |
| `disabled` | Indicates if the saved search for this view is disabled. Disabled saved searches are not visible in Splunk Web. |  |
| `is_scheduled` | Indicates if this search is to be run on a schedule. |  |
| `next_scheduled_time` | The next time when the view is delivered. |  |

### `/services/search/concurrency-settings`

#### GET

List search concurrency settings.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `max_searches_perc` | Number | The maximum number of searches the scheduler can run as a percentage of the maximum number of concurrent searches. Default: 50%. |
| `auto_summary_perc` | Number | The maximum number of concurrent searches to be allocated for auto summarization, as a percentage of the concurrent searches that the scheduler can run. Default: 50. |
| `max_searches_per_cpu` | Number | The maximum number of concurrent historical searches allowed per cpu. Default: 1. |
| `base_max_searches` | Number | A baseline constant to add to the max number of searches (computed as multiplier of the CPUs.) Default is 6. |
| `max_rt_search_multiplier` | Number | A number by which the maximum number of historical searches is multiplied to determine the maximum number of concurrent real-time searches. Note: The maximum number of real-time searches is computed as max_rt_searches = max_rt_search_multiplier x max_hist_searches |

### `/services/search/concurrency-settings/scheduler`

Edit settings that determine concurrent scheduled search limits.

#### POST

Edit settings that determine concurrent scheduled search limits.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `max_searches_perc` | Number | The maximum number of searches the scheduler can run as a percentage of the maximum number of concurrent searches. Default: 50. |
| `auto_summary_perc` | Number | The maximum number of concurrent searches to be allocated for auto summarization, as a percentage of the concurrent searches that the scheduler can run. Default: 50. |

### `/services/search/concurrency-settings/search`

Edit settings that determine the maximum number of concurrent scheduled searches.

#### POST

Edit settings that determine the maximum number of concurrent scheduled searches.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `max_searches_per_cpu` | Number | The maximum number of concurrent historical searches allowed per cpu. Default: 1. |
| `base_max_searches` | Number | A baseline constant to add to the max number of searches (computed as multiplier of the CPUs.) Default is 6. |
| `max_rt_search_multiplier` | Number | A number by which the maximum number of historical searches is multiplied to determine the maximum number of concurrent real-time searches. Note: The maximum number of real-time searches is computed as max_rt_searches = max_rt_search_multiplier x max_hist_searches |

### `/services/search/jobs`

List search jobs.

#### GET

Get details of all current searches.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cursorTime` | The earliest time from which no events are later scanned. Can be used to indicate progress. See description for doneProgress . |  |
| `custom` | Custom job property. (See the search/jobs POST request for an example of how to create a custom property.) Note: Filtering for custom search jobs fails in a search head cluster environment. Remove the ?search=custom filter to see all search jobs including custom jobs. |  |
| `delegate` | For saved searches, specifies jobs that were started by the user. Defaults to scheduler. |  |
| `diskUsage` | The total amount of disk space used, in bytes. |  |
| `dispatchState` | The state of the search. Can be any of QUEUED, PARSING, RUNNING, FINALIZING, PAUSE, INTERNAL_CANCEL, USER_CANCEL, BAD_INPUT_CANCEL, QUIT, FINALIZING, FAILED, DONE. |  |
| `doneProgress` | A number between 0 and 1.0 that indicates the approximate progress of the search. doneProgress = (latestTime – cursorTime) / (latestTime – earliestTime) |  |
| `dropCount` | For real-time searches only, the number of possible events that were dropped due to the rt_queue_size (default to 100000). |  |
| `earliestTime` | A time string that sets the earliest (inclusive), respectively, time bounds for the search. Can be used to indicate progress. See description for doneProgress . |  |
| `eventAvailableCount` | The number of events that are available for export. |  |
| `eventCount` | The number of events returned by the search. |  |
| `eventFieldCount` | The number of fields found in the search results. |  |
| `eventIsStreaming` | Indicates if the events of this search are being streamed. |  |
| `eventIsTruncated` | Indicates if events of the search are not stored, making them unavailable from the events endpoint for the search. |  |
| `eventPreviewableCount` | Number of in-memory events that are not yet committed to disk. Returned if timeline_events_preview is enabled in limits.conf . |  |
| `eventSearch` | Subset of the entire search that is before any transforming commands. The timeline and events endpoint represents the result of this part of the search. |  |
| `eventSorting` | Indicates if the events of this search are sorted, and in which order. asc = ascending; desc = descending; none = not sorted |  |
| `isDone` | Indicates if the search has completed. |  |
| `isEventPreviewEnabled` | Indicates if the timeline_events_preview setting is enabled in limits.conf . |  |
| `isFailed` | Indicates if there was a fatal error executing the search. For example, invalid search string syntax. |  |
| `isFinalized` | Indicates if the search was finalized (stopped before completion). |  |
| `isPaused` | Indicates if the search is paused. |  |
| `isPreviewEnabled` | Indicates if previews are enabled. |  |
| `isRealTimeSearch` | Indicates if the search is a real time search. |  |
| `isRemoteTimeline` | Indicates if the remote timeline feature is enabled. |  |
| `isSaved` | Indicates that the search job is saved, storing search artifacts on disk for 7 days from the last time that the job was viewed or touched. Add or edit the default_save_ttl value in limits.conf to override the default value of 7 days. |  |
| `isSavedSearch` | Indicates if this is a saved search run using the scheduler. |  |
| `isZombie` | Indicates if the process running the search is dead, but with the search not finished. |  |
| `keywords` | All positive keywords used by this search. A positive keyword is a keyword that is not in a NOT clause. |  |
| `label` | Custom name created for this search. |  |
| `latestTime` | A time string that sets the latest (exclusive), respectively, time bounds for the search. Can be used to indicate progress. See description for doneProgress . |  |
| `messages` | Errors and debug messages. |  |
| `numPreviews` | Number of previews generated so far for this search job. |  |
| `performance` | A representation of the execution costs. |  |
| `priority` | An integer between 0-10 that indicates the search priority. The priority is mapped to the OS process priority. The higher the number the higher the priority. The priority can be changed using action parameter for POST search/jobs/{search_id}/control. For example, for the action parameter, specify priority=5 . Note: In *nix systems, non-privileged users can only reduce the priority of a process. |  |
| `remoteSearch` | The search string that is sent to every search peer. |  |
| `reportSearch` | If reporting commands are used, the reporting search. |  |
| `request` | GET arguments that the search sends to splunkd. |  |
| `resultCount` | The total number of results returned by the search. In other words, this is the subset of scanned events (represented by the scanCount) that actually matches the search terms. |  |
| `resultIsStreaming` | Indicates if the final results of the search are available using streaming (for example, no transforming operations). |  |
| `resultPreviewCount` | The number of result rows in the latest preview results. |  |
| `runDuration` | Time in seconds that the search took to complete. |  |
| `scanCount` | The number of events that are scanned or read off disk. |  |
| `searchEarliestTime` | Specifies the earliest time for a search, as specified in the search command rather than the earliestTime parameter. It does not snap to the indexed data time bounds for all-time searches (something that earliestTime/latestTime does). |  |
| `searchLatestTime` | Specifies the latest time for a search, as specified in the search command rather than the latestTime parameter. It does not snap to the indexed data time bounds for all-time searches (something that earliestTime/latestTime does). |  |
| `searchProviders` | A list of all the search peers that were contacted. |  |
| `sid` | The search ID number. |  |
| `statusBuckets` | Maximum number of timeline buckets. |  |
| `ttl` | The time to live, or time before the search job expires after it completes. |  |

#### POST

Start a new search and return the search ID (<sid>)

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `adhoc_search_level` | String |  |
| `allow_partial_results` | Boolean | true |
| `auto_cancel` | Number | 0 |
| `auto_finalize_ec` | Number | 0 |
| `auto_pause` | Number | 0 |
| `custom` | String |  |
| `earliest_time` | String |  |
| `enable_lookups` | Boolean | true |
| `exec_mode` | Enum | normal |
| `force_bundle_replication` | Boolean | false |
| `id` | String |  |
| `index_earliest` | String |  |
| `index_latest` | String |  |
| `indexedRealtime` | Boolean |  |
| `indexedRealtimeOffset` | Number |  |
| `latest_time` | String |  |
| `max_count` | Number | 10000 |
| `max_time` | Number | 0 |
| `namespace` | String |  |
| `now` | String | current system time |
| `reduce_freq` | Number | 0 |
| `reload_macros` | Boolean | true |
| `remote_server_list` | String | empty list |
| `replay_speed` | Number greater than 0 |  |
| `replay_et` | Time modifier string |  |
| `replay_lt` | Time modifier string. |  |
| `required_field_list` | String | empty list |
| `reuse_max_seconds_ago` | Number |  |
| `rf` | String |  |
| `rt_blocking` | Boolean | false |
| `rt_indexfilter` | Boolean | true |
| `rt_maxblocksecs` | Number | 60 |
| `rt_queue_size` | Number | 10000 events |
| `search required` | String |  |
| `search_listener` | String |  |
| `search_mode` | Enum | normal |
| `spawn_process` | Boolean | true |
| `status_buckets` | Number | 0 |
| `sync_bundle_replication` | Boolean |  |
| `time_format` | String | %FT%T.%Q%:z |
| `timeout` | Number | 86400 |
| `workload_pool` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `sid` | Search ID |  |

### `/services/search/v2/jobs/export`

Stream search results as they become available.

#### POST

Performs a search identical to POST search/jobs. For parameter and returned value descriptions, see the POST parameter descriptions for search/jobs .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `search` | String |  |
| `auto_cancel` | Number |  |
| `auto_finalize_ec` | Number |  |
| `auto_pause` | Number |  |
| `earliest_time` | String |  |
| `enable_lookups` | Bool |  |
| `force_bundle_replication` | Bool |  |
| `id` | String |  |
| `index_earliest` | String |  |
| `index_latest` | String |  |
| `latest_time` | String |  |
| `max_time` | Number |  |
| `namespace` | String |  |
| `now` | String |  |
| `output_mode` | Enum | xml |
| `reduce_freq` | Number |  |
| `reload_macros` | Bool |  |
| `remote_server_list` | String |  |
| `required_field_list` | String |  |
| `rf` | String |  |
| `rt_blocking` | Bool |  |
| `rt_indexfilter` | Bool |  |
| `rt_maxblocksecs` | Number |  |
| `rt_queue_size` | Number |  |
| `search_listener` | String |  |
| `search_mode` | Enum |  |
| `sync_bundle_replication` | Bool |  |
| `time_format` | String |  |
| `timeout` | Number |  |

### `/services/search/jobs/export (deprecated and disabled)`

Stream search results as they become available.

#### GET

Performs a search identical to POST search/jobs

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `auto_cancel` | Number |  |
| `auto_finalize_ec` | Number |  |
| `auto_pause` | Number |  |
| `earliest_time` | String |  |
| `enable_lookups` | Bool |  |
| `force_bundle_replication` | Bool |  |
| `id` | String |  |
| `index_earliest` | String |  |
| `index_latest` | String |  |
| `latest_time` | String |  |
| `max_time` | Number |  |
| `namespace` | String |  |
| `now` | String |  |
| `output_mode` | Enum | xml |
| `reduce_freq` | Number |  |
| `reload_macros` | Bool |  |
| `remote_server_list` | String |  |
| `required_field_list` | String |  |
| `rf` | String |  |
| `rt_blocking` | Bool |  |
| `rt_indexfilter` | Bool |  |
| `rt_maxblocksecs` | Number |  |
| `rt_queue_size` | Number |  |
| `search required` | String |  |
| `search_listener` | String |  |
| `search_mode` | Enum |  |
| `sync_bundle_replication` | Bool |  |
| `time_format` | String |  |
| `timeout` | Number |  |

#### POST

Performs a search identical to POST search/jobs. For parameter and returned value descriptions, see the POST parameter descriptions for search/jobs .

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `search` | String |  |
| `auto_cancel` | Number |  |
| `auto_finalize_ec` | Number |  |
| `auto_pause` | Number |  |
| `earliest_time` | String |  |
| `enable_lookups` | Bool |  |
| `force_bundle_replication` | Bool |  |
| `id` | String |  |
| `index_earliest` | String |  |
| `index_latest` | String |  |
| `latest_time` | String |  |
| `max_time` | Number |  |
| `namespace` | String |  |
| `now` | String |  |
| `output_mode` | Enum | xml |
| `reduce_freq` | Number |  |
| `reload_macros` | Bool |  |
| `remote_server_list` | String |  |
| `required_field_list` | String |  |
| `rf` | String |  |
| `rt_blocking` | Bool |  |
| `rt_indexfilter` | Bool |  |
| `rt_maxblocksecs` | Number |  |
| `rt_queue_size` | Number |  |
| `search_listener` | String |  |
| `search_mode` | Enum |  |
| `sync_bundle_replication` | Bool |  |
| `time_format` | String |  |
| `timeout` | Number |  |

### `/services/search/jobs/{search_id}`

Manage the {search_id} search job.

#### DELETE

Delete the {search_id} search job.

#### GET

Get information about the {search_id} search job.

#### POST

Update the {search_id} search job.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `custom.* required` | String |  |

### `/services/search/jobs/{search_id}/control`

Run a job control command for the {search_id} search.

#### POST

Run a job control command for the {search_id} search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `action required` | Enum |  |

### `/services/search/v2/jobs/{search_id}/events`

Access {search_id} search events.

#### GET

Get {search_id} search events.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count` | Number | 100 |
| `earliest_time` | String |  |
| `f` | String |  |
| `field_list` | String | * |
| `latest_time` | String |  |
| `max_lines` | Number | 0 |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `output_time_format` | String | time_format |
| `segmentation` | String | raw |
| `time_format` | String | %m/%d/%Y:%H:%M:%S |
| `truncation_mode` | Enum | abstract |

#### POST

Access {search_id} search events.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count` | Number | 100 |
| `earliest_time` | String |  |
| `f` | String |  |
| `field_list` | String | * |
| `latest_time` | String |  |
| `max_lines` | Number | 0 |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `output_time_format` | String | time_format |
| `search` | String |  |
| `segmentation` | String | raw |
| `time_format` | String | %m/%d/%Y:%H:%M:%S |
| `truncation_mode` | Enum | abstract |

### `/services/search/jobs/{search_id}/events (deprecated and disabled)`

Get {search_id} search events.

#### GET

Access {search_id} search events.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count` | Number | 100 |
| `earliest_time` | String |  |
| `f` | String |  |
| `field_list` | String | * |
| `latest_time` | String |  |
| `max_lines` | Number | 0 |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `output_time_format` | String | time_format |
| `search` | String |  |
| `segmentation` | String | raw |
| `time_format` | String | %m/%d/%Y:%H:%M:%S |
| `truncation_mode` | Enum | abstract |

### `/services/search/v2/jobs/{search_id}/results`

Access {search_id} search results.

#### GET

Get {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |

#### POST

Access {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `search` | String |  |

### `/services/search/jobs/{search_id}/results (deprecated and disabled)`

Get {search_id} search results.

#### GET

Get {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `search` | String |  |

### `/services/search/v2/jobs/{search_id}/results_preview`

Preview {search_id} search results.

#### GET

Preview {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |

#### POST

Access a preview of {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `search` | String |  |

### `/services/search/jobs/{search_id}/results_preview (deprecated and disabled)`

Preview {search_id} search results.

#### GET

Preview {search_id} search results.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `add_summary_to_metadata` | Boolean | false |
| `count` | Number | 100 |
| `f` | String |  |
| `field_list` | String |  |
| `offset` | Number | 0 |
| `output_mode` | Enum | xml |
| `search` | String |  |

### `/services/search/jobs/{search_id}/search.log`

Get the {search_id} search log.

#### GET

Get the {search_id} search log.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `attachment` | Boolean | false |

### `/services/search/jobs/{search_id}/summary`

Get the getFieldsAndStats output of the events to-date, for the search_id search.

#### GET

Get the getFieldsAndStats output of the events to-date, for the search_id search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `earliest_time` | String |  |
| `f` | String |  |
| `field_list` | String |  |
| `histogram` | Boolean | false |
| `latest_time` | String |  |
| `min_freq` | Number | 0 |
| `output_time_format` | String | time_format |
| `search` | String | Empty string |
| `time_format` | String | %m/%d/%Y:%H:%M:%S |
| `top_count` | Number | 10 |

### `/services/search/jobs/{search_id}/timeline`

Get event distribution over time of the untransformed events read to-date, for the search_id search.

#### GET

Get event distribution over time of the untransformed events read to-date, for the search_id search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `output_time_format` | String | time_format |
| `time_format` | String | %m/%d/%Y:%H:%M:%S |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `c` | Event count |  |
| `a` | Available. Not all events in a bucket are retrievable. Generally capped at 10000. |  |
| `t` | Time in epoch seconds |  |
| `d` | Bucket size (time) |  |
| `f` | Indicates if the search finished scanning events from the time range of this bucket. |  |
| `etz` | Timezone offset, in seconds, for the earliest time of this bucket. etz and ltz are different if the buckets are months or days and you have a DST change during the middle. |  |
| `ltz` | Timezone offset, in seconds, for the latest time of this bucket. |  |

### `/services/search/v2/parser`

Access search language parsing.

#### POST

Parses Splunk search language and returns semantic map.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `enable_lookups` | Boolean | false |
| `output_mode` | String | xml |
| `parse_only` | Boolean | false |
| `q required` | String |  |
| `reload_macros` | Boolean | true |

### `/services/search/parser (deprecated and disabled)`

Get search language parsing.

#### GET

Parses Splunk search language and returns semantic map.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `enable_lookups` | Boolean | false |
| `output_mode` | String | xml |
| `parse_only` | Boolean | false |
| `q required` | String |  |
| `reload_macros` | Boolean | true |

### `/services/search/scheduler`

#### GET

Get current search scheduler enablement status.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `saved_searches_disabled` | Boolean | 0 or 1 |

### `/services/search/scheduler/status`

Enable or disable the search scheduler.

#### POST

Enable or disable the search scheduler.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `disabled` | Boolean |  |

### `/services/search/timeparser`

Get time argument parsing.

#### GET

Get a lookup table of time arguments to absolute timestamps.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `now` | String |  |
| `output_time_format` | String | %FT%T.%Q%:z |
| `time required` | String |  |
| `time_format` | String | %FT%T.%Q%:z |

### `/services/search/typeahead`

Get search string auto-complete suggestions.

#### GET

Get a list of words or descriptions for possible auto-complete terms.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `count required` | Number |  |
| `max_servers` | Number | 2 |
| `output_mode` | String | csv |
| `prefix required` | String |  |

### `/services/services/orchestrator/v1/datasets`

Return information about SPL2-supported datasets. For more information, see Datasets in the SPL2 Search Manual .

#### GET

Return information about datasets that you have access to. For views, you must have execute permission on the SPL2 module associated with the view.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `results` | An array of objects with the same content as GET. The datasetid appears in the name. |  |
| `nextLink` | The link to the next page of results. |  |
| `totalCount` | The total number of elements that match the requested filters. Might be larger than the length of the results, if pagination is applied. |  |

### `/services/Services/orchestrator/v1/datasets/{datasetid}`

Provides information about a specific dataset , based on the dataset ID.

#### GET

Returns information about a dataset. The response depends on the kind of dataset.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `datasetid` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `id` | The dataset ID. |  |
| `owner` | User ID of the user that created the dataset. |  |
| `created` | Deprecated. The date and time object was created. The 'created' parameter is deprecated as of version v1. Although this parameter continues to function, it might be removed in a future version. Use the createdAt parameter instead. |  |
| `createdAt` | The date and time object was created. |  |
| `modified` | Deprecated. The date and time object was modified. The 'modified' parameter is deprecated as of version v1. Although this parameter continues to function, it might be removed in a future version. Use the updatedAt parameter instead. |  |
| `updatedAt` | The date and time dataset was updated. |  |
| `createdby` | Deprecated. The name of the user who created the object. This value is obtained from user credentials and may not be changed. Deprecated due to non-standard platform casing. Use the createdBy parameter instead. |  |
| `createdBy` | The user ID of the user who created the object. This value is obtained from user credentials and may not be changed. |  |
| `module` | The name of the module that the dataset belongs to. Currently only supported for the view dataset kind. Example: my_module |  |
| `modifiedby` | Deprecated. The name of the user who most recently modified the object. Deprecated due to non-standard platform naming. Use the updatedBy parameter instead. |  |
| `updatedBy` | The name of the user who most recently modified the object. |  |
| `resourcename` | Deprecated. The dataset name qualified by the module name. Deprecated due to non-standard platform casing. Use the resourceName parameter instead. |  |
| `resourceName` | The dataset name qualified by the module name. |  |
| `appclientidcreatedby` | Deprecated. The AppClientId of the creator app of the dataset. Deprecated due to non-standard platform casing. Use the appClientIdCreatedBy parameter instead. |  |
| `appclientidmodifiedby` | Deprecated. The AppClientId of the modifier app of the dataset. Deprecated due to non-standard platform casing. Use the appClientIdUpdatedBy parameter instead. |  |
| `appClientIdCreatedBy` | The AppClientId of the creator app of the dataset. |  |
| `appClientIdUpdatedBy` | The AppClientId of the modifier app of the dataset. |  |
| `kind` | The kind of dataset, such as index, lookup, savedsearch, or view. Example: index |  |
| `namespace` | The name of the namespace that contains the dataset. |  |
| `title` | The title of the dataset. Does not have to be unique. |  |
| `summary` | A summary of the dataset's purpose. |  |
| `awsRegion` | AWS Region, for example: us-east-2. Returned for the following dataset kinds: awss3 |  |
| `bucket` | The S3 bucket name. Returned for the following dataset kinds: awss3 |  |
| `bucketKey` | The S3 bucket key. Returned for the following dataset kinds: awss3 |  |
| `filePrefix` | The prefix for the log files. Max 100 characters. Returned for the following dataset kinds: awss3 |  |
| `dataFormat` | The data format for the log files. Returned for the following dataset kinds: awss3 |  |
| `compressionType` | Compression type for the data format. Optional for backward compatibility. Returned for the following dataset kinds: awss3 |  |
| `sendBatchSize` | Optional parameter that controls the number of logs that will be accumulated before the file in S3 is created. integer Returned for the following dataset kinds: awss3 |  |
| `registerRuntimes` | The runtimes for the datasets. Returned for the following dataset kinds: awss3 |  |
| `s3authentication.awsAccessKeyId` | The AWS Access KEY ID. Returned for the following dataset kinds: awss3 |  |
| `s3authentication.awsSecretAccessKey` | The AWS Secret Access KEY. Returned for the following dataset kinds: awss3 |  |
| `s3authentication.awsSecretAccessKeyPath` | The paths used by Vault for the AWS Secret Access KEY. Returned for the following dataset kinds: awss3 |  |
| `externalKind` | The type of the external lookup. Returned for the following dataset kinds: lookup |  |
| `externalName` | The name of the external lookup. Returned for the following dataset kinds: lookup |  |
| `caseSensitiveMatch` | Match case-sensitivity against the lookup. Returned for the following dataset kinds: lookup |  |
| `filter` | A search that filters the results out of the lookup before those results are returned. Returned for the following dataset kinds: lookup savedSearch |  |
| `disabled` | Specifies whether or not the Splunk index is disabled. Returned for the following dataset kinds: index |  |
| `frozenTimePeriodInSecs` | The number of seconds after which indexed data rolls to frozen. Freezing data means it is removed from the index. Returned for the following dataset kinds: index metric |  |
| `endpoint` | The Splunk HEC destination endpoint to send data to. Returned for the following dataset kinds: hecexporter |  |
| `caCertificate` | The CA certificate used to verify server identity during the TLS handshake. Returned for the following dataset kinds: hecexporter |  |
| `clientCertificate` | The client certificate presented during TLS handshake. Returned for the following dataset kinds: hecexporter |  |
| `skipTLSVerification` | Where to skip TLS verification, whether or not TLS files are provided. Returned for the following dataset kinds: hecexporter |  |
| `index` | The index where the incoming events should be indexed in. Returned for the following dataset kinds: hecexporter |  |
| `source` | The source that identifies the incoming data. Returned for the following dataset kinds: hecexporter |  |
| `sourcetype` | The source type of the incoming data. Returned for the following dataset kinds: hecexporter |  |

### `/services/services/orchestrator/v1/spl2/convert`

Converts an SPL search to SPL2.

#### POST

Converts a single SPL search into an SPL2 search.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `spl1` | String |  |
| `runtime` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `spl2` | The converted search. |  |
| `messages` | One or more text messages might be returned in the response. |  |

### `/services/services/orchestrator/v1/spl2/module/dispatch`

Dispatch a module that contains one or more SPL2 statements. For more information about what constitutes an SPL2 statement, see Modules and SPL2 statements in the SPL2 Search Manual .

#### POST

Start one or more new searches and return a search ID (SID) for each named search statement.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `module` | String |  |
| `namespace` | String |  |
| `queryParameters` | String |  |
| `queryName` | String |  |
| `earliest` | String | -24h@h |
| `latest` | String | now |
| `timezone` | String | Current system timezone |
| `relativeTimeAnchor` | String | The time the search job is created |
| `collectEventSummary` | Boolean | False |
| `collectFieldSummary` | Boolean | False |
| `collectTimeBuckets` | Boolean | False |
| `adhocSearchLevel` | String | fast |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `sid` | Search ID. |  |

### `/services/services/orchestrator/v1/spl2/modules/permissions`

Access a list of role-based permissions for a module. Requires the edit_spl2_module_permissions capability.

#### GET

Retrieve all of the permissions for a module.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `resourceName` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `operation` | Array |  |
| `resourceName` | String |  |
| `resourceType` | String |  |
| `role` | String |  |

#### PUT

Update permissions for a module. You must specify the existing permissions and any new or changed permissions.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `resourceType` | String |  |
| `resourceName` | String |  |
| `permissions` | JSON array |  |

### `/services/services/orchestrator/v1/spl2/modules/{resourceName}`

Return information about a module, or create, update, or delete an SPL2 module.

#### GET

Retrieves information about a specific module.

#### PUT

Create or update a module in a specific namespace.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `namespace` | String |  |
| `definition` | String |  |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `415` | Unsupported media type. The type must be application/json . |  |

#### DELETE

Delete a module in a specific application. Specify the namespace and the module name.

---

## System

### `/services/server/control`

#### GET

List actions that can be performed at this endpoint.

### `/services/server/control/restart`

Restart the splunkd server daemon and Splunk Web interface. The POST operation is equivalent to the splunk restart CLI command.

#### POST

Restart the splunkd server daemon and Splunk Web interface.

### `/services/server/control/restart_webui`

#### POST

Restart the Splunk Web interface.

### `/services/server/httpsettings/proxysettings`

Create an HTTP Proxy Server configuration for splunkd.

#### POST

Create a HTTP Proxy server configuration stanza for use with splunkd.

### `/services/server/httpsettings/proxysettings/proxyConfig`

Access, update, or delete the HTTP Proxy Server configurations for splunkd including http_proxy , https_proxy and no_proxy .

#### GET

Access the {proxyConfig} HTTP proxy server configurations for splunkd.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `http_proxy` | String | Identifies the server proxy. When set, splunkd sends all HTTP requests through the proxy server defined in http_proxy on the proxy. The default value is unset. |
| `https_proxy` | String | Identifies the server proxy. When set, splunkd sends all HTTPS requests through the proxy server defined in https_proxy . If not set, splunkd uses the http_proxy variable instead. The default value is unset. |
| `no_proxy` | String | Identifies the no proxy rules. When set, splunkd uses these rules to decide whether the proxy server needs to be bypassed for matching hosts and IP addresses. Requests going to a localhost/loopback address are not proxied. The default value is localhost, 127.0.0.1, ::1 . |

#### POST

Update the {proxyConfig} HTTP proxy server configurations for splunkd.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `http_proxy` | String | Identifies the server proxy. When set, splunkd sends all HTTP requests through the proxy server defined in http_proxy on the proxy. The default value is unset. |
| `https_proxy` | String | Identifies the server proxy. When set, splunkd sends all HTTPS requests through the proxy server defined in https_proxy . If not set, splunkd uses the http_proxy variable instead. The default value is unset. |
| `no_proxy` | String | Identifies the no proxy rules. When set, splunkd uses these rules to decide whether the proxy server needs to be bypassed for matching hosts and IP addresses. Requests going to a localhost/loopback address are not proxied. The default value is localhost, 127.0.0.1, ::1 . |

#### DELETE

Delete the {proxyConfig} HTTP proxy server configurations for splunkd.

### `/services/server/logger`

#### GET

Enumerate splunkd logging categories.

### `/services/server/logger/{name}`

#### GET

Access information about the specified splunkd logging category.

#### POST

Set the logging level for a specific logging category.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `level` | Enum | Required . The desired logging level for this category. One of the following valid values. [FATAL \| WARN \| INFO \| DEBUG] |

### `/services/server/roles`

#### GET

Access the roles applicable to this server.

### `/services/server/security/rotate-splunk-secret`

Rotates the splunk.secret file on a standalone Splunk Enterprise instance.

#### POST

Rotates the splunk.secret file on a standalone Splunk Enterprise instance.

### `/services/server/settings`

#### GET

Returns server configuration for a Splunk deployment.

---

## Workload Management

### `/services/workloads/categories`

List and edit workload categories.

#### GET

List information about workload categories.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cpu_weight` | Number | Specifies the fraction of the cpu assigned to this category as a ratio of the total of cpu_weight across all categories. This fraction is then applied to the cpu shares assigned to the parent group. The value must be > 0 and <= 100. |
| `mem_weight` | Number | Specifies the percentage of memory assigned to this category as a percent of the parent group. The total amount of memory limit for this category is a percentage of the value assigned to the parent group. The value must be > 0 and <= 100. |

#### POST

Edit workload categories.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `cpu_weight` | Number | Specifies the fraction of the cpu assigned to this category as a ratio of the total of cpu_weight across all categories. This fraction is then applied to the cpu shares assigned to the parent group. The value must be > 0 and <= 100 |
| `mem_weight` | Number | Specifies the percentage of memory assigned to this pool as a percent of the parent group. The total amount of memory limit for this pool is a percentage of the value assigned to the parent group. The value must be > 0 and <= 100. |

### `/services/workloads/pools`

Perform CRUD operations on workload pools.

#### GET

List information about workload pools.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `cpu_weight` | Number | Specifies the fraction of the cpu assigned to this pool as a ratio of the total of cpu_weight across all pools in a category. This fraction is then applied to the cpu shares assigned to the category. |
| `mem_weight` | Number | Specifies the amount of memory assigned to this pool as a percent of the value assigned to the category. |
| `category` | string | Specifies the category in which a poll is created. Can be either "search", "ingest", or "misc". |
| `default_category_pool` | Boolean | Specifies the workload pool marked as default pool for its category. This property is defined per workload_pool stanza. Default is 0. |
| `default_pool` | Boolean | Specifies a workload pool defined in the search category as the default pool for the search category. Note: deprecated parameter retained for backwards compatibility with 7.2.x |
| `ingest_pool` | Boolean | Specifies a workload-pool defined in the ingest category as the default pool for the ingest category. Note: deprecated parameter retained for backwards compatibility with 7.2.x |

#### POST

Create and configure workload pools.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `cpu_weight` | Number | Specifies the fraction of the cpu assigned to this pool as a ratio of the total of cpu_weight across all pools. This fraction is then applied to the cpu shares assigned to the parent group. |
| `mem_weight` | Number | You must set this value to 100 to avoid OOM errors. |
| `category` | string | Specifies the category in which a poll is created. Can be either "search", "ingest", or "misc". |
| `default_category_pool` | Boolean | Specifies the workload pool marked as default pool for its category. This property is defined per workload_pool stanza. Default is 0. |
| `default_pool` | Boolean | Specifies a workload pool defined in the search category as the default pool for the search category. Note: deprecated parameter retained for backwards compatibility with 7.2.x |
| `ingest_pool` | Boolean | Specifies a workload-pool defined in the ingest category as the default pool for the ingest category. Note: deprecated parameter retained for backwards compatibility with 7.2.x |

### `/services/workloads/rules`

Perform CRUD operations on workload rules and admission rules.

#### GET

List information about workload rules and admission rules.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `workload_rule_type` | String | Specifies the rule type. Supported values are: search_filter : returns admission rules only. all : returns both admission rules and workload rules. Note: To list workload rule information only, specify the endpoint URI with optional rule_name , for example services/workloads/rules/rule_name . |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `predicate` | String | Specifies the predicate (condition) that a search must meet for the specified action to be taken. |
| `action` | String | Specifies the action taken when a search meets the predicate (condition). |
| `workload_pool` | String | Specifies the workload pool associated with the workload rule. |
| `order` | Boolean | Specifies the evaluation order for this workload rule amongst a group of workload rules. |

#### POST

Create and configure, or enable/disable a workload rule or an admission rule.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `predicate` | String | Specifies a predicate (condition) that must be true for a search to gain access to the workload pool. The syntax is <type>=<value>, with optional AND, OR, NOT, (). For example, app=search AND role=power maps all searches belonging to both the Search app and the power role to the designated workload pool. Valid predicate <type> are app , role , index , user , search_type , search_mode , search_time_range , and runtime . For valid predicate type values, see Predicate type values in the Workload Management manual. You can only specify one predicate for each workload rule. Multiple predicates are not supported. |
| `action` | String | For workload rules: Specifies the action taken when a search meets the specified predicate (condition). Supported actions are alert , move and abort . For admission rules: You must specify filter as the action. |
| `workload_pool` | String | Specifies the workload pool associated with the workload rule. Specifies the destination workload pool for the move action. |
| `order` | Number | Specifies the evaluation order for this workload rule amongst a group of workload rules. For newly created rules, the order cannot be specified. It can only be specified for existing rules. |
| `workload_rule_type` | String | Supported value: search_filter . You must specify this parameter to enable or disable an admission rule. |

#### DELETE

Delete workload rules and admission rules.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `workload_rule_type` | String | Specifies the rule to delete is an admission rule. Supported value: search_filter . |

### `/services/workloads/config/enable`

Enable workload management.

#### POST

Enable workload management

### `/services/workloads/config/disable`

Endpoint to disable workload management.

#### POST

Disable workload management

### `/services/workloads/config/get-base-dirname`

Get the name of the splunk parent cgroup.

#### GET

Get the name of the splunk parent cgroup.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `workload_pool_base_dir_name` | String | Specifies the parent level cgroup for splunk. Note: This setting applies only to systems running non-systemd setups. With systemd, this setting is ignored. |

### `/services/workloads/config/preflight-checks`

Run Linux preflight checks for workload management.

#### GET

Run Linux preflight checks for workload management.

### `/services/workloads/config/set-base-dirname`

Set the name of the splunk parent cgroup.

#### POST

Set the name of the splunk parent cgroup.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `workload_pool_base_dir_name` | String | Specifies the parent level cgroup for splunk. Note: This setting applies only to systems running non-systemd setups. With systemd, this setting is ignored. |

### `/services/workloads/policy/search_admission_control`

Enable or disable admission rules.

#### GET

List the enabled status of admission rules.

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `admission_rules_enabled` | Boolean | Specifies the enabled status of admission rules. 0 (disabled) or 1 (enabled). |

#### POST

Enable or disable admission rules.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `admission_rules_enabled` | Boolean | Enable or disable admission rules. 0 (disabled) or 1 (enabled). |

### `/services/workloads/status`

Get information on the current status of workload management.

#### GET

Get information on the current status of workload management.

**Request parameters**

| Name | Type | Description |
|------|------|-------------|
| `advanced` | Boolean | advanced=1 returns dispatch time for each process running in each search pool. |

**Returned values**

| Name | Type | Description |
|------|------|-------------|
| `default_pool` | String | Specifies the workload pool marked as the default pool. |
| `ingest_pool` | Number | Specifies the workload pool marked as the ingest pool. |
| `error_message` | String | Displays the last error message observed while trying to enable workload management. This message is reset to empty on each successful enablement of workload management. |
| `enabled` | Boolean | Specifies whether or not workload management is enabled. |
| `isSupported` | Boolean | Specifies whether or not workload management is supported on this machine. |
| `os_build` | String | Specifies the operating system build information. |
| `os_extended_name` | String | Specifies the extended name of the underlying operating system. |
| `os_name` | String | Specifies the name of the underlying operating system. |
| `os_version` | String | Specifies the operating system version. |

