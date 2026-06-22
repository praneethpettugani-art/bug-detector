# Security Analyzer Project Plan

## Part 1 — Python Security Analyzer

### Goal
Detect common Python security issues without full data-flow tracking.

### Issues to detect
- Hardcoded passwords/API keys
- Unsafe functions: `eval`, `exec`, `import`, `compile`
- Simple SQL injection patterns via string concatenation or formatting
- Missing input validation hints around user input

### What to learn
- Python basics for tooling
- File I/O, `argparse` (CLI), regular expressions, `pathlib`, JSON output
- Python `ast` module
  - `ast.parse`, `ast.walk`, `ast.NodeVisitor`
  - Node types: `Call`, `Assign`, `Name`, `Attribute`, `Constant`, `FunctionDef`, `If`, `Expr`
- Security rule patterns
  - Detect calls like `eval(x)`, `exec(x)`, `compile(...)`
  - Detect secrets in assignments such as `password = "..."`, `api_key = "..."`
- Basic reporting
  - Line numbers, severity levels (`low`/`medium`/`high`), short messages

### Build steps (2-week plan)
- Week 1
  - Day 1–2: Learn AST basics and write a `NodeVisitor` that prints all `Call` nodes.
  - Day 3–4: Add rules for hardcoded secrets and unsafe calls.
  - Day 5: Write CLI: `scan_single_file.py` using `argparse`.
- Week 2
  - Day 1–2: Add SQL injection pattern rules:
    - Patterns: `"SELECT ... " + var`, `"SELECT ... " % var`, `"SELECT ... ".format(...)`, f-strings used in SQL.
  - Day 3: Add input-validation hints:
    - Warn when code uses `input()` or request-like calls without visible validation.
  - Day 4: Add JSON output and a summary print.
  - Day 5: Test on 5–10 small vulnerable samples and refine rules.

---

## Part 2 — C/C++ Analyzer + Taint-Based SQL Injection Detection

### Goal
Extend analysis to C/C++ and add a taint-analysis layer to detect SQL injection and missing input validation flows.

### Issues to detect
- Unsafe functions: `strcpy`, `strcat`, `sprintf`, `scanf` without bounds, `gets`, reentrant `rand`
- Hardcoded secrets (string literals assigned to variables like `password`, `key`, `token`)
- Missing input validation on user input (e.g., `scanf`/`fgets` without bounds checks)
- SQL injection via string concatenation in SQL queries

### Taint-based detection
- Mark sources as tainted:
  - input from stdin
  - `getenv`
  - network input
  - command-line arguments
- Track tainted data to sinks:
  - SQL execution
  - `system`/`execve`
  - eval-equivalent operations
  - file writes
- Emit warnings when tainted data reaches a sink without sanitization

### What to learn
- C/C++ basics for tooling
- Build with `gcc`/`clang`, understand headers, compilation flags
- Clang tooling basics
  - `libclang` or `clang-tidy` for static checks
  - Clang Static Analyzer for path-sensitive issues
- Optional: write a simple clang plugin or use `clang-tidy` custom checks
- Security patterns in C
  - Unsafe string functions and their safer replacements (`strncpy`, `snprintf`, `fgets`)
- Taint analysis concepts
  - Sources, sinks, sanitizers
  - Simple tag-based taint: boolean flags on variables and propagation through assignments/operations
- Data-flow tracking
  - Map variable names to taint status
  - Track through function calls (simplified: in-file only first pass)

### Reporting and testing
- JSON output
- Severity levels
- Example vulnerable C files

### Suggested implementation path
- Build a static analyzer that recognizes unsafe C/C++ functions and hardcoded secrets.
- Add a taint layer that labels sources and propagates taint through assignments and string operations.
- Report SQL injection and unsafe sink usage when tainted data reaches a sink without sanitization.

---

## Recommended Document Structure
- Part 1: Python-focused analyzer plan
- Part 2: C/C++ analyzer plan with taint analysis
- Goals, issues, learning objectives, and implementation timeline
- Deliverables: CLI tool, JSON reporting, sample vulnerable test cases
