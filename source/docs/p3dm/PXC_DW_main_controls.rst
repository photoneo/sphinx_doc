
.. _main-controls:

Main controls
=============


Acquisition Modes - Triggering a Scan
-------------------------------------


* Single scan mode (default)

  * The device waits for the trigger command to capture a 3D scan. 
  * Use the :guilabel:`Trigger`/ :guilabel:`Set and Trigger` / :guilabel:`Trigger Diagnostics` button   

    * The :guilabel:`Set and Trigger` button automatically temporarily saves changes made in the Device Settings or Structure tabs and triggers a scan.  
    * The :guilabel:`Trigger Diagnostics` button takes a special scan that contains the most information and can take longer to compute. See Diagnostic scan section for more information. 

    .. image:: \\images\\TriggerButtonSettings.png
        :align: right
        :scale: 70%
   
    * :guilabel:`Trigger`, :guilabel:`Set and Trigger` and :guilabel:`Trigger Diagnostics` are 3 settings for the same button. Settings are changed through the dropdown menu accessible throught the small arrow 
      next to the button. 
* Free run mode

  * The device performs consecutive scans at maximum speed (if not slowed down by the Maximum FPS setting). 
  * To turn the free run mode **on** or **off**, use the button :guilabel:`Free run`. 
  * When the device is in *Free-run mode*, you can pause and restart the acquisition with the :guilabel:`Pause/Start` button.  

Photoneo 3D Sensors can also use a hardware trigger to acquire scans. In hardware trigger mode, the scan is triggered by a signal change on a specific GPIO pin. More information
can be found in the section Hardware trigger. 

You may prevent the device from taking a scan by using the :guilabel:`Pause` button at any time. Using this function is more intuitive in the API, where a secondary
application may prevent the first application from triggering a scan.

.. tip:: Once the window is open, hit :kbd:`F5` or the :guilabel:`Trigger` button to trigger a scan.
    
     


