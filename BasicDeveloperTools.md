# Prepping your computing environment for BDA 2022

## Brief overview

* Install a command line interpreter/terminal/console program (or find the one included on your platform).
* Get a code editor or IDE, for editing Python scripts.
* Optionally get a Markdown editor for editing Markdown plain-text markup files (most code editors support this at some level).
* Install the Git command-line tools (or see if your platform has them already installed).
* Optionally install a Git GUI.
* **Important:** Set up an account on GitHub.com if you don't already have one.



## Command line interpreter/terminal/console program

A **terminal** or **console** program accepts keyboard (and mouse) input, communicates it to some hosted software, and displays the input and the software response. Most often, terminal programs automatically run some kind of **shell** program—software that runs textual commands that interact with your file system and operating system.

Our lab sessions presume you know how to launch a terminal program, and how to use it to navigate around your file system using whatever shell it supports.

Recommended tools:

* *Linux users:* An **xterm** running any modern shell should be fine.
* *Mac OS X users:*
  * The **Terminal** app that comes with OS X is completely adequate for our purposes; it's in the Utilities folder in your Applications folder. More popular among serious developers is **iTerm 2**, which resembles Terminal at launch, but is more customizable. It's free (donations welcome) from: [iTerm2 - Mac OS Terminal Replacement](http://iterm2.com/). By default these run the GNU **bash** shell, a popular shell for Linux operating systems (under the covers, macOS runs a relative of the Linux OS).
  * Mac users should also install **Xcode** using the *Mac App Store* app. This is a large download requiring a time-consuming installation; don't leave this for the last minute. After installing (or upgrading) Xcode, be sure to launch it. This causes it to install a set of command-line tools. It's a good idea to open *System Preferences* after this, and open the *Software Updates* preference pane; you may find some updates for the command-line tools (this is a quicker install). If you have limited space and would rather not install Xcode, it's possible to install only the command-line tools. I believe you'll have to set up a (free) Apple Developer account to do this; contact me for details if you'd like to pursue this.
* *Windows users:*
  * Installing Git for Windows (see below) provides a command line interpreter called **Git Bash** that is well-suited to our purposes (Bash is the name of a popular Unix command-line shell). The rest of this entry is for those interested in other options (which may be useful if you anticipate using the command line a lot outside of this course).
  * The **Command Prompt** program (aka, **CMD**, a shell that runs in a built-in WIndows console) comes with Windows and will work for our purposes. A popular alternative, with some extra features like tabs and customization options, is **Console** (aka **Console2**), an open-source project at SourceForge: [Console | SourceForge.net](http://sourceforge.net/projects/console/). It's what I use in a Windows virtual machine I maintain on my macOS machines for testing course software. A newer fork has become available that implements the same functionality, but with an interface better suited to Windows 7/8/10: [ConsoleZ](https://github.com/cbucher/console/wiki). For a quick (but somewhat dated, 2015) overview of various Windows terminal/shell offerings, see: [A better Windows command line experience: Comparing PowerCmd vs. Console2 vs. ConsoleZ vs. ConEmu Vs. Cmder | Aaron T. Grogg](https://aarontgrogg.com/blog/2015/07/31/a-better-windows-command-line-experience-comparing-powercmd-vs-console2-vs-consolez-vs-conemu-vs-cmder/).
  * There's newer option (introduced for Windows 10) worth considering: You can install a Microsoft-provided Linux subsystem on top of Windows 10 (*Windows Subsystem for Linux* aka *WSL*), providing you a "real" Linux terminal. I have not yet tried this myself, but if you are interested in this option, see: [Learn about the Windows Subsystem for Linux | Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/about), and [Bash on Windows 10 goes beyond Ubuntu and gets support for Fedora and SuSE, too | TechCrunch](https://techcrunch.com/2017/05/11/microsofts-bash-on-windows-10-goes-beyond-ubuntu-and-gets-support-for-fedora-and-suse-too/).



## Text editor/code editor/IDE

You will need a *plain text editor* (not a word processor) to write software (Python scripts) and plain-text documentation files using the Markdown markup language (you'll be writing most course assignments in Jupyter notebooks, but some code will be in external files). You could get by with a bare-bones text editor, but consider learning how to use a *code editor*—a text editor that understands various programming languages, providing capabilities that ease or speed development, such a syntax-aware highlighting, automatic indentation, and code completion. Alternatively, consider using an *integrated development environment* (IDE), a toolset that combines a code editor with other useful development tools, such as built-in command consoles, debugging aids, and variable and class browsers. The Anaconda Python distribution we will be using provides **Spyder** (https://www.spyder-ide.org/) a very capable cross-platform IDE focused on supporting scientific computing with Python. We may provide an introduction to Spyder in a lab.

These days many code editors have IDE-like capabilities, and the distinction between such tools is blurring.

A very popular cross-platform (Mac/Win/Linux) code editor among data scientists is **Sublime Text** (ST, currently at version 4, though ST3 is still in wide use). This is a commercial app, but is 100% functional in its indefinite trial mode (do pay for it if you try it and find yourself relying on it). ST4 is a very capable editor by itself, but its real strength comes from the hundreds of 3rd-party packages developers have created for it. Its main downside is a somewhat awkward preference/customization system. Expect to struggle with it at first, but if you develop on multiple platforms, or you do both scientific and web programming, it will probably be worth the effort. It's available here: [Sublime Text - Download](http://www.sublimetext.com/download). After installation, the first thing you should do is install the Package Control package manager ([Package Control - the Sublime Text package manager](https://packagecontrol.io/)), which simplifies access to the ecosystem of packages. Many ST3/ST4 tutorials are available online (the interface is little changed from ST3, so ST3 tutorials remain useful for ST4 users).

A more recent alternative is **Visual Studio Code** (VSC), a free, cross-platform code editor from Microsoft, based on its commercial Visual Studio platform: [Visual Studio Code](https://code.visualstudio.com/). The [Stack Overflow Developer Survey 2021](https://insights.stackoverflow.com/survey/2021) found VSC to be by far the most popular development environment among respondents (see the "Integrated development environment" section of the Technology page). Despite being newer than ST, it has many similar capabilities and extensions, thanks in part to having a huge, well-funded company behind it.

Our Canvas site has links to LinkedIn Learning instructional videos for ST and VSC.

There are many other code editors and IDEs to choose from; see the above-mentioned survey for a list. The *Anaconda* package of Python tools that we'll use for lab work includes the Spyder Python IDE mentioned above. Information on installing Anaconda will be provided in a separate document in the LabResources repo.

Other popular, free alternative editors that are simpler than code editors and IDEs but that will serve our needs include:

* Windows: [Notepad++](http://notepad-plus-plus.org/)

* macOS: [BBEdit (free mode)](http://www.barebones.com/products/bbedit/)

* Linux: Text editors that ship with many distributions, such as **kate** or **gedit**, provide decent code editing capability.



## Markdown editor

You will be using the Markdown plain-text markup language heavily in course assignments. Almost all of the Markdown work will take place within Jupyter notebooks, which support Markdown editing in a web browser. So no special Markdown editor is necessary for the course; the limited Markdown editing you'll need to do outside of a Jupyter notebook can be easily handled by a plain text editor.

That said, there are good free and inexpensive Markdown editors that you may want to investigate if you are new to Markdown; they do make it easier to write Markdown text.

There are several good Markdown editors that will let you write Markdown in a plain text editor pane, and either render it with a button push, or render it live in a second pane. On macOS I have used the dual-pane **MacDown** editor (https://macdown.uranusjr.com/), though currently I favor the single-pane **Typora** editor (https://www.typora.io/; \$14.99) that provides a more WYSIWYG interface, with quick toggling between source and rendered views. Typora is also available for Windows and Linux. For one of many lists of good Markdown editors for various platforms, see [5 markdown editors I recommend trying | Opensource.com](https://opensource.com/article/21/10/markdown-editors).

Note that VSC and ST all have Markdown plugins (I personally find it easier to use a dual-pane Markdown editor). If you explore Markdown editors, be sure to choose one that has support for equations/formulas using MathJax syntax (this is an extension to Markdown), including both inline math (a short formula in a sentence) and displayed math (an equation set in its own space). This web site collects info on math support in Markdown, including an editor list near the end: [Math in MarkDown · cben/mathdown Wiki](https://github.com/cben/mathdown/wiki/math-in-markdown).



## Git

The course will expose you to the basics of the Git *distributed version control system* (DVCS, also known as a Source Configuration Management (SCM) system), and use of the GitHub web site for software collaboration and sharing. Your assignments will be due as content uploaded to student Git repositories ("repos").

Git is implemented as a large collection of command-line programs. There are Git GUIs that provide a point-and-click interface for most Git functions. We'll be teaching basic use of Git via the command line, but you may want to use a Git GUI once you understand basic command-line usage.

### Command-line Git

The Git web site is: http://git-scm.com/. It provides comprehensive documentation, and basic installers for all major platforms.

If you don't already have Git installed on your computer, install it:

* Linux users: You likely already have Git (try "which git" at a command line prompt), but if not, you should be able to install it easily via your package manager.

* Windows users: Use the installer at the Git web site, or, for an installation with some extra capabilities, visit: [Git for Windows](http://gitforwindows.org/). When I last installed Git, many of the "extras" from the Git for Windows site were in fact offered as options when I used the installer from [git-scm.com](http://git-scm.com), so I am not clear on what Git for Windows offers, besides a somewhat primitive-looking Git GUI. When I ran the [git-scm.com](http://git-scm.com) installer (a while ago!), I accepted the default components (which includes integration with Windows Explorer, and a bash-like shell integrated with Git), and accepted the default handling of line endings (*check out files as Win, commit as Unix*).

* Mac users:

  * If you installed Xcode, it most likely installed a version of Git for you; type "which git" at the command line to see if your terminal app can find it. If it's found, that's the simplest solution. Next simplest: A Mac installer is available at the Git web site.
  * Alternatively (and what I do), consider installing the **Homebrew** package manager, and use it to install Git. Homebrew will give you easy access to many packages and programs ported to the Mac from the Linux community and elsewhere (though I don't anticipate we will need these for our labs). To get Git via Homebrew:
    * Install Homebrew via the instructions at its home page: [Homebrew — The missing package manager for OS X](http://brew.sh/). This involves pasting a 1-line command into an open terminal window (and responding to some prompts).
    * Again in a terminal window (in any directory), type: `brew install git`.
    * A nice feature of using a package manager is the ease of updating: now and then, run `brew update` to update Homebrew itself, and then `brew upgrade git` to get the latest Git.

  

### Git GUIs

You'll learn how to use Git from the command line; it's important to have some familiarity with that. However, if you are more comfortable with a GUI, most development tasks can be performed with one of several good Git GUIs. I use [Sourcetree | Free Git GUI for Mac and Windows](https://www.sourcetreeapp.com/) (alas, there is no Linux support); consider it if you think you'd like to follow along with my Sourcetree usage in labs. GitHub maintains its own Git GUI: [GitHub Desktop | Simple collaboration from your desktop](https://desktop.github.com/). The Git web site maintains a list of GUIs for various platforms: [Git - GUI Clients](https://git-scm.com/downloads/guis). 



### GitHub

GitHub is a web site that can host Git repos to support distributed access and development. GitHub is a commercial web site, but they provide free support for academic use. Our course has a *GitHub organization* (an "org") that will we use for distributing and collecting course resources and student assignments. 

If you don't already have a GitHub account, sign up for one on the main page: https://github.com/. Once you do so, you'll need to let me know your account name, so I can link it to our organization. Stay tuned for an announcement on how to communicate that to me.

After you have an account, consider requesting the [GitHub Student Developer Pack](https://education.github.com/pack). You will likely need to provide evidence of your Cornell affiliation to get the pack, e.g., a photo of your CU ID. For more info about the pack, see: [Apply for a student developer pack - GitHub Docs](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/use-github-for-your-schoolwork/apply-for-a-student-developer-pack). The main benefit is the free GitHub account upgrade, which lets you have private Git repositories on GitHub (free accounts normally can only host public repos).