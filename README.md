selinux
=========

Installs selinux and enfoce/disable it

Requirements
------------

None

Role Variables
--------------
if `selinux_enabled` was true, SELinux would be  activate.

Dependencies
------------

None

Example Playbook
----------------
```
- hosts: all
  vars:
    selinux_enabled: true

  roles:
    - role: ivoamorim.selinux
```

License
-------

BSD
