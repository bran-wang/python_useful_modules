import json
import logging
import requests

LOG = logging.getLogger(__name__)

def _default_json_response_handler(resp, default_error_handler):
    if resp.status_code == 200:
        return json.loads(resp.text)
    else:
        default_error_handler()


class Connection(object):
    def __init__(self, base_url, username, password, verify):
        self.username = username
        self.password = password
        self.verify = verify
        self.base_url = base_url
        self.session = requests.session()
        self.session.auth = (self.username, self.password)
        self.session.verify = self.verify

    def _get_generic_error_handler(self, method, url, resp):
        def _generic_error_handler():
            LOG.warn("status_code: %d\nbody:\n%s", resp.status_code, resp.text)
            if resp.status_code == 401:
                raise exceptions.yogaAuthenticationFailed()
            elif resp.status_code == 403:
                raise exceptions.yogaAuthorizationFailed()
            elif resp.status_code == 404:
                raise exceptions.NotFound()
            else:
                msg = "{} {} failed, user={}, verify={}".format(method, url, self.username, self.verify)
                raise exceptions.yogaServiceError(msg=msg)
          return _generic_error_handler()

    def post(self, url, data, handler=_default_json_response_handler):
        self.session.get(url)
        resp = self.session.post(url, data)
        return handler(resp, self._get_generic_error_handler('POST', url, resp))

    def get(self, url, handler=_default_json_response_handler):
        resp = self.session.get(url)
        return handler(resp, self._get_generic_error_handler('GET', url, resp))

    def put(self, url, data, handler=_default_json_response_handler):
        self.session.get(url)
        resp = self.session.put(url, data)
        return handler(resp, self._get_generic_error_handler('PUT', url, resp))

    def delete(self, url, handler=_default_json_response_handler):
        self.session.get(url)
        resp = self.session.delete(url)
        return handler(resp, self._get_generic_error_handler('DELETE', url, resp))


    def create_name(self, name):
        url = "{}/api/v1/name".format(self.base_url)
        data = {
            "name": "joke"
        }

        def get_handler(name):
            def my_handler(resp, default_error_handler):
                if resp.status_code == 201:
                    return json.loads(resp.text)
                elif resp.status_code == 409:
                    msg = "name {} already exists.".format(name)
                    raise exceptions.DuplicateName(msg)
                else:
                    default_error_handler()
             return my_handler
         return self.post(url, json.dumps(data), get_handler(name))

    def delete_name(self, name):
        url = "{}/api/v1/name".format(self.base_url)
        return self.delete(url)

    def update_name(self, name):
        url = "{}/api/v1/name".format(self.base_url)
        data = {
            "name": "bran"
        }
        
        def my_handler(resp, default_error_handler):
            if resp.status_code == 200 or resp.status_code == 201:
                return json.loads(resp.text)
            else:
                default_error_handler()
        return self.put(url, json.dumps(data), my_handler)

