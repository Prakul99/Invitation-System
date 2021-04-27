To go to the welcome page simple go 

http://www-test.cs.umanitoba.ca/~prakul/cgi-bin/welcome.cgi

All the cgi files are in cgi-bin on my umanitoba server.

There is a names.txt which is storing all the names and their attending status in cgi-bin.


The working of the system is following.

First you click on the link and go to welcome page.
you will put your name and status for the event.
If your name is not valid or you did not mark you status, you will shown an error.
After putting the information the system will take you to the required replied page.
In replied page you have another option to change your attending status.

After you reply for invitation, If the user reloads the page, they will see the same response and hence they do not need to submit the response again.
The Person who sends the invitation can also see the names and their attending status.


To run the Invitation system on your server,

- You need to copy all of the files and pase it on your server's CGI bin.
- change the permissions to run the files, (I am using chmod 711).

Thanks,
Enjoy :)
