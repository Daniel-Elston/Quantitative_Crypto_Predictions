import sys
import os

def setup_environment(root_dir):
    
    subdir_config = 'A_Main/Configurations'
    filename_config = 'config.yaml'
    
    config_dir = os.path.join(root_dir, subdir_config)
    config_path = os.path.join(config_dir, filename_config)
    
    sys.path.append(config_dir)
    
    from config_loader import ConfigLoader
    
    config = ConfigLoader(config_path)
    config.load()
    
    return config