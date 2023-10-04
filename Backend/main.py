""" This code executes:
1) run Flask app;
"""

# Import project Modules
from views import *


if __name__ == '__main__':
    # run api
    app.run(port="8080",host="0.0.0.0")
