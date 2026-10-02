# AI Prompt Version Control
AI Prompt Version Control is a Flask and MySQL-based web application designed to store, manage, search, and track different versions of AI prompts.

## Prompt Versioning
Each prompt can have multiple versions.

For example:
**Version 1**  
Explain this topic in simple words.
↓  
**Version 2**  
Explain this topic in simple words with a real-life example.
↓  
**Version 3**  
Explain this topic in simple words with a real-life example and a simple analogy.
All versions are stored separately, allowing the user to see how a prompt has evolved over time.

## Database
The project uses **MySQL** as the backend database.

### prompts
The `prompts` table stores the main information about each prompt, including:

- `prompt_id`
- `dataset_id`
- `instruction`
- `context`
- `category`
- `dataset_source`

### prompt_versions
The `prompt_versions` table stores the different versions of each prompt, including:

- `version_id`
- `prompt_id`
- `version_number`
- `prompt_text`
- `change_description`
The `prompt_id` connects each prompt with its corresponding versions.

## Dataset
The project uses the **Dolly 15K dataset** as the initial source of prompts.
The dataset contains instructions, contexts, and categories that are imported into the MySQL database and used by the application.

## Local Execution
The application can be run locally using Flask and MySQL.

### Run the Application
python app.py
The application is currently configured for local execution.

###Technologies Used
- Python – Application logic
- Flask – Web application framework
- MySQL – Database management
- HTML & CSS – Frontend
- Jinja2 – Dynamic HTML rendering
- GitHub – Source code management

