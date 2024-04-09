import asyncio  # For running the game in browser

from config.core import Core


def main():
    app = Core()
    asyncio.run(app.run())


if __name__ == "__main__":
    main()
