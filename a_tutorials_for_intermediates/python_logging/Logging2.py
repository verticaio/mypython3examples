import logging


class FirstClass(object):
    def __init__(self):
        self.current_number = 0
        #Create Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        # Create the Handler for logging data to a file
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.INFO)

        # Create a Formatter for formatting the log messages
        logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        # Add the Formatter to the Handler
        logger_handler.setFormatter(logger_formatter)

        # Add the Handler to the Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('Completed configuring logger()!')

    def increment_number(self):
        self.current_number += 1
        self.logger.warning('Incrementing number!')
        self.logger.info('Still incrementing number!!')

    def decrement_number(self):
        self.current_number -= 1
        self.logger.warning('Clearing number!')
        self.logger.info('Still clearing number!!')

    def clear_number(self):
        self.current_number = 0
        self.logger.warning('Clearing number!')
        self.logger.info('Still clearing number!!')


number = FirstClass()
number.increment_number()
number.increment_number()
print("Current number: %s" % str(number.current_number))
number.clear_number()
print("Current number: %s" % str(number.current_number))
