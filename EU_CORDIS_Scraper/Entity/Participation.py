from . import Project, Organization
from .BaseEntity import BaseEntity


class Participation(BaseEntity):

    def __init__(self, project: Project, organization: Organization, org: dict):
        self.project = project
        self.organization = organization
        self.role = org['@type']
        self.budget = org['@ecContribution']
        self.terminated = org['@terminated']