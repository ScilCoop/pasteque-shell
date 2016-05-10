from api.Api import Api

# This is an API module
# http://redmine.scil.coop/projects/pt-server/wiki/Api_doc7#getAll-2
class CashRegistersApi(Api):
    def __init__(self):
        Api.__init__(self, "CashRegistersAPI")

    def getAll(self):
        self.set_action("getAll")
