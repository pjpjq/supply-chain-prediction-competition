import logging
import functools

root_logger = logging.getLogger()


def get_formatter(name=None):
    if name:
        return logging.Formatter('%(asctime)s [%(process)d] [{}] %(message)s'.format(name))
    else:
        return logging.Formatter('%(asctime)s [%(process)d] %(message)s')


def init_logger(stream_handler=True, log_file=None, level=logging.INFO):
    root_logger.handlers = []
    root_logger.filters = []
    root_logger.setLevel(level)
    formatter = get_formatter()
    if stream_handler:
        stream_handler = ColorizingStreamHandler()
        stream_handler.setFormatter(formatter)
        root_logger.addHandler(stream_handler)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)


class LoggerCTX:
    def __init__(self, name):
        self.name = name
        self.old_formatter = []

    def __enter__(self):
        self.old_formatter = []
        for handler in root_logger.handlers:
            self.old_formatter.append(handler.formatter)
            handler.setFormatter(get_formatter(self.name))
        return self.name

    def __exit__(self, exc_type, exc_val, exc_tb):
        for idx, handler in enumerate(root_logger.handlers):
            if idx < len(self.old_formatter):
                handler.setFormatter(self.old_formatter[idx])
            else:
                handler.setFormatter(get_formatter())


# Most code is stolen from http://goo.gl/qTpR3


class ColorizingStreamHandler(logging.StreamHandler):
    # color names to indices
    color_map = {
        'black': 0,
        'red': 1,
        'green': 2,
        'yellow': 3,
        'blue': 4,
        'magenta': 5,
        'cyan': 6,
        'white': 7,
    }

    # levels to (background, foreground, bold/intense)
    level_map = {
        logging.DEBUG: (None, None, False),
        logging.INFO: (None, 'green', False),
        logging.WARNING: (None, 'yellow', True),
        logging.ERROR: (None, 'red', True),
        logging.CRITICAL: ('red', 'white', True),
    }

    csi = '\x1b['
    reset = '\x1b[0m'

    @functools.lru_cache(maxsize=1)
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def format(self, record):
        message = logging.StreamHandler.format(self, record)
        if True or self.is_tty():
            # Don't colorize any traceback
            parts = message.split('\n', 1)
            parts[0] = self.colorize(parts[0], record)
            message = '\n'.join(parts)
        return message

    def colorize(self, message, record):
        if record.levelno in self.level_map:
            bg, fg, bold = self.level_map[record.levelno]
            params = []
            if bg in self.color_map:
                params.append(str(self.color_map[bg] + 40))
            if fg in self.color_map:
                params.append(str(self.color_map[fg] + 30))
            if bold:
                params.append('1')
            if params:
                message = ''.join((self.csi, ';'.join(params), 'm', message,
                                   self.reset))
        return message
