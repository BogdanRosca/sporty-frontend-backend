import sys
from pathlib import Path
from utils.auth import init_auth_env

# Add the project root directory to Python path
project_root = Path(__file__).parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

init_auth_env()
