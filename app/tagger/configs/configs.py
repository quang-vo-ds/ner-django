from src.utils.utils import get_datetime_str
class ARGS:
    seed = 101
    verbose = True
    debug = False
    data_io = "ncbi_disease"
    train_no = None
    dev_no = None
    test_no = None
    model = 'BiRNNCNNCRF'
    rnn_type = 'LSTM'
    load = None
    epoch_num = 40
    min_epoch_num = 1
    batch_size = 16
    gpu = 0
    check_for_lowercase = True
    emb_fn = "/kaggle/input/glove6b/glove.6B.200d.txt"
    emb_dim = 200
    emb_delimiter = ' '
    emb_load_all = False
    freeze_word_embeddings = False
    rnn_hidden_dim = 200
    ## Character CNN config
    word_len = 20
    char_embeddings_dim = 100
    freeze_char_embeddings = False
    char_window_size = [2,3,4]
    char_cnn_filter_num =len(char_window_size)
    dropout_ratio = 0.5
    dataset_sort = False
    word_seq_indexer = None
    evaluator = 'f1-macro'
    opt = 'adam'
    lr = 0.001 # in paper
    lr_decay = 0.95
    weight_decay = 5e-4
    momentum = 0.95
    patience = 4 # in paper
    report_fn = '%s_report.txt' % get_datetime_str()
    clip_grad = 5
    save = '%s_tagger.hdf5' % get_datetime_str()
    word_seq_indexer = '%s_word_seq_indexer.hdf5' % get_datetime_str()
    tag_seq_indexer = '%s_tag_seq_indexer.hdf5' % get_datetime_str()
    tag_sequences_train = '%s_tag_sequences_train.hdf5' % get_datetime_str()
    save_best = True