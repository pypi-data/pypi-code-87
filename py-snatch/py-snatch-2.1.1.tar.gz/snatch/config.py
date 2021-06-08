"""Get Environment Secrets for Snatch."""
import os
import sys
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from loguru import logger
from scalpl import Cut

from snatch.helpers.secrets_manager import SecretManager

load_dotenv()


def get_environment_from_secrets_manager(
    environment: str, log_level: str
) -> Dict[Any, Any]:
    """Load settings from Secrets Manager..

    :return Dict[Any, Any]
    """
    current_env = os.getenv("ENV", "production") if not environment else environment

    if "local" not in current_env:
        logger.remove()
        logger.add(sys.stderr, level=log_level)

    secrets = SecretManager(
        current_environment=current_env,
        project_name="snatch",
        current_env_data={},
    )

    secrets_manager_data = {"current_environment": current_env}
    if not secrets.can_read_secrets:
        return secrets_manager_data

    logger.info(
        f"Reading settings from `snatch/{current_env}` (logger level: {log_level})..."
    )

    secrets_manager_data.update(secrets.get_project_secrets())

    return secrets_manager_data


def get_settings(environment: Optional[str], log_level: str):

    config = {
        "snatch": {
            "boa_vista_secret_token": os.getenv("SNATCH_BOA_VISTA_SECRET_TOKEN", "foo"),
            "datasource_boa_vista_url": os.getenv(
                "SNATCH_DATASOURCE_BOA_VISTA_URL", "http://datasource_boa_vista"
            ),
            "banco_central_secret_token": os.getenv(
                "SNATCH_BANCO_CENTRAL_SECRET_TOKEN", "foo"
            ),
            "datasource_banco_central_url": os.getenv(
                "SNATCH_DATASOURCE_BANCO_CENTRAL_URL", "http://datasource_banco_central"
            ),
        }
    }
    config.update(
        get_environment_from_secrets_manager(
            environment=environment, log_level=log_level
        )
    )

    settings = Cut(config)
    return settings
