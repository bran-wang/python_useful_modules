from __future__ import print_function

import urllib2

import taskflow.engines
from taskflow.patterns import linear_flow as lf
from taskflow import task


def flow_watch(state, details):
    print('Flow State: {}'.format(state))
    print('Flow Details: {}'.format(details))


def task_watch(state, details):
    print('Task State: {}'.format(state))
    print('Task Details: {}'.format(details))


def fetch(url):
    request = urllib2.Request(url=url)
    response = urllib2.urlopen(request)
    return response.getcode()


class GoogleFetch(task.Task):
    def execute(self, google_url, *args, **kwargs):
        status_code = fetch(google_url)
        print('Baidu Response Code: {}'.format(status_code))


class AmazonFetch(task.Task):
    def execute(self, amazon_url, *args, **kwargs):
        status_code = fetch(amazon_url)
        print('Github Response Code: {}'.format(status_code))


if __name__ == "__main__":
    flow = lf.Flow('simple-linear-listen').add(
        GoogleFetch(),
        AmazonFetch()
    )

    engine = taskflow.engines.load(flow,
                                   store=dict(
                                       google_url='http://www.baidu.com',
                                       amazon_url='http://github.com'))

    engine.notifier.register('*', flow_watch)
    engine.atom_notifier.register('*', task_watch)

    engine.run()
