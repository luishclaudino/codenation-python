from main import create_token, verify_signature


class TestChallenge4:
    """
    This is a class for testing the main script functions.

    Attributes:
        token (string): Valid token for testing.
        invalid_token (string): Invalid token for testing.
        error_message (dict): The error message returned
                              if the encryption or decryption fails.
        data (dict): The data to be encrypted or decrypted.
        secret_key (string): The secret key to encrypt and
                             decrypt the message.
    """
    token = (b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
             b'eyJsYW5ndWFnZSI6IlB5dGhvbiJ9.'
             b'sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M')

    invalid_token = (b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.'
                     b'eyJsYW5ndWQmLSI6IlB5dGhvbiJ9.'
                     b'sM_VQuKZe_VTlqfS3FlAm8XLFhgvQQLk2kkRTpiXq7M')

    error_message = {"error": 2}

    data = {"language": "Python"}

    secret_key = "acelera"

    def test_create_token(self):
        """
        This test function asserts that the created token is valid.
        """
        assert create_token(self.data, self.secret_key) == self.token

    def test_verify_signature(self):
        """
        This test function asserts that verify_signature function
        returns the data if the token is valid.
        """
        assert verify_signature(self.token) == self.data

    def test_verify_signature_fail(self):
        """
        This test function asserts that verify_signature function
        returns an error message in case the token is invalid.
        """
        assert verify_signature(self.invalid_token) == self.error_message
