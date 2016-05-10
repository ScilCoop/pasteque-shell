from Config import config


# Some tools functions
def payload():
    return {"login": config["login"], "password": config["password"]}


def base_url():
    return config["host"] + "api.php"


def action_url(api, action):
    return base_url() + "&p=" + api + "&action=" + action


# This is where the API is build from.
# It is supposed to manage the request building: either POST or GET.
# Inherit your API module from this class and give it to the Request class.
# Stay close to the requests behavior: http://docs.python-requests.org/en/master/
class Api(object):
    data = None

    def __init__(self, api):
        self.data = payload()
        self.data["p"] = api

    @staticmethod
    def url():
        return base_url()

    def set_action(self, action):
        self.data["action"] = action
