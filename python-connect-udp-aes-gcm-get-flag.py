import socket, hashlib
from Crypto.Cipher import AES



UDP_IP_ADDRESS = "10.10.149.151"
UDP_PORT_NO = 4000

# Create socket connect
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect to UDP Server
clientSock.connect((UDP_IP_ADDRESS,UDP_PORT_NO))


# Note that you have to use byte as mentioned in the task, you may modify as it suit you


# As mentioned in the task instruction, send 'hello' to UDP Server
# clientSock.send(b'hello\n')  # --- OR --- # clientSock.send('hello'.encode('UTF-8'))

# Store the 'hello' response back from UDP Server
# hello = clientSock.recv(4096)

# First 'hello' data get from UDP Server
# Sample output
# b"You've connected to the super secret server, send a packet with the payload ready to receive more information"
# print(data) # --- OR (convert byte to string) --- # print(data.decode("UTF-8"))



# Send 'ready' as instruct by UDP Server to receive more information
# clientSock.send(b'ready\n')

# Store the 'ready' response back from UDP Server
# ready = clientSock.recv(4096)

# Second 'ready' data get from UDP Server
# Sample output
# b"key:thisisaverysecretkeyl337 iv:secureivl337 to decrypt and find the flag that has a SHA256 checksum of ]w\xf0\x18\xd2\xbfwx`T\x86U\xd8Ms\x82\xdc'\xd6\xce\x81n\xdeh\xf6]rb\x14c\xd9\xda send final in the next payload to receive all the encrypted flags"
# print(ready)
# print('\n')



# Extract the SHA256 checksum given in the instruction
# checksum = ready[104:136]
checksum = b']w\xf0\x18\xd2\xbfwx`T\x86U\xd8Ms\x82\xdc\'\xd6\xce\x81n\xdeh\xf6]rb\x14c\xd9\xda'

# Change the byte to hex for the 'SHA256 checksum'
hex_checksum = checksum.hex()

# Print the value of hex_checksum
print(hex_checksum)

# You may extract the 'key' and 'iv' using the same method of extracting 'checksum'
# --- OR ---
# You may just hardcoded it
key_given='thisisaverysecretkeyl337'.encode('utf-8')
iv_given='secureivl337'.encode('utf-8')

# Print out the value of 'key' and 'iv' for your reference
print(key_given)
print(iv_given)



while True:

    # UDP Server sends sequentially in the form of the encrypted plaintext followed by the tag
    # So you will need to send 2 'final' to UDP Server, first to get 'encrypted plaintext'
    # Second to get the 'tag'


    # Send 'final' as instruct by UDP Server to receive all encrypted flags
    # This is the first 'final' which will get the 'encrypted plaintext'
    clientSock.send(b'final\n')

    # Store the 'encrypted_plaintext' response back from UDP Server
    encrypted_plaintext = clientSock.recv(4096)

    # Output of encrypted_plaintext
    # b'h\t:\xe9\xab\x8e\xb0\xc4}%/\xca\x1d'
    # flag = b'h\t:\xe9\xab\x8e\xb0\xc4}%/\xca\x1d'
    print(encrypted_plaintext)



    # Send second 'final' to UDP Server again to get following 'tag'
    clientSock.send(b'final\n')

    # Store the 'tag' response back from UDP Server
    tag = clientSock.recv(4096)

    # Output of tag 
    # b'Y\xdf\xa0\xe5\x8f+9%\xa8\x8eAO\xdbe\x83d'
    # tag = b'Y\xdf\xa0\xe5\x8f+9%\xa8\x8eAO\xdbe\x83d'
    print(tag)



    # With the 'key', 'iv', 'tag' and 'encrypted_plaintext'
    # We can decrypt the data by creating a decryptor of AES
    # You can google it for associated_data in AES
    # We put associated_data back in or the tag will fail to verify
    # when we finalize the decryptor.
    associated_data = ''
    decryptor = AES.new(key=key_given, mode=AES.MODE_GCM, nonce=iv_given)
    decryptor.update(associated_data)
    decrypted_text = decryptor.decrypt(encrypted_plaintext)
    # print(decrypted_text)



    # One you have the 'decrypted_text', you can compare against the 256 checksum given by the UDP Server from start
    # Which is the correct flags 256 checksum
    sha_signature = hashlib.sha256(decrypted_text).hexdigest()
    if(sha_signature == hex_checksum):
        print('flag is: '+ decrypted_text.decode('utf-8')+' !!!')
        break
    else:
        print(str(decrypted_text)+'is NOT flag')

clientSock.close()
