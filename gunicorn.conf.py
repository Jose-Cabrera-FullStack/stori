import multiprocessing

bind = '0.0.0.0:8010'
workers = multiprocessing.cpu_count() * 2
worker_class = 'uvicorn.workers.UvicornWorker'
