from singularity import Singularity
from singularity.db import Mongo

app = Singularity(env_path="/Users/hash/work/personal/singularity-core/.env")

# setup databse
db = Mongo()
app.add_event_handler("startup", db.init)
