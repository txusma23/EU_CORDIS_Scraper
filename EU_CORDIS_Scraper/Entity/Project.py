from . import Participation, Topic
from .BaseEntity import BaseEntity


class Project(BaseEntity):

    def __init__(self, project: dict) -> object:
        self.id = project['id']
        self.rcn = project['rcn']
        self.acronym = project['acronym']
        self.name = project['title']
        self.abstract = project['objective']
        self.total_cost = project['totalCost']
        self.eu_contribution = project['ecMaxContribution']
        self.start_date = project['startDate']
        self.end_date = project['startDate']

        self.topic = None
        self.consortium = []

    def add_participation(self, participation: Participation):
        self.consortium.append(participation)

    def set_topic(self, topic: Topic):
        self.topic = topic
