from functools import lru_cache

from pydantic_settings import BaseSettings


class ApplicationConfig(BaseSettings):
    """
    Default values for the configuration. To override
    any value, put it into a ".env" file or export it.
    """

    # Environment
    ENVIRONMENT: str = "DEVELOPMENT"

    # Setup
    SERVICE_HOST: str = "127.0.0.1"
    PORT: int = 5000
    SSL: bool = True
    IS_DEVELOPMENT: bool = True
    # URL where the OpenAPI schemas are served. If it's None, all documentation
    # UI is disabled. Locally, override this setting to enable documentation.
    # Example: OPENAPI_URL: Optional[str] = "/openapi.json"
    OPENAPI_URL: str | None = None


@lru_cache
def get_config():
    application_config = ApplicationConfig()
    return application_config


config = get_config()
