#!/bin/bash

# This script converts comments into the format expected by docurium.

# Ensure that the regexp search and replace tool `sar` is present in $PATH.
if ! which "sar" &> /dev/null; then
	echo 'Unable to locate the regexp search and replace tool `sar`.'
	echo 'To install `sar`, run:'
	echo ''
	echo '   go get github.com/mewkiz/cmd/sar'
	echo ''
	exit 1
fi

# Parse command line arguments.
if [ $# -ne 1 ]; then
	echo "Usage: docuriumify.sh FILE.cpp"
	exit 1
fi
cpp_file=$1

# Line comment starting at the beginning of the line.
#
# Replace `// foo` with `/// foo`
sar -i '(^|[\n])//([^/\n])' '${1}///${2}' ${cpp_file}

# Empty line comment starting at the beginning of the line.
#
# Replace `//` with `///`
sar -i '[\n]//[\n]' '\n///\n' ${cpp_file}

# Enum member line comments.
sar -i '([\n][ \t]*[a-zA-Z0-9_]+[ \t]*[=][ \t]*[a-zA-Z0-9_]+,[ \t]*//)([^/])' '${1}/<${2}' ${cpp_file}
