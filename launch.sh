#!/bin/bash
echo "Starting car..."

echo "Launching client HTTP server"
cd client
python3 -m http.server 8080 &

echo "Launching car HTTP server"
cd ..
python3 httpserver.py 8081 &

echo "Launching socket server"
cd server
python3 server.py
