#!/home/mariolo/python/vep26/bin/python
import sys, os

# Add a custom Python path for your project
sys.path.insert(0, "/home/mariolo/python/agenda")

# Set the DJANGO_SETTINGS_MODULE environment variable.
# This should match the name for the project you added to the path above
os.environ['DJANGO_SETTINGS_MODULE'] = 'agenda.settings'

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")

