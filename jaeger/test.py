import sys
import time
from lib.tracing import init_tracer
from opentracing import tags


def say_hello(hello_to):
    with tracer.start_span('say-hello') as span:
        span.set_tag('hello-to', hello_to)

        hello_str = 'Hello, %s!' % hello_to
        time.sleep(1)
        span.log_kv({'event': 'string-format', 'value': hello_str})

        print(hello_str)
        time.sleep(2)
        span.log_kv({'event': 'println'})


assert len(sys.argv) == 2

tracer = init_tracer('hello-world')

hello_to = sys.argv[1]
say_hello(hello_to)

# yield to IOLoop to flush the spans
time.sleep(2)
tracer.close()

