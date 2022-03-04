# Python WMI Query Tool

Run a WMI (WQL) query on a remote host.

## Installation

Using pip:

```shell
pip install pywmitool
```

Or, clone this project and use the setup

```shell
python setup.py install
```

## Help

```
usage: pywmitool [-h] -a ADDRESS -u USERNAME [-p PASSWORD] [-d DOMAIN] -q WQL [-n NAMESPACE] [--debug] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -a ADDRESS, --address ADDRESS
                        host name or address of remote host
  -u USERNAME, --username USERNAME
                        Username
  -p PASSWORD, --password PASSWORD
                        password (asked if not provided)
  -d DOMAIN, --domain DOMAIN
                        optional domain name
  -q WQL, --wql WQL     WQL string
  -n NAMESPACE, --namespace NAMESPACE
                        Namespace, defaults to `root/cimv2`
  --debug               Enable debug logging
  --version             Print version and exit
  ```

## Example usage

```shell
pywmitool -a HOST_OR_IP -u USERNAME -q "SELECT Name FROM Win32_OperatingSystem"
```

