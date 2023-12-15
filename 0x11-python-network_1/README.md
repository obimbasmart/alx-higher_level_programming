# Python - Network #1

## Mandatory task

<details><summary><code>0-hbtn_status.py</code>Write a Python script that fetches https://alx-intranet.hbtn.io/status </summary>

- You must use the package `urllib`
- You are not allowed to import any packages other than urllib
- The body of the response must be displayed like the following example - (tabulation before -)
- You must use a with statement
- guillaume@ubuntu:~/0x11$ ./0-hbtn_status.py | cat -e
``````bash
Body response:$
    - type: <class 'bytes'>$
    - content: b'OK'$
    - utf8 content: OK$
guillaume@ubuntu:~/0x11$ 
``````
</details>


<details><summary><code>1-hbtn_header.py</code>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. </summary>

- You must use the packages `urllib` and `sys`
- You are not allow to import packages other than `urllib` and sys
- The value of this variable is different for each request
- You don’t need to check arguments passed to the script (number or type)
- You must use a `with` statement
</details>



<details><summary><code>2-post_email.py</code>
Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8) </summary>

- The email must be sent in the email variable
- You must use the packages urllib and sys
- You are not allowed to import packages other than urllib and sys
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement 

</details>

<details><summary><code>3-error_code.py</code>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8). </summary>

- You have to manage `urllib.error.HTTPError` exceptions and print: Error - code: followed by the `HTTP` status code
- You must use the packages urllib and sys
- You are not allowed to import other packages than `urllib` and `sys`
- You don’t need to check arguments passed to the script (number or type)
- You must use the with statement
</details>

<details><summary><code>4-hbtn_status.py</code>Write a Python script that fetches https://alx-intranet.hbtn.io/status </summary>

- You must use the package `requests`
- You are not allow to import packages other than `requests`
- The body of the response must be display like the following example - (tabulation before -)
</details>


<details><summary><code>5-hbtn_header.py</code>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header</summary>

- You must use the packages requests and sys
- You are not allow to import other packages than requests and sys
- The value of this variable is different for each request
- You don’t need to check script arguments (number and type)
</details>


<details><summary><code>6-post_email.py</code>
Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.</summary>

- The email must be sent in the variable `email`
- You must use the packages requests and `sys`
- You are not allowed to import packages other than `requests` and `sys`
- You don’t need to error check arguments passed to the script (number or type)

</details>



<details><summary><code>7-error_code.py</code>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response. </summary>

- If the HTTP status code is greater than or equal to 400, print: Error - code: followed by the value of the HTTP status code
- You must use the packages requests and sys
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)
</details>

<details><summary><code>8-json_api.py</code>
Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.</summary>

- The letter must be sent in the variable ` q`
- If no argument is given, set `q=""`
- If the response body is properly `JSON` formatted and not empty, display - the id and name like this: `[<id>] <name>`
- Otherwise:
- Display Not a valid `JSON` if the `JSON` is invalid
- Display No result if the `JSON` is empty
- You must use the package requests and sys
- You are not allowed to import packages other than `requests` and `sys`
</details>

<details><summary><code>10-my_github.py</code>Write a Python script that takes your GitHub credentials (`username` and `password`) and uses the GitHub API to display your `id` </summary>

- You must use Basic `Authentication` with a personal access token as - password to access to your information (only read:user permission is - needed)
- The first argument will be your `username`
- The second argument will be your password (in your case, a personal - access token as password)
- You must use the package `requests` and `sys`
- You are not allowed to import packages other than requests and sys
- You don’t need to check arguments passed to the script (number or type)

## Advanced task

<details><summary><code>100-github_commits.py</code>The Holberton School staff evaluates candidates applying for a back-end position with multiple technical challenges, like this one: </summary>

<br>

> Please list 10 commits (from the most recent to oldest) of the repository “rails” by the user “rails”
You must use the GitHub API, [here](https://developer.github.com/v3/repos/commits/) is the documentation 
Print all commits by: `<sha>: <author name>` (one by line)

Write a Python script that takes 2 arguments in order to solve this challenge.

- The first argument will be the repository name
- The second argument will be the owner name
- You must use the packages requests and `sys`
- You are not allowed to import packages other than requests and `sys`
- You don’t need to check arguments passed to the script (number or type)