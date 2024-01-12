# GitHub X Integration

This Python application integrates GitHub webhooks with X to automatically tweet when a new GitHub repository is created.

## Setup

1. *Clone the Repository:*

    bash
    git clone https://github.com/yourusername/github-X-integration.git
    cd github-X-integration
    

2. *Install Dependencies:*

    bash
    pip install Flask tweepy
    

3. *Replace Placeholder Values:*

    Replace the following placeholder values in the script with your actual credentials:

    - X_API_KEY: Your X API key.
    - X_API_SECRET: Your X API secret.
    - X_ACCESS_TOKEN: Your X access token.
    - X_ACCESS_SECRET: Your X access token secret.
    - GITHUB_WEBHOOK_SECRET: Your GitHub webhook secret.

## Usage

1. *Run the Application:*

    bash
    python yourscript.py
    

2. *Configure GitHub Webhook:*

    Configure a GitHub webhook to point to http://localhost:5000/github-webhook.

3. *Create a New GitHub Repository:*

    The application will automatically tweet about the new repository.

## Features

- Webhook endpoint (/github-webhook) for GitHub events.
- Tweets about new GitHub repositories using Tweepy and the X API.
- Validates GitHub webhook payloads for security.

## Configuration

Replace the "yourusername" and "github-X-integration" placeholders with your GitHub username and the desired repository name.

## Webhook Security

The application validates GitHub webhook payloads using HMAC for security.

## Important Note

Ensure that you have the necessary permissions to use the X API and adhere to X's terms of service. Additionally, respect GitHub's terms of service and the privacy of users when using webhooks.

## License

This project is licensed under the [MIT License](LICENSE).