import os, sys
from dotenv import load_dotenv
load_dotenv()
PYTHONPATH = os.getenv('PYTHONPATH')
PROJECT_ROOT = os.path.abspath(PYTHONPATH)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
import asyncio
from app.main import main


if __name__ == "__main__":
    asyncio.run(main())