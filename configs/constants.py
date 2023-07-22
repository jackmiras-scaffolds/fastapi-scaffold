from os import path


class Constants:
    """
    ---------------------------------------------------------------------------
    Application
    ---------------------------------------------------------------------------

    Here you may define all your HTTP statuses.
    """

    BASE_PATH = "/".join(path.dirname(__file__).split("/")[:-1])
    API_V1 = "/api/v1"

    """
    ---------------------------------------------------------------------------
    HTTP Statuses
    ---------------------------------------------------------------------------

    Here you may define all your HTTP statuses.
    """
    HTTP_OK = 200
    HTTP_CREATED = 201
    HTTP_NO_CONTENT = 204
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_FORBIDDEN = 403
    HTTP_NOT_FOUND = 404
    HTTP_CONFLICT = 409
    HTTP_UNPROCESSABLE_ENTITY = 422
    HTTP_INTERNAL_SERVER_ERROR = 500
