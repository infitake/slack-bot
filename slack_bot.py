# Bot User OAuth Access Token:xoxb-587165755527-577379837633-PHLxf4vaF7g8X6fu43jAwRs3
# OAuth Access Token: xoxp-587165755527-586060408980-586425283173-c3c10acfcfd7a01e1b663846878d4950
from slackclient import SlackClient
import time

class SlackConnections(object):
    def __init__(self):
        self.slack_client = SlackClient('xoxb-587165755527-577379837633-PHLxf4vaF7g8X6fu43jAwRs3')
        self.appname="infi_assist"

    def slackConnect(self):
        return self.slack_client.rtm_connect()

    def slackRead(self):
        return self.slack_client.rtm_read()

    def parseSlackInput(self, input, botId):
        bot = "<@"+ botId + ">"
        if input and len(input) > 0:
            input = input[0]
            if 'text' in input and bot in input["text"]:
                user = input["user"]
                message = input["text"].split(bot)[1].strip(' ')
                channel = input["channel"]
                return [str(user), str(message), str(channel)]
            else:
                return [None, None, None]

    def getBotId(self, botName):
        api_calls = self.slack_client.api_call('users.list')
        users = api_calls['members']
        for user in users:
            if "name" in user and botName in user.get("name") and not user.get("deleted"):
                return user.get('id')

    def writeToSlack(self, channel, text):
        return self.slack_client.api_call('chat.postMessage', channel=channel, text=text, as_user=True)


class MainFunc(SlackConnections):
    def __init__(self):
        super(MainFunc, self).__init__()
    
    def decideToTakeAction(self, input):
        if input:
            user, message, channel = input
            return self.writeToSlack(channel, message)
    
    def run(self):
        # first connect with the slack
        self.slackConnect()
        botId = self.getBotId(self.appname)
        print(botId)
        while True:
            self.decideToTakeAction(self.parseSlackInput(self.slackRead(), botId))
            time.sleep(1)

if __name__ == "__main__":
    instance = MainFunc()
    instance.run()