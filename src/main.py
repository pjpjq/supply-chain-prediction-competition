import os
import logging
import click

from utils.logger import init_logger

logger = logging.getLogger(__name__)


def main():
    output_dir = "../logs/"
    init_logger(log_file=os.path.join(output_dir, 'work.log'))

    logger.info("info 还行")


if __name__ == '__main__':
    main()
