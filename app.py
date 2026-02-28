import os
import json
from pathlib import Path


class ConfigLoader:
    """Loads configuration from JSON files."""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self._cache = {}
    
    def load(self, name: str) -> dict:
        if name in self._cache:
            return self._cache[name]
        
        path = self.config_dir / f"{name}.json"
        if not path.exists():
            raise FileNotFoundError(f"Config '{name}' not found at {path}")
        
        with open(path) as f:
            data = json.load(f)
        
        self._cache[name] = data
        return data
    
    def reload(self, name: str) -> dict:
        self._cache.pop(name, None)
        return self.load(name)


def get_env(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


def initialize_app():
    loader = ConfigLoader()
    db_config = loader.load("database")
    return db_config
