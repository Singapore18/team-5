import os
import logging
import sys
from flask import Flask
application = Flask(__name__)
from .db import *

db = DBConnection()

import minds.routes.square
import minds.routes.formsubmit
