import os
import toml
from typing import Dict, Any
from pathlib import Path

class ConfigurationError(Exception):
    """Custom exception for configuration errors"""
    pass

class Config:
    """Configuration manager with environment support and validation"""
    
    def __init__(self):
        self._config = {}
        self._load_config()
    
    def _load_config(self):
        """Load configuration from multiple sources in order of precedence"""
        config_dir = Path(__file__).parent.parent / 'config'
        
        # Load default configuration
        default_config = self._load_toml_file(config_dir / 'default.toml')
        
        # Load environment-specific configuration
        env = os.getenv('NBA_ENV', 'development')
        env_config = self._load_toml_file(config_dir / f'{env}.toml', required=False)
        
        # Load secrets
        secrets_config = self._load_toml_file(config_dir / 'secrets.toml', required=False)
        
        # Merge configurations
        self._config = self._deep_merge(default_config, env_config or {})
        self._config = self._deep_merge(self._config, secrets_config or {})
        
        # Override with environment variables
        self._apply_env_overrides()
        
        # Validate configuration
        self._validate_config()
    
    def _load_toml_file(self, path: Path, required: bool = True) -> Dict[str, Any]:
        """Load a TOML file"""
        try:
            with open(path, 'r') as f:
                return toml.load(f)
        except FileNotFoundError:
            if required:
                raise ConfigurationError(f"Required configuration file not found: {path}")
            return {}
        except toml.TomlDecodeError as e:
            raise ConfigurationError(f"Error parsing {path}: {e}")
    
    def _deep_merge(self, dict1: Dict, dict2: Dict) -> Dict:
        """Recursively merge two dictionaries"""
        result = dict1.copy()
        for key, value in dict2.items():
            if isinstance(value, dict) and key in result and isinstance(result[key], dict):
                result[key] = self._deep_merge(result[key], value)
            else:
                result[key] = value
        return result
    
    def _apply_env_overrides(self):
        """Override configuration with environment variables"""
        # Environment variables should be in the format NBA_SECTION_KEY
        # Example: NBA_EMAIL_SMTP_SERVER
        for env_var, value in os.environ.items():
            if env_var.startswith('NBA_'):
                parts = env_var.lower().split('_')[1:]  # Remove 'NBA_' prefix
                self._set_nested_value(self._config, parts, value)
    
    def _set_nested_value(self, config: Dict, keys: list, value: str):
        """Set a value in nested dictionary using a list of keys"""
        for key in keys[:-1]:
            config = config.setdefault(key, {})
        try:
            # Try to convert string values to appropriate types
            if value.lower() in ('true', 'false'):
                value = value.lower() == 'true'
            elif value.isdigit():
                value = int(value)
            elif value.replace('.', '').isdigit() and value.count('.') == 1:
                value = float(value)
            config[keys[-1]] = value
        except (KeyError, AttributeError):
            pass
    
    def _validate_config(self):
        """Validate required configuration values"""
        required_fields = [
            ('email', 'smtp_server'),
            ('email', 'smtp_port'),
            ('database', 'path'),
            ('logging', 'level'),
        ]
        
        for section, field in required_fields:
            if not self._get_nested_value(self._config, [section, field]):
                raise ConfigurationError(f"Missing required configuration: {section}.{field}")
    
    def _get_nested_value(self, config: Dict, keys: list) -> Any:
        """Get a value from nested dictionary using a list of keys"""
        for key in keys:
            if not isinstance(config, dict) or key not in config:
                return None
            config = config[key]
        return config
    
    def get(self, *keys: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation"""
        value = self._get_nested_value(self._config, keys)
        return value if value is not None else default

# Global configuration instance
_config_instance = None

def get_config() -> Config:
    """Get the global configuration instance"""
    global _config_instance
    if _config_instance is None:
        _config_instance = Config()
    return _config_instance
