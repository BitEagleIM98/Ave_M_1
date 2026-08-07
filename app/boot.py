from dotenv import load_dotenv
load_dotenv()
import asyncio
from app.main import main


asyncio.run(main())