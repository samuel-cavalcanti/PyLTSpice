import sys
import unittest

from PyLTSpice.LTSpice_executable_path import LTSpiceExecutablePath


class TestLTSpiceExecutablePath(unittest.TestCase, unittest.TestResult):

    @staticmethod
    def init_LTSpiceExecutable(platform: str) -> LTSpiceExecutablePath:
        sys.platform = platform
        return LTSpiceExecutablePath()

    def test_linux_support(self):
        self.init_LTSpiceExecutable("linux")

    def test_mac_os_support(self):
        self.assertRaises(Exception, self.init_LTSpiceExecutable, "darwin")

    def test_windows_support(self):
        self.init_LTSpiceExecutable("win32")
        self.init_LTSpiceExecutable("cygwin")

    def test_get_default_linux_LTSpice_path(self):
        ltsplice_executable_path = self.init_LTSpiceExecutable("linux")
        path = ltsplice_executable_path.get()
        self.assertTrue(".wine/drive_c/Program Files/LTC/LTspiceXVII/XVIIx64.exe" in path)

    @unittest.skipIf(sys.platform != 'win32' and sys.platform != "cygwin",
                     "unable do find ltsplice executable if you not using windows")
    def test_get_default_win32_LTSpice_path(self):
        ltsplice_executable_path = self.init_LTSpiceExecutable("win32")
        path = ltsplice_executable_path.get()
        print(path)
        self.assertTrue("C:\Program Files (x86)\LTC\LLTspiceXVII\\" in path)


if __name__ == '__main__':
    unittest.main()
