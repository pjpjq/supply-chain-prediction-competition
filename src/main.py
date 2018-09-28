import os
import logging

import click
from tqdm import tqdm
from config import datasets_dir, models_dir, logs_dir

from utils.logger import init_logger

logger = logging.getLogger(__name__)


def main():
    init_logger(log_file=os.path.join(logs_dir, 'work.log'))

    logger.info("info 还行")


if __name__ == '__main__':
    main()
