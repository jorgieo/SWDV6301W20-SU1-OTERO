from datetime import datetime
import secrets


class Transaction:
    """
    Super class for all transaction types.
    On instantiation system time is used to tag the object and a 32-character hexadecimal code
    is automatically generated.
    Attributes:
            timestamp: system date and time.
            transID: 32 random hex characters.
            description: dictionary of transaction object attributes.
                'timestamp': timestamp attribute
                'id': transID attribute
                'type': transaction type
                'items': items involved in the transaction
    """
    def __init__(self):
        self.timestamp = self._timetag()
        self.transID = self._generate_ID()
        self.description = {'timestamp': self.timestamp,
                            'id': self.transID,
                            'type': '',
                            'items': []}

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

    def getDescription(self):
        """
        Returns a description of the transaction.
        """
        return self.description

    def getDate(self):
        """
        Returns the time stamp of the transaction.
        """
        return self.timestamp

    def getID(self):
        return self.transID

    def setType(self, type):
        self.description['type'] = type
