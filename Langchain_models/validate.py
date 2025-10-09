from huggingface_hub import HfApi
from requests.exceptions import HTTPError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
print("🔄 Loading .env file...")
load_dotenv(override=True)  # Force override any existing env vars

# Debug: Print current working directory and check if .env file exists
print(f"📁 Current directory: {os.getcwd()}")
env_path = os.path.join(os.getcwd(), '.env')
print(f"📄 .env file exists: {os.path.exists(env_path)}")

if os.path.exists(env_path):
    with open(env_path, 'r') as f:
        env_content = f.read()
        print(f"📋 .env file content preview:")
        for line in env_content.split('\n')[:5]:  # Show first 5 lines
            if 'HUGGINGFACE' in line:
                # Mask the token for security
                parts = line.split('=')
                if len(parts) == 2:
                    key, value = parts
                    masked_value = f"{value[:8]}...{value[-8:]}" if len(value) > 16 else value
                    print(f"   {key.strip()}={masked_value}")
                else:
                    print(f"   {line}")
            else:
                print(f"   {line}")

token = os.getenv("HUGGINGFACEHUB_API_TOKEN")  

if not token:
    print("❌ HUGGINGFACEHUB_API_TOKEN not found in environment variables")
    print("Make sure you have a .env file with your Hugging Face token")
    exit(1)

print(f"🔍 Token found: {token[:8]}...{token[-8:] if len(token) > 16 else ''}")
print("🔗 Validating token with Hugging Face API...")

api = HfApi()

try:
    user_info = api.whoami(token=token)
    print("✅ Token is valid!")
    print(f"👤 Logged in as: {user_info.get('name', 'Unknown')}")
    print(f"📧 Email: {user_info.get('email', 'Not available')}")
    print(f"🔗 Profile: https://huggingface.co/{user_info.get('name', '')}")
except HTTPError as e:
    print("❌ Token is invalid or unauthorized.")
    print(f"HTTP Error: {e}")
    if "401" in str(e):
        print("\n💡 Solutions:")
        print("1. Get a new token at: https://huggingface.co/settings/tokens")
        print("2. Make sure the token has 'Read' permissions")
        print("3. Update your .env file with the new token")
except Exception as e:
    print("❌ Some other error occurred.")
    print(f"Error: {e}")

print("\n🚀 Testing model access...")
try:
    # Test accessing a simple model
    model_info = api.model_info("gpt2", token=token)
    print("✅ Model access works! You can use Hugging Face models.")
except Exception as e:
    print(f"❌ Model access failed: {e}")
    print("You may need a token with broader permissions.")



'''
These is ai generated for chaking is it hf token is valid or not if it is valid then you can use hf model other vise you will get error
'''
