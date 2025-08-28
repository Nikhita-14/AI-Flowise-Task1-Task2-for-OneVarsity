# Task 2 – Flowise Custom Node: Keyword Extractor

## What It Does

This custom node uses the `compromise` NLP library to extract keywords (nouns) from input text.

## How to Use

1. Clone Flowise from GitHub
2. Place the node in `packages/components/nodes/custom/`
3. Register it in `index.ts`
4. Rebuild Flowise:
   ```bash
   pnpm install
   pnpm build
   pnpm dev
```
Create a new flow in Flowise UI

Add:

Text Input → Keyword Extractor → Output

Export your flow as sample_flow.json