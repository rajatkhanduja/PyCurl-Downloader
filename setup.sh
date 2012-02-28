python_version=2.7

# Install pycurl
sudo apt-get install python-pycurl

# Make the main file executable
chmod a+x main.py

# Copy the downloader class library to /usr/lib/python (this can be changed based on the version of python)
sudo cp downloader.py /usr/lib/python$python_version/

# Copy the main file to the bin folder
sudo cp main.py /usr/bin/pycurl-download

# Create a log file and change its read write permission
sudo touch /var/log/downloader.log ; sudo chmod 777 /var/log/downloader.log
