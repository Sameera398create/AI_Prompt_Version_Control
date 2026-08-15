# AI Prompt Version Control
## About the Project
AI prompts are often modified and improved multiple times while developing AI applications. If an old prompt is simply replaced, it becomes difficult to know what was changed, why it was changed, or what the previous version looked like.
AI Prompt Version Control** is a web-based application that helps store, manage, and track different versions of AI prompts using a MySQL database.
Instead of overwriting an existing prompt, the system stores the updated prompt as a new version while keeping the previous versions available. This makes it easier to track the evolution of a prompt and compare different versions.

## How It Works
text
User
  ↓
Flask Web Application
  ↓
MySQL Database
  ↓
Search / View Prompts
  ↓
View Version History
  ↓
Create New Version
  ↓
Store Changes
  ↓
Compare Versions

For example:
Version 1
Explain this topic in simple words.

        ↓

Version 2
Explain this topic in simple words with a real-life example.

        ↓

Version 3
Explain this topic in simple words with a real-life example
and a simple analogy.
All versions are stored separately, allowing the user to see how the prompt has evolved over time.

#Database
The project uses MySQL as the backend database.

prompts

The prompts table stores the main information about each prompt, including:

prompt_id
dataset_id
instruction
context
category
dataset_source
prompt_versions

The prompt_versions table stores the different versions of each prompt, including:

version_id
prompt_id
version_number
prompt_text
change_description

The prompt_id connects each prompt with its corresponding versions.

#Dataset
The project uses the Dolly 15K dataset as the initial source of prompts.
The dataset contains instructions, contexts, and categories that are imported into the MySQL database and used by the application.

#Deployment
The application is deployed using Railway and connected to a MySQL database through environment variables.

## Live Demo
[AI Prompt Version Control - Live Demo](https://aipromptversioncontrol-production.up.railway.app)

##Technologies Used
Python – Application logic
Flask – Web application framework
MySQL – Database management
HTML & CSS – Frontend
Jinja2 – Dynamic HTML rendering
GitHub – Source code management
Railway – Application deployment

