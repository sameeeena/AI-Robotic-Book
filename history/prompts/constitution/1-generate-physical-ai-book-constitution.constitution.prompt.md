---
id: 1
title: Generate Physical AI Book Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: unknown
command: /sp.constitution
labels: ["book", "constitution", "physical-ai", "humanoid-robots"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

You are to generate the file `sp.constitution.md` for a beginner-level technical book titled **Physical AI and Humanoid Robots**.
Create a strict writing constitution that Claude Code must follow for generating all future content.

Your output must include:

## 1. Tone & Style Rules
- Beginner-friendly
- Clear, simple explanations
- No complex math unless required and always explained
- Use analogies where helpful
- Use clean formatting and short paragraphs
- Always avoid unnecessary jargon

## 2. Structure Rules
- Book length: 6–8 chapters
- Each chapter must include:
  - Overview
  - Key concepts
  - Illustrations/diagrams (ASCII or described)
  - Simple examples
  - FAQ section
  - Quick summary

## 3. Technical Depth
The book must be beginner-friendly but still technically accurate. Include:
- What humanoid robots are
- Sensors, motors, balance, movement
- Basics of Physical AI
- Simple AI concepts (vision, speech, control loops)
- Simple robotics coding examples (pseudo-code only)

## 4. Visual & Diagram Rules
- Provide diagrams using ASCII or descriptive text
- Keep them simple
- No copyrighted diagrams or images

## 5. Ethical Rules
- No dangerous robotics instructions
- Nothing harmful, biological, weaponized or unsafe
- Educational purpose only

## 6. Formatting Rules
- Use markdown headers
- Use lists and tables where needed
- Keep formatting consistent
- Use code blocks for pseudo-code

## 7. Consistency Rules
- Maintain the same writing style across the entire book
- Keep terminology consistent
- Clarify terms on first uOverview
  - Key concepts
  - Illustrations/diagrams (ASCII or described)
  - Simple examples
  - FAQ section
  - Quick summary

## 3. Technical Depth
The book must be beginner-friendly but still technically accurate. Include:
- What humanoid robots are
- Sensors, motors, balance, movement
- Basics of Physical AI
- Simple AI concepts (vision, speech, control loops)
- Simple robotics coding examples (pseudo-code only)

## 4. Visual & Diagram Rules
- Provide diagrams using ASCII or descriptive text
- Keep them simple
- No copyrighted diagrams or images

## 5. Ethical Rules
- No dangerous robotics instructions
- Nothing harmful, biological, weaponized or unsafe
- Educational purpose only

## 6. Formatting Rules
- Use markdown headers
- Use lists and tables where needed
- Keep formatting consistent
- Use code blocks for pseudo-code

## 7. Consistency Rules
- Maintain the same writing style across the entire book
- Keep terminology consistent
- Clarify terms on first use

## 8. Content Boundaries
The book must NOT include:
- Advanced robotics engineering
- Detailed electrical wiring
- Dangerous mechanical instructions
- Confidential or proprietary info

## 9. Final Guarantee
Claude Code must use this constitution for:
- Writing all book chapters
- Adding diagrams
- Generating examples
- Creating summaries
- Ensuring educational clarity

Generate the full constitution in clear markdown.

## Response snapshot

Successfully generated the "Physical AI and Humanoid Robots Book Constitution" at .specify/memory/constitution.md with version 1.0.0.

## Outcome

- ✅ Impact: Constitution generated and saved.
- 🧪 Tests: N/A
- 📁 Files: Created .specify/memory/constitution.md
- 🔁 Next prompts: Next step will be to use this constitution for book content.
- 🧠 Reflection: Successfully generated the constitution based on user requirements and template.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
