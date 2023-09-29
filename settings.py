""" This code executes:
1) Flask settings for dev-challenge-xx-online-round project;
2) Path to project folder
3) Past to database
4) Endpoint
"""
# Import python Modules
import os

# Contains full-path to the project folder
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
# Contains full-path to the database (It contains information about sheets)
DATABASE = os.path.join(PROJECT_ROOT, 'database', 'excel')
# Contains endpoint
ENDPOINT = "/api/v1/"
