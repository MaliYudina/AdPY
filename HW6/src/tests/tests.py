import unittest
import HW6.src.helpers.config as config
import sys

from HW6.src.helpers.config import APP_NAME

test_config = config.Config()


class TestApp(unittest.TestCase):
    def setUp(self):
        """Hook method for setting up the test fixture before exercising it."""
        self.test_config = config.Config()
        self.init_env_in_windows_part_cases = ['.\\', 'C:\\']
        self.init_env_in_not_windows_part_cases = ['./', '~/', '~/.{}'
            .format(APP_NAME), '/etc/{}'.format(APP_NAME)]

    def test_config_file_creation(self):
        """Test if config_file was created, if created == True"""
        self.assertTrue(self.test_config.config_file)

    def test_config_paths_availability(self):
        """Test if config_paths was generated, if we receive the path == True"""
        self.assertTrue(self.test_config.config_paths)

    @unittest.skipUnless(  # Test if not Windows
        not sys.platform.lower().startswith('win'), 'Does not run on Windows')
    def test_get_windows_system_disk_on_linux(self):
        self.assertRaises(
            EnvironmentError,
            test_config.get_windows_system_disk)

    @unittest.skipUnless(  # Test if equals Windows
        sys.platform.lower().startswith('win'), 'Only run on Windows')
    def test_get_windows_system_disk(self):
        disk_result = test_config.get_windows_system_disk()
        self.assertRegex(disk_result, 'C', msg='System disc is not C ')


if __name__ == '__main__':
    unittest.main()
