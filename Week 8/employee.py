from sqlalchemy import Column, Integer, String, Numeric
from base import Base
import secrets


class Employee(Base):
    """Items in the inventory."""

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.uid = self._genID()
        self.keycard = self._genKey()

    def __repr__(self):
        return f"Employee Name: {self.name}\nRole: {self.role}\nid: {self.uid}\nKeycard: {self.keycard}"

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    def _genID(self):
        return secrets.token_hex(12)

    def getID(self):
        return self.uid

    def _genKey(self):
        return secrets.token_hex(12)

    def getKey(self):
        return self.keycard

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    role = Column(String)
    uid = Column(String)
    keycard = Column(String)
