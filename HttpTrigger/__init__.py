import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Hello World function processed a request.')
    return func.HttpResponse("Hello World from Azure Function!", status_code=200)
