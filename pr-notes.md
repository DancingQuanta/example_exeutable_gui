Version: 0.21

Message from `versioneer install`

```
 creating toy_gui/_version.py
 appending to toy_gui\__init__.py
 appending 'versioneer.py' to MANIFEST.in
 appending versionfile_source ('toy_gui/_version.py') to MANIFEST.in
```
The paths slashes are not consistent.

Paths in setup.cfg are parsed by configparser as strings which then is directly
used by python.

Options;

* VersioneerConfig attributes pre processing
* The configparser can be made to parse paths by passing a function to it that
convert paths.

Either results in windows paths in outputs.

Manifest must have posix paths.

Normalised paths for IO and posixpath for putput.

Don't change paths.

The real issue is in creating virtual environments for testing.

What is common.Common.subpath?

General issues:

* W605 invalid escape sequence '\*' ignore
