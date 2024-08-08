import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

logs_dir = os.getcwd() + '\\results\\logs'
log_file_path = os.path.join(logs_dir, log_file)

logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

