.. raw:: html

    <style> .red {color:red} </style>
    <style> .green {color:green} </style>
    <style> .orange {color:orange} </style>
    <style> .blue {color:blue} </style>



.. role:: red

.. role:: green

.. role:: orange

.. role:: blue

.. _network-discovery:

Network Discovery 
==================

The Network Discovery window lists all available devices on the network. After the application starts, please wait a moment until all devices are found, or click on the refresh button in the upper left corner above the displayed devices. 

.. image:: \\images\\NetworkDiscovery.png

.. tip:: If your device is not listed, please make sure that it is turned on and connected to the network. After a short time, the device will appear on the list. The time required to discover a newly powered device should be under 3 minutes. The time required to discover the device after it was disconnected or the connection was lost should be under 45 seconds.

.. warning:: If no device is shown on your list, please check your network configuration. See the chapter :ref:`Configuring Device Network Settings <configuring-device-network-settings>` for more information.

Selecting a device will display its details such as **name**, **description**, **status**, and **ID**, as well as its **network settings**, **firmware version** and **model**.

The status field has three different “Occupied” states :

  * Occupied by me (via PhoXi Control): Indicated simply as "Occupied" (means the user is already connected)
  * Occupied by someone else (via PhoXi Control) : Displayed as "Occupied" with a red box showing the :red:`IP address`. 
  * Occupied via GigE Vision Interface. Displayed as "Occupied" with a red box labeled :red:`GigE Vision` (and the IP address if provided by the device)

IPv4 and IPv6 address rows contain dynamic interface labels. The labels dynamically change color: :red:`non-routable addresses`, :orange:`sub-1Gbps interface speed`, and :blue:`normal operation (1Gbps)`.


.. _device-states-overview:

Device States Overview
----------------------
The following list represents all the possible device states. It is only possible to connect to a device in :green:`Ready` state.

.. image:: \\images\\DeviceStates.png
    :align: center
    
|
+------------------------+----------------------------------------------------------------------------------------+
|| :red:`Not started`    || The device has just been plugged in or was restarted.                                 |
||                       || After a few seconds, the status will change to :orange:`Starting`.                    |
+------------------------+----------------------------------------------------------------------------------------+
|| :orange:`Starting`    || The device is starting its operating application.                                     |
||                       || After a few seconds, the status will change to :green:`Ready`.                        |
+------------------------+----------------------------------------------------------------------------------------+
| :green:`Ready`         | The device is ready for a new connection.                                              |
+------------------------+----------------------------------------------------------------------------------------+
|| :red:`Occupied`       || The device appears as occupied after the connection is established.                   |
||                       || Only one connection at a time is permitted.                                           |
||                       || It is not possible to connect to an occupied device.                                  |
+------------------------+----------------------------------------------------------------------------------------+
|| :orange:`Terminating` || The device is being terminated after the user disconnects from the device.            |
||                       || After a few moments, the status will change to :orange:`Starting` and :green:`Ready`. |
+------------------------+----------------------------------------------------------------------------------------+

This list can also be found in the lower left corner of the Network Discovery window. 

.. _connecting-to-the-device:

Connecting to the device
------------------------

To connect to a device, simply double-click on the device name or select it and click :guilabel:`Connect`. It usually takes about 2-5 seconds for the device to connect; however, based on the internal state of the device, it can take up to 1 minute. 
|br|
Once the device is connected, a new :ref:`Device window <device-window>` will open and its status in Network Discovery will change from :green:`Ready` to :red:`Occupied`. 
Therefore, if you share a device with other users, make sure you disconnect from it after you finish using it. 

Please ensure that you are using a wired network connection to the device. WIFI connections are not recommended due to lower speed and reliability. 

Relationship Between GUI and API
--------------------------------

Connection to the device via API causes the GUI to open the Device window similar to when connecting via the GUI. When you connect to the device through GUI, it is possible 
to work with the device through API.
 















.. |br| raw:: html

    <br>