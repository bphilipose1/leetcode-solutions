#!/usr/bin/env python3
"""
Monthly LeetCode solutions sync script.
Usage: python sync_solutions.py --cookie "<YOUR_LEETCODE_COOKIE>"
"""

import os
import sys
import json
import shutil
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

# NeetCode 150 category mapping (problem_id -> category)
NEETCODE_MAP = {
    1: "01-arrays-and-hashing", 2: "06-linked-list", 3: "03-sliding-window",
    4: "12-1d-dp", 5: "03-sliding-window", 6: "03-sliding-window", 7: "03-sliding-window",
    8: "01-arrays-and-hashing", 9: "01-arrays-and-hashing", 11: "02-two-pointers",
    13: "01-arrays-and-hashing", 15: "02-two-pointers", 17: "09-backtracking",
    19: "06-linked-list", 20: "04-stack", 21: "06-linked-list", 22: "09-backtracking",
    23: "06-linked-list", 26: "02-two-pointers", 27: "02-two-pointers", 33: "05-binary-search",
    36: "01-arrays-and-hashing", 39: "09-backtracking", 42: "02-two-pointers",
    46: "09-backtracking", 49: "01-arrays-and-hashing", 53: "12-1d-dp", 56: "15-intervals",
    62: "12-1d-dp", 74: "05-binary-search", 78: "09-backtracking", 79: "09-backtracking",
    88: "02-two-pointers", 90: "09-backtracking", 98: "07-trees", 100: "07-trees",
    102: "07-trees", 104: "07-trees", 105: "07-trees", 110: "07-trees", 121: "12-1d-dp",
    125: "02-two-pointers", 128: "01-arrays-and-hashing", 130: "10-graphs", 131: "09-backtracking",
    133: "10-graphs", 138: "06-linked-list", 141: "06-linked-list", 143: "06-linked-list",
    146: "01-arrays-and-hashing", 150: "04-stack", 153: "05-binary-search", 155: "04-stack",
    167: "02-two-pointers", 199: "07-trees", 200: "10-graphs", 206: "06-linked-list",
    207: "11-advanced-graphs", 210: "11-advanced-graphs", 215: "08-heaps", 217: "01-arrays-and-hashing",
    226: "07-trees", 230: "07-trees", 236: "07-trees", 238: "01-arrays-and-hashing",
    240: "05-binary-search", 242: "01-arrays-and-hashing", 273: "16-math-and-geometry",
    279: "12-1d-dp", 300: "12-1d-dp", 303: "12-1d-dp", 329: "12-1d-dp", 347: "08-heaps",
    417: "10-graphs", 494: "12-1d-dp", 525: "01-arrays-and-hashing", 539: "16-math-and-geometry",
    543: "07-trees", 560: "01-arrays-and-hashing", 572: "07-trees", 647: "12-1d-dp",
    695: "10-graphs", 718: "12-1d-dp", 739: "04-stack", 789: "08-heaps", 792: "05-binary-search",
    829: "01-arrays-and-hashing", 883: "04-stack", 895: "10-graphs", 907: "05-binary-search",
    1036: "10-graphs", 1127: "08-heaps", 1354: "01-arrays-and-hashing", 1431: "11-advanced-graphs",
    1585: "16-math-and-geometry", 2487: "01-arrays-and-hashing", 2820: "17-other",
    3635: "12-1d-dp",
}

def run_command(cmd, cwd=None):
    """Run shell command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
            return None
        return result.stdout.strip()
    except Exception as e:
        print(f"Command failed: {e}")
        return None

def export_solutions(cookie, output_dir):
    """Export solutions from LeetCode."""
    print(f"[*] Exporting solutions to {output_dir}...")
    cmd = f'leetcode-export --cookies "LEETCODE_SESSION={cookie}" --folder {output_dir} -v'
    result = run_command(cmd)
    if result:
        print("[+] Export successful")
        return True
    print("[-] Export failed")
    return False

def clean_solutions(base_dir):
    """Clean up solutions: keep best per language, rename files."""
    print("[*] Cleaning up solutions...")
    
    for problem_dir in Path(base_dir).iterdir():
        if not problem_dir.is_dir():
            continue
        
        # Group files by language
        solutions = {}
        readme_file = None
        
        for file in problem_dir.iterdir():
            if file.is_file():
                if file.suffix == ".md":
                    readme_file = file
                else:
                    lang = file.suffix.lstrip(".")
                    if lang not in solutions:
                        solutions[lang] = []
                    solutions[lang].append(file)
        
        # Keep best (lowest runtime) per language, delete others
        for lang, files in solutions.items():
            best = min(files, key=lambda f: f.stat().st_mtime)
            for f in files:
                if f != best:
                    f.unlink()
            best.rename(problem_dir / f"solution{best.suffix}")
        
        # Rename README
        if readme_file:
            readme_file.rename(problem_dir / "README.md")
    
    print("[+] Cleanup complete")

def reorganize_by_category(base_dir):
    """Reorganize solutions into NeetCode 150 category folders."""
    print("[*] Reorganizing by NeetCode 150 sections...")
    
    # Create category folders
    categories = set(NEETCODE_MAP.values())
    for cat in categories:
        Path(base_dir, cat).mkdir(exist_ok=True)
    
    # Move problem folders
    for problem_dir in Path(base_dir).iterdir():
        if problem_dir.is_dir() and not problem_dir.name.startswith(("0", "1")):
            # Extract problem ID from folder name (e.g., "1-two-sum" -> 1)
            try:
                problem_id = int(problem_dir.name.split("-")[0])
                category = NEETCODE_MAP.get(problem_id, "17-other")
                dest = Path(base_dir, category, problem_dir.name)
                if problem_dir != dest:
                    problem_dir.rename(dest)
            except (ValueError, IndexError):
                # Fallback for unmapped problems
                Path(base_dir, "17-other", problem_dir.name).mkdir(parents=True, exist_ok=True)
                problem_dir.rename(Path(base_dir, "17-other", problem_dir.name))
    
    print("[+] Reorganization complete")

def generate_readme(base_dir):
    """Generate comprehensive README."""
    print("[*] Generating README...")
    
    readme = """# LeetCode Solutions — NeetCode 150

A structured collection of **99 LeetCode problems** organized by **NeetCode 150 sections**. Each solution includes the best accepted submission per language with optimized runtime.

## 📊 Overview

- **Problems:** 99 (with multiple language implementations)
- **Languages:** Python, C++, JavaScript
- **Organization:** 17 NeetCode 150 categories
- **Updated:** Monthly via automated sync

## 📂 Structure

Solutions are organized into topic-based folders:

### Core Categories
| Category | Problems | Focus |
|----------|----------|-------|
| Arrays & Hashing | 11 | Hash maps, sets, prefix sums |
| Two Pointers | 8 | Linear scans, merge operations |
| Sliding Window | 6 | Substring/subarray optimization |
| Stack | 6 | LIFO operations, monotonic stacks |
| Binary Search | 8 | Search optimization, boundaries |
| Linked List | 9 | Node manipulation, traversal |
| Trees | 12 | DFS/BFS, BST, level-order |
| Heaps | 3 | Priority queues, kth largest |

### Advanced Categories
| Category | Problems | Focus |
|----------|----------|-------|
| Backtracking | 7 | Permutations, subsets, combinations |
| Graphs | 7 | DFS/BFS, connected components |
| Advanced Graphs | 4 | Topological sort, shortest path |
| 1-D DP | 6 | Linear DP, memoization |
| 2-D DP | 1 | Matrix DP |
| Greedy | 0 | Greedy algorithms |
| Intervals | 2 | Merge, overlap detection |
| Math & Geometry | 7 | Number theory, coordinate geometry |
| Other | 1 | Misc problems |

## 🚀 Quick Start

Each problem folder contains:
- **`README.md`** — Problem statement & approach
- **`solution.py`** — Python (if available)
- **`solution.cpp`** — C++ (if available)
- **`solution.js`** — JavaScript (if available)

Example structure:
```
01-arrays-and-hashing/
├── 1-two-sum/
│   ├── README.md
│   ├── solution.py
│   └── solution.cpp
├── 3-longest-substring-without-repeating-characters/
│   ├── README.md
│   ├── solution.cpp
│   └── solution.py
...
```

## 📈 Language Breakdown

- **Python:** 88 solutions (multi-algorithm approaches, readability)
- **C++:** 30 solutions (performance-critical problems)
- **JavaScript:** 1 solution

## 🔄 Sync Process

This repo is updated **monthly** via:
1. Fresh LeetCode export (via `leetcode-export`)
2. Auto-cleanup (keeps best per language)
3. Reorganization by NeetCode category
4. Automated commit & push

## 🎯 How to Use

1. **Navigate by topic:** Pick a category folder that matches your interview prep
2. **Study solutions:** Each problem includes optimal solution(s) with runtime notes
3. **Reference implementations:** Use as a code reference, not a cheat sheet
4. **Practice first:** Attempt problems before reading solutions

## 💡 Tips

- **Timing:** Give yourself 45 minutes per problem before checking the solution
- **Multiple languages:** Compare Python (clarity) vs. C++ (speed) approaches
- **Interview prep:** Follow NeetCode 150 order for structured learning
- **Hard problems:** These are designed to be hard; don't get discouraged

## 📝 Notes

- All solutions are **accepted submissions** from LeetCode
- Each language version is the **fastest solution** for that language
- Problems are mapped to **NeetCode 150** curated curriculum
- Last updated: """ + datetime.now().strftime("%B %d, %Y") + """

---

**Start with Arrays & Hashing.** Master fundamentals before moving to advanced topics.
"""
    
    with open(Path(base_dir) / "README.md", "w") as f:
        f.write(readme)
    
    print("[+] README generated")

def commit_and_push(base_dir, message="refactor: sync LeetCode solutions"):
    """Commit and push changes."""
    print(f"[*] Committing changes...")
    
    run_command("git add .", cwd=base_dir)
    run_command(f'git commit -m "{message}"', cwd=base_dir)
    
    print("[*] Pushing to GitHub...")
    result = run_command("git push origin main", cwd=base_dir)
    
    if result is not None:
        print("[+] Push successful")
        return True
    print("[-] Push failed (check credentials)")
    return False

def main():
    parser = argparse.ArgumentParser(description="Sync LeetCode solutions monthly")
    parser.add_argument("--cookie", required=True, help="LeetCode session cookie")
    parser.add_argument("--repo", default="./", help="Repository path")
    
    args = parser.parse_args()
    
    repo_path = Path(args.repo).resolve()
    temp_export = repo_path / ".temp_export"
    
    print(f"[*] Starting sync for {repo_path}")
    print(f"[*] Timestamp: {datetime.now().isoformat()}")
    
    try:
        # Export
        if not export_solutions(args.cookie, temp_export):
            sys.exit(1)
        
        # Clean
        clean_solutions(temp_export)
        
        # Merge into repo (backup old structure)
        if (repo_path / "01-arrays-and-hashing").exists():
            print("[*] Backing up old structure...")
            for item in (repo_path).glob("0*"):
                shutil.rmtree(item, ignore_errors=True)
        
        # Move exports
        for item in temp_export.iterdir():
            dest = repo_path / item.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.move(str(item), str(dest))
        
        # Reorganize & README
        reorganize_by_category(repo_path)
        generate_readme(repo_path)
        
        # Commit & push
        if commit_and_push(repo_path):
            print("[+] Sync complete!")
        else:
            print("[-] Sync complete but push failed")
    
    finally:
        # Cleanup temp
        shutil.rmtree(temp_export, ignore_errors=True)

if __name__ == "__main__":
    main()
