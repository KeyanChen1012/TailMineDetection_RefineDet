
# Fixed parameters
SCALAR = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
CLASSES = ['background', '2']
KEEP_DIFFICULT = False
RESULTS_LOG_PATH = 'results'
WEIGHT_DECAY = 0.0005
MOMENTUM = 0.9
OPTIMIZER = 'SGD'  # SGD, Adam, RMSprop
DEVICE = 'gpu'  # cpu or gpu
IS_TENSORBOARDX = True

# Train use
IMG_FORMAT = '.tiff'
MAX_EPOCH = 1000
MODEL_PATH = r'model'
MODEL_SAVE_EPOCH_FREQUENCY = 2
MODEL_LOG_ITERATION_FREQUENCY = 20
MODEL_TEST_ITERATION_FREQUENCY = 20
BATCH_SIZE = 2
TEST_BATCH_SIZE = 2
LR = 0.0005

# Previous use
MODEL_STATUS = 'train'  # for generate train.csv or test.csv and indicate the nets status
READ_PATH_DATASET = [
    r'F:\DataSet\WKK\Debug'
]
# READ_PATH_DATASET = r'F:\DataSet\WKK\sample_wkk_hb_BeiHang\8Bit'
PRIOR_MEAN_STD = \
    {"mean": [60.94673879975087, 61.1032557768852, 56.83122350238761], "std": 38.15972769815662}

# 图像的尺寸和网络尺寸是否接近，若不接近则在图上进行切割，如果接近直接Resize
IS_SRC_IMG_SIZE_NEAR_NET_SIZE = False

# 同类目标的标注框在大图上是否变化十分大，表现为大的基本贴合大图，
# 小的十分小，如果为True，则判断目标与输入网络尺寸的大小，将切割时长宽的大小进行适应性调整
IS_BBOX_SCALE_VARY_MUCH = True

INPUT_SIZE = (512, 512)

# 打印调试信息
IS_DEBUG = False

# net
CFG = {
    'feature_maps': [64, 32, 16, 8],
    'min_sizes': [25, 170, 315, 460],
    'max_sizes': [170, 315, 460, 605],
    'aspect_ratios': [[1.5, 2, 2.5], [1.5, 2, 2.5], [1.5, 2.5], [1.5, 2.5]],
    'clip': True,
    'variances': [0.1, 0.2]

}

