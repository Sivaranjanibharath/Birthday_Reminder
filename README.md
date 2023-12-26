# Background
This is my first side project to demo how you can create a web application using Flask and AWS features. This is a very simple birthday reminder app that has two rudimentary features.
* Register someones birthday for alerts
* Send a reminder text/email/other sns modes based alerts on the day of the event
  * Note: The sending reminder functionality is done manually by executing the python module reminder.py. This can be automated by using basic os scheduler or something more mature like [Quartz](https://www.quartz-scheduler.org/) or [AWS Cloudwatch rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html)
# Dependencies
This program uses,
* [sqlite3](https://docs.python.org/3/library/sqlite3.html) a python wrapper of [sqlite](https://www.sqlite.org/index.html) a light weight in memory database.
* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) python java AWS SDK
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) a lightweight framework to create web applications used for non-prod apps and for POCs 
* [SNS](https://aws.amazon.com/sns/) a PUB/SUB messaging service provided by AWS

# Installation
You can pull the code and set basic presets and you should be good to go!

## Database initialization
* Ensure you have Sqlite dependency added to your python venv and execute the below function to create the `birthdays` database and table.
* In your py env you can launch the repl and execute the below code
```python
def create_table():
    connection = sqlite3.connect('birthdays.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS birthdays (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')
    connection.commit()
    connection.close()
```
This should create a db file called `birthdays.db`

## AWS Installation
* You will need an AWS Account
* Create a SNS topic using [AWS Cli](https://aws.amazon.com/cli/)  or [AWS  Managment Console](https://aws.amazon.com/console/). Instructions Ref: [Create topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html)
* Create a subscription for the topic just created with your email or sms or other applicable modes using [AWS Cli](https://aws.amazon.com/cli/)  or [AWS  Managment Console](https://aws.amazon.com/console/). Instructions Ref: [Subscribe to SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html)
* Create an IAM user using [AWS Cli](https://aws.amazon.com/cli/)  or [AWS  Managment Console](https://aws.amazon.com/console/)
* Provide full access for the created IAM user to an [IAM managed policy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonSNSFullAccess.html) that provides full access to SNS
* Download the access key and secret for the created user
* Set a default credentials profile for those credentials using AWS Cli. You can follow the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

## Flask installation
[Flask](https://flask.palletsprojects.com/en/3.0.x/) a lightweight framework to create web applications used for non-prod apps and for POCs. Use the flask documentation to learn more about it.