# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from error import ValueTooSmallError
from error import ValueTooLargeError
from error import AlphaError, OffGridError, CrashError

###############################################################
# Exception classes used by the distutils implementation classes
###############################################################
from distutils.errors import \
     DistutilsExecError, DistutilsPlatformError, \
     CompileError, LibError, LinkError, UnknownFileError

###############################################################
# Exception classes used by the CCompiler implementation classes
###############################################################

from distutils.ccompiler import \
     CCompiler, gen_lib_options
from distutils import log

#############################################################
                   # HTTP ERROR EXCEPTIONS
#############################################################

from error import (  
    HTTPError,
    BadRequestsError,
    UnauthorizedError,
    ServiceUnavailableError,
)

from flask import Flask

import json

import logging, sys, json_logging


app = Flask(__name__)

json_logging.init_flask(enable_json=False)
json_logging.init_request_instrument(app)

logger = logging.getLogger("test-logger")
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))


# Flask constructor takes the name of
# current module (__name__) as argument.

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route("/json-message")
# ‘/’ URL is bound with hello_world() function.
def log_json():
    message = {
        "path": "json-messae",
        "infra": "pod",
        "protocol": "http",
    }

    logger.info(message)
    return message


# nested json


@app.route("/custom-exception")
# ‘/’ URL is bound with hello_world() function.
def log_custom_exception():
    raise ValueTooSmallError
    return "Hello World"


@app.route("/unparseable-exception")
# ‘/’ URL is bound with hello_world() function.
def log_unparseable_exception():
    raise ValueTooLargeError


@app.route("/multi-line")
# ‘/’ URL is bound with hello_world() function.
def log_multiline():
    logger.info("This is\n a multiline log\n Hope it works")
    return "Hello World"


@app.route("/health-check")
# ‘/’ URL is bound with hello_world() function.
def health_check():
    logger.info("health check")
    logger.info("ping localhost")
    return {"status": 200}

##############################################################


@app.route("/letter-exception")
# ‘/’ URL is bound with hello_world() function.
def log_letter_exception():
    raise AlphaError

@app.route("/crash-exception")
# ‘/’ URL is bound with hello_world() function.
def log_crash_exception():
    raise CrashError

@app.route("/dist-exception")
# ‘/’ URL is bound with hello_world() function.
def log_dist_exception():
    raise  DistutilsExecError 


@app.route("/compile-exception")
# ‘/’ URL is bound with hello_world() function.
def log_compile_exception():
    raise  CompileError 

@app.route("/library-exception")
# ‘/’ URL is bound with hello_world() function.
def log_library_exception():
    raise  LibError 

@app.route("/file-exception")
# ‘/’ URL is bound with hello_world() function.
def log_file_exception():
    raise  UnknownFileError 

@app.route("/http-exception")
# ‘/’ URL is bound with hello_world() function.
def log_http_exception():
    raise  BadRequestsError


@app.route("/auth-exception")
# ‘/’ URL is bound with hello_world() function.
def log_auth_exception():
    raise  UnauthorizedError

@app.route("/svc-exception")
# ‘/’ URL is bound with hello_world() function.
def log_svc_exception():
    raise  ServiceUnavailableError

# main driver function
if __name__ == "__main__":

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host="0.0.0.0")
