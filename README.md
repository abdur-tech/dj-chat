# DJ-Chat

DJ-Chat is a real-time chat application built with Django and Django Channels. It supports WebSocket connections for live messaging, making it a perfect fit for chat-based applications.

## Features

- Real-time messaging with WebSocket (WSS) support.
- User authentication and session management.
- Multi-user chat rooms.
- Asynchronous communication with Django Channels.


## Prerequisites

- Python 3.9.2
- PostgreSQL (optional if using a different database)


## Installation

1. **Clone the repository:**


   git clone https://github.com/abdur-tech/dj-chat.git

## Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

## Install the dependencies:

cd dj-chat
pip install -r requirements.txt


## Set up the database:

If you're using PostgreSQL, ensure it's running and create a database for the project. Update the DATABASES setting in settings.py with your credentials.

## Apply migrations:

python manage.py makemigrations
python manage.py migrate

## Create a superuser:

python manage.py createsuperuser

## Run the development server:

python manage.py runserver

Open your browser and navigate to http://127.0.0.1:8000/ to see the application.

