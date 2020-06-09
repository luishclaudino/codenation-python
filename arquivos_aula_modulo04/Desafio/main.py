import jwt


def create_token(data, secret):
    """
    This function creates a jwt token using the HS256 algorithm
    based on given data and secret key.

    Parameters:
        data (dict):
            Represents the data.

        secret (string):
            Represents the secret key to encrypt and
            decrypt the message.

    Returns:
        string: The token created with algorithm HS256
    """

    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    """
    This function verifies the signature token validity.

    Parameters:
        token (string):
            The token created with algorithm HS256,
            using 'acelera' as secret key.

    Returns:
        dict: The data inside the token or an error.
    """
    secret_key = 'acelera'

    # Try to decode the given token.
    try:
        data = jwt.decode(token, secret_key, algorithms=['HS256'])
    # If it raises an Exception, it returns the error message.
    except Exception:
        return {"error": 2}
    # If decoding was successful, it returns the data inside the token.
    else:
        return data
