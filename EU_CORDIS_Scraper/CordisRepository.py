import importlib
import json
import logging

import requests
import xmltodict


class CordisRepository:

    def __init__(self):
        logging.basicConfig(level=logging.INFO)

        config_file = importlib.resources.read_text('EU_CORDIS_Scraper.config', 'config.json')
        self.config = json.loads(config_file)

    def get_project(self, project_id, add_consortium=False) -> dict:
        logging.info(f"Getting project info: {project_id}")
        url = self.config["project_url"].replace("{id_project}", str(project_id))
        try:
            response = requests.get(url)
        except requests.exceptions.TooManyRedirects:
            logging.error(f'Wrong project id: {project_id}')
            exit()
        xml = response.text
        o = xmltodict.parse(xml)

        return o['project']

    def get_topic(self, topic_code) -> dict:
        url = self.config["topic_url"].replace("{topic_code}", topic_code)
        try:
            response = requests.get(url)
        except requests.exceptions.TooManyRedirects:
            logging.error(f'Wrong topic code: {topic_code}')
            exit()

        return json.loads(response.text)

    def get_financed_projects_by_topic(self, topic_code: str) -> list:
        ret = []

        topic = self.get_topic(topic_code.lower())
        topic_id = topic['TopicDetails']['ccm2Id']

        url = self.config["topics_project_url"].replace("{topic_id}", str(topic_id))
        response = requests.get(url)
        projects = json.loads(response.text)
        logging.info(f"Projects loaded! Num projects: {len(projects)}")

        return projects

