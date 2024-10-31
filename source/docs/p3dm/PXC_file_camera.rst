.. _file_cam:

File Cameras
============

Every 3D scan captured by PhoXi 3D Scanner or MotionCam-3D can be saved into a Photoneo RAW (\*.praw) file. The main advantade
of this native format is that is contains all the information about the scanning configuration and additional informatin about the device. All other formats can be exported from \*.praw files.

Additionally, synamic scans taken by MotionCam-3D can be saved into a Photoneo MotionCam-3D RAW (\*.pmraw) file. This format is capable of creating 
a file camera consisting of a single file, but containing many scans.

Single or multiple \*.praw files can be loaded into PhoXi Control either by using the menu or by dragging and dropping the files anywhere on the GUI. 
Opening N \*.praw files will create a new virtual device called File Camera.

This virtual device behaves in a very similar way to a regular device. In case of drag-and-dropping multiple \*.praw files or opening a \*.pmraw file,
you can use :guilabel:`Previous frame` and :guilabel:`Next frame` buttons, which replace the :guilabel:`Trigger` button, to cycle through the frames.
While looking at the last scan, you can press :kbd:`Right Arrow` to seamlessly move to the first scan. Respectively, you can move to the last scan by pressing :kbd:`Left Arrow`, while looking at the first scan.

.. image:: \\images\\FileCameraMainControl.png

.. tip:: PhoXi Control already contains 2 example file cameras, which contain 1 or more captured frames and can be ised for testing purposes. 

.. note:: The scanning parameters for File Camera are read-only, as these scans have already been taken and processed.

:ref:`Network Discovery <network-discovery>` window offers specific options for File Cameras when **right-click** is used, or by using a keyboard shortcut. 

.. image:: \\images\\FileCameraOptions.png
    :align: right
    :scale: 80%


* **Add as internal file camera**

   * Internal File Camera remains in Network Discovery even after you restart the PhoXi Control application.  
     Otherwise, the File Camera is present only until the end of application.


* **Remove from list** (:kbd:`Delete`) 

  * This option will remove the File Camera from the list of devices, but keep underlying files on disk. 


* **Delete from the filesystem** (:kbd:`Shift + Delete`)

  * This option will remove the File Camera from the list of devices and also delete underlying files from the disk.    


Setting the order of scans in an internal File Camera
-----------------------------------------------------

After creating an internal File Camera using a group of scans, it is possible to define the order of the loaded scans usin *order.cache* file in the directory of the internal 
File Camera which can be found at:
``%AppData%/PhotoneoPhoXiControl/File3DCameras/<file camera name>``

Create a file *order.cache* and open it in a text editor. The order of the scans being loaded in the internal file camera can be defined as follows:

* Defining the order by name (alphabetical order)

  * Line 1: "order_by_name" 

* Defining the order by the last modified date/time

  * Line 1: "order_by_modified_time" custom 

* Definins a custom order (**files not mentioned will be skipped**)

  * Line 1: "scan_1.praw"
  * Line 2: "scan_14.praw"

.. note:: The File Camera needs to be set to an Internal File Camera in order for *order.cache* configuration file to affect the order. Scans loaded to PhoXi Control by 
    :menuselection:`Menu --> Open File Camera` or by dragging the scans will be normally loaded in the order they were selected in their original directory. 

Scanning Setting and \*.praw Files Compatibility
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The scanning settings are applicable to the device depending on its FW version. A \*.praw file contains complete data about the scan, including scanning settings.
It needs to be noted that older versions of PhoXi Control might not display all parameters of devices with newer FW.















