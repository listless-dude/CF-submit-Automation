# Introduction

A simple problem submitter in Codeforces using Python/Selenium.

## Usage

### Clone the repo
`git clone https://github.com/mr-oogway/CF-submit-Automation.git`

### Install packages
`pip install selenium` or `pip install requirements.txt`

### Install Chrome webdrivers

Download Chrome webdriver according to your current Chrome version installed on your system
https://chromedriver.chromium.org/downloads

Then extract the downloaded file and replace the `SeleniumDrivers/` with the contents of extracted folder.

### Modify main.py

Change line 14 and line 16 to your Codeforces email and password. It is a bit insecure to type credential on a script. But this is for testing purpose only.

`email.send_keys("your-cf-email")`
and
`email.send_keys("your-cf-email")`

Go to the problem statement you want to solve. Change line 20 with that URL.
example: `browser.get('https://codeforces.com/contest/1782/problem/A')`

Change line 22, to submit the file and replace it with the absolute path to the problem file.

It is not complete automation, we still have to do some stuff manually, so hope to improve it in next versions.