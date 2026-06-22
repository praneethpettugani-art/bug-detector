# Security Analyzer Toolset

A comprehensive security analysis framework for detecting vulnerabilities in Python and C/C++ code.

## Features

### Python Security Analyzer
- Detects hardcoded secrets (passwords, API keys, tokens)
- Identifies unsafe function calls (`eval`, `exec`, `compile`, `__import__`)
- Detects SQL injection patterns via string concatenation and formatting
- Flags missing input validation on user inputs

### C/C++ Taint-Based Analyzer
- Identifies unsafe C/C++ functions (`strcpy`, `strcat`, `sprintf`, `gets`, etc.)
- Tracks tainted data from sources (stdin, `getenv`, network, command-line args)
- Detects SQL injection via dynamic query construction
- Reports unsafe sinks without sanitization
- Simple data-flow tracking through variable assignments

## Installation

```bash
git clone https://github.com/yourusername/security-analyzer.git
cd security-analyzer
```

No external dependencies required for basic analysis. Optional: Install for extended features.

## Usage

### Python Analyzer

```bash
python3 security_analyzer.py <file.py>
python3 security_analyzer.py <file.py> --json
```

Example:
```bash
python3 security_analyzer.py vulnerable_app.py --json > findings.json
```

### C/C++ Taint Analyzer

```bash
python3 c_cpp_taint_analyzer.py <file.c>
python3 c_cpp_taint_analyzer.py <file.c> --json
```

Example:
```bash
python3 c_cpp_taint_analyzer.py vulnerable_code.c --json > findings.json
```

## Output Format

### Console Output
```
<line_number>: <SEVERITY> - <message>
Total issues: <count>
```

### JSON Output
```json
{
  "file": "<path>",
  "findings": [
    {
      "line": <line_number>,
      "code": "<issue_code>",
      "severity": "<low|medium|high>",
      "message": "<description>"
    }
  ]
}
```

## Severity Levels
- **high**: Critical security vulnerabilities (hardcoded secrets, SQL injection, unsafe sinks)
- **medium**: Potentially dangerous operations (`eval`, `exec`, taint sources)
- **low**: Missing validation, suspicious patterns

## Project Structure

```
security-analyzer/
├── security_analyzer.py          # Python AST-based analyzer
├── c_cpp_taint_analyzer.py       # C/C++ regex-based taint tracker
├── security_tooling_plan.md      # Project planning document
├── README.md                      # This file
└── .gitignore
```

## Building from Source

### Requirements
- Python 3.7+
- No external dependencies (uses only stdlib)

### Running Tests
```bash
python3 security_analyzer.py <sample_vulnerable_file.py> --json
python3 c_cpp_taint_analyzer.py <sample_vulnerable_file.c> --json
```

## Learning Resources

See `security_tooling_plan.md` for:
- Detailed 2-week learning plan
- Security concepts explained
- Implementation guidance
- Testing strategies

## Future Enhancements

- Full data-flow analysis
- Clang-based C/C++ parsing
- Cross-function taint propagation
- Custom rule engine
- Web UI for report visualization
- Integration with CI/CD pipelines

## License

MIT License

## Contributing

Contributions welcome! Please submit issues and pull requests.

## Authors

Security Analyzer Team
