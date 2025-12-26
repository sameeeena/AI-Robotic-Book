import sys
import os

# Add backend to path so we can import 'main'
# Vercel functions run in a specific environment, but relative paths should work if files are bundled.
# We append the absolute path of the backend/rag-backend directory.
sys.path.append(os.path.join(os.path.dirname(__file__), '../backend/rag-backend'))

from main import app

# Set root_path for Vercel
app.root_path = "/api"
