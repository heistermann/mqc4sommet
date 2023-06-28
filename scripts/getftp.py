import ftplib
import io
import os
import sys

ftpserver = sys.argv[1]
ftpuser = sys.argv[2]
ftppw = sys.argv[3]
trgdir = sys.argv[4]


ftp = ftplib.FTP(ftpserver)
ftp.login(ftpuser , ftppw)

probes = [1,4,"c-4",12,21,22,26,31,33,34,35,36]

for probe in probes:
    print("----------------------")
    print("Processing %s" % probe)
    if not probe=="c-4":
        files = ftp.nlst('marquardt/sonde%d/' % probe)
    else:
        files = ftp.nlst('marquardt/%s/' % probe)
    for file in files:
        fname = os.path.basename(file)
        fpath = os.path.join(trgdir, str(probe), fname)
        if os.path.exists(fpath):
            print("EXISTS: %s" % file)
            continue
        try:
            r = io.BytesIO()
            ftp.retrbinary('RETR ' + file , r.write)
            data = r.getvalue().decode()
            r.close()
            print("SUCCESS: %s" % file)
        except:
            print("FAILED: %s" % file)
            continue
        f = open(fpath , 'w+')
        f.write(data)
        f.close()
ftp.close()
