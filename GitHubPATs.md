# GitHub Personal Access Tokens

For `git` actions that modify your assignment repo on GitHub (e.g., `git push`), GitHub will require you to authorize the action with your GitHub credentials. `git` will ask for a username and password. In 2021, GitHub began requiring users to authorize such actions using **personal access tokens** (PATs) rather than their account passwords. If you find the credentials you enter don't work, you probably need to generate a PAT. This document explains what PATs are, and describes how to generate one for interacting with a repo in the BDA org.

## TL;DR — Brief PAT how-to

A PAT is a GitHub-generated random-looking string that works as a password.

* Follow the instructions here: [Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  * The token name isn't important; it's to help you maintain your tokens on GitHub. Just pick something convenient, e.g., "BDA org access".
  * Set an expiration date after the end of the course (e.g., in July).
  * For scope/permissions, make sure to select **repo** (which will select all the options in the repo group). You may select other options as you see fit, e.g., if you want to create a token that you'll use for other activities besides maintaining your BDA repo.
  * Generate the token. GitHub will display the token, a long, random-looking string.
* **Copy the token, and treat it just like you'd treat an important password.** Keep it secure, and keep it secret.
  * If you use a password manager, use it to store your PAT just like you'd store any other password (use your GitHub username as the username associated with the PAT).
  * If you don't use a password manager, consider investing time in setting one up. Cornell provides free LastPass enterprise accounts to students: [Secure Password Management | IT@Cornell](https://it.cornell.edu/password-mgmt).
  * If you don't copy or lose the token, *it cannot be retrieved later*. You can regenerate the token (there is a `Regenerate token` button for that); this will create a *new* token (with the specified settings) and deauthorize the old one, so if the old token is being used by an application, it will have to be replaced with the new one.



## More about personal access tokens

In computer security, a *token* is "an object (in software or in hardware) which represents the right to perform some operation" ([Token - Wikipedia](https://en.wikipedia.org/wiki/Token)).

A GitHub personal access token is essentially a kind of supplemental password associated with a GitHub user's account. 

An account's *main password* has the following properties:
* It is unique (there is only one associated with an account).
* It grants full access to everything associated with the account.
* If changed, it must be updated everywhere the account is accessed by password.

A PAT is a machine-generated string (random-looking and thus nearly impossible to guess), generated at an account holder's request, usable like a password to provide access to account resources, but differing from a password in important respects:
* An account may have multiple PATs associated with it, each created for a specific purpose (e.g., to use on a specific machine, or for a specific project).
* Each PAT may have restrictions on what account resources it can provide access to.
* Each PAT may have an expiration date, set when it is generated.
* The account holder may revoke a PAT at any time.
* GitHub automatically removes personal access tokens once they've been unused for a year.

Since GitHub switched to PAT-based authorization (in summer 2021), `git` commands on remote machines that access restricted resources in a user's GitHub account (e.g., `git push` back to a user's GitHub repo, or `git clone` and  `git pull` with a private repo), and which thus ask for a username and password, should be provided the usual username, ***but be provided a PAT in place of the user's main password***. Entering the main password will cause the connection to fail. See the *Using a token on the command line* section of the PAT creation docs cited above.

*Note for Git experts who use SSH:* PATs can only be used for remote Git operations using the HTTPS protocol. If a repository uses a remote URL with the secure shell protocol (SSH), it must be changed to use HTTPS.

Follow the TL;DR instructions above to generate a PAT as needed. On the command line, use it when prompted for a password (see below for tips on storing the PAT so you don't have to type it every time). If you are using a Git GUI, you can store the PAT in the GUI's credential settings so you don't have to enter it manually with every GitHub interaction. For the SourceTree GUI, you would do this in the *Accounts* pane of SourceTree's preferences window.



## Resources

* [Creating a personal access token - GitHub Docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* [Caching your GitHub credentials in Git - GitHub Docs](https://docs.github.com/en/get-started/getting-started-with-git/caching-your-github-credentials-in-git) — Tips for securely saving your PAT on your local machine so you don't have to type it every time you do a `git push`.
* [Git - gitcredentials Documentation](https://git-scm.com/docs/gitcredentials) — Git's general documentation on providing usernames and passwords to Git.