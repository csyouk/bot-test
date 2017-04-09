from slacker import Slacker
from random import random

def main():
    slack = Slacker("xoxb-166602669331-oG2LmrTDyEjlCpKam0Ak5oVo")

    slack.chat.post_message("#general", random())

    response = slack.users.list()
    users = response.body["members"]
    print(users)
    for k, v in users[0].items():
        print("Key : {}        |       Value : {}".format(k, v))


if __name__ == '__main__':
    main()