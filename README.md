# HTTPForce
HTTPForce is a simple program that uses a dictionary attack to bruteforce HTTP basic authentication pages.

Lets just get this out of the way real quick:
Im not responsible if you use this program nefariously or get in trouble with it.

Now that you're totally not going to illegally hack cameras in other countries, lets get started!

Make sure you install the requests module before runnning this program.
'pip install requests'

USAGE: 'python3 httpforce.py'

This program is pretty straightforward to use.
Username: The username you want to attempt to bruteforce
Wordlist: the wordlist to run through for password attempts, one password on each line.
URL: The target URL you want to attack. Make sure you put the full URL and not just the IP.

There are two main options when you begin the program: 
"1) Dictionary attack http basic authentication page" prompts you for each value and begins the attack.
"2) Use preconfigured options" creates two text files in your working directory that are referenced in the program.
These files store the credentials you use most and automatically set them each time you choose this option.

Make sure the site you are attacking is actually a Basic Authentication Page!
This looks like a white text box that pops up with a username and password input value when you visit the site.
If you attack a site that is not Basic Auth, the program will likley give a "false positives" error and exit.

There really isnt much more to this program...
If you have any suggestions or bug reports please let me know.

Happy hacking!

