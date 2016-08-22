# FTP-Python
#!/usr/bin/env python  
import os from ftplib import FTP  
if os.path.exists('README'):  
raise IOError('refusing to overwrite your README file')  
def writeline(data):  
fd.write(data)  
fd.write(os.linesep)  
f = FTP('ftp.kernel.org')  
f.login()  
f.cwd('/pub/linux/kernel')  
fd = open('README', 'w')  
f.retrlines('RETR README', writeline)  
fd.close()  
f.quit()  
  
# Uploading a File  
  
#!/usr/bin/env python  
from ftplib import FTP  
import sys, getpass, os.path  
if len(sys.argv) != 5:  
print "usage: %s <host> <username> <localfile> <remotedir>" % (  
sys.argv[0])  
exit(2)  
host, username, localfile, remotedir = sys.argv[1:]  
password = getpass.getpass(  
"Enter password for %s on %s: " % (username, host))  
f = FTP(host)  
f.login(username, password)  
f.cwd(remotedir)  
fd = open(localfile, 'rb')  
f.storbinary('STOR %s' % os.path.basename(localfile), fd)  
fd.close()  
f.quit()  
