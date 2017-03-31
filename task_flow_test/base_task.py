from __future__ import print_function

import urllib2

import taskflow.engines
from taskflow.patterns import linear_flow as lf
from taskflow import task


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
    flow = lf.Flow('simple-linear').add(
        GoogleFetch(),
        AmazonFetch()
    )

    taskflow.engines.run(flow, store=dict(google_url='http://www.baidu.com',
                                          amazon_url='http://github.com'))
