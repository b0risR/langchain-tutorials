# langchain-tutorials
Executed (and edited) langchain academy notebooks

## Branches

This repository organizes course work by branch. `main` only holds this README; the notebooks and code live on per-course branches.

- [`lca-lc-foundations`](https://github.com/b0risR/langchain-tutorials/tree/lca-lc-foundations) — LangChain Academy: LangChain Foundations

## `lca-lc-foundations` file structure

```
├── notebooks/
│   ├── module-1/
│   │   ├── resources/
│   │   │   └── moon.png
│   │   ├── 1.1_foundational_models.ipynb
│   │   ├── 1.1_prompting.ipynb
│   │   ├── 1.2_tools.ipynb
│   │   ├── 1.2_web_search.ipynb
│   │   ├── 1.3_memory.ipynb
│   │   ├── 1.4_multimodal_messages.ipynb
│   │   ├── 1.5_personal_chef.ipynb
│   │   ├── 1.5_personal_chef.py
│   │   └── langgraph.json
│   ├── module-2/
│   │   ├── resources/
│   │   │   ├── 2.1_mcp_server.py
│   │   │   ├── acmecorp-employee-handbook.pdf
│   │   │   └── Chinook.db
│   │   ├── 2.1_mcp.ipynb
│   │   ├── 2.1_travel_agent.ipynb
│   │   ├── 2.2_runtime_context.ipynb
│   │   ├── 2.2_state.ipynb
│   │   ├── 2.3_multi_agent.ipynb
│   │   ├── 2.4_wedding_planners.ipynb
│   │   ├── bonus_rag.ipynb
│   │   └── bonus_sql.ipynb
│   └── module-3/
│       ├── agent-chat-ui/
│       │   ├── .github/
│       │   │   └── workflows/
│       │   │       └── ci.yml
│       │   ├── public/
│       │   │   └── logo.png
│       │   ├── src/
│       │   │   ├── app/
│       │   │   │   ├── api/
│       │   │   │   │   └── [..._path]/
│       │   │   │   │       └── route.ts
│       │   │   │   ├── globals.css
│       │   │   │   ├── layout.tsx
│       │   │   │   └── page.tsx
│       │   │   ├── components/
│       │   │   │   ├── icons/
│       │   │   │   │   ├── github.tsx
│       │   │   │   │   └── langgraph.tsx
│       │   │   │   ├── thread/
│       │   │   │   │   ├── agent-inbox/
│       │   │   │   │   │   ├── components/
│       │   │   │   │   │   │   ├── inbox-item-input.tsx
│       │   │   │   │   │   │   ├── state-view.tsx
│       │   │   │   │   │   │   ├── thread-actions-view.tsx
│       │   │   │   │   │   │   ├── thread-id.tsx
│       │   │   │   │   │   │   └── tool-call-table.tsx
│       │   │   │   │   │   ├── hooks/
│       │   │   │   │   │   │   └── use-interrupted-actions.tsx
│       │   │   │   │   │   ├── index.tsx
│       │   │   │   │   │   ├── types.ts
│       │   │   │   │   │   └── utils.ts
│       │   │   │   │   ├── history/
│       │   │   │   │   │   └── index.tsx
│       │   │   │   │   ├── messages/
│       │   │   │   │   │   ├── ai.tsx
│       │   │   │   │   │   ├── generic-interrupt.tsx
│       │   │   │   │   │   ├── human.tsx
│       │   │   │   │   │   ├── shared.tsx
│       │   │   │   │   │   └── tool-calls.tsx
│       │   │   │   │   ├── artifact.tsx
│       │   │   │   │   ├── ContentBlocksPreview.tsx
│       │   │   │   │   ├── index.tsx
│       │   │   │   │   ├── markdown-styles.css
│       │   │   │   │   ├── markdown-text.tsx
│       │   │   │   │   ├── MultimodalPreview.tsx
│       │   │   │   │   ├── syntax-highlighter.tsx
│       │   │   │   │   ├── tooltip-icon-button.tsx
│       │   │   │   │   └── utils.ts
│       │   │   │   └── ui/
│       │   │   │       ├── avatar.tsx
│       │   │   │       ├── button.tsx
│       │   │   │       ├── card.tsx
│       │   │   │       ├── input.tsx
│       │   │   │       ├── label.tsx
│       │   │   │       ├── password-input.tsx
│       │   │   │       ├── separator.tsx
│       │   │   │       ├── sheet.tsx
│       │   │   │       ├── skeleton.tsx
│       │   │   │       ├── sonner.tsx
│       │   │   │       ├── switch.tsx
│       │   │   │       ├── textarea.tsx
│       │   │   │       └── tooltip.tsx
│       │   │   ├── hooks/
│       │   │   │   ├── use-file-upload.tsx
│       │   │   │   └── useMediaQuery.tsx
│       │   │   └── providers/
│       │   │       ├── client.ts
│       │   │       ├── Stream.tsx
│       │   │       └── Thread.tsx
│       │   ├── .codespellignore
│       │   ├── .dockerignore
│       │   ├── .env.example
│       │   ├── .gitignore
│       │   ├── .prettierignore
│       │   ├── components.json
│       │   ├── eslint.config.js
│       │   ├── LICENSE
│       │   ├── next.config.mjs
│       │   ├── package.json
│       │   ├── pnpm-lock.yaml
│       │   ├── postcss.config.mjs
│       │   ├── prettier.config.js
│       │   ├── README.md
│       │   ├── tailwind.config.js
│       │   └── tsconfig.json
│       ├── resources/
│       │   └── Chinook.db
│       ├── 3.2_managing_messages.ipynb
│       ├── 3.3_hitl.ipynb
│       ├── 3.4_dynamic_models.ipynb
│       ├── 3.4_dynamic_prompts.ipynb
│       ├── 3.4_dynamic_tools.ipynb
│       ├── 3.5_email_agent.ipynb
│       ├── 3.5_email_agent.py
│       └── langgraph.json
├── .env.example
├── .gitignore
├── env_utils.py
├── example.env
├── LICENSE
├── pyproject.toml
├── README.md
├── requirements.txt
└── uv.lock
```
