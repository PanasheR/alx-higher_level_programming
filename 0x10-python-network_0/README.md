# 0x10. Python - Network #0

## Resources
- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Requirements
- All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
- All your files must be executable
- The first line of all your bash files should be exactly #!/bin/bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing
- All curl commands must have the option -s (silent mode)
- The first line of all your Python files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.7.*)
- All your modules should be documented: python3 -c 
- 'print(__import__("my_module").__doc__)'
- All your classes should be documented: python3 -c 
- 'print(__import__("my_module").MyClass.__doc__)'
- All your functions (inside and outside a class) should be documented: python3 -c 
- 'print(__import__("my_module").my_function.__doc__)' and python3 -c 
- 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

#0 Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
- The size must be displayed in bytes
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
```

#1 Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
- Display only body of a 200 status code response
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
```

#2 Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$ 
```

#3 Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$
```

#4 Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response
- A header variable X-School-User-Id must be sent with the value 98
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$ 
```

#5 Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response
- A variable email must be sent with the value test@gmail.com
- A variable subject must be sent with the value I will always be here for PLD
- You have to use curl
Please test your script in the container provided, using the web server running on port 5000
```
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$
```

#6 Technical interview preparation:
- Write a function that finds a peak in a list of unsorted integers.
    - Prototype: def find_peak(list_of_integers):
    - You are not allowed to import any module
    - Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
    - 6-peak.py must contain the function
    - 6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
    - Note: there may be more than one peak in the list
```
guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt 
2 6-peak.txt
guillaume@ubuntu:~/0x10$ 
```
