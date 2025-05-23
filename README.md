# AI FAQ Builder

[Live App →](https://ai-faq-builder.streamlit.app)  
AI FAQ Builder is a simple web application that lets you upload PDF documents and automatically generates frequently asked questions (FAQs) from the content using OpenAI's GPT models. It is built with Streamlit for easy deployment and user interaction.

## Overview

This tool is designed to help users quickly extract useful information from lengthy documents. It is ideal for summarizing content into FAQ-style questions that can be used for customer support, training, documentation, and more.

## How to Run

1. Clone the repository

   git clone https://github.com/amnaabbasi03/ai-faq-builder.git
   cd ai-faq-builder

2. Create a .env file

   Create a file named `.env` in the project root and add your OpenAI API key in the following format:

   OPENAI_API_KEY=your-api-key-here

   You can refer to `.env.example` for guidance. Make sure not to upload your real `.env` file to GitHub.

3. Install the required Python packages

   pip install -r requirements.txt

   If you encounter any encryption-related errors, also install:

   pip install pycryptodome

4. Start the Streamlit app

   streamlit run app.py

   The app will open in your web browser. You can upload your PDF, and it will generate a list of FAQs you can download as a text file.

## Use Cases

- HR teams generating FAQs from employee handbooks
- Legal departments summarizing contracts
- Educators creating questions from reading materials
- Startups creating help center content from technical documents
- Government offices and agencies automating responses to citizen queries

## Disclaimer

This is a demonstration project meant for educational and prototyping purposes. It is not optimized for production use. Ensure you handle API keys securely and do not upload sensitive or confidential documents without proper safeguards.

