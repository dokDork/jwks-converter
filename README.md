# jwks-converter
[![License](https://img.shields.io/badge/license-MIT-_red.svg)](https://opensource.org/licenses/MIT)  
<img src="https://github.com/dokDork/jwks-converter/raw/main/images/jwks-converter.png" width="250" height="250">  
  
## Description
The script reads a JWKS (JSON Web Key Set) file containing RSA public key parameters encoded in base64url format. It extracts the modulus (n) and exponent (e), decodes them into integers, and reconstructs the RSA public key. Finally, it exports the key in PEM format, which is commonly used in cryptographic applications. For example, running python jwks_to_pem.py jwks.json with a valid JWKS file prints the PEM-encoded RSA public key to the console, ready for use in verification or encryption tasks.

If you want, I can also help you refine or adapt these descriptions!

  
## Example Usage
 ```
python3 jwks-converter.py jwks.json
 ``` 
  
## Command-line parameters
```
python3 jwks-converter.py >jwks file>
```

| Parameter | Description                          | Example       |
|-----------|--------------------------------------|---------------|
| `jwks file`      | JSON file which contains public key of asymmetric algorithm used to sign a Token JWT | `<root site>/jwks.json`, `<root site>/.well-known/jwks.json` |

  
## How to install it on Kali Linux (or Debian distribution)
It's very simple  
```
cd /opt
sudo git clone https://github.com/dokDork/jwks-converter.git
cd jwks-converter 
chmod 755 jwks-converter.py 
python3 jwks-converter.py 
```
