from django.db import models
 
from .db import db_conn


# Create your models here.
docusers=db_conn['docusers']
sendmessage=db_conn['sendmessage']