# LabResources

This repo will host resources for lab sessions, including software installation instructions, and most importantly, **all assignment Jupyter notebooks**.  Clone the repo to a location you'll maintain throughout the course (not inside other course org repos, e.g., not inside your local copy of your course personal repo—the repo you'll create for Lab01, named according to your GitHub username).  You'll only need to clone this repo *once*.  Afterward, running `git pull` at the start of each lab session (in a terminal opened to work in your local `LabResources` folder) will update your local copy of the repo to contain the latest lab content, including the latest assignment.

Assignments will typically be provided as a Jupyter notebook named `AssignmentXX.ipynb` (where `XX` is a number) that provides explanatory information along with problem descriptions, and a solutions template, `SolutionsXX.ipynb`, that contains only the problem descriptions.  You should **copy the solutions template to your own course GitHub org repo**, and edit that copy to complete the assignment, as described below.



## Basic developer tools

Please see the separate [**Basic developer tools**](BasicDeveloperTools.md) Markdown document for guidance on setting up your computer with the basic software development tools needed for course assignments (terminal, code editor, Git, etc.).



## GitHub authorization

For `git` actions that modify your assignment repo on GitHub (e.g., `git push`), GitHub will require you to authorize the action with your GitHub credentials. `git` will ask for a username and password. In 2021, GitHub began requiring users to authorize such actions using **personal access tokens** rather than their account passwords. If you find the credentials you enter don't work, you probably need to generate a new token. See [**GitHub Personal Access Tokens**](GitHubPATs.md) for more information.



## Anaconda environment

The main computing environment we'll use for labs and assignments will by Python with various scientific computing packages from the PyData ecosystem, and (later in the course) the PyStan package providing access to the Stan probabilistic computing language.

We will use Anaconda Python 3 for assignments. If you are a Python expert, and brave (or foolhardy!), you may use whatever Python 3 environment you wish, but it's up to you to ensure compatibility with Anaconda Python 3, which is the environment we will use to execute your assignment notebooks for grading.

An important virtue of Anaconda Python is the `conda` command that it installs. `conda` is a package manager that maintains *conda environments* comprising Python packages and (importantly!) other software packages and libraries, ensuring they interact properly, and isolating them from other versions that may be on your system. So if you have another version of Python already on your system, you should be able to install the course's environment without creating conflicts with other software.

See the [**PythonForBDA**](PythonForBDA.md) document (in this repo) for instructions on how to install the BDA `conda` environment; it includes a flowchart to guide you through the process.





## Assignment submission

Please follow these instructions to work on your assignment solutions and submit them via GitHub.  "Your personal repo" here refers to the repo you used to submit the Assignment01 `README.md` file—the repo named according to your GitHub username.

1. Create a folder in your personal repo named for the assignment, `AssignmentXX` (with `XX` replaced by `02`, `03`, etc.).

2. After cloning or pulling the latest LabResources repo content, **copy** the `SolutionsXX.ipynb` template into the assignment folder in your personal repo.  If the assignment uses other resources (e.g., Python modules or data files), copy those as well.

3. Work on the assignment in your repo.  For each working session:
   * Open a terminal session with the assignment folder in your repo as the working directory.
   * Activate the `bda20` conda environment.
   * Launch the Jupyter notebook server with the command: `jupyter noteboook`. This should open a tab in your default web browser with the Jupyter notebook interface, displaying content in your local assignment folder.
   * Edit the `SolutionsXX.ipynb` notebook with your solutions in new cells created below each problem.  Feel free to add and commit intermediate stages of your work as often as you like, and to push intermediate stages back to GitHub if you wish.

4. When you are done working on the assignment, be sure to add and commit your final solutions (and any other resources you may have had to edit or create) in your local repo.
5. Push your repo back to the course org using: `git push`
6. Visit the [course org on GitHub](https://github.com/CU-BDA-2020) to make sure your content was pushed. Check to see when the content in the relevant assignment folder in your repo was last updated; the time stamp should verify that you just pushed the content. Note that GitHub will attempt to render Jupyter notebooks you upload. It does this imperfectly. Don't be concerned about visual anomalies as seen on GitHub. For grading, we pull your content to our computers and run your notebooks in real Jupyter sessions.