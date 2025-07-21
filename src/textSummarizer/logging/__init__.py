# mentioning custom log
"""We are doing some info logging here. It'll keep the track of what's actually happing under the hood with files.
which module you are running. From where are u running it"""
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) # itll show the log in the terminal 
    ]
)

logger = logging.getLogger("textSummarizerLogger")