#!/usr/bin/python
from basic_discovery import BasicDiscoverer


class Discoverer(BasicDiscoverer):
    def discovery(self, *args):
        response = self.client.list_tables()
        instances = list()
        for reservation in response['TableNames']:
            instances.append(reservation)
        data = list()
        for instance in instances:
            name = ""
            ldd = {
                    "{#INSTANCE_ID}":   instance
            }
            data.append(ldd)
        return data
