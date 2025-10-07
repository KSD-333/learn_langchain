from huggingface_hub import HfApi
from requests.exceptions import HTTPError
import os

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  

if not token:
    print("❌ HUGGINGFACEHUB_API_TOKEN not found in environment variables")
    exit(1)

api = HfApi()

try:
    user_info = api.whoami(token=token)
    print("✅ Token is valid!")
    print("User info:", user_info)
except HTTPError as e:
    print("❌ Token is invalid or unauthorized.")
    print("Error:", e)
except Exception as e:
    print("❌ Some other error occurred.")
    print("Error:", e)
