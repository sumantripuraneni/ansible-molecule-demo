
def test_httpd_is_installed(host):
    httpd = host.package("httpd")
    assert httpd.is_installed
    #assert nginx.version.startswith("1.2")


def test_httpd_running_and_enabled(host):
    httpd = host.service("httpd")
    assert httpd.is_running
    assert httpd.is_enabled
