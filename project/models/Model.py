#!/usr/bin/env python
import sys
import os
import json


class Model(object):

    def mongodb_uri(self):
        services = json.loads(os.getenv("VCAP_SERVICES", "{}"))
        if services:
            creds = services['mongodb-1.8'][0]['credentials']
            uri = "mongodb://%s:%s@%s:%d/%s" % (
                creds['username'],
                creds['password'],
                creds['hostname'],
                creds['port'],
                creds['db'])
            print >> sys.stderr, uri
            return uri
        else:
            uri = "mongodb://localhost:27017"