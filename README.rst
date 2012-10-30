flooding
==========================================

Introduction

Usage, etc.

More details in src/flooding/USAGE.txt .


Works with RabbitMQ version 2.8.7.


Install production / staging server
-----------------------------------

Linux task machine (i.e. task 200). The task server checks out the
master trunk of flooding.

Init
    $ bin/fab staging_taskserver init
Update
    $ bin/fab staging_taskserver update_task

See staging-task-200.cfg as an example, it actually serves tasks 200,
210 and 220.


WARNING: buildout run on jupiter
--------------------------------

Buildout chokes if you run it with the smb share still mounted.  So,
as root, first unmount ('umount') the share::

  #> umount /srv/flooding.lizardsystem.nl/var/external_data

After buildout finished correctly, mount it again as root::

  #> mount /srv/flooding.lizardsystem.nl/var/external_data


Development installation
------------------------

The first time, you'll have to run the "bootstrap" script to set up setuptools
and buildout::

    $> python bootstrap.py

And then run buildout to set everything up::

    $> bin/buildout

(On windows it is called ``bin\buildout.exe``).

You'll have to re-run buildout when you or someone else made a change in
``setup.py`` or ``buildout.cfg``.

The current package is installed as a "development package", so
changes in .py files are automatically available (just like with ``python
setup.py develop``).

If you want to use trunk checkouts of other packages (instead of released
versions), add them as an "svn external" in the ``local_checkouts/`` directory
and add them to the ``develop =`` list in buildout.cfg.

Tests can always be run with ``bin/test`` or ``bin\test.exe``.


Model Migration:

Add field workflow_template

      flooding21=> Alter table flooding_scenario
                   Add COLUMN workflow_template integer;

Create Foreign key

      flooding21=> ALTER TABLE flooding_scenario
                   ADD CONSTRAINT workflowfk
                   FOREIGN KEY (workflow_template)
                   REFERENCES lizard_flooding_worker_workflowtemplate
                   (id);

Load data

     $> bin/django loaddata lizard_flooding_worker

Update field with same available workflow_template_id

       flooding21=> UPDATE flooding_scenario
                    SET workflow_template=[workflow_template_id];



Symlink a buildout configuration
--------------------------------

Initially, there's no ``buildout.cfg``. You need to make that a symlink to the
correct configuration. On your development machine, that is
``development.cfg`` (and ``staging.cfg`` or ``production.cfg``, for instance
on the server)::

    $> ln -s development.cfg buildout.cfg

