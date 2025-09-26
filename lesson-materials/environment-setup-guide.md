# W1D1 Environment Setup Guide

"Before a chef cooks, they set up their kitchen. Before we code, 
we set up our development environment. This isn't just installation—
it's building your professional workspace."

## Step 1: Python Installation Check (5 min)

### Windows users - open Command Prompt:
Press Windows Key + R, type 'cmd', press Enter

```bash
python --version
```

### Mac/Linux users - open Terminal:
Press Cmd + Space, type 'terminal', press Enter  

```bash
python3 --version
```

## Step 2: Professional IDE Setup (10 min)

"VS Code isn't just a text editor—it's your coding command center. 
Watch how it helps us write better code faster."

**Live Installation:**
*   Navigate to code.visualstudio.com
*   Download and install (share screen)
*   Install Python extension
*   Show IntelliSense autocomplete
*   Demonstrate error highlighting

## Step 3: Project Organization (5 min)

**Professional project structure**
```bash
mkdir python-foundations
cd python-foundations
python -m venv venv
```

**Activate virtual environment**
*   Windows: `venv\Scripts\activate`
*   Mac/Linux: `source venv/bin/activate`

You should see `(venv)` in your prompt

**Why This Matters:**
"Virtual environments are like having separate kitchens for different cuisines. 
Your Italian restaurant setup won't interfere with your sushi bar setup."
