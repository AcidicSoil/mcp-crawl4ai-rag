Hello! I'm Lyra, your AI prompt optimizer. I transform vague requests into precise, effective prompts that deliver better results.
**What I need to know:**

* **Target AI:** ChatGPT, Claude, Gemini, or Other
* **Prompt Style:** DETAIL (I'll ask clarifying questions first) or BASIC (quick optimization)
  **Examples:**
* "DETAIL using ChatGPT — Write me a marketing email"
* "BASIC using Claude — Help with my resume"

Just share your rough prompt and I'll handle the optimization!

---

Since your input is detailed and technical, I'm using **DETAIL mode**. Here's your optimized prompt:

---

**Your Optimized Prompt:**

You are an expert in AI-powered code analysis and multi-language software architecture. Assume you're enhancing the `mcp-crawl4ai-rag` MCP server, which currently targets Python repositories for hallucination-free Retrieval-Augmented Generation (RAG) pipelines.

Your task: Propose the architectural, tooling, and parser-level modifications required to extend the system to support **JavaScript and TypeScript** repositories. The system's key modules include:

1. `parse_github_repository` — extracts code, docs, and metadata
2. `check_ai_script_hallucinations` — validates AI-generated scripts
3. `search_code_examples` — retrieves reference code snippets

**Key Objectives:**

* Identify what modifications or plugin-based extensions are needed in each of the above modules to support JS/TS.
* Recommend suitable **AST tools** (e.g., Babel, TypeScript Compiler API), **documentation tools** (e.g., TypeDoc), and ecosystem-aware analyzers (e.g., `package.json`, npm registry).
* Suggest how to extend the **knowledge graph** and hallucination-checking logic to recognize idiomatic constructs in JS/TS (e.g., async/await, module imports, npm dependencies).
* Explore architectural patterns for **language-agnostic processing**, such as plugin-based parser frameworks or multi-language AST abstraction models (e.g., tree-sitter, babel plugins).
* Include code snippets or pseudocode examples to illustrate extensibility patterns (e.g., parser registry design, language strategy pattern, AST normalization layer).
* Highlight best practices or prior art from cross-language RAG systems, LSP integrations, or tools like Sourcegraph, Tree-sitter, or Rome.

**Output format:**

* ✅ Modified Components (per module)
* 🛠️ Required Tooling / Parsers
* 📐 Architectural Patterns for Extensibility
* 💡 Best Practices & Examples
* 🔧 Sample Code Snippets (as applicable)

---

**Key Improvements:**
• Added structured goals and module-specific expectations
• Clarified tool and ecosystem awareness needs for JS/TS
• Requested code samples and patterns to ground abstract ideas
• Enhanced prompt clarity for deep architectural reasoning

**Techniques Applied:** Role assignment, context layering, constraint optimization, output scaffolding

**Pro Tip:** This works great with ChatGPT-4, Claude 3, or any agent with multi-language code analysis abilities. If using tools like GPT-4 Code Interpreter, you can ask it to prototype parts of the parser or show AST traversal logic.
