## Development Guidelines

All major development will be completed in this repository. While you are encouraged to explore and code in the DevContainer provided by Jeff, class requirements for project iterations require that each member of the team commit code to the repository. So, you need to know how to use Git and GitHub at a basic level.

> [!NOTE]
> The following commands assume you're working in a Linux environment. On a Windows machine, you should execute them in WSL or with the Git terminal for Windows

To contribute to this repository, you need to first clone it to your local machine. The easiest way to do this is in a terminal.

Navigate to a directory on your machine where you prefer to store your code. For me, that's `~/dev/projects`, it may be different for you. I'm just going to refer to it as the `projects` from now on.

```bash
cd ~/dev/projects
```

Clone the repository.

```bash
git clone https://github.com/4306-team-noname/barrios.git
```

To be continued...

## Github flow
> [!IMPORTANT] 
> __The Golden Rule__
> Don't forget to `fetch`, then `pull`, then `branch`
1. __Create a new branch__. You can do this in VS Code through the version control panel. Click the three dots, then `Branch > Create Branch`. Give it a name that either indicates what feature you're working on, or what issue number you're addressing. For this example, let's pretend we're creating a branch called `my-feature-branch`.
2. __Publish the branch__. Once the branch is created, the name of the branch you're working on should be changed in the version control panel. Instead of `main` it will say `my-feature-branch`. The big button at the bottom of the panel will probably say `Publish Branch`. Click the button to add your branch to the remote repository.
3. __Do work, make commits, push__. Do some work in your branch! Make commits, push code, etc. When you're all done, push your code one more time.
4. __Make a pull request__. Okay, this sounds weird but a "Pull Request" is different that `git pull`. Pull requests are a GitHub feature, not a git feature. So, open your browser and head to GitHub. Navigate to [the barrios repo](https://github.com/4306-team-noname/barrios) and click on the link above the code that says `n branches` (where `n` is the number of branches). That will take you to a page that has all the active branches. Find your branch and click the `New pull request` button. This will take you to a pull request form.
5. __Fill out the form__. Fill out the form. By default, it will have your last commit message as the pull request message. If you want to leave a comment, go ahead and do that too, especially if you think it will be helpful to whoever is reviewing your code. When you're ready, click the big, green `Create pull request` button.
6. __Wait for a review__. Once someone has looked over your code, they'll approve it for merging, or they'll request changes. Make those changes, push your code, then request a new review. When everything's good and your pull request has been approved, it's time to merge.
7. __Merge pull request__. Merge your changes into the main branch. Congratulations! You're done (for now).