# FTP-Python
#!/usr/bin/env python  
from ftplib import FTP  
f = FTP('ftp.ibiblio.org')  
print "Welcome:", f.getwelcome()  
f.login()  
print "Current working directory:", f.pwd()  
f.quit()  
