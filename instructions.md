# Git Branching Exercises

## Step 1: Complete Learn Git Branching Exercises

Complete the exercises from this interactive tutorial:
**https://learngitbranching.js.org/**

Work through the exercises to understand Git branching concepts including:
- Basic Git commands
- Branching and merging
- Remote repositories
- Advanced Git concepts

## Step 2: Clone the Repository

Clone this repository to your local machine:

```bash
git clone git@github.com:Anamari-ctrl/SummerSchool.git
```

## Step 3: Create Notes File

1. Navigate to the cloned repository:
   ```bash
   cd SummerSchool
   ```

2. Create a file to document your learning from the Git branching exercises:
   ```bash
   touch git-branching-notes.md
   ```

3. Add your notes from practicing "Learn Git Branching" to this file. Include:
   - Key concepts learned
   - Important Git commands
   - Branching strategies
   - Any challenges you encountered

## Step 4: Create and Push Your Exercise Branch

1. Create a new branch with your name followed by "-exercise1":
   ```bash
   git checkout -b yourname-exercise1
   ```
   (Replace "yourname" with your actual name)

2. Add your notes file to Git:
   ```bash
   git add git-branching-notes.md
   ```

3. Commit your changes:
   ```bash
   git commit -m "Add Git branching exercise notes"
   ```

4. Push your branch to the remote repository:
   ```bash
   git push origin yourname-exercise1
   ```