# Python Simple UDP Connect AES GCM

> Austin Lai | August 4th, 2021

---

<!-- Description -->

Python Simple UDP Connect using socket with AES GCM decryption to get flag

Created for one of TryHackMe Room.

**[Please check out the full script _here_](https://github.com/austin-lai/Python-Simple-UDP-Connect-AES-GCM/blob/main/python-connect-udp-aes-gcm-get-flag.py)**

<!-- /Description -->

## Detail of script usage

The script will connect to UDP Server with a specific given port.

Then will need you to send 4 message to UDP server to get response and instruction

- " hello "
- " ready "
- " final " --- First " final " will get the 256 checksum of flag
- " final " --- Second " final " will get the tag

Then it will decrypt the AES GCM and check the 256 checksum against the one given by UDP Server.

<br />

---

> Do let me know any command or step can be improve or you have any question you can contact me via THM message or write down comment below or via FB
