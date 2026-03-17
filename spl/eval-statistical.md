# Evaluation Functions - Statistical Eval

Category: **Evaluation - Statistical Eval**  
Reference: [help.splunk.com](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions)  
Splunk version: 10.2

| Function | Syntax | Description | Usable With | Docs |
|----------|--------|-------------|-------------|------|
| `avg` | `avg(<values>)` | This function takes one or more values and returns the average of numerical values as an integer. Each argument must be either a field (single or multivalue) or an expression that evaluates to a number. At least one numeric argument is required. When the function is applied to a multivalue field, each numeric value of the field is included in the total. The eval command ignores arguments that don't exist in an event or can't be converted to a number. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions#ariaid-title2) |
| `max` | `max(<values>)` | This function takes one or more numeric or string values, and returns the maximum. Strings are greater than numbers. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions#ariaid-title3) |
| `min` | `min(<values)` | This function takes one or more numeric or string values, and returns the minimum. Strings are greater than numbers. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions#ariaid-title4) |
| `random` | `random()` | This function takes no arguments and returns a pseudo-random integer ranging from zero to 2 31 -1. | eval, fieldformat, where | [docs](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/evaluation-functions/statistical-eval-functions#ariaid-title5) |
