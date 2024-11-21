
.. _saving-scans:

Saving 3D Scans
===============

PhoXi Control allows you to save scans both manually and automatically. The automatic saving mode is called recording.

The output can contain:

  * **Point cloud** : an organized set of 3D points.
  * **Normals** : for each captured 3D point, the normal vector expresses the orientation of the captured surface. 
  * **Texture** : grayscale intensity or RGB values for each 3D point.
  * **Depth map** : the depth data for each pixel. 
  * **ColorCameraImage** : 2D RGB texture captured by the color camera unit in MotionCam-3D Color. 
  * **Confidence data** : the data expressing the estimated noise of the acquired point. 
  * **Information about the device**, such as the ID number, or calibration data of the image sensor.
  * **Information about the 3D scan**, e.g. duration, scanning parameters, coordinate system

All theese data can be stored only in the native Photoneo RAW formats (\*.praw or \*.pmraw). They can be opened later in PhoXi Control as a :ref:`File Camera <file_cam>` and 
converted to ant other supported file format.

Other scan formats (PLY, PTX, TIF) are capable of storing only partial information, usually only point cloud, normals, and texture. The saving options dialog enables
the user to choose from output structures saved in each file format. 

List of Supported Formats
^^^^^^^^^^^^^^^^^^^^^^^^^


* Photoneo RAW data format (\*.praw)
* MotionCam-3D RAW data format (\*.pmraw)
* Stanford's PLY (\*.ply)
* Leica's PTX (\*.ptx)
* Text file (\*.txt)
* Raw images in tif (\*.tif)

For each format, you can choose which data to store (point clud, normals, texture,...). For further information, see the Saving Options section below. 

Saving Single Scan Manually
^^^^^^^^^^^^^^^^^^^^^^^^^^^

After triggering a scan, use the :guilabel:`Save` button to open the saving dialog. Choose one of the supported formats and saving directory.

.. image:: \\images\\SingleScanManually.png
    :scale: 80%

Saving Scans Automatically - Recording
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Firstly, use the Savings Oprions dialog to define the destination and the file formats in which the acquired scan should be stored.

.. tip:: Using \*.txt format to save data during recording is **not** reccomended.

Afterwards, click the :guilabel:`Record` button to start or stop automatic recording. 

When recording is used in free run more, the disk writing speed may limit the number of stored frames and some frames might be skipped and not stored. This usually happens
when multiple file formats are being saved at once or when compression is used to save \*.praw files. If this occurs, the status bar in PhoXi Control displays the message:
**"Scans cannot be saved, they are generated faster than the computer can process them. Consider changing saving options."**.

Recording Options
^^^^^^^^^^^^^^^^^

Use the button :guilabel:`Recording Options` to configure how the 3D scans and corresponding data are saved. 

.. image:: \\images\\RecordingOptions.png
    :align: right
    :scale: 50%

The :guilabel:`Folder path` and :guilabel:`File pattern` fields are used by automatic recording.  
The :guilabel:`Folder path` defines the destination where the scans will be saved. The :guilabel:`File pattern` defines the name of the files, hash signs will be replaced by a counter
starting at the defined value. The image on the right depicts the settings that will save the scan with the name *scan_0000*. Users can define the frequency of saved scans by changin the 
*N* parameter. Additionally, the number of scans can be limited by the *Maximum number of scans* parameter. Use the checkboxes on the left to select all the formats
in which the scan should be saved during automatic recording. Use the :guilabel:`Options` buttons on the right to define which data should be saved when using 

Specifics of File Formats
"""""""""""""""""""""""""

* An Explanation of the Confidence map can be found in the 2D Image Tabs section
* Using a text file to save data may result in longer saving time, depending on the speed of your SSD or HDD. The same is true when the binary format is not used in the PLY format. 
* TIF file is one-dimensional, therefore it creates multiple files for each stored component. 



Understanding Scanner Outputs - Topology of the 3D Scan
"""""""""""""""""""""""""""""""""""""""""""""""""""""""

The point cloud acquired by Phoxi 3D Scanners is topologically organized according to the image sensor. An image from the image sensor is called texture. There is one 
computed 3D point for each pixel in the texture. If any point from the scene is not illuminated by projection (usually because of shadows) the corresponding pixel has no 3D value
(its coordinates are [0,0,0]) and is called a "zero 3D point".

For example, the pixel at position [x=2010, y=350] in the texture is the (2064*350 + 2010) = 724 410\ :sup:`th` point in the point cloud. 

PhoXi Control also allows for unorganized point clouds to be saved. In **unorganizes point clouds**, the "zero 3D points" are omitted and not saved; therefore, the topology
is lost. If you have an unorganized point cloud and would like to restore its organization, you will need to iterate over the point cloud and find corresponding pixel in the depth
map by comparing the Z value.


Understanding MotionCam-3D Output - Topology of the 3D Scan
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

On MotionCam-3D the relationship between the number of pixels on the image sensor and the number of point in the point cloud is not 1:1. The ratio depends on the 
Sampling and Output Topologies.





















