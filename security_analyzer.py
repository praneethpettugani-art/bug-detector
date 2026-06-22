#!/usr/bin/env python3
import ast
import argparse
import json
from pathlib import Path

SEVERITY = {
    "hardcoded_secret": "high",
    "unsafe_call": "medium",
    "sql_injection": "high",
    "missing_validation": "low",
}

SECRET_KEYWORDS = ["password", "passwd", "secret", "api_key", "token", "credential"]
UNSAFE_CALLS = ["eval", "exec", "compile", "__import__"]
SQL_KEYWORDS = ["select", "insert", "update", "delete", "drop", "create"]
INPUT_CALLS = ["input", "sys.stdin.read", "sys.stdin.readline"]


class SecurityVisitor(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_Assign(self, node):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    name = target.id.lower()
                    if any(keyword in name for keyword in SECRET_KEYWORDS):
                        self.report(node, "hardcoded_secret", f"Hardcoded secret assigned to '{target.id}'")
        self.generic_visit(node)

    def visit_Call(self, node):
        func_name = self.get_call_name(node.func)
        if func_name in UNSAFE_CALLS:
            self.report(node, "unsafe_call", f"Unsafe call to '{func_name}'")

        if func_name in INPUT_CALLS:
            if not self.has_validation(node):
                self.report(node, "missing_validation", f"User input from '{func_name}' has no obvious validation")

        if self.is_sql_pattern(node):
            self.report(node, "sql_injection", "Possible SQL injection via dynamic query construction")

        self.generic_visit(node)

    def get_call_name(self, func):
        if isinstance(func, ast.Name):
            return func.id
        if isinstance(func, ast.Attribute):
            return func.attr
        return ""

    def has_validation(self, node):
        return False

    def is_sql_pattern(self, node):
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in {"execute", "executemany", "execute_query"}:
                for arg in node.args:
                    if isinstance(arg, ast.BinOp) or isinstance(arg, ast.JoinedStr):
                        return True
        return False

    def report(self, node, code, message):
        self.issues.append({
            "line": node.lineno,
            "code": code,
            "severity": SEVERITY.get(code, "medium"),
            "message": message,
        })


def scan_file(path: Path):
    source = path.read_text(encoding="utf-8", errors="ignore")
    tree = ast.parse(source, filename=str(path))
    visitor = SecurityVisitor()
    visitor.visit(tree)
    return visitor.issues


def main():
    parser = argparse.ArgumentParser(description="Python security analyzer")
    parser.add_argument("path", type=Path, help="Python file to scan")
    parser.add_argument("--json", dest="json", action="store_true", help="Output findings as JSON")
    args = parser.parse_args()

    findings = scan_file(args.path)
    if args.json:
        print(json.dumps({"file": str(args.path), "findings": findings}, indent=2))
        return

    for finding in findings:
        print(f"{finding['line']}: {finding['severity'].upper()} - {finding['message']}")

    print(f"\nTotal issues: {len(findings)}")


if __name__ == "__main__":
    main()
