import logging

def setup(log_filename):
    logging.basicConfig(
                    filename=log_filename,
                    filemode='w',
                    format='%(asctime)s (%(levelname)s): %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S'
                    )

    logging.info("Logger for 'api_functions' module initialized.")
