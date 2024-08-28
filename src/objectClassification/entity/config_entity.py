# Update the entity

from dataclasses import dataclass # decorator 
from pathlib import Path

# this is custom entity we created
# now we are accessing different varible from other files(config/config.py) 
# in below class
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# this class only return these values not other than these 