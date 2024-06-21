from setuptools import setup, find_packages

setup(
    name='cluster_hmi_resources',
    use_scm_version=True,
    description='Resources for automation testing of digital instrument clusters.',
    author='Dinesh-D-2000',
    author_email='dineshdeena488@gmail.com',
    url="https://github.com/Dinesh-D-2000/cluster_hmi_tests",
    packages=find_packages(include=["drivers.*", "test_resources.*","webpage.*"]),
    include_package_data=True,
)