# WebHackUrls
Python OSINT tool for urls recon thanks to the waybackmachine.

## Prerequisites:

- requests
- selenium
- re

## Install:
```bash
$ git clone https://github.com/mathis2001/WebHackUrls

$ cd WebHackUrls

$ python3 webhackurls.py
```
## Usage:
```bash
./webhackurls.py [-h] -d target.xyz [-k keyword] [-l limit] [-s] [-r rate-limit] [-p proxy] [-o output] [-oD domain names output]
```
Can be use with other tools for more efficient results

![tes](https://user-images.githubusercontent.com/40497633/170056609-1588032a-9517-4e34-b673-e20425bbe7fe.png)


## Options:
```bash
  -h, --help  show this help message and exit
  
  -d          target domain (exp: target.com)
  
  -k          search for a specific extension or keyword (js, xml, json, pdf... or admin, login, dashboard...)
  
  -l          limit (number of links you want)
  
  -s          take screenshot of each url found
  
  -r          delay between two screenshots

  -p          send request for each url to the given proxy (exp: 127.0.0.1:8080)
  
  -o          Output file name
  
  -oD         Output file name for domain names
```
## Screenshots:
![image](https://user-images.githubusercontent.com/40497633/170048245-33a3c4f8-8e22-4e1b-a952-51c4b09052e5.png)

![test](https://user-images.githubusercontent.com/40497633/170048855-b3bbe235-ea48-424e-a396-fdef19f3f251.png)

![test](https://user-images.githubusercontent.com/40497633/170049348-8390a45e-8ad8-4fae-b127-69ce2205e4cc.png)

![tempsnip](https://user-images.githubusercontent.com/40497633/174833111-6c85556d-ae65-46ba-bed7-15cb71c08143.png)

![image](https://user-images.githubusercontent.com/40497633/218415209-52ddebb5-979f-450f-802c-2cae2fab1cc8.png)

![image](https://github.com/mathis2001/WebHackUrls/assets/40497633/99f3b366-fce8-4a1f-88a6-8fecba99ed1e)





