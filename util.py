import pickle
import tensorflow as tf

__model=None

def get_predicted_intensity(df):
    df = tf.constant(df)
    df = tf.keras.utils.timeseries_dataset_from_array(df, sequence_length=4, targets=None, sequence_stride=1)
    STD=22.389924
    MEAN=40.016973
    p=__model.predict(df)
    p  = p * STD + MEAN
    return p

def load_saved_artifacts():
    global __model
    if __model is None:
        with open("./artifacts/cyclone_intensity_prediction.pickle",'rb') as f:
            __model=pickle.load(f)
    print("loading pickle file...")

if __name__=="__main__":
    load_saved_artifacts()
    