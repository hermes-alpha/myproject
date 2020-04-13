# Respecting the import order in Python files

'''
# System libraries for packages in the default installation of Python
import os
import re
from datetime import datetime

# Third-party libraries for the additional installed Python packages
import boto
from PIL import Image

# Django modules for different modules from the Django framework
from django.db import models
from django.conf import settings

# Django apps for third-party and local apps
from cms.models import Page

# Current-app modules for relative imports from the current app
from .models import NewsArticle
from . import app_settings
'''
