import json

class Storage:
    def __init__(self, filename):
        self.filename = filename

    def save(self, chromosomes):
        with open(self.filename, 'w') as file:
            json.dump({"chromosomes": chromosomes}, file)




