#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

SOURCES = [r"scanf\(", r"fgets\(", r"gets\(", r"getenv\(", r"argv", r"argc", r"recv\(", r"read\("]
UNSAFE_FUNCTIONS = ["strcpy", "strcat", "sprintf", "gets", "scanf", "system", "execve", "popen"]
SQL_SINKS = [r"mysql_query", r"sqlite3_exec", r"PQexec", r"sqlite3_prepare", r"OCIStmtExecute"]
TAINTED_NAMES = ["stdin", "argv", "argc", "getenv", "recv", "read"]


class TaintAnalyzer:
    def __init__(self, lines):
        self.lines = lines
        self.tainted_vars = set()
        self.issues = []

    def analyze(self):
        for index, line in enumerate(self.lines, start=1):
            stripped = line.strip()
            self.check_sources(index, stripped)
            self.check_unsafe_calls(index, stripped)
            self.check_sql_sink(index, stripped)
            self.propagate_taint(index, stripped)
        return self.issues

    def check_sources(self, lineno, line):
        for pattern in SOURCES:
            if re.search(pattern, line):
                self.report(lineno, "taint_source", f"Taint source detected: {pattern}")
                break

    def check_unsafe_calls(self, lineno, line):
        for func in UNSAFE_FUNCTIONS:
            if re.search(rf"\b{func}\b", line):
                if func == "scanf" and re.search(r"%[0-9]*s", line) is None:
                    self.report(lineno, "unsafe_call", "scanf without explicit buffer size")
                elif func in {"strcpy", "strcat", "sprintf", "gets"}:
                    self.report(lineno, "unsafe_call", f"Unsafe string function '{func}'")
                elif func in {"system", "execve", "popen"}:
                    self.report(lineno, "unsafe_call", f"Command execution sink '{func}'")

    def check_sql_sink(self, lineno, line):
        for sink in SQL_SINKS:
            if re.search(rf"\b{sink}\b", line):
                if self.contains_tainted_variable(line):
                    self.report(lineno, "sql_injection", f"Tainted data reaches SQL sink '{sink}'")
                else:
                    self.report(lineno, "sql_sink", f"SQL execution sink detected: {sink}")

    def contains_tainted_variable(self, line):
        for var in self.tainted_vars:
            if re.search(rf"\b{re.escape(var)}\b", line):
                return True
        return False

    def propagate_taint(self, lineno, line):
        assign_match = re.match(r"\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.*)", line)
        if assign_match:
            target, expr = assign_match.groups()
            if self.expr_is_tainted(expr):
                self.tainted_vars.add(target)

    def expr_is_tainted(self, expr):
        for var in self.tainted_vars + TAINTED_NAMES:
            if re.search(rf"\b{re.escape(var)}\b", expr):
                return True
        return False

    def report(self, lineno, code, message):
        self.issues.append({
            "line": lineno,
            "code": code,
            "severity": self.severity(code),
            "message": message,
        })

    def severity(self, code):
        if code in {"sql_injection", "unsafe_call"}:
            return "high"
        if code == "taint_source":
            return "medium"
        return "low"


def scan_file(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    analyzer = TaintAnalyzer(text.splitlines())
    return analyzer.analyze()


def main():
    parser = argparse.ArgumentParser(description="Simple C/C++ taint analysis scanner")
    parser.add_argument("path", type=Path, help="C or C++ source file to scan")
    parser.add_argument("--json", dest="json", action="store_true", help="Output findings as JSON")
    args = parser.parse_args()

    findings = scan_file(args.path)
    if args.json:
        print(json.dumps({"file": str(args.path), "findings": findings}, indent=2))
    else:
        for finding in findings:
            print(f"{finding['line']}: {finding['severity'].upper()} - {finding['message']}")
        print(f"\nTotal issues: {len(findings)}")


if __name__ == "__main__":
    main()
