import logging

from EU_CORDIS_Scraper.CordisRepository import CordisRepository
from EU_CORDIS_Scraper.Entity.Organization import Organization
from EU_CORDIS_Scraper.Entity.Participation import Participation
from EU_CORDIS_Scraper.Entity.Project import Project
from EU_CORDIS_Scraper.Entity.Topic import Topic


class CordisSearch:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        self.repository = CordisRepository()

    def get_project(self, id: int, add_consortium=True, add_topic=True) -> Project:
        project_dict = self.repository.get_project(id)
        project = Project(project_dict)

        if add_consortium:
            for org_dict in project_dict['relations']['associations']['organization']:
                organization = Organization(org_dict)
                project.add_participation(Participation(project, organization, org_dict))

        if add_topic:
            for p in project_dict['relations']['associations']['programme']:
                if p['@type'] == 'relatedTopic':
                    topic_dict = p
                    topic = Topic(topic_dict)
                    project.set_topic(topic)
                    break

        return project

    def get_consortium(self, id_project):
        ret = []
        project_dict = self.repository.get_project(id_project)
        project = Project(project_dict)
        for org_dict in project_dict['relations']['associations']['organization']:
            organization = Organization(org_dict)
            ret.append(Participation(project, organization, org_dict))

        return ret

    def get_topic(self, code):
        topic_dict = self.repository.get_topic(code.lower())

        return Topic(topic_dict['TopicDetails'])

    def get_financed_projects_by_topic(self, code, add_consortium=True):
        ret = []
        project_dicts = self.repository.get_financed_projects_by_topic(code)

        for project_dict in project_dicts:
            project = self.get_project(project_dict['businessIdentifier'], add_consortium, add_topic=False)

            ret.append(project)

        return ret


