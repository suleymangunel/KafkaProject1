import sys
import os


if __name__ == '__main__':
    _argv_cnt = len(sys.argv)
    param1 = sys.argv[1] if _argv_cnt > 1 else None
    param2 = sys.argv[2] if _argv_cnt > 2 else None

    if _argv_cnt > 1:

        if param1 is not None and param1 == "kafka" and param2 is not None:
            if param2 == "1":
                import kafka_producer
                kafka_producer.main()
            else:
                import kafka_consumer
                kafka_consumer.main()

        if param1 == "bs":
            import bsexample
            bsexample.main()

        if param1 == "sl":
            import seleniumexample
            seleniumexample.main()

        if param1 == "cookie":
            import ClickCookie
            ClickCookie.main()
