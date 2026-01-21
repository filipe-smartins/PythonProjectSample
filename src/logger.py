import logging
from pathlib import Path

from settings.settings import base_dir, usuario

log_dir = Path(base_dir) / 'data' / 'logs'
log_dir.mkdir(parents=True, exist_ok=True)
log_path = log_dir / 'log.log'

logging.basicConfig(
    level=logging.INFO,
    filename=str(log_path),
    format='%(levelname)s: %(asctime)s - Module: %(module)s Function: %(funcName)s -> %(message)s',
)

logger = logging.getLogger(__name__)

logger.info(f'\nSystem started by user: {usuario}\n')
