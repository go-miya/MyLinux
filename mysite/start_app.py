from app.helloworld.session import HelloWorldModule
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Service in Downstream")
    HelloWorldModule().start()
