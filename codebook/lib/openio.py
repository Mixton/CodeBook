from oio.api.object_storage import ObjectStorageAPI
import json

# Constant connection options
DATABASE_NS    = "OPENIO"
DATABASE_PROXY = "http://172.28.128.3:6006"

class Object(object):
    data = None
    meta = None

    def __init__(self, data, meta = None):
        assert data != None
        self.data = data
        self.meta = meta

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

class Container:
    account = None
    name = None
    api = None

    def __init__(self, name, account = "DEFAULT"):
        self.api = ObjectStorageAPI(DATABASE_NS, DATABASE_PROXY)
        self.account = account
        self.name = name

    def create(self):
        self.api.container_create(self.account, self.name)
        return self

    def delete(self):
        self.api.container_delete(self.account, self.name)
        return self

    def add(self, obj, filename):
        data = json.dumps(obj.dat())
        self.api.object_create(self.account, self.name,
                               obj_name=filename,
                               data=str(data))
        return self

    def fetch(self, filename, object_type = Object):
        meta, data = self.api.object_fetch(self.account, self.name, filename)

        data = json.loads(''.join(data))
        meta = {
            'type':   data['type'],
            'output': data['output']
        }

        return object_type(data['source'], meta)

class SourceObject(Object):
    def __init__(self, data, meta):
        super(SourceObject, self).__init__(data, meta)
        # Valid extensions
        extensions = {'c', 'cpp', 'py', 'pl', 'rb'}
        assert 'type' in meta
        assert 'output' in meta
        assert meta['type'] in extensions

    def dat(self):
        return { 'source': self.data,
                 'type': self.meta['type'],
                 'output': self.meta['output'] }


