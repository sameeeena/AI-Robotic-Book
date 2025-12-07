# Implementation Plan

This document outlines the step-by-step instructions for building the Humanoid Robotic Book project.

## 1. Docusaurus Setup Instructions

### 1.1 Create Docusaurus Project
- **Action**: Initialize a new Docusaurus project.
- **Details**: `npx create-docusaurus@latest my-website classic`

### 1.2 Add Chapters to /docs
- **Action**: Create markdown files for each chapter in the `docs/` directory.
- **Details**:
    - `docs/chapter-1.md`
    - `docs/chapter-2.md`
    - ... (for all planned chapters)

### 1.3 Update sidebars.js
- **Action**: Configure the `sidebars.js` file to include all chapters in the documentation sidebar.
- **Details**: Ensure each chapter (`chapter-N`) is correctly linked and ordered in the sidebar.

### 1.4 Edit Homepage
- **Action**: Customize the `src/pages/index.js` (or similar) file to reflect the project's branding and purpose.
- **Details**: Add a compelling introduction, project overview, and call-to-action for the book.

### 1.5 Add Navbar Items
- **Action**: Modify the `docusaurus.config.js` file to add necessary items to the navigation bar.
- **Details**: Include links to "Documentation", "Chatbot", and any other relevant sections.

## 2. Book Content Implementation

For each chapter (e.g., `chapter-N.md`):

### 2.1 Create chapter-N.md
- **Action**: Create the markdown file for the specific chapter.
- **Details**: The file should be located at `docs/chapter-N.md`.

### 2.2 Add Overview
- **Action**: Write a comprehensive overview of the chapter's topic.
- **Details**: Introduce key concepts and learning objectives.

### 2.3 Add Diagrams
- **Action**: Incorporate relevant diagrams and illustrations to explain complex concepts.
- **Details**: Use markdown image syntax `![Alt Text](path/to/image.png)`. Consider using tools like Mermaid.js for embedded diagrams if supported by Docusaurus.

### 2.4 Add Examples
- **Action**: Provide clear and concise code examples where applicable.
- **Details**: Use fenced code blocks with language highlighting.

### 2.5 Add Summary
- **Action**: Conclude the chapter with a summary of key takeaways.
- **Details**: Reiterate important points and link to subsequent chapters or related resources.

### 2.6 Follow Constitution Rules
- **Action**: Ensure all content adheres to the project's code quality, testing, performance, security, and architecture principles as defined in `.specify/memory/constitution.md`.
- **Details**: Pay attention to clarity, accuracy, and consistency.

## 3. RAG Backend Implementation

### 3.1 Create /rag-backend/index.js
- **Action**: Initialize the main entry point for the RAG backend.
- **Details**: Create the file `rag-backend/index.js`.

### 3.2 Add Express
- **Action**: Set up an Express.js server to handle API requests.
- **Details**: `npm install express` and configure basic server boilerplate.

### 3.3 Add OpenAI + embeddings
- **Action**: Integrate OpenAI API for generating embeddings.
- **Details**: `npm install openai` and configure client with API key. Implement functions to take text input and return embedding vectors.

### 3.4 Add Qdrant Client
- **Action**: Integrate Qdrant client for vector database operations.
- **Details**: `npm install @qdrant/qdrant-js` (or similar) and configure connection to Qdrant instance.

### 3.5 Create /embed Route
- **Action**: Implement an API endpoint to embed book content into the Qdrant vector database.
- **Details**:
    - **Method**: `POST /embed`
    - **Input**: JSON payload with `chapter_id` and `text_content`.
    - **Process**: Generate embeddings for `text_content` using OpenAI, then store in Qdrant with `chapter_id` as metadata.

### 3.6 Create /query Route
- **Action**: Implement an API endpoint to query the vector database for relevant information.
- **Details**:
    - **Method**: `POST /query`
    - **Input**: JSON payload with `user_query` and `difficulty`, `language` filters.
    - **Process**: Generate embedding for `user_query`, query Qdrant for similar vectors, retrieve original text segments, and potentially use OpenAI for generating a natural language response.

### 3.7 Export Routes
- **Action**: Export all defined API routes from `rag-backend/index.js`.
- **Details**: Ensure the Express app uses these routes.

## 4. Chatbot Page Implementation

### 4.1 Create /src/pages/chat.js
- **Action**: Create the React component for the chatbot interface.
- **Details**: File should be `src/pages/chat.js` within the Docusaurus project.

### 4.2 Add Input Box
- **Action**: Implement a text input field for user queries.
- **Details**: Allow users to type their questions.

### 4.3 Add Chat Bubbles
- **Action**: Design and implement UI components to display chat messages (user questions and bot responses).
- **Details**: Distinguish between user and bot messages visually.

### 4.4 Add Difficulty Dropdown
- **Action**: Include a dropdown menu to select the desired response difficulty.
- **Details**: Options could include "Beginner", "Intermediate", "Advanced". This will be passed to the RAG backend.

### 4.5 Add Language Selector
- **Action**: Implement a selector for the response language.
- **Details**: Options could include "English", "Spanish", etc. This will be passed to the RAG backend for potential translation or language-specific retrieval.

### 4.6 Fetch from Backend
- **Action**: Integrate the chatbot frontend with the RAG backend.
- **Details**: Use `fetch` or `axios` to send user queries to the `/query` endpoint and display the responses.

## 5. Deployment Implementation

### 5.1 GitHub Pages (Frontend)

#### 5.1.1 Set Repository Name
- **Action**: Ensure the Docusaurus configuration (likely `docusaurus.config.js`) has the correct `basename` or `url` for GitHub Pages.
- **Details**: Set `url: 'https://<username>.github.io'`, `baseUrl: '/<repo-name>/'`.

#### 5.1.2 Configure Deployment Branch
- **Action**: Set up GitHub Actions or adjust `package.json` scripts to deploy the built Docusaurus site to the `gh-pages` branch.
- **Details**: Configure the workflow to build the project and push the output to the `gh-pages` branch on every push to the main branch.

### 5.2 Backend Deployment

#### 5.2.1 Deploy to Vercel/Render
- **Action**: Deploy the `rag-backend` (Node.js/Express) to a cloud platform like Vercel or Render.
- **Details**: Configure the deployment to point to the `rag-backend` directory and run `npm start` or similar.

#### 5.2.2 Add Environment Keys
- **Action**: Configure environment variables on the deployment platform.
- **Details**: Add `OPENAI_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY` (if applicable), and any other sensitive keys.

## 6. Final Testing

### 6.1 Test Each Chapter
- **Action**: Manually review each chapter in the deployed Docusaurus site.
- **Details**: Verify content accuracy, formatting, diagram rendering, and example code.

### 6.2 Test Chatbot
- **Action**: Interact with the chatbot on the `/chat` page.
- **Details**:
    - Test various queries, including edge cases.
    - Verify difficulty and language selections work as expected.
    - Check for accurate and relevant responses from the RAG backend.

### 6.3 Test Search
- **Action**: Utilize Docusaurus's built-in search functionality (if configured).
- **Details**: Verify that searching for keywords from different chapters yields correct results.

### 6.4 Test Translation
- **Action**: If multi-language support is implemented, test chapter content and chatbot responses in different languages.
- **Details**: Ensure all translated content is accurate and culturally appropriate.

### 6.5 Test Deployment
- **Action**: Verify both the frontend (GitHub Pages) and backend (Vercel/Render) are accessible and functional.
- **Details**: Check all links, images, and API calls are working correctly in the deployed environment.