 #!/bin/bash

# Exit on error
set -e

echo "Starting deployment script..."

# Install frontend dependencies and build
echo "Building React frontend..."
cd /home/site/wwwroot/chatbot
npm install
npm run build

# Install backend dependencies
echo "Installing Python backend dependencies..."
cd /home/site/wwwroot/chatbot/backend
pip install -r requirements.txt

echo "Deployment completed successfully!"
