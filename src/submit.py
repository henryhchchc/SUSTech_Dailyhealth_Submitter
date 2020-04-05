#! /usr/bin/python3

import sys
import os
import json
import requests
import datetime


def exit_with_error(error_message, status=-1):
    print(error_message, file=sys.stderr)
    exit(status)


submit_url = "http://dailyhealth-api.sustech.edu.cn/api/form/save"


def send_request(config):
    form_content = config["form"]
    today = datetime.datetime.today()
    date_string = "%d-%02d-%02d" % (today.year, today.month, today.day)
    form_content["formDate"] = date_string
    response = requests.post(submit_url, data=json.dumps(
        form_content), headers=config["headers"])
    print("Response: %d" % response.status_code)


def main():
    if sys.version_info.major < 3:
        exit_with_error("Python 3 is required to run this script")
    if len(sys.argv) != 2:
        exit_with_error("Usage: submit.py <config file>")
    config_fn = sys.argv[1]
    if not os.path.exists(config_fn):
        exit_with_error("Config file not exist")
    print("Reading config: %s" % config_fn)
    with open(config_fn, "r") as config_file:
        config_content = config_file.read()
    config = json.loads(config_content)
    send_request(config)


if __name__ == "__main__":
    main()
