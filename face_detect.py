"""
    Simple people detection application for testing packaging app openvino deployment tools.
    We can use the Deployment Manager present in OpenVINO to create a runtime package from our application. 
    To do this try the following:
        Start the Deployment Manager in interactive mode
        Select the hardware where you want to deploy your model
        Select the folder containing your application code, models, and data
    These packages can be easily sent to other hardware devices to be deployed.
    To deploy the Inference Engine components from the development machine to the target host, perform the following steps:
        Transfer the generated archive to the target host using your preferred method.
        Unpack the archive into the destination directory on the target host (replace the openvino_deployment_package with the name you use).
            For Linux:  tar xf openvino_deployment_package.tar.gz -C <destination_dir>
            For Windows, use an archiver your prefer.
"""

from openvino.inference_engine import IENetwork, IECore
import numpy as np
import cv2
import argparse
import logging

logging.getLogger().setLevel(logging.INFO)

#def load_model(args):
#    model=args.model
def load_model(args):
    model = args.model
    device = args.device
    model_weights = model + '.bin'
    model_structure = model + '.xml'
    net = IENetwork(model_structure, model_weights)
    ie = IECore()
    logging.info('Plugin initialized.')
    exec_net = ie.load_network(network=net, device_name=device, num_requests=1)
    logging.info('IENetwork loaded into the plugin as exec_net')
    input_blob = next(iter(net.inputs))
    output_blob = next(iter(net.outputs))
    return net, exec_net, input_blob, output_blob

def preprocess_frame(frame, net, input_blob):
    model_shape = net.inputs[input_blob].shape 
    model_w = model_shape[3]
    model_h = model_shape[2]
    frame4infer = np.copy(frame)
    frame4infer = cv2.resize(frame4infer, (model_w, model_h))
    frame4infer = frame4infer.transpose((2,0,1))
    frame4infer = frame4infer.reshape(1, 3, model_h, model_w)
    return frame4infer

def detect_face(exec_net, frame4infer, input_blob, output_blob):
    exec_net.start_async(request_id=0, inputs={input_blob:frame4infer})
    if exec_net.requests[0].wait(-1) == 0:
        output = exec_net.requests[0].outputs[output_blob]
    return output

def find_bb_coord(output, height, width):
    bb_coordinates = ()
    conf = 0
    for box in output[0][0]: # Output shape is 1x1xNx7                
        confidence = box[2]
        if confidence >= 0.6:
            xmin = int(box[3] * width)
            ymin = int(box[4] * height)
            xmax = int(box[5] * width)
            ymax = int(box[6] * height)
            # if multiple people in the same input frame
            # choose the one detected with bigest confidence
            if confidence > conf:
                conf = confidence
                bb_coordinates = (xmin,ymin,xmax,ymax)
    return bb_coordinates

def draw_bb(bb_coords, frame):
    cv2.rectangle(frame, (bb_coords[0],bb_coords[1]), (bb_coords[2],bb_coords[3]), (255,0,0), 2)

def main(args):
    cam = cv2.VideoCapture(0)
    width = int(cam.get(3))
    height = int(cam.get(4))
    cam.open(0)
    net, exec_net, input_blob, output_blob = load_model(args)
    logging.info('Model loaded! Starting inference...')
    try:
        if not cam.isOpened():
            print("Unable to open camera!")
        if cam.isOpened():
            print("Streaming from build-in camera!  Press 'q' or 'Ctrl+c' to leave.")
            while cam.isOpened():
                flag, frame = cam.read()
                if not flag:
                    break
                frame4infer = preprocess_frame(frame, net, input_blob)
                infer_output = detect_face(exec_net, frame4infer, input_blob, output_blob)
                bb_coords = find_bb_coord(infer_output, height, width)
                frame_copy = frame.copy()
                cv2.rectangle(frame_copy, (bb_coords[0],bb_coords[1]), (bb_coords[2],bb_coords[3]), (255,0,0), 2)
                cv2.imshow('Found Face', frame_copy)
                k = cv2.waitKey(1) & 0xFF
                if k == ord('q'):
                    break
    except KeyboardInterrupt:
        pass

    cam.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    print('Hello!')
    parser=argparse.ArgumentParser()
    logging.info('Get arguments.')
    parser.add_argument('--device', type=str, help='device', default='CPU')
    parser.add_argument('--model', type=str, help='The path to the model xml file', default='face-detection-adas-binary-0001')
    args=parser.parse_args()

    main(args)
    

#if __name__=='__main__':
#    parser=argparse.ArgumentParser()
#    parser.add_argument('--model', default="face-detection-adas-binary-0001")
    
#    args=parser.parse_args()
#    main(args)