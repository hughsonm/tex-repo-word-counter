# tex-repo-word-counter
Tracks the word count of a TeX project in a git repository with respect to time
# Instructions
1. Set up and activate a virtual environment.
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

3. Run `count.py` and tell it where to find the repo you want to analyze, as well as the name of the default branch.
The name of the default branch is probably either `"master"` or `"main"`
```bash
python3 count.py "path/to/repo" "main"
```

4. Look at the cool/depressing graph!
