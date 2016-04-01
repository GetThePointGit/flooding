flooding
==========================================

Introduction

Usage, etc.

More details in src/flooding/USAGE.txt .


Works with RabbitMQ version 2.8.7.


Install Packages Ubuntu 14.04
-----------------------------
    $ sudo apt-get install binutils libproj-dev python-gdal gdal-bin python-scipy python-numpy


Install production / staging server
-----------------------------------

Linux task machine (i.e. task 200). The task server checks out the
master trunk of flooding.

Init
    $ bin/fab staging_taskserver init
Update
    $ bin/fab staging_taskserver update_task

Init
    $ bin/fab production_taskserver init
Update
    $ bin/fab production_taskserver update_task

See staging-task-200.cfg as an example, it actually serves tasks 200,
210 and 220.

Problems can arise when installing netcdf4. Try:

    $ sudo apt-get install libhdf5-serial-dev libnetcdf-dev



Deploying production webserver
--------------------------------

Deploying is done with ansible::

   $ bin/ansible-playbook ansible/deploy.yml --limit production_web


In case you need to release manually: ssh to the relevant server (look in
``ansible/inventory`` for the hostname) and **sudo to buildout**::

    $ cd /srv/HOSTNAME  # different for production/staging
    $ git pull
    $ bin/develop up
    $ bin/buildout
    $ bin/django migrate
    $ bin/supervisorctl reload


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



Workflows
------------------------
The next workflow_templates are created on migration:

DEFAULT_TEMPLATE_CODE = 1 (workflow for a scenario with sobek model)
IMPORTED_TEMPLATE_CODE = 2 (workflow for a scenario with onknown model via import)
THREEDI_TEMPLATE_CODE = 3 (workflow for scenario with 3di model)
MAP_EXPORT_TEMPLATE_CODE = 4 (workflow for map's export)

The range of template's code 0 - 50 area reserved for auto workflows.


Upload/download wateren- and kerigne-sahpes
-------------------------------------------
Create a symbolic link ``BUILDOUT_DIR/var/ror_export`` to the mounted directory
(see ``ROR_KERINGEN_PATH`` in ``settings.py``)::

    $ ln -s /mnt/flooding/Flooding/ror_keringen var


GISDATA
-------
Copy shape-files to ``BUILDOUT_DIR/var/gisdata`` from old-webserver.


EXCEL files
-----------
Copy excel-files to ``BUILDOUT_DIR/var/excel`` from old-webserver.


Setup mount to flod-share
-------------------------
Set ``cifspw``, mount in ``fstab``. Then create dir ``/mnt/flod-share``.

    $ sudo mkdir /mnt/flod-share
    $ sudo chown buildout:buildout /mnt/flod-share
    $ sudo mkdir -p /p-isilon-d1.external-nens.local/nens/flooding
    $ sudo chown buildout:buildout -R /p-isilon-d1.external-nens.local
    $ ln -s /mnt/flod-share flod-share
    $ ln -s /mnt/flod-share/pyramids pyramids
    $ ln -s /mnt/flod-share/ror_keringen ror_keringen
    $ ln -s /mnt/flod-share/exportruns/export_runs_csvs export_run_results

Symlink a buildout configuration
--------------------------------

Initially, there's no ``buildout.cfg``. You need to make that a symlink to the
correct configuration. On your development machine, that is
``development.cfg`` (and ``staging.cfg`` or ``production.cfg``, for instance
on the server)::

    $> ln -s development.cfg buildout.cfg


Raster Server
-------------

We also use an instance of the "raster-server" to serve WMS layers for
grid data. The grid data is stored as gislib "pyramids".

To use gislib and raster-server in Flooding, both need to be checked out
as development packages, using the "flooding-branch" branch.

Running Buildout, a configuration file for the raster-server is
created as etc/rasterserver.json. It says that the rasters are served
from BUILDOUT_DIR/var/pyramids. It is possible to symlink
/mnt/flooding/Flooding/pyramids to that directory, or to copy a few
rasters from the mounted share to that directory, or to change the
etc/rasterserver.json.in input file to use something file (in that
case, don't commit it).

The command to run the raster-server in development is, in the
buildout directory:


    $> RASTER_SERVER_SETTINGS=etc/rasterserver.json bin/runflask

The server will run at 0.0.0.0:5000 and visiting it should show a
working demo page where the available layers can be shown (although
there might be way too many for the page to render if you are using
the full Flooding share).

The URL used to find the WMS server is set in the Django settings as
RASTER_SERVER_URL. developmentsettings.py sets it to
'http://127.0.0.1:5000/wms' by default, change it to whatever you need
in localsettings.py if you are using virtual machines or similar.


Windows (task-server)
--------------------------------

* Check out the ``windows`` subdirectory, and customize it if needed.
* Check out the ``objectenbeheer/settings/windows.py`` module, and customize it if needed.

* Run ``build_windows.sh`` from Linux to wrap everything in a nice zip.

* In Windows, download Python 2.7.x from http://www.python.org/download/.
* In Windows, download Psycopg2 from http://www.stickpeople.com/projects/python/win-psycopg/.

* Extract the zip in the configured place, e.g. ``D:\Programs\flooding``.

* In Windows, configure your ``PYTHONPATH`` environment variable to point to the absolute path of the ``flooding\lib`` subdirectory.
  If you don't know how to do this, read https://kb.wisc.edu/cae/page.php?id=24500.

* To tune local settings like the database connection, create or edit ``objectenbeheer\lib\flooding\localsettings.py``.















