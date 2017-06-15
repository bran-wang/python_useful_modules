import uuid
from oslo_utils import uuidutils

#print dir(uuid)

cluster_id = str(uuid.uuid4())
print cluster_id

if uuidutils.is_uuid_like(cluster_id):
    print "cluster id is UUID\n"
else:
    print "cluster id is not UUID\n"


