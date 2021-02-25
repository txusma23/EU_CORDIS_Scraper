from .BaseEntity import BaseEntity


class Organization(BaseEntity):

    def __init__(self, org: dict):
        self.pic = org['id']
        try:
            self.short_name = org['shortName']
        except KeyError:
            self.short_name = None
        self.name = org['legalName']
        self.type = org['relations']['categories']['category']['title']
        self.country = org['relations']['regions']['region']['name']
