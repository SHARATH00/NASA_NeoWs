import logging

def setup_logger():
    logging.basicConfig(
        filename="logs/pipeline.log",
        filemode="a",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()
