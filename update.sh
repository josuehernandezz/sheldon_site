#!/bin/bash

set -e  # Exit immediately if a command fails

# Load environment variables from the .env file
if [ -f ".env" ]; then
    echo "Loading environment variables from .env file..."
    source .env
else
    echo ".env file not found, exiting script."
    echo -e "\nMake sure to define the following variables in your .env file:"
    echo "
WORK_DIR=/path/to/repo/base/directory
VENV_DIR=$WORK_DIR/venv
PROJECT_DIR=$WORK_DIR/project_container
PYTHON=$VENV_DIR/bin/python
MANAGE_PY=$PROJECT_DIR/manage.py"
    exit 1
fi

echo -e "\n -- 1 -- Changing working directory to $WORK_DIR ..."
cd "$WORK_DIR"

echo -e "\n -- 2 -- Fetching updates from GitHub ..."
git fetch

# Check if there are changes by pulling and checking for output indicating a change
GIT_PULL_OUTPUT=$(git pull origin main)

# If there were no changes, exit the script early
if [[ "$GIT_PULL_OUTPUT" == *"Already up to date."* ]]; then
  echo -e "\n -- No changes found. Exiting deployment script."
  exit 0
fi

echo -e "\n -- 3 -- Pulling changes into the local branch ..."
echo "$GIT_PULL_OUTPUT"

echo -e "\n -- 4 -- Activating Python virtual environment ..."
source "$VENV_DIR/bin/activate"

echo -e "\n -- 5 -- Making database migrations ..."
$PYTHON $MANAGE_PY makemigrations

echo -e "\n -- 6 -- Applying database migrations ..."
$PYTHON $MANAGE_PY migrate

echo -e "\n -- 7 -- Collecting static files"
$PYTHON $MANAGE_PY collectstatic --noinput

echo -e "\n -- 8 -- Deployment script completed successfully."

echo -e "\n -- 9 -- Don't forget to run: "

echo -e "\nsudo systemctl status gunicorn.service"

echo -e "\n -- 10 -- Don't forget to restart the gunicorn.service so the changes are applied to the website."

echo -e "\nsudo systemctl restart gunicorn.service\n"
