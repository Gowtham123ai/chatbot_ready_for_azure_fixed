#!/bin/bash
gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.chatbot:app --bind=0.0.0.0:8000
