# Python Port Scanner

A simple port scanner built with Python

## How it works

This scans a range of ports for a given URL and prepares a report showing which ports are open.

## Instructions

Install with Pip/PyPi in the command line interface:

```
pip install port-scanner
```

In your Python code, import the library:

```
import portscanner
```

Create an instance of the Target class:

```
my_target = portscanner.Target("example.com")
```

Scan your target one or more times. All the settings shown below are optional, and the example code shows what the defaults would be if nothing is specified.

- "min" and "max" represent the range of ports to scan
- "timeout" is how long in seconds the scanner will wait for an unresponsive port before moving on to the next one

```
my_target.scan(min = 1, max = 100, timeout = 0.01)
```

Generate a report of the results of your scan(s), which will be returned as a list. Set all to "True" or leave it blank if you want your report to include all of the scans for your target, or set it to "False" to see only the most recent scan.

```
my_target.report(all = True)
```