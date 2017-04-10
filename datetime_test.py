import datetime
import time


kwargs = {}
kwargs["created_time"] = datetime.datetime.utcnow().isoformat()
kwargs["state"] = "start"

print "created time is: ", kwargs['created_time'], ", state is: ", kwargs["state"]

print("do some thing")
time.sleep(5)

kwargs["complete_time"] = datetime.datetime.utcnow().isoformat()
kwargs["state"] = "active"

print "completed time is: ", kwargs['complete_time'], ", state is: ", kwargs["state"]


