.. _multiinstance:

Multiple Versions of PhoXi Control
==================================

Multiple versions of PhoXi Control can be installed on one computer. This is achieved by choosing different installation directories during the installation. The process is as follows:

.. tabs::

    .. tab:: WINDOWS
        On Windows, the installer asks for a path where the application should be installed. By default, this path is:
        ``C:\Program Files\Photoneo\PhoXiControl-<version>``
        When another version of PhoXi Control is being installed, a different path should be specified, for example:
        ``C:\Program Files\Photoneo\PhoXiControl-custom``

    .. tab:: LINUX 
        Ubuntu installer automatically installs PhoXi Control in the following folder:
        ``/opt/Photoneo/PhoXiControl-1.13.x``
        To install PhoXi Control to a different folder, pass it as an argument to the install script:

        .. code-block:: console

            $ sudo ./PhotoneoPhoXiControlInstaller-1.13.x-Ubuntu.run /your/custom/path

        To match the old behaviour of the Ubuntu installer, use the original location:
        
        .. code-block:: console

            $ sudo ./PhotoneoPhoXiControlInstaller-1.13.x-Ubuntu.run /opt/Photoneo/PhoXiControl

        
.. attention:: PhoXi Control path environment variable is set to the **latest installed version** of PhoXi Control, not the most recent PhoXi Control version (Example: User installs PhoXi Control 1.13 and then installs PhoXi Control 1.12). This may affect access to certain features only available in the newest release and are dependent on the path defined in the environment variable.

