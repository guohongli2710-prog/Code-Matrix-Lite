graph TD
    User((Developer / CI Trigger))
    GitRepo[(Private Codebase)]
    CI_Runner[Local CI/CD Container]

    subgraph "Code-Matrix Multi-Agent Matrix"
        Planner[Planner Agent<br>Task DAG Generation]
        RepoMap[Repo-Map Agent<br>Milvus RAG Context]
        Coder[Coder Agent<br>AST-Aware Generation]
        TestFix[Test-Fix Agent<br>Self-Reflection Loop]
    end

    User --> Planner
    GitRepo -.-> RepoMap
    Planner <--> RepoMap
    Planner --> Coder
    Coder <--> RepoMap
    Coder --> TestFix
    TestFix --> CI_Runner
    CI_Runner -.->|Error and Stack Trace| TestFix
    TestFix -.->|Self-Correction Max 5 Retries| Coder
