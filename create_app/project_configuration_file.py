import json
import os
from tempfile import mkstemp
from typing import Dict, Optional


class ProjectConfigurationFile:
    MODE = "w+"

    def __init__(self, config: Dict):
        self.config: Dict = config
        self.path: Optional[str] = None

    def __enter__(self):
        config_file_fd, config_file_path = mkstemp()
        self.path = config_file_path
        opened_config_file = os.fdopen(
            config_file_fd,
            ProjectConfigurationFile.MODE,
        )
        json.dump(self.config, opened_config_file)
        opened_config_file.close()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.remove(self.path)
