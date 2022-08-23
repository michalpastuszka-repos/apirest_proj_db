from apiflask_first import create_app
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    APP = create_app()
    APP.run(host="0.0.0.0", port=5000)