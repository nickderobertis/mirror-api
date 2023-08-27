import os
from typing import Union

import typer
import uvicorn


def _main(port: int = 8060, reload: bool = False, status_code: Union[int, None] = None):
    """
    Run a sample API server that returns whatever requests are sent to / as responses
    """
    if status_code:
        os.environ["MIRROR_API_STATUS_CODE"] = str(status_code)
    uvicorn.run(
        "mirror_api._app_entrypoint:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
        reload=reload,
    )


def main():
    typer.run(_main)


if __name__ == "__main__":
    main()
