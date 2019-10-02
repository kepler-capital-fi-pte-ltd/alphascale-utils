"""
A simple script to return the correct path in EFS. Is useful as folder names are changed while ETL is running.
Example use:
  file = "efs/processed_data/barra_100_asset_exposure/USA1.csv"
  df = pd.read_csv(valid_path(file))
"""
def valid_path(path : str, test_data=True):
    """
    :path: the full file path you want to validate
    :test_data: do you want to grab the file path from the test data or sample data bucket
    """
    main_dir = '/home/alfredo/efs/'
    if test_data:
        full_path = main_dir + 'processed_data_test/' + path
        return full_path
    else:
        full_path = main_dir + 'processed_data/' + path
        if os.path.exists(full_path):
            return full_path
        else:
            return full_path.replace("processed_data", "processed_data_old")
