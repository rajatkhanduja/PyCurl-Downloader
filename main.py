#!/usr/bin/python
# Author : Rajat Khanduja
# Program to make use of the downloader class (based on pycurl) and
# download
# Arguments should be as follows
# 		argv[1] : target_link
#		argv[2] : output_link
#		argv[3] (optional) : '-p' (to enable usage behind proxy)
#		argv[4] (optional) : proxy (if not provided, but '-p' given, then environment variable is used.
#
#
# Note that if '-p' parameter is passed, then http_proxy would be used
# (either from the next parameter or from environment variable)
#
#
# "Copyright 2011 Rajat Khanduja"
#
#
# This file is part of Pycurl-Downloader.
#
# Pycurl-Downloader is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pycurl-Downloader is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pycurl-Downloader.  If not, see <http://www.gnu.org/licenses/>.


from downloader import downloader
import sys
import os


def main(argv):

	# Get the information from the arguments
	try:
		target_address=argv[1]
		output_file=argv[2]
	except IndexError:
		print "my error handler"
		print "Incorrect number of arguments"
		print "Usage downloader <target_address> <output_file> [-p [proxy]]"
		sys.exit(1)		# Exit status 1 for invalid usage

	# Get the information about the proxy
	if len(argv)>3:
		if argv[3]=="-p":

			try:
				# Check if proxy is passed as an argument
				http_proxy=argv[4]

			except IndexError:
				# If proxy is not passed, use the environment variable
				http_proxy=os.environ['http_proxy']


	# Ensure that http_proxy variable is set
	try:
		http_proxy
	except NameError:
		http_proxy=None


	# Create a downloader object
	handle=downloader(target_address,output_file,http_proxy)

	# Download the files
	handle.download()

	# Concatenate the resulting segments
	handle.concatenate()

	# Delete temporary files
	handle.delete_temp()

if __name__=="__main__":
	main(sys.argv)
