import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('distro, package', [
    ('centos', 'libselinux'),
    ('centos', 'selinux-policy'),
    ('debian,ubuntu', 'selinux-basics'),
])
def test_packages_is_installed(host, distro, package):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    assert host.package(package).is_installed


@pytest.mark.parametrize('distro, file', [
    ('centos,debian,ubuntu', '/etc/selinux/config'),
])
def test_configuration_file_exists(host, distro, file):
    if host.system_info.distribution not in distro:
        pytest.skip("skipping unmatch distribution")
    file = host.file(file)
    assert file.exists


def test_getenforce_is_disabled(host):
    # Docker is prohibited using selinux and forced to disable
    cmd = 'getenforce | grep Disabled'
    result = host.run(cmd)
    assert result.rc == 0


def test_configuration_is_enforcing_v4(host):
    cmd = "grep 'SELINUX=enforcing' /etc/selinux/config"
    result = host.run(cmd)
    assert result.rc == 0
