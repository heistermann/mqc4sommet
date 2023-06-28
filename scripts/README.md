# call getftp.py

Create a shell script `anyname.sh` which contains the following

```
#!/bin/bash

CONDA=~/miniconda3/bin
SCRIPT=getftp.py
CONDAENV=my-env-name

TRGDIR=/home/my/target/directory

FTPSERVER=ftp.uni-potsdam.de
FTPUSER=fptusername
FTPPW=ftppassword

$CONDA/activate $CONDAENV
python $SCRIPT "$FTPSERVER" "$FTPUSER" "$FTPPW" "$TRGDIR"
$CONDA/deactivate
```

You can then execute via `$ ./anyname.sh` or move the process to a cronjob.

