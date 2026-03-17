# Evaluation Functions - Informational

Category: **Evaluation - Informational**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `isarray` | `isarray(<value>)` | This function takes one argument and evaluates whether the value is an array data type. The function returns TRUE if the value is an array. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title2) |
| `isbool` | `isbool(<value>)` | This function takes one argument and evaluates whether the value is a Boolean data type. The function returns TRUE if the value is Boolean. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title3) |
| `isdouble` | `isdouble(<value>)` | This function takes one argument and evaluates whether the value is a double data type. The function returns TRUE if the value is a double value. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title4) |
| `isint` | `isint(<value>)` | This function takes one argument and returns TRUE if the value is an integer. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title5) |
| `ismv` | `ismv(<value>)` | This function takes one argument and evaluates whether the field is a multivalue data type. The function returns TRUE if the field is a multivalue. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title6) |
| `isnotnull` | `isnotnull(<value>)` | This function takes one argument and returns TRUE if the value is not NULL. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title7) |
| `isnull` | `isnull(<value>)` | This function takes one argument and returns TRUE if the value is NULL.. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title8) |
| `isnum` | `isnum(<value>)` | This function takes one argument and returns TRUE if the value is a number. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title9) |
| `isobject` | `isobject(<value>)` | This function takes one argument and evaluates whether the value is an object. The function returns TRUE if a string is a valid JSON object. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title10) |
| `isstr` | `isstr(<value>)` | This function takes one argument and returns TRUE if the value is a string. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title11) |
| `typeof` | `typeof(<value>)` | This function takes one argument and returns the data type of the argument. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/informational-functions#ariaid-title12) |
