# zabbix-cloudwatch
> Cloudwatch integration for Zabbix 3.x

#### Requires:
- Zabbix 3.x
- Python 2.7.x
- Boto3

#### First Steps:

1. Create specialized user account in AWS and grant it permissions for required services and API calls (for example `describe_instances()` for EC2)
2. Clone github repo: https://github.com/pexessj/zabbix-cloudwatch
3. Copy contents of `zabbix-scripts` into `/usr/lib/zabbix` directory, change owner of  the dir and its contents to user under which you run Zabbix
4. [Install](http://boto3.readthedocs.io/en/latest/guide/quickstart.html) system-wide `boto3` package
5. Import `templates/cloudwatch_template.xml` into Zabbix
6. Put credentials of account created in (1) into `/usr/lib/zabbix/scripts/conf/aws.conf`
7. Create host with 0.0.0.0 as interface and link it to the template. Change macros `ACCOUNT` and `REGION` to correspond to your case:

![example](http://pichoster.net/images/2017/08/25/28a121dc1fb35b88c3970bdbd3971f71.png)

8. Enable/Disable all discovery rules/items/triggers you think necessary, add new or modify existing ones.

Default template has rules and items for following services:
* EC2 (requires `describe_instances()` API call permissions)
* RDS (requires `describe_db_instances()` API call permissions)
* ELB (requires `describe_load_balancers()` API call permissions)
* EMR (requires `list_clusters()` API call permissions)
* DynamoDB (requires `list_tables()` API call permissions)

This project is a fork of [@wawastein](https://github.com/wawastein/zabbix-cloudwatch) project.
