from dotenv import load_dotenv
import os

load_dotenv()

k = os.environ.get("BEARER_TOKEN")
print(k)