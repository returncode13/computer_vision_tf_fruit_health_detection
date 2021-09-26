config={
    
        "DATA_LOCATION":"/data/kaggle/zindi/fruit_disease_detection",
<<<<<<< HEAD
        "META_DATA_CSV":"train_yolo.csv",  #csv file holding information about the images. centers of bboxes, width etc.
        "TRAIN_IMAGES_DIR":"Train_Images",  #directory holding training images
        "EVAL_IMAGES_DIR":"Eval_Images",  #directory holding eval images
=======
        "META_DATA_CSV":"Train.csv",  #csv file holding information about the images. centers of bboxes, width etc.
        "TRAIN_IMAGES_DIR":"Train_Images",  #directory holding training images
>>>>>>> 59b1c9224e946cbb52d46fa796e925acad8e32fc
        "IMAGE_WIDTH":512,      #image width input to yolo
        "IMAGE_HEIGHT":512,    #image height input to yolo
        "Y_GRIDS":7,              #number of grids in the y direction
        "X_GRIDS":7,              #number of grids in the x direction
        "BBOXES":2,                #bounding boxes per grid location
        "nclasses":3,            #classes
        
        #using a prob_dist to balance 
        "balance_prob":"[]",
        "batch_size":4
}