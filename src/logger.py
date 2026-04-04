import logging
import pathlib
import json


logger = logging.getLogger("metrics")

def loggingSetup():
    config_file = pathlib.Path("logging_configs/config.json")
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)

def main():
    loggingSetup()
    logger.debug("DEBUG")
    logger.info("INFO")
    logger.warning("Warning Message!")
    logger.error("ERROR")
    logger.critical("CRITICAL ERROR")
    try:
        1/0
    except ZeroDivisionError:
        logger.exception("Exception Message")

if __name__ == "__main__":
    main()
    
""" Basic Logging (Root log)
#Dynamically finds path to update metrics.log
base_dir =(Path(__file__).parent).parent
log_dir = base_dir / "logs"
log_file = log_dir / "metrics.log"


#Logs into metrics.log with a specific format
logging.basicConfig(
    filename=str(log_file),
    encoding="utf-8",
    filemode="a", # append 
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
)
"""
