import logging
from rich.logging import RichHandler

log = logging.getLogger("Local")
log.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.WARNING, format="%(message)s", handlers=[RichHandler()])