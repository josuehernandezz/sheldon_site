# Sheldon Site, Welcome to the Project!

Hello future lab member! My name is Josue C. Hernandez, and I built this site in the summer of 2024 for the Sheldon Research Group. I wrote this file to introduce you to using and updating this platform.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Next Steps](#next-steps)

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
   - **Python**: Familiarity with Python is necessary for working with the website.
   - **HTML, CSS, and JavaScript**: Knowledge of these languages is important if you plan to style the site or add new pages.

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

---

Thank you for being part of the lab! If you have any questions, feel free to reach out.


## Installation

To set up this project on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/josuehernandezz/sheldon_site.git
   cd sheldon_site

2. **Create and activate the virtual environment**:
   - **MacOS/Linux**:
   ```bash
   python - m venv venv
   source venv/bin/activate

   - **Windows**:
   python -m venv venv
   venv\Scripts\activate

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Change Directory and Start the Development Server**:
    ```bash
    cd project_container
    python manage.py runserver

## Usage

Editing the software is recommended only for those proficient in the technologies mentioned previously. If you wish to make updates to the website, it is advisable to create a new branch to ensure your changes do not affect the main website. Once you are satisfied with your edits, you can merge the branch into the main branch.

1. **To Create and Switch to a New Branch:**
    ```bash
    git branch NameOfFeatureBeingAdded
    git switch NameOfFeatureBeingAdded

Make your edits on the new branch until you are ready to merge with the main branch.

## Next Steps

1. **Log into the EC2 instance and fetch the latest changes:**
    ```bash
    git fetch
    git pull origin main

2. **Restart the website with the following command:**
    ```bash
    sudo systemctl restart gunicorn.service
