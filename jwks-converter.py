from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64
import json
import sys

def base64url_to_int(val):
    """Decodes a base64url-encoded string to an integer."""
    val += '=' * (4 - (len(val) % 4))  # Add padding if necessary
    decoded = base64.urlsafe_b64decode(val)
    return int.from_bytes(decoded, 'big')

def convert_jwks_to_pem(jwks_file_path):
    """
    Converts the 'n' and 'e' values from a JWKS file to a PEM-encoded public key.

    Args:
        jwks_file_path (str): The path to the JWKS file (JSON format).

    Returns:
        str: The PEM-encoded public key as a string, or None if an error occurs.
    """
    try:
        with open(jwks_file_path, 'r') as f:
            jwks = json.load(f)

        # Assuming the first key in the JWKS is the one we want to use
        key = jwks['keys'][0]
        n_str = key['n']
        e_str = key['e']

        n_int = base64url_to_int(n_str)
        e_int = base64url_to_int(e_str)

        # Construct the RSA public key object
        public_numbers = rsa.RSAPublicNumbers(e_int, n_int)
        public_key = public_numbers.public_key()

        # Export the public key to PEM format
        pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return pem.decode('utf-8')

    except FileNotFoundError:
        return "Error: The file was not found at the specified path."
    except KeyError:
        return "Error: The JWKS file is missing the 'keys', 'n', or 'e' fields."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_jwks_file>")
        print("  <path_to_jwks_file>: The path to the JWKS file (JSON format).")
    else:
        jwks_file_path = sys.argv[1]
        pem_key = convert_jwks_to_pem(jwks_file_path)
        if "Error:" in pem_key:
             print(pem_key) # Print the error message
        else:
            print(pem_key) # Print the PEM key if successful
