# Tasks: Physical AI and Humanoid Robots Book + Docusaurus + RAG

**Input**: Design documents from `specs/001-deployment-testing/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: The feature specification requested comprehensive testing. Therefore, relevant test tasks will be included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic Docusaurus setup.

- [ ] T001 Install Docusaurus in `frontend/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core backend infrastructure and initial Docusaurus configuration that MUST be complete before any user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T002 Create backend folder `backend/`
- [ ] T003 Build Express server in `backend/src/app.js`
- [ ] T004 Connect Qdrant in `backend/src/services/qdrant.js`
- [ ] T005 Add environment variables configuration for backend in `backend/.env` and `backend/src/config.js`
- [ ] T006 Update Docusaurus sidebar configuration in `frontend/docusaurus.config.js`
- [ ] T007 Customize Docusaurus theme in `frontend/src/css/custom.css`
- [ ] T008 Add Docusaurus homepage content in `frontend/src/pages/index.js`
- [ ] T009 Add translation switch UI in `frontend/src/components/TranslationSwitch.js`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Verify Backend Deployment (Priority: P1) 🎯 MVP

**Goal**: Ensure the backend is deployable and functional with RAG capabilities.

**Independent Test**: Successfully deploy the backend and verify the `/embed` and `/query` endpoints are accessible and functional.

### Tests for User Story 1

- [ ] T010 [P] [US1] Integration test for `/embed` route in `backend/tests/integration/embed.test.js`
- [ ] T011 [P] [US1] Integration test for `/query` route in `backend/tests/integration/query.test.js`

### Implementation for User Story 1

- [ ] T012 [P] [US1] Add `/embed` route in `backend/src/api/embed.js`
- [ ] T013 [P] [US1] Add `/query` route in `backend/src/api/query.js`
- [ ] T014 [P] [US1] Create frontend chatbot UI in `frontend/src/pages/chat.js`
- [ ] T015 [US1] Add text input component for chatbot in `frontend/src/components/ChatInput.js`
- [ ] T016 [US1] Connect chatbot to backend `/query` route in `frontend/src/components/Chatbot.js`
- [ ] T017 [US1] Add loading state to chatbot UI in `frontend/src/components/Chatbot.js`
- [ ] T018 [US1] Add difficulty toggle to chatbot UI in `frontend/src/components/Chatbot.js`
- [ ] T019 [US1] Add language selector to chatbot UI in `frontend/src/components/Chatbot.js`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Comprehensive Application Testing (Priority: P1)

**Goal**: Ensure all book content and core Docusaurus features are in place and working, including translation.

**Independent Test**: Verify all chapters are generated, Docusaurus content is loaded, and translation is functional.

### Tests for User Story 2

- [ ] T020 [P] [US2] E2E test for chapter navigation in `frontend/tests/e2e/chapters.test.js`
- [ ] T021 [P] [US2] E2E test for search functionality in `frontend/tests/e2e/search.test.js`
- [ ] T022 [P] [US2] E2E test for translation functionality in `frontend/tests/e2e/translation.test.js`

### Implementation for User Story 2

- [ ] T023 [P] [US2] Generate 8 chapters in `frontend/docs/chapters/`
- [ ] T024 [P] [US2] Add diagrams for each chapter in `frontend/docs/chapters/`
- [ ] T025 [P] [US2] Add examples for each chapter in `frontend/docs/chapters/`
- [ ] T026 [P] [US2] Write FAQ section for each chapter in `frontend/docs/chapters/`
- [ ] T027 [P] [US2] Write introduction and conclusion in `frontend/docs/intro.md` and `frontend/docs/conclusion.md`
- [ ] T028 [P] [US2] Write About page content in `frontend/src/pages/about.js`
- [ ] T029 [P] [US2] Add generated chapters to Docusaurus `frontend/docs/`
- [ ] T030 [US2] Add chat page to Docusaurus navigation in `frontend/docusaurus.config.js`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final review, cleanup, and deployment tasks.

- [ ] T031 Configure GitHub Pages deployment for `frontend/`
- [ ] T032 Deploy the Docusaurus site to GitHub Pages
- [ ] T033 Deploy the backend to Vercel/Render
- [ ] T034 Comprehensive final testing of the deployed application (chapters, chatbot, search, translation, deployment itself)
- [ ] T035 Documentation updates in `docs/` (if any changes were made during implementation)
- [ ] T036 Code cleanup and refactoring across `frontend/` and `backend/`
- [ ] T037 Security hardening for `backend/`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - Integrates with US1 for the chat page and translation switch, but content generation can be parallel.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models/Endpoints/Content within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Integration test for /embed route in backend/tests/integration/embed.test.js"
Task: "Integration test for /query route in backend/tests/integration/query.test.js"

# Launch initial implementation tasks for User Story 1 together:
Task: "Add /embed route in backend/src/api/embed.js"
Task: "Add /query route in backend/src/api/query.js"
Task: "Create frontend chatbot UI in frontend/src/pages/chat.js"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (Backend deployment & chatbot integration)
   - Developer B: User Story 2 (Book content generation & Docusaurus content integration)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence