---
title: "How to: SSH keys with PuTTY"
---

# How to: SSH keys with PuTTY

## Creating the SSH key pair
When installing PuTTY you also get an application called __PuTTYgen__

1. Open __PuTTYgen__
2. Click __Generate__ 
3. Follow instructions (if there are any)
4. It is HIGHLY recommended to set a passphrase for the key
5. Save BOTH public and private keys
  * The Private key is just for you!
  * The public key is what you add to servers to allow the user who has the matching
  private key to log on to that server. If your are asked for a key, pubkey, etc, for
  authentication to a server, you should provide them ONLY with the public key.

![PuTTYgen](/assets/images/SSH/puttygen.jpg)

Sidenote: You can choose the type of key to generate. Google it if interested

## Using the SSH key pair with PuTTY

At this stage you have presumably added the public key has been added to the server
you are trying to access. When going to connect to a server using the they you need
to tell PuTTY to use it

1. In the PuTTY left pane navigate to _Connection_ -> _SSH_ -> _Auth_ -> _Credential_
2. Under _Private key file for authentication_ navigate to the private key you
have already created. Putty private keys end with the extension _.ppk_
3. Now you can navigate back to _Session_ in the left pane and connect to the server as normal

![Using the PuTTY private key](/assets/images/SSH/puttyuse.jpg)

