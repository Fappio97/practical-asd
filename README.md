# Exercise 1
The `git log` command in Git is used to display the commit history of a repository. The output of `git log` provides information about each commit in the repository. The file `exercise_1/pgf_log.txt` is an example, extracted from an open-source project on GitHub. This is an example of how two commits would be reported in `git log` output:

```
commit 5e2526a1edadb9beff974405a20bdf6147855d5d
Author: John Doe <john@doe.com>
Date:   Thu Oct 12 14:08:27 2023 +0200

    Found a new bug in parsing the --verbose argument.

commit c12ec313436034d08fd9c452d51001daafbe7fac
Author: John Doe <john@doe.com>
Date:   Thu Oct 12 14:04:57 2023 +0200

    Fixed a bug in parsing the --verbose argument.
    Now I am absolutely 100% sure everything works.

```

Your task is to develop, **following a test-driven development workflow**, a small library `parse_commits` to perform queries over the output of `git log`. Write your solution in the folder `exercise_1`. Your `parse_commits` implementation should be enough to support the following features, that you must provide in separate (see below) scripts:

1. Print to `STDOUT` all the _contributors_ (e.g., developers that have at least one commit) to a repository and their total number of commits;

2. Print to `STDOUT` all commits whose SHA-1 starts by an input substring. The SHA-1, the alphanumeric string that follows `commit`, is a unique identifier for commits in a repository.

3. Given in input two dates $D_1, D_2$ with $D_2 > D_1$, and a `git log` output $L$, filters $L$ removing all the commits that were performed before $D_1$ or after $D_2$. Print the remaining commits to `STDOUT`. _(If you use Python, `datetime.datetime.strptime` might be useful to parse the timestamp in `git log` output. In particular, the timestamp format to be used is `%a %b %d %H:%M:%S %Y %z`.)_

5. Given a file containing a list of blacklisted words, print to `STDOUT` the list of contributors' names that have at least one commit in the repository whose commit message contains one or more words in the blacklist, along with the SHA-1 of such commits.

6. Given a contributor email address, prints to `STDOUT` a report about how many commits she performed on each hour of each weekday. For example, you could output something like this:

```
Activity Matrix for Contributor: john@doe.com


Time/Day   Mon   Tue   Wed   Thu   Fri   Sat   Sun
00:00      0     0     0     0     0     0     0
01:00      0     0     0     0     0     0     0 
...
09:00      2     3     1     5     2     0     0 
...
23:00      2     1     2     3     0     0     0
```

where one could read that a contributor performed 5 commits on Thursdays between 09:00 and 09:59. _Don't worry about columns lining up; it's not the topmost priority._

**If you believe something is not clear or is ambiguous in the above assignment, take some design choices and explain them somewhere in the source with a comment**. For grading purposes, provide me some `1_contributors.py`, `2_filter_sha.py`, `3_filter_daterange.py`, `4_filter_words.py` and `5_print_activity_matrix.py` scripts I can run as follows, as well as any kind of "documentation" on how to run them. I will run the scripts from the root of the repository, so make sure doing this works:

```
# Moves from root of repository to base folder of Exercise 1
cd exercise_1 
python3 1_contributors.py [path to git log output]
python3 2_filter_sha.py [sha substring] [path to git log output]
python3 3_filter_datarange.py [date 1] [date 2] [path to git log output]
python3 4_filter_words.py [banned words filelist] [path to git log output]
python3 5_print_activity_matrix.py [email] [path to git log output]
```

where the arguments are:

*  `[path to git log output]` is a relative path to a text file containing the output of `git log`. 
* `[date 1], [date 2]` are dates in whatever format you like - if you do something exotic, document it. 
* `[sha substring]` is a substring without spaces. 
* `[banned words filelist]` is a relative path to a text file containing a list of banned words - one per line.
* `[email]` is an email address.

_The scripts being in Python are just examples - you can use whatever you like, as long as you read CLI args and/or text files and write to `STDOUT`_.

## On reading command line arguments
If possible, try to avoid asking for user input (e.g., `input()` in Python) in your scripts. In Python, you can read command line arguments as follows:

```python
# argv_example.py
import sys

if __name__ == '__main__':
    for pos, arg in enumerate(sys.argv):
	print(pos, arg)    
```

where `sys.argv` is a Python list that contains the command line arguments a script is invoked with. Practically, executing the following in `bash`:

```bash
python3 arg_example.py abc xyz -t q -v 0
```

yields the prints:

```
0 arg_example.py
1 abc
2 xyz
3 -t
4 q
5 -v
6 0
```

# Exercise 2
The folder `exercise_2` contains a Python package `app` and a tests folder `tests`. Write a GitHub Actions workflow that performs the following steps. **Steps [0,1,2,3,4] and [5,6,7] must be executed on two separate jobs**.

  0. Setup a local `virtualenv` Python environment, and activate it.
  1. Checks if the Python code contained in `app` is conformant to the `black` default style guide.
  2. Package and install the Python application by running `python -m build` and `pip install`.
  3. Runs the test module `tests/test_sanity_checks.py` by running `pytest`.
  4. Runs the module `tests/test_slow.py` by running `pytest`.

If all the above steps are successful, the following happen:

  5. Publish your application to `pypi` package index by running `publish.sh`
  6. Deploys the application by running the `deploy.sh` script.
  7. Notifies the team about the deployment status, by running the `notify_team.sh`.

The following commands are the rough equivalent to execute the previous steps in your local environment, starting from the root folder of the repository:

```bash
cd exercise_2

# Setting up local environment and dependencies [0-2]
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
black .
python3 -m build 
pip install dist/*.whl

# Running test suites, fast-to-slow order [3-4]
pytest tests/test_sanity_checks.py
pytest tests/test_slow.py

# Publish, deploy, notify [5-7]
chmod +x publish.sh
bash publish.sh
chmod +x deploy.sh
bash deploy.sh
chmod +x notify_team.sh
bash notify_team.sh
```

# Exercise 3
To bright up your teammates' work day, you decide to create a `commit-msg` Git hook that appends to each commit a random `xkcd` comic. For example, if someone performs a commit with commit message `revert: trying to fix issue #12 makes the server overheat and cause a fire hazard`, your hook will produce this:

```
revert: trying to fix issue #12 makes the server overheat and cause a fire hazard


Here's a random comic so you can procrastinate instead of working:
https://xkcd.com/2331/
```

In particular, the original commit message is separate by two blank lines, the string `Here's a random comic so you can procrastinate instead of working:` and on a newline a link to a random `xkcd` comic, obtained by concatenating a random positive integer (smaller than `2843`) to the base URL `https://xkcd.com/`.

__Recall the input parameter to the `commit-msg` hook **is not** the commit message, but the path of a temporary file where the commit message is written to. Check out Git client-side hooks' documentation.__


