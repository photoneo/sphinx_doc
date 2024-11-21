.. raw:: html

    <style> .red {color:red} </style>
    <style> .green {color:green} </style>
    <style> .purple {color:purple} </style>

.. role:: red

.. role:: green

.. role:: purple



.. _device-window:


Device Window
=============

The Device Window is the main screen used to control the device. It is divided into 3 sections:

* :ref:`Main Controls <main_controls>` (:red:`red`)
* :ref:`Device settings pane <deivce_settings_pane>` (:green:`green`)
* :ref:`Visualisation pane <visualisation_pane>` (:purple:`purple`)

.. image:: \\images\\DeviceWindow.png

.. _main_controls:

Main Controls
-------------

The :ref:`Main Controls <main-controls>` provide the basic functions and advanced tools for triggering and :ref:`saving scans <saving-scans>`, and for safe disconnection from the device. 

.. _deivce_settings_pane:

Device settings pane
--------------------

The :ref:`Device settings pane <device-settings-pane>` :
* Contains the scanning profiles selector and scanning parameters (tab :guilabel:`Settings`)
* Allows control of the output data received from the device (tab :guilabel:`Structure`)

.. note:: The set of scanning parameters and profiles depends on the firmware version of your device. This documentation is based on the FW version 1.13.



.. _visualisation_pane:

Visualisation pane
------------------

The :ref:`Visualisation pane <visualisation-pane>` displays the output from the Scanner in various views. After the Device window is opened, hit :kbd:`F5` or press the :guilabel:`Trigger scan` button in the
:ref:`main controls <main_controls>` to trigger the scan. The output is provided as a 3D point cloud (3D Viewer tab) and a set of corresponding data as 2D images (all other tabs). 
The view can be switched using the tabs at the bottom. Each view has its own display settings on the right. These settings do not change the data themselves, 
just their visualization.


.. _saving_scans:

Saving 3D Scans
---------------

The :ref:`Saving 3D Scans <saving-scans>` explains what the output of a scan can contains as well as supported formats to save the scans in. 
It also explains how to manually or automatically save scans.



















