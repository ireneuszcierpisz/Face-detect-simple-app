## Simple face detection application for packing testing using **openvino deployment tools**.

### Creating a run time package using Intel OpenVINO toolkit:

   I used **Deployment Manager** present in **Intel OpenVINO** to create a runtime package from this application.

   To do this try the following:
   
        Start the Deployment Manager in interactive mode
        Select the hardware where you want to deploy your model
        Select the folder containing your application code, models, and data 
        
   These package can be easily sent to other hardware devices to be deployed.

   To deploy the **Inference Engine** components from the development machine to the target host, perform the following steps:

        Transfer the generated archive to the target host using your preferred method.

        Unpack the archive into the destination directory on the target host (replace the openvino_deployment_package with the name you use).
            For Linux:  tar xf openvino_deployment_package.tar.gz -C <destination_dir>
            For Windows, use an archiver your prefer.
