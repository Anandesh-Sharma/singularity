from singularity import Singularity
from singularity.db import Mongo

app = Singularity()

# setup databse
db = Mongo()
app.add_event_handler("startup", db.init)
