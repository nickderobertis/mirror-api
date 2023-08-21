import typer
import uvicorn


def main(port: int = 8060, reload: bool = False):
    """
    Run a sample API server that returns whatever requests are sent to / as responses
    """
    uvicorn.run(
        "mirror_api._app_entrypoint:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
        reload=reload,
    )


if __name__ == "__main__":
    typer.run(main)
