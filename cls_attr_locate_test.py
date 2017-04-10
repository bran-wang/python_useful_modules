from pydoc import locate
import datetime

class Base(object):
    MANDATORY_FIELDS = []
    KIND = __name__

    def __init__(self, *args, **kwargs):
        self.KIND = self.__module__ + '.' + self.__class__.__name__
        missing_fields = []
        for field in self.MANDATORY_FIELDS:
            try:
                setattr(self, field, kwargs.pop(field))
            except KeyError:
                missing_fields.append(field)

        if missing_fields:
            print("Missing required fields %s", missing_fields)

        self.kind = self.KIND

    def to_dict(self):
        result = {}
        for field in self.MANDATORY_FIELDS:
            result[field] = getattr(self, field)
        result['kind'] = self.KIND
        return result

    @classmethod
    def from_dict(cls, d):
        return cls(**d)


class Cluster(Base):
    MANDATORY_FIELDS = ['id', 'name', 'created_time', 'state']


kwargs = {'id': 'a86a7468-3dc7-44ac-8fd5-40736b58a393', 'name': 'test_cluster'}
created_at = datetime.datetime.utcnow().isoformat()
cluster = Cluster(created_time=created_at, state='CREATING', **kwargs)
cluster_dict = cluster.to_dict()
print cluster_dict

cls = locate(cluster_dict['kind'])
print cls
new_cluster = cls.from_dict(cluster_dict)
print new_cluster
