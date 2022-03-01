# -*- coding: utf-8 -*-
"""

@author: Abderrahmen Amich
@email:  aamich@umich.edu
"""

import warnings

from absl import app, flags
from mtd import test
from sys import argv, exit, stderr




if __name__ == "__main__":
    
    #### User configuration ####
                                                                                                                                                                                            
    if len(argv) < 7 or len(argv) > 17:
        print('Use: {} [data_name] [attack] [p] [n]  [Q_max] [lamda] [batch_size=128] [epsilon=0.3] [ssd_training_mode=SIMCLR] [arch =resnet50] [ckpt=./models_ssd]  [data_dir = data directory path] [data-mode = for SSD {base,ssl,org}] [normalize = normalise data for SSD] [batch_number=b1]  [size = ssd_getDatasets resize param ]'.format(argv[0]), file=stderr)
        exit(1)
    elif len(argv) >= 7:
        
        flags.DEFINE_string("data", argv[1], "used dataset.")
        flags.DEFINE_string("attack", argv[2], "evasion attack.")
        flags.DEFINE_integer("n", argv[4], "Number of student models.")
        flags.DEFINE_integer("p", argv[3], "Number of adv-trained student models.")
        flags.DEFINE_integer("Q_max", argv[5], "maximum number of queries for pool renewal.")
        flags.DEFINE_float("lamda", argv[6], "Noise scale.")
        flags.DEFINE_integer("test_set", 5000, "test set size.")
        flags.DEFINE_integer("class_nb", 10, "Number of labels.")
        if len(argv) == 7:
            flags.DEFINE_integer("batch", 32, "batch size.")
            flags.DEFINE_float("eps", 0.3, "Total epsilon for attacks.")
            flags.DEFINE_string("models_batch", 'b1', "the starting batch of student models.")
            
        elif len(argv) == 8:
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", 0.3, "Total epsilon for attacks.")
            flags.DEFINE_string("models_batch", 'b1', "the starting batch of student models.")
            
        elif len(argv) == 9:
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("models_batch", 'b1', "the starting batch of student models.")
            
        elif len(argv) == 10:
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("training_mode",argv[9],"pretrained model for ssd, traingin type")
        elif len(argv)==11 :
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("training_mode",argv[9],"pretrained model for ssd, traingin type")
            flags.DEFINE_string("models_batch", argv[10], "the starting batch of student models.")
        elif len(argv)==12 :
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("training_mode",argv[9],"pretrained model for ssd, traingin type")
            flags.DEFINE_string("arch",argv[10],"pretrained model for ssd, architeture")
            flags.DEFINE_string("models_batch", argv[11], "the starting batch of student models.")
        elif len(argv)==13 :
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("training_mode",argv[9],"pretrained model for ssd, traingin type")
            flags.DEFINE_string("arch",argv[10],"pretrained model for ssd, architeture")
            flags.DEFINE_string("ckpt",argv[11],"checkpoint to pretraiend model")
            flags.DEFINE_string("models_batch", argv[12], "the starting batch of student models.")
        elif len(argv)==17 :
            flags.DEFINE_integer("batch",argv[7] , "batch size.")
            flags.DEFINE_float("eps", argv[8], "Total epsilon for attacks.")
            flags.DEFINE_string("training_mode",argv[9],"pretrained model for ssd, traingin type")
            flags.DEFINE_string("arch",argv[10],"pretrained model for ssd, architeture")
            flags.DEFINE_string("ckpt",argv[11],"checkpoint to pretraiend model")
            flags.DEFINE_string("data_dir",argv[12],"directory to data")
            flags.DEFINE_string("data_mode",argv[13]," data mode = {org,vase,ssl}")
            flags.DEFINE_boolean("normalize",argv[14]," Normalize inpur dara")
            flags.DEFINE_string("models_batch", argv[15], "the starting batch of student models.")
            flags.DEFINE_integer("size",argv[16] , "idk")



    warnings.filterwarnings('ignore', '.*do not.*', )
    app.run(test)
