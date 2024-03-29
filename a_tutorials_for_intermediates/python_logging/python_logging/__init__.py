from os import path, remove
import logging
import logging.config
import json


from .first_class import FirstClass
from .second_class import SecondClass

if path.isfile("python_logging.log"):
    remove("python_logging.log")


# Log that the logger was configured
logger = logging.getLogger(__name__)
logger.info('Completed configuring logger()!')

# Create Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create the Handler for logging data to a file
logger_handler = logging.FileHandler('python_logging.log')
logger_handler.setLevel(logging.DEBUG)

# Create a Formatter for formatting the log messages
logger_formatter = logging.Formatter('%(lineno)d:%(asctime)s: %(levelname)s - %(name)s - %(funcName)s - %(message)s')

# Add the Formatter to the Handler
logger_handler.setFormatter(logger_formatter)

# Add the Handler to the Logger
logger.addHandler(logger_handler)
logger.info('Completed configuring logger()!')