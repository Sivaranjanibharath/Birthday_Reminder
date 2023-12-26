import sqlite3
from datetime import date
from typing import List, Dict
import boto3
import os

birthday_reminder_sns_topic_arn = os.getenv("BIRTHDAY_SNS_ARN")

# Initialize boto3 client using the default AWS credential profile (ie) you should run aws configure and provide
# the aws secret and access key for the IAM users with sns publish permissions
client = boto3.client('sns')


def fetch_eligible_reminders() -> List[Dict]:
    """
    This is a function to fetch eligible reminders from DB
    """
    d = date.today()
    print(d)
    connection = sqlite3.connect('birthdays.db')
    print(f"SELECT name,date FROM birthdays where date = {d}")
    reminders = []
    for row in connection.execute(f"SELECT name, date FROM birthdays where date = '{d}'"):
        r = {
            "name": row[0],
            "dob": row[1]
        }
        reminders.append(r)
    connection.close()
    return reminders


def send_birthday_reminder(reminders_list: List[Dict]):
    """
    This is a function that accepts list of dictionaries that contains name and dob.Then it uses name and
    dob to compile a message for SNS topic that it then publishes.
    :return: none
    """
    for reminder in reminders_list:
        name = reminder["name"]
        dob = reminder["dob"]
        response = client.publish(
            TopicArn=birthday_reminder_sns_topic_arn,
            Message=f'Hey!!This is a birthday reminder for {name} on {dob} ',
            Subject=f'birthday reminder for {name}'
        )
        print(f"Sucessfully posted sns message for {name} and got sns message id as {response['MessageId']} ")


if __name__ == "__main__":
    """
    This module fetches the name,date and publishes the reminder message
    """
    reminders = fetch_eligible_reminders()
    send_birthday_reminder(reminders)
