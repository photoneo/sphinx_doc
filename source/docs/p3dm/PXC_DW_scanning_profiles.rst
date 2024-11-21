
.. _scanning-profiles:

.. |cog| image:: \\images\\Cog.png
    :align: middle
    :scale: 85%

.. |search-history| image:: \\images\\SearchHistory.png
    :align: middle
    :scale: 75%

.. |search-dock| image:: \\images\\SearchHistoryDock.png
    :align: middle
    :scale: 85%

.. |search-delete| image:: \\images\\SearchHistoryDelete.png
    :align: middle
    :scale: 85%

.. |search-clear| image:: \\images\\SearchHistoryClear.png
    :align: middle
    :scale: 85%
    :width: 60


.. image:: \\images\\ScanningProfilesDefault.png
    :align: right
    :scale: 80%

Scanning Profiles
=================

Scanning profiles allow users to easily change multiple scanning parameters at once. There are several profiles pre-configured with different scanning parameters for different uses.
Factory profiles are **not editable**, and **cannot** be **deleted or renamed**, however, it is possible to clone them and edit the cloned profile. 
A different set of factory profiles is available for MotionCam-3D and PhoXi 3D Scanner. It is also possible to define *custom profiles*.

Use the |cog| button to enter the advanced configuration. 

.. image:: \\images\\UserProfileDialog.png
    :align: right
    :scale: 75%
    :width: 470px

* :guilabel:`Select` - switch to the chosen profile. 
* :guilabel:`Create a new from existing` - this creates a new duplicate profile from your selected profile.  
* :guilabel:`Delete` - deletes user-created profile. 
* :guilabel:`Rename` - renames the user-created profile. 
* :guilabel:`Mark as startup profile` - the device will be started with this user profile. 
* :guilabel:`Reset to factory settings` - reset settings to factory default. 
* :guilabel:`Import` - imports a user profile from a \*.phop file. 
* :guilabel:`Export` - saves a user profile into the \*.phop file.

Using a Custom Profile
----------------------

* Use the |cog| button and create a new profile from the existing one, which is closest to your use case. You might want to mark it as a startup profile as well.
* Modify the desired parameters to your needs.
* Use the :guilabel:`Set and Store` button below to store the settings in your custom-made profile permanently.  


Scanning Parameters
-------------------

.. note::The set of scanning parameters available depends on the version of the firmware installed on the device. This manual is based on the firmware version 1.13.4.

The scanning process consists of three phases: capturing (or acquisition), processing (computation), and transfer.

Scanning parameters are divided into several logical groups. These groups differ for the PhoXi 3D Scanner, MotionCam-3D and MotionCam-3D Color.

PhoXi 3D Scanner
^^^^^^^^^^^^^^^^

.. image:: \\images\\ScanningParametersScanner.png
    :align: right
    :scale: 80%

* :guilabel:`Capturing Settings` - these options change exposure times and methods of projecting light patterns.
* :guilabel:`Processing Settings` - these options affect the computation of the poin cloud and allow the setting of filtering criteria such as the region of interest.  
* :guilabel:`Coordinate Settings` - defines the coordinate space for the point cloud 

MotionCam-3D
^^^^^^^^^^^^

.. image:: \\images\\ScanningParametersMotionCam.png
    :align: right
    :scale: 80%

* :guilabel:`General Settings` - settings that control the operating mode of MotionCam-3D (camera or scanner mode) 
* :guilabel:`\*Color Settings` - settings for 2D RGB camera unit 
* :guilabel:`Camera Mode` - settings for acquisition in camera mode 
* :guilabel:`Scanner Mode` - settings for acquisition in scanner mode 
* :guilabel:`Processing Settings` - point cloud computation and filtering (ROI) 
* :guilabel:`Coordinate Settings` - define the coordinate space for the point cloud 

\*only with the MotionCam-3D Color 

The total scanning time is the sum of the time required for acquisition (defined by capturing settings), computation (defined by processing settings) and transfer (defined by Output Structure).

Controls
^^^^^^^^

* :guilabel:`Search box` :kbd:`Ctrl+F` 

  * Search setting by name. Search box offers auto-suggestions based on all available settings for the connected device. 

* :guilabel:`Set button` :kbd:`Ctrl+S` 

  * Sets scanning parameters for the current session only. Settings are discarded after the Scanner is disconnected.

* :guilabel:`Set and store button` :kbd:`Ctrl+Shift+S` 

  * Stores scanning parameters permanently to the Scanner memory (applies to the current profile).
  
* :guilabel:`Refresh button` :kbd:`Ctrl+R` 

  * Retrieves current settings for the selected profile from the Scanner memory.  

.. image:: \\images\\Structure.png
    :align: right
    :scale: 45%
    :height: 335

Structure
---------


Output structure lets you choose what kind of data will be retrieved from the device. Any changes to the output structure will affect the transfer stage. 
The read-out time can be sped up by selecting only the data which you need for your application.



.. list-table:: 
   :header-rows: 1
   :widths: 20 80

   * - **Feature**
     - **Description**
   * - **PointCloud**
     - The point cloud is a set of measured 3D points. Each 3D point has the coordinates X, Y, and Z in the point cloud coordinate space (see Coordinate settings). The point cloud has a topology that depends on the device in use. On PhoXi 3D Scanners, each point in the point cloud corresponds to the pixel on the image sensor.
       
       On MotionCam-3D, the points are organized in superpixel topology - 2 or 4 3D points per one superpixel in irregular patterns or can be interpolated into a grid topology that resembles that of the scanner. Unmeasured points (pixels) caused by shadows are given the default coordinates [0, 0, 0]. Based on the saving options, these unmeasured points might or might not be saved.
       
       The point cloud can be examined in the 3D Viewer tab.
   * - **NormalMap**
     - The normal vector for each 3D point can also be calculated. The normal vector is perpendicular to the area surrounding the point (see Normal estimation radius).

       Normals can be inspected in the 3D Viewer tab after selecting the display parameter in the right panel.
   * - **DepthMap**
     - The "depth" of a point is the absolute 3D distance from the image sensor to the measured point (the ray of light that hits the surface of the object). The DepthMap is, therefore, always in the camera coordinate system and corresponds to the Z coordinate value in the point cloud.

       **Note:** Even when you change the point cloud coordinate space, the DepthMap always shows the distance (depth) in the camera coordinate system.
   * - **Texture**
     - Texture is the 2D photo of the scene. The texture is either in grayscale (in the red spectrum - the source of the illumination is either LED diode or laser projection) or Color captured by the RGB camera unit on MotionCam-3D Color (source of the illumination is either ambient light or internal white LED). The texture is also used to color the 3D point cloud.
   * - **ConfidenceMap**
     - For each measured 3D point, the "confidence" value expresses certainty about the accuracy of the point measurements. For example, a confidence value of 0.12 means that the estimated error for a point measurement is 0.12 mm. This value is based on a heuristic method that considers the light conditions for each pixel.
   * - **EventMap**
     - EventMap is a 2D output available only on MotionCam-3D. For each measured point, it shows the time when it was captured. The time is in milliseconds and is measured from the beginning of exposure - each point can have a value from 0 up to the total duration of exposure - i.e., 10 ms.
   * - **ColorCameraImage**
     - This output is only accessible on the MotionCam-3D Color. When set to true, it outputs an image from the RGB camera unit in the resolution specified in the Color Settings in the settings tab.

.. note:: Adjusting the resolution of the ColorCameraImage can affect the performance of the MotionCam-3D Color. 

.. image:: \\images\\Search.png
    :align: right
    :scale: 70%
    

Search history
--------------

|search-history| icon situated next to the search bar at the bottom of the Sevice Settings Pane allows 
the user to open the Search history window. This window contains the recent search inputs and can be very 
helpful when reusing a specific parameter repeatedly.

In the bottom right corner of the window, 3 buttons are available:

.. image:: \\images\\Search2.png
    :align: right
    :scale: 65%

* |search-dock| - Dock the Search history window
* |search-delete| - Delete selected history (:kbd:`Delete`)
* |search-clear| - Clear search history 

Docking the Search history window will result in the seach history being available 
under the search bar. 



















