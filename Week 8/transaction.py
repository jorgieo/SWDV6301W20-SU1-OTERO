from datetime import datetime
import secrets


class Transaction:
    """
    Super class for all transaction types.
    On instantiation system time is used to tag the object and a 32-character hexadecimal code
    is automatically generated.
    Attributes:
            timestamp: system date and time.
            transID: 16 random hex characters.
            type: the type of transaction it is.
            netTotal: the final amount of the transaction
            items: a list of items involved in the transaction
    """
    def __init__(self):
        self.timestamp = self._timetag()
        self.transID = self._generate_ID()
        self.type = ''
        self.netTotal = 0
        self.items = []

    def __repr__(self):
        return f"{self.timestamp}\n{self.transID}\n{self.type}\n${self.netTotal}\n"

    def _generate_ID(self):
        """
        Automatic ID generator.
        """
        return secrets.token_hex(16)

    def _timetag(self):
        """
        Autimatic time stamp.
        """
        return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

    def getDate(self):
        """
        Returns the time stamp of the transaction.
        """
        return self.timestamp

    def getID(self):
        return self.transID

    def setType(self, type):
        self.type = type

