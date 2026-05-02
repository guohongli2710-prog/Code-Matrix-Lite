# 🚀 Code-Matrix-Lite: Multi-Agent Refactoring Core

> **⚠️ NDA & Open Source Disclaimer:**
> This repository contains ONLY the *desensitized and abstracted core interfaces* of the internal Code-Matrix system. The full implementation, including the private AST parsers, local Milvus vector database integrations, and internal CI/CD webhook handlers, are strictly bound to our enterprise infrastructure and cannot be open-sourced due to Non-Disclosure Agreements (NDA).

## 📖 Overview
Code-Matrix is an advanced, ReAct-based multi-agent system designed for automated legacy codebase refactoring and self-healing unit test generation. It heavily utilizes LLMs with long-context windows for deep repository understanding.

## 🏗️ Architecture Design
The core workflow involves four primary agents in a closed feedback loop:

```mermaid
graph TD
    User((Developer / CI Trigger))
    GitRepo[(Private Codebase)]
    CI_Runner[Local CI/CD Container]

    subgraph "Code-Matrix Multi-Agent Matrix"
        Planner[**Planner Agent**\nTask DAG Generation]
        RepoMap[**Repo-Map Agent**\nMilvus RAG Context]
        Coder[**Coder Agent**\nAST-Aware Generation]
        TestFix[**Test-Fix Agent**\nSelf-Reflection Loop]
    end

    User --> Planner
    GitRepo -.-> RepoMap
    Planner <--> RepoMap
    Planner --> Coder
    Coder <--> RepoMap
    Coder --> TestFix
    TestFix --> CI_Runner
    CI_Runner -.->|Error/Stack Trace| TestFix
    TestFix -.->|Self-Correction (Max 5 Retries)| Coder
