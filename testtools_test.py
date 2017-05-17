import shutil
import tempfile
import testtools
import os

from pecan import set_config
from pecan.testing import load_test_app

import ConfigParser

CFG_PATH = os.environ.get('APP_CONFIG', '/etc/yoga/app.conf')
cfg = ConfigParser.ConfigParser()
cfg.read(CFG_PATH)

class BaseTest(testtools.TestCase):
    def setUp(self):
        super(BaseTest, self).setUp()
        cfg.read(os.path.join(os.path.dirname(__file__), '../etc/yoga/app.conf'))
        self._tmpdir = tempfile.mkdtemp()
        cfg.set('info', 'log_dir', self._tmpdir)

    def tearDown(self):
        super(BaseTest, self).tearDown()
        shutil.rmtree(self._tmpdir)
        set_config({}, overwrite=True)


class APITest(BaseTest):
    def setUp(self):
        super(APITest, self).setUp()
        self.app = load_test_app(os.path.join(os.path.dirname(__file__), 'test_config.py')

    def tearDown(self):
        super(APITest, self).tearDown()


