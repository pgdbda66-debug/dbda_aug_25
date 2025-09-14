dbda@dbda-virtualbox:~/ones cat -n file_path.sh

1 #!/bin/bash

if [ $# -ne 1 ]; then

fi

echo "command usage: $0 <filepath>"

3 1234567

exit 1

8 file path=$1

10

if [ $file path]: then

11

echo "$ file_path exists

12

if [ -f $file_path]; then

13

echo "file_path is a regular file"

14

elif [-d Sfile_path]; then

15

echo "$file_path is a directory"

16

else

17

18 ft

echo "$file_path is not a regular file nor a directory

19 else

20

echo "$ file_path does not exist
