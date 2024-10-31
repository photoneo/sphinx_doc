
.. _visualisation-pane:

Visualisation pane
------------------

3D Viewer
^^^^^^^^^

Use this tab to inspect the point cloud and obtain a general overview of the scanned scene. 

OpenGL Support
""""""""""""""

In case that OpenGL does not have the required version necessary to visualize 3D point clud, the following error message will appear. It provides additional information about the 
current setup for your computer and notifies you that the given version of OpenGL does not meet the requirements to showcase 3D point cloud. 


.. image:: \\images\\OpenGLError.png
    
Changing the Visualisation
""""""""""""""""""""""""""

.. list-table:: 
   :header-rows: 1
   :widths: 20 80

   * - **Feature**
     - **Description**
   * - **Reset view**
     - Resets the camera to the default position.
   * - **Screenshot**
     - Allows the user to save a `.png` screenshot of the 3D Viewer window.
   * - **Intensity**
     - Select the data source for coloring the point cloud:
       
       - **Plain White** - All points are white, no shader is applied.
       - **Texture** - Points have color from the photo (Texture) of the scene.
       - **Normals** - The color is based on point orientation (direction of the normal vector).
       - **Depth** - **Grayscale** - The color of the point is based on its distance from the device. The farthest points are white; the closest points are black. If the coordinate space is set to Marker space and objects are below the marker pattern, negative depth may occur.
       - **Depth** - **Hue** - The color of the point is based on its distance from the device. The farthest points are red, green, and the nearest points are blue. If the coordinate space is set to Marker space and objects are below the marker pattern, negative depth may occur.
   * - **Visualization settings**
     - Adjusting the brightness and contrast of the scene:
       
       - **Contrast** - Manually set :guilabel:`Min` and :guilabel:`Max` values or use :guilabel:`Smart` or :guilabel:`Full` presets to adjust the contrast of the scene. This setting can be used only for the current frame or all frames by checking the box :guilabel:`Apply to every frame`. Additionally, when using the Depth - Hue intensity visualization, a trio of icons can be used for flexible range display options, enabling clamping, graying out, or hiding values beyond the selected range.
       .. image:: \\images\\VisualizationSettings.png
        :scale: 60%
       - The brightness of the scene can be adjusted by applying gamma correction. This is useful for viewing dark objects. It can be adjusted using a slider or setting the value manually. Clicking on :guilabel:`Reset` resets the value of Gamma to 1.
   * - **Show normals as ticks**
     - This checkbox allows the rendering of normal vectors for selected 3D points. The selection of 3D points can be adjusted using the Stride setting and the length of the vectors by the Length setting.
   * - **Coordinates**
     - Displaying the coordinate system:
       
       - **Axis** - Renders the axis of the coordinate system. \*
       - **Scanning volume** - Renders the scanning volume of the respective device.
       - **Primary Camera and Projection** - Renders the position and field of view of the Primary camera.
       - **Color Camera** - Renders the position and field of view of the Color Camera.
       - **Current Camera** - Renders the position and field of view of the Current Camera.
   
\*If after checking the Axis you do not see anything different, try zooming out in your 3D point cloud. 
Because the coordinate system origin is at the camera, you may not see the arrows representing axes if your current camera position aligns. 

Transformation matrix 
""""""""""""""""""""""
Shows the transformation matrix from "Point Cloud Space" to the currently chosen "Camera space" (or vice versa). Point Cloud Space is a general term used for the currently
chosen Coordinate Space (CameraSpace, MarkerSpace, RobotSpace, CustomSpace or PrimaryCameraSpace).

Frame Information
"""""""""""""""""
Shows information about the current frame, such as:

* **Index** - serial number of scanned frames in a current session
* **Total scans** - number of scans made by the scanner or number of \*.praw / \*.pmraw files in the :ref:`File Camera <file_cam>`







