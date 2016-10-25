#!/usr/bin/env python
# -*- coding: utf-8 -*-

from concurrent import futures
from multiprocessing import cpu_count
import requests

executor = futures.ProcessPoolExecutor(max_workers=cpu_count())


def _save(endpoint, token, agent, log, extra):
    headers = dict()
    headers["X-LOGCENTRAL-TOKEN"] = token
    headers["User-Agent"] = agent
    for k, v in extra.items():
        headers[k] = v

    requests.post(endpoint, data=log, headers=headers)


def log(endpoint, token, agent, log, extra=None):
    executor.submit(_save, endpoint=endpoint, token=token, agent=agent, log=log, extra=extra)