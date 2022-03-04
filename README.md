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

## Example usage

```shell
pywmitool -a HOST_OR_IP -u USERNAME -q "SELECT Name FROM Win32_OperatingSystem"
```

