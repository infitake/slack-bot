import pytest

input = [{'client_msg_id': '8169ece2-122e-44cb-8524-349470cc925c', 'type': 'message', 'text': '<@UGZB5QMJM> this is what ayou want', 'user': 'UH81SC0UU', 'team': 'TH94VN7FH', 'channel': 'DH82NK610', 'event_ts': '1553411891.006100', 'ts': '1553411891.006100'}]


@pytest.fixture
def SlackConnections():
    from slack_bot import SlackConnections
    return SlackConnections()

@pytest.fixture
def MainFunc():
    from slack_bot import MainFunc
    return MainFunc()

# @pytest.mark.skip(reason=" not full")
def test_slackBot(SlackConnections):
    assert SlackConnections.slackConnect()

def test_parseInput(SlackConnections):
    assert SlackConnections.parseSlackInput(input, 'UGZB5QMJM') == ["UH81SC0UU", "this is what ayou want", "DH82NK610"]

def test_getBotId(SlackConnections):
   assert SlackConnections.getBotId("infi_assist") == 'UGZB5QMJM'

def test_writeToSlack(SlackConnections):
    assert SlackConnections.writeToSlack("DH82NK610","it's running ohooo")["ok"] == True

@pytest.mark.skip(reason="not fully implemented")
def test_slackRead(SlackConnections):
    SlackConnections.slackConnect()
    print(SlackConnections.slackRead())


def test_decideToTakeActions_Message(MainFunc):
    input = ["UH81SC0UU", "this is what ayou want", "DH82NK610"]
    assert MainFunc.decideToTakeAction(input)

def test_decideToTakeActions_None(MainFunc):
    input = [None, None, None]
    assert MainFunc.decideToTakeAction(input)