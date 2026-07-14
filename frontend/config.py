# Change your API target URL inside your Streamlit code to this:
import os

# 1. First, check if Render has set an environment variable (like PORT or RENDER)
# 2. If it's running on Render, use the cloud backend URL
# 3. If it's running on your computer, default to localhost (127.0.0.1)

if os.environ.get("RENDER") or os.environ.get("PORT"):
    API_URL = "https://bug-backend-service.onrender.com"
else:
    API_URL = "http://127.0.0.1:8000"
