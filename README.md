## Packaging an Application using **openvino deployment tools**.

### Creating a run time package using Intel OpenVINO toolkit:

   I used **Deployment Manager** present in **Intel OpenVINO** to create a runtime package from this application.

   To do this try the following:
   
        Start the Deployment Manager in interactive mode
        Select the hardware where you want to deploy your model
        Select the folder containing your application code, models, and data 
        
   These package can be easily sent to other hardware devices to be deployed.

   To deploy the **Inference Engine** components from the development machine to the target host, perform the following steps:

        Transfer the generated archive to the target host using your preferred method.

        Unpack the archive into the destination directory on the target host.
            For Linux:  tar xf openvino_deployment_package.tar.gz -C <destination_dir>
            For Windows, use an archiver your prefer.

## Steps

   Source the OpenVINO environment
   ``cd C:\Program Files (x86)\IntelSWTools\openvino\bin`` and than run ``setupvars.bat``
   
   if ``OpenVINO environment initialized``
   ``cd C:\Program Files (x86)\IntelSWTools\openvino\deployment_tools\tools\deployment_manager>``
   
   **Start the Deployment Manager in interactive mode**
   run ``python deployment_manager.py``
   
   You will see the menu:
   
   ``Deployment Manager
   Version 0.6
   --------------------------------------------------------------------------------
           1. [ ] Inference Engine Runtime for Intel(R) CPU

           2. [ ] Inference Engine Runtime for Intel(R) Processor Graphics

           3. [ ] Inference Engine Runtime for Intel(R) Gaussian Neural Accelerator

           4. [ ] Inference Engine Runtime for Intel(R) Vision Accelerator Design with
              Intel(R) Movidius(tm) VPUs



           a. Select/deselect all

           q. Cancel and exit

   Add or remove items by typing the number and hitting "Enter"
   Press "Enter" to continue.
   --------------------------------------------------------------------------------``
   
   than **select the target device on which you plan to deploy your model** 'by typing the number and hitting "Enter"'
   
   
   **Next menu**:
   
   ``Deployment Manager
   Version 0.6
   --------------------------------------------------------------------------------
   Review the targets below that will be added into the deployment package.
   If needed, change the output directory or add additional user data from the specific folder.

   --------------------------------------------------------------------------------


   Selected targets:
            - Inference Engine Runtime for Intel(R) CPU



           b. Back to selection dialog
           o. Change output directory [ C:\Users\directory\where\the\runtime\package\will\be\send ]
           u. Provide(or change) path to folder with user data
              (IRs, models, your application, and associated dependencies) [ None ]
           t. Change archive name [ openvino_deploy_package ]
           g. Generate package with current selection [ default ]
           q. Cancel and exit
   --------------------------------------------------------------------------------
   Please type a selection or press "Enter"``
   
   Type 'u'+'Enter' to provide the **path to the directory which contains the model and application code**.
   Type 'o'+'Enter' to provide the **full path to the output directory**.
   Type 'g'+'Enter' to generate runtime package.
   
   
   You will see:
   
   ``Deployment Manager
   Version 0.6
   --------------------------------------------------------------------------------
   Review the targets below that will be added into the deployment package.
   If needed, change the output directory or add additional user data from the specific folder.

   --------------------------------------------------------------------------------


   Selected targets:
            - Inference Engine Runtime for Intel(R) CPU



           b. Back to selection dialog
           o. Change output directory [ C:\Users\directory\where\the\runtime\package\will\be\send]
           u. Provide(or change) path to folder with user data
              (IRs, models, your application, and associated dependencies) [ C:\Users\directory\with\model's\IR\files\and\app\code]
           t. Change archive name [ openvino_deploy_package_FaceDetect ]
           g. Generate package with current selection [ default ]
           q. Cancel and exit
   --------------------------------------------------------------------------------
   Please type a selection or press "Enter" g
   [ 2020-08-01 08:02:16,509 ] INFO : Deployment archive is ready.You can find it here:
           C:\Users\directory\where\the\runtime\package\was\send\openvino_deploy_package_with_my_app.zip``
  
  #### The application code, models and OpenVINO Toolkit are included in the package created by the deployment manager.
   
   
   
   
   
   
   
