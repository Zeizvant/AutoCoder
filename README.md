# Autocoder Bot Action 🤖

An AI-powered GitHub Action that transforms GitHub Issues into production-ready code. By leveraging OpenAI's ChatGPT, this action parses issue descriptions, generates the requested file structure, and submits it back to your repository as a **Pull Request**.



## 🚀 Features

* **Issue-to-Code**: Converts natural language descriptions into directory structures and files.
* **Automated PRs**: Creates a new branch and submits a Pull Request for review.
* **Customizable**: Works with any language or framework requested in the issue body.
* **Clean Integration**: Uses a composite action to keep your workflow files organized.

## 🛠️ Setup

### 1. Requirements
* An **OpenAI API Key**.
* A processing script (e.g., `script.sh`) located in your repository.
* A label in your repository named `autocoder-bot`.

### 2. Configure Secrets
Navigate to your repository **Settings > Secrets and variables > Actions** and add:
* `OPENAI_API_KEY`: Your secret key from OpenAI.

### 3. Permissions
For the bot to create branches and PRs, you must ensure your workflow has write permissions. Add this to your workflow file:
```yaml
permissions:
  contents: write
  pull-requests: write
