# Sheldon Site, Welcome to the Project!

Hello future lab member,

This website was built by Josue C. Hernandez in the summer of 2024 for the Sheldon Research Group. I wrote this file to introduce you to using and updating the website (if necessary) so you are not completely lost.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Tech Stack](#tech-stack)
4. [Managing Content](#managing-content)
5. [Caution](#caution)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Updating the site](#pushing-updates-to-the-website)

## Introduction

# Welcome to the Lab Website!

The purpose of this code is to run our lab's website, designed to share our research and recruit future lab members. In the future, we may also utilize this site to display group resource usage, such as instrument reservations and logging group activities.

## Prerequisites

Before proceeding, it’s essential that the person managing the website is comfortable with the following:

1. **Command Line Interface**:

   - **MacOS/Linux**: Use the Terminal application.
   - **Windows**: Use Windows PowerShell or Command Prompt.

   If you’re unfamiliar with command line usage, I recommend learning these basics or having a more proficient lab member assist you.

2. **Programming Knowledge**:
   - **Python**: Familiarity with Python is necessary for making edits to the website.
   - **HTML, CSS (Tailwind CSS), and JavaScript**: Knowledge of these languages is important if you plan to style the site or add new pages.

## Tech Stack

Here’s a brief overview of the technology stack used for this website:

- **Operating System**: Ubuntu server running on an AWS EC2 instance.
- **Web Server**: Nginx.
- **WSGI**: Gunicorn.
- **Web Framework**: Django.
- **Frontend Styling**:
  - Uses Django's built-in template logic for dynamic components.
  - Integrates TailwindCSS for easy styling.
  - Employs Django-compressor to optimize static file serving.

## Managing Content

The site is designed to be user-friendly for non-technical users through the Sheldon Group admin panel. You can easily edit various components:

- **Adding a Lab Member**:
  - Click on the "Lab Members" link to view a table of all members.
  - Edit a specific member by clicking on their name.
  - To add a new member, click the "Add Lab Member" button at the top right of the Lab Members section.

A similar process applies for editing or adding other items in the side panel.

## Caution

I do not recommend editing the code unless you are confident in your abilities with the following technologies:

- Command line interface
- Git/GitHub
- Python
- Django web framework and its general concepts

## Installation

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/josuehernandezz/sheldon_site.git
   cd sheldon_site

   ```

2. **Create and activate the virtual environment**:

   - **MacOS/Linux**:

   ```bash
   python -m venv venv
   source venv/bin/activate

   - **Windows**:
   python -m venv venv
   venv\Scripts\activate

   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt

   ```

You will need to create a file that is called '.env' This is a special file that holds secret information. If you are setting this up for the first time, you can create a text file in your coding environment exactly like '.env', then you need to add a SECRET_KEY and DEBUG value.

You will need to generate a new secret key.

4. **Generate Secret Key**
   ```bash
   openssl rand -base64 64
   ```

The out put value will look something like this:
kz5MIGsfVyQYCJ06cSGimTg4G/Gh2pPcO4c3jmT2S9AWP+smMNOgQQM01yN4OQyq
14DG7roq+xfc0KV+TELYqQ==

In your .env file you would then add this line:

SECRET_KEY=kz5MIGsfVyQYCJ06cSGimTg4G/Gh2pPcO4c3jmT2S9AWP+smMNOgQQM01yN4OQyq14DG7roq+xfc0KV+TELYqQ==

Notice that I removed the indentation and made it all in one line.
For your DEBUG variable, set it to this:

DEBUG=False

The contents of your .env file should then be:

5. **Contents of .env File**:
   ```bash
    SECRET_KEY=kz5MIGsfVyQYCJ06cSGimTg4G/Gh2pPcO4c3jmT2S9AWP+smMNOgQQM01yN4OQyq14DG7roq+xfc0KV+TELYqQ==
    DEBUG=False
   ```

Then you can go ahead and start the development server as shown below..

6. **Change Directory and Start the Development Server**:
   ```bash
   cd project_container
   python manage.py runserver
   ```

I cannot teach every single aspect about making changes to the website or that would be to large to include in a simple README.md file. So you need to do your own research and teach yourself how to use django.

## Usage

Editing the software is recommended only for those proficient in the technologies mentioned previously. If you wish to make updates to the website, it is advisable to create a new branch to ensure your changes do not affect the main website. Once you are satisfied with your edits, you can merge the branch into the main branch.

1. **To Create and Switch to a New Branch:**
   ```bash
   git branch NameOfFeatureBeingAdded
   git switch NameOfFeatureBeingAdded
   ```

Make your edits on the new branch until you are ready to merge with the main branch.

NOTE: DO NOT DO THIS UNLESS YOU UNDERSTAND WHAT IS GOING ON. YOU CAN BREAK THE WEBSITE IF YOU DO NOT KNOW WHAT YOU ARE DOING.

2. **Commit Branch Changes:**
   ```bash
   git add .
   git commit -m 'This command will create a comment for the changes you made. Make sure it is descriptive!'
   ```

Once you have added your commit message to the new branch you made, merge those changes with main and push them to the remote repository on github.

3. **Merge Back to Main Branch:**
   ```bash
   git switch main
   git merge -m 'Merging changes from {the-branch-you-created}' {the-branch-you-created}
   git push origin main
   ```

The changes should now be pushed to github and you can follow the steps below to save those changes on the lab website.

## Pushing Updates To The Website

Log into the website server using SSH (this access needs to be given to you first by the previous lab member who had access).

The server admin will need to give you access by having you create an SSH key and having you copy your public key
to the ~/.ssh/authorized_keys file.

The link below allows you to sign in to your AWS account to access the server if there is any need to change ports for security reasons. NOTE: THIS IS ONLY RECOMMENDED IF YOU KNOW WHAT YOU ARE DOING. DO NOT MESS WITH ANYTHING YOU DON'T UNDERSTAND. THIS IS NOT REQUIRED FOR REGULAR WEBSITE MAINTENANCE.

https://uci.awsapps.com/start/#/?tab=accounts Or search for "uci aws account sign in" on your favorite search engine.

1. **Log into the EC2 instance and fetch the latest changes:**

   ```bash
   cd ~/sheldon_site
   git fetch
   git pull origin main

   ```

2. **Restart the website with the following command:**
   ```bash
   sudo systemctl restart gunicorn.service
   ```

---

Thank you for being part of the lab! If you have any questions, feel free to reach out.
