# Chatbot Application

A full-stack chatbot application built with React frontend and FastAPI backend, integrated with Azure OpenAI.

## Features

- 🤖 AI-powered chatbot using Azure OpenAI GPT-3.5 Turbo
- ⚛️ React frontend with modern UI
- 🚀 FastAPI backend with RESTful API
- 🌐 CORS enabled for both local and production environments
- 📱 Responsive design

## Project Structure

```
chatbot/
├── backend/
│   ├── chatbot.py          # FastAPI application
│   ├── openai.env          # Environment variables
│   ├── requirements.txt    # Python dependencies
│   └── test_chatbot.py     # Test cases
├── public/                 # React public assets
├── src/                    # React source code
├── package.json           # Node.js dependencies
├── azure-pipelines.yml    # CI/CD pipeline
├── deploy.sh              # Deployment script
├── startup.sh             # Startup script
├── web.config             # IIS configuration
└── README.md              # This file
```

## Prerequisites

- Node.js 18.x or higher
- Python 3.9 or higher
- Azure OpenAI service with GPT-3.5 Turbo deployment

## Local Development

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables in `openai.env`:
   ```
   AZURE_OPENAI_KEY=your_azure_openai_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_DEPLOYMENT_NAME=your_deployment_name
   ```

4. Start the backend server:
   ```bash
   uvicorn chatbot:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend Setup

1. Install Node.js dependencies:
   ```bash
   npm install
   ```

2. Start the development server:
   ```bash
   npm start
   ```

3. Open http://localhost:3000 in your browser

## Deployment to Azure App Service

### Prerequisites

- Azure account with App Service and Azure OpenAI access
- Azure DevOps account (for CI/CD pipeline)

### Manual Deployment

1. Build the frontend:
   ```bash
   npm run build
   ```

2. Deploy to Azure using Azure CLI or Azure Portal

### CI/CD Pipeline

The project includes `azure-pipelines.yml` for automated deployment:

1. Connect your Azure DevOps to your Azure subscription
2. Configure the following pipeline variables:
   - `azureServiceConnection`: Azure service connection name
   - `webAppName`: Your Azure Web App name

3. Push to main/master branch to trigger deployment

## Environment Variables

### Backend (.env)
- `AZURE_OPENAI_KEY`: Your Azure OpenAI API key
- `AZURE_OPENAI_ENDPOINT`: Your Azure OpenAI endpoint URL
- `AZURE_DEPLOYMENT_NAME`: Your deployment name (e.g., gpt-35-turbo)

### Frontend
- `REACT_APP_API_BASE`: Backend API base URL (default: http://localhost:8000)

## API Endpoints

- `POST /chat` - Send a message to the chatbot
  - Request: `{"prompt": "your message"}`
  - Response: `{"text": "bot response", "references": []}`

## Troubleshooting

1. **CORS Issues**: Ensure the backend CORS settings include your frontend URL
2. **Azure OpenAI Errors**: Verify your API key, endpoint, and deployment name
3. **Build Errors**: Check Node.js and Python versions compatibility

## License

MIT License
