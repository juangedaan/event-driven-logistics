#!/bin/bash

PROJECT_DIR="/home/juanmb/Projects/git/event-driven-logistics"
SESSION="logistics"

tmux new-session -d -s $SESSION

tmux rename-window -t $SESSION:0 'Dashboard'
tmux send-keys -t $SESSION:0 "cd $PROJECT_DIR && python3 -m app.dashboard.app" C-m

tmux new-window -t $SESSION:1 -n 'Consumer'
tmux send-keys -t $SESSION:1 "cd $PROJECT_DIR && python3 -m app.consumer" C-m

tmux new-window -t $SESSION:2 -n 'Producer'
tmux send-keys -t $SESSION:2 "cd $PROJECT_DIR && python3 -m app.producer" C-m

tmux new-window -t $SESSION:3 -n 'Notifier'
tmux send-keys -t $SESSION:3 "cd $PROJECT_DIR && python3 -m app.notifier" C-m

tmux new-window -t $SESSION:4 -n 'DynamoDB'
tmux send-keys -t $SESSION:4 "aws dynamodb scan --table-name Shipments --endpoint-url http://localhost:8000 --region us-west-2 --output table" C-m

tmux new-window -t $SESSION:5 -n 'Docker'
tmux send-keys -t $SESSION:5 "cd $PROJECT_DIR/deployment && docker-compose up" C-m

tmux select-window -t $SESSION:0
tmux attach -t $SESSION
