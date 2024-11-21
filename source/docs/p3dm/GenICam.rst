.. geni_cam:

GenICam Interface
=================

The Generic Interface for Cameras standard is the base for plug-and-play handling of cameras and devices. It was developed by the European Machine Vision Association (EMVA)

GenICam support is provided via the GenTL library that works as a wrapper around PhoXi Control C++ API. PhoXi Control has to be running in order to use the GenICam interface. 

.. warning:: If at this point you **do not have** PhoXi Control installed, please follow the steps mentioned in :ref:`the installation section <install>`. 

The available examples for Python and Halcon support can be found in the installation directory:

* On Windows OS, the path to the GenTL directory is usually:

  * ``Program Files/Photoneo/PhoXiControl-1.13.x/API/GenTL``

* On Linux OS, the path to the GenTL directory is usually:

  * ``./opt/Photoneo/PhoXiControl-1.13.x/API/GenTL`` 