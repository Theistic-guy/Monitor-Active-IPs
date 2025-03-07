# Monitor-Active-IPs
A network monitoring tool that helps users identify active network connections and check their IP details.

Download the zip , extract and double-click the `.exe`. It will run the `netstat` command and fetch the active connections then do an ip lookup using ipinfo and list the server names. If it can't find a known server , `Unknown` would be listed as a result . Enter `y` (when prompted) to re-run and lookup connections of that time. 

**alternative to exe** : Simply run the python script on your system or create your own exe using `pyinstaller`
