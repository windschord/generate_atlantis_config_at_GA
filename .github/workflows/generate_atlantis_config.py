# generate_atlantis_config.py
import os
import yaml

def find_backend_directories(root_dir='.'):
    backend_dirs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if 'backend.tf' in filenames:
            backend_dirs.append(dirpath)
    return backend_dirs

def generate_atlantis_config(directories):
    projects = []
    for directory in directories:
        project_name = os.path.basename(directory)
        projects.append({
            'name': project_name,
            'dir': directory,
            'workspace': 'default',
            'autoplan': {
                'when_modified': ['*.tf', '*.tfvars'],
                'enabled': True
            }
        })
    
    atlantis_config = {
        'version': 3,
        'projects': projects
    }
    
    with open('atlantis.yaml', 'w') as f:
        yaml.dump(atlantis_config, f)

if __name__ == "__main__":
    backend_dirs = find_backend_directories()
    generate_atlantis_config(backend_dirs)
