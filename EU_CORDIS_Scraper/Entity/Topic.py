from . import Project
from .BaseEntity import BaseEntity


class Topic(BaseEntity):

    def __init__(self, topic: dict):
        try:
            self.id = topic['id']
        except KeyError:
            self.id = topic['ccm2Id']
        try:
            self.code = topic['code']
        except KeyError:
            self.code = topic['identifier']

        if isinstance(topic['frameworkProgramme'], str):
            self.frameworkProgramme = topic['frameworkProgramme']
        else:
            self.frameworkProgramme = topic['frameworkProgramme']['abbreviation']

        self.title = topic['title']

        self.financed_projects = []

    def add_financed_project(self, project: Project):
        self.financed_projects.append(project)
