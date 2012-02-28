Pycurl-Download is a program that uses the python binding of the Curl library to make it easier and faster to download massive files. 
It is especially useful for those behind proxy who are restricted by the servers to download huge files. This can overcome that hurdle and download massive files, the only restricting parameter being the 'server' on which the file is kept. Based on certain settings, which could be unfavourable for Pycurl-Download, such downloads might fail and yeild erroneous files. This has to be fixed.

INSTALLATION GUIDELINES
-----------------------------------------------------------------------------------------

1. cd to the folder.
2. Make the setup executable
	chmod a+x setup.sh
3. Run the setup with sudo privileges.
	sudo ./setup.sh

This completes the installation

USAGE GUIDELINES
-----------------------------------------------------------------------------------------
Set the proxy variables. 
export http\_proxy="http://\<username\>[:password]@\<proxy-server\>[:\<proxy-port\>]

To use, simply open a terminal and execute the command as follows 
	
	pycurl-download <target-address> <output-file>

	eg :-
		
	pycurl-download http://<remote-file-address> ~/Desktop/<file-name>


TODO -list 
--------------

1. Create a GUI
2. Make it portable to Windows based systems 
3. For terminal usage, create visualisation of the percentage downloaded/left , expected time remaining, download speed, etc.
