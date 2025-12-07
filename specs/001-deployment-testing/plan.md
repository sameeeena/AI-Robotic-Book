# Implementation Plan: Physical AI and Humanoid Robots Book + Docusaurus + RAG

**Branch**: `001-deployment-testing` | **Date**: 2025-12-07 | **Spec**: specs/001-deployment-testing/spec.md
**Input**: Feature specification from `/specs/001-deployment-testing/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The project involves creating an 8-chapter book on Physical AI and Humanoid Robots, hosted on a Docusaurus website. It will include a RAG-enabled chatbot for interactive content and will support translation and personalization. The deployment will utilize GitHub Pages for the frontend and Vercel/Render for the backend, followed by comprehensive final testing of all features.

## Technical Context

**Language/Version**: Node.js 24.11
**Primary Dependencies**: Express.js, OpenAI SDK, Qdrant Client, Docusaurus, React
**Storage**: Qdrant (vector database for RAG), Local filesystem (Docusaurus content)
**Testing**: Dedicated testing of chapters, chatbot, search, translation, and overall deployment using Jest + React Testing Library (Unit/Integration) and Playwright (E2E)
**Target Platform**: GitHub Pages (Frontend), Vercel/Render (Backend)
**Project Type**: Web application (Frontend + Backend)
**Performance Goals**: Backend 99.9% uptime within 5 minutes of successful deployment; entire deployment process completes within 10 minutes.
**Constraints**: Secure management and injection of environment keys for backend.
**Scale/Scope**: 8-chapter book, RAG-enabled chatbot, support for multiple languages and personalization options.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Tone & Style**: Beginner-friendly explanations, minimal jargon, clear formatting. (PASS)
- **II. Structure**: 6-8 chapters, each with overview, key concepts, diagrams, examples, FAQ, summary. (PASS)
- **III. Technical Depth**: Beginner-friendly yet technically accurate; pseudo-code examples. (PASS)
- **IV. Visual & Diagram Rules**: ASCII art/descriptive text for diagrams; no copyrighted images. (PASS)
- **V. Ethical Rules**: No dangerous instructions, harmful content; educational purpose only. (PASS)
- **VI. Formatting Rules**: Consistent markdown, code blocks for pseudo-code. (PASS)
- **VII. Consistency Rules**: Uniform terminology, new terms clarified. (PASS)
- **VIII. Content Boundaries**: No advanced engineering, wiring, dangerous instructions, proprietary info. (PASS)
- **IX. Final Guarantee**: Claude Code adherence to constitution. (PASS)

## Project Structure

### Documentation (this feature)

```text
specs/001-deployment-testing/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
.specify/
backend/
├── src/
│   ├── api/             # Express routes for RAG, chatbot, translation
│   ├── services/        # OpenAI, Qdrant integration, business logic
│   └── utils/           # Helper functions
├── tests/
│   ├── unit/
│   └── integration/
docs/                    # Docusaurus chapter content
frontend/                # Docusaurus project root
├── src/
│   ├── components/      # React components for chatbot, UI elements
│   ├── pages/           # Docusaurus pages (e.g., chat.js)
│   └── theme/           # Docusaurus theme customizations
├── static/
└── docusaurus.config.js
history/
node_modules/
package.json
pages/
rag-backend/             # This will be `backend/` as per the chosen structure
```

**Structure Decision**: The project will adopt a split frontend/backend structure. The Docusaurus site will reside in the `frontend/` directory, containing the book chapters within `frontend/docs/` and custom pages/components. The RAG and chatbot backend will be developed within a `backend/` directory, using Node.js/Express, and will house API endpoints, services for OpenAI/Qdrant integration, and utilities.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
|           |            |                                     |
