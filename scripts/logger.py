import logging

def get_logger():
    logging.basicConfig(
        filename="logs/pipeline.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger('neo_logger')

logger = get_logger()