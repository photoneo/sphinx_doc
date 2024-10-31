
.. _diagnostic-scans:

Diagnostic Recording
====================

.. image:: \\images\\RecordingFormats.png
        :align: right
        :scale: 60%

This tool servers to save scans for diagnostic purposes independently from the client application. The setup allows choosing how often and where the scans are saved, and 
what information is contained within them. Open the :guilabel:`Recoring Options` and select PRAW format. Then scroll down and you can see the possibility of recording 

.. image:: \\images\\RecordingFormatsOptions.png
        :align: right
        :scale: 60%

When the maximum log file size is surpassed, deletion of \*.praw files will commence, beginning with the older \*.praw file. This tool can save:
* 3D scans with diagnostic data
* 3D scans with full diagnostic data (default, recommended)
* 2D outputs
* 2D outputs with diagnostic data

.. note:: Different diagnostic profiles have different performance impact, resulting in higher processing or transfer time.

Diagnostic Scan
===============

.. image:: \\images\\TriggerButtonSettings.png
    :align: right
    :scale: 70%

The user can also trigger a single diagnostic scan. Click on the drop-down arrow nect to :guilabel:`Trigger` and select :guilabel:`Trigger Diagnostic`.   

This scan saves the most amount of information. It can take longer to compute and the user is notified about the diagnostic frame by a yellow taskbar.

.. image:: \\images\\YellowTaskbar.png

After saving the scan with the :guilabel:`Save` button, it can be sent to Photoneo Support.  
















