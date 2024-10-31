

.. _install:

Installation
************

Computer Requirements
=====================

+-------------------+----------------------------------------------------------------------------+
|| Processor        || Intel Core i7 or higher, x64 architecture                                 |
||                  || (Processor performance affects the responsiveness of the application)     |
+-------------------+----------------------------------------------------------------------------+
|| Operating system || Only 64-bit platforms:                                                    |
||                  || Windows 10/11                                                             |
||                  || Ubuntu 18/20/22                                                           |
+-------------------+----------------------------------------------------------------------------+
| RAM               | Recommended 16GB (minimum 2GB for the application connected to 1 device)   |
+-------------------+----------------------------------------------------------------------------+
| SSD               | 128GB (minimum 4GB free disk space)                                        |
+-------------------+----------------------------------------------------------------------------+
| GPU               | GeForce GTX 1060 3GB or similar external GPU with OpenGL v3.0. support     |
+-------------------+----------------------------------------------------------------------------+

.. note:: Photoneo 3D Sensors have a very high resolution mode producing up to 3 million 3D points, therefore the requirements
    made on the graphical performance of your graphics card are higher.
    Old or slow graphics cards can reduce the performance of the 3D viewer. 


.. note:: PhoXi Control is necessary to have access to API. Please, after downloading PhoXi Control, check :ref:`the API section <API-section>` of this knowledgebase to learn more. 

.. tip:: While the installer will prompt you to uninstall any existing version of PHoXi Control, this step can be ignored, as :ref:`multiple versions of PhoXi Control <multiinstance>` can be installed on one computer. However, only one instance can run at a time. 



.. tabs::

   .. tab:: WINDOWS
      
      1. Download and run the latest `PhoXi Control <https://www.photoneo.com/downloads/phoxi-control/>`_ installer.
      2. Double-click the downloaded *.exe installation file.
      3. Run PhoXi Control as a standard Windows application. The applicaiton automatically starts after the computer starts. 
      
      .. note:: The user is able to install PhoXi Control with or without the included :ref:`file camera <file_cam>` examples or the API. This can be changed durin the *Choose Components* part of the installation process.

    Default installation paths:

    * Shortcut folder:
        ``C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Photoneo PhoXi Control``

    * Installation folder:
        ``C:\Program Files\Photoneo\PhoXiControl-<version>``
    * Application data folder:
        ``%AppData%/PhotoneoPhoXiControl/``

  


   
   .. tab:: LINUX

      1. Download and run the latest `PhoXi Control <https://www.photoneo.com/downloads/phoxi-control/>`_ installer.
      2. Unpack the downloaded *.tar file.
        .. code-block:: console

         $ tar -xvf PhotoneoPhoXiControlInstaller-<version>-Ubuntu[22 20 18]-STABLE.tar.gz 

      3. Make the file executable and then execute with :command:`sudo`. The installation requires the user to accept :abbr:`EULA (End-user license agreement)`, to do this automatically, pass the :command:`--accept` flag to the installer script.
        .. code-block:: console

            $ chmod +x PhotoneoPhoXiControlInstaller-<version>-Ubuntu[22 20 18]-STABLE.run
            $ sudo ./PhotoneoPhoXiControlInstaller-<version>-Ubuntu[22 20 18]-STABLE.run
            $ sudo ./PhotoneoPhoXiControlInstaller-Ubuntu-<version>.run --accept /opt/Photoneo/PhoXiControl-<version>
      4. Successful installation output will show you the installation path and will ask you to reboot.
      5. Restart your computer 
        .. code-block:: console

            $ sudo reboot
      6. Run PhoXi Control from a command line or from a launcher. 
       .. code-block:: console

            $ PhoXiControl

    Default installation paths:

    * Installation folder:
            ``/opt/Photoneo/PhoXiControl-<version>``
    * Application data folder:
            ``/home/<username>/.PhotoneoPhoXiControl``

    
   