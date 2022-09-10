"""
Reference: https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning

Data validation: This step is required before model training to decide whether you should retrain the model or stop the execution of the pipeline. This decision is automatically made if the following was identified by the pipeline.

Data schema skews: These skews are considered anomalies in the input data, which means that the downstream pipeline steps, including data processing and model training, receives data that doesn't comply with the expected schema. In this case, you should stop the pipeline so the data science team can investigate. The team might release a fix or an update to the pipeline to handle these changes in the schema. Schema skews include receiving unexpected features, not receiving all the expected features, or receiving features with unexpected values.

Data values skews: These skews are significant changes in the statistical properties of data, which means that data patterns are changing, and you need to trigger a retraining of the model to capture these changes.
"""

from utils import *

Log(AppConst.DATA_VALIDATION)


# Check data schema skews
def check_receiving_unexpected_features():
    Log().log.info("start check_receiving_unexpected_features")
    Log().log.info("end check_receiving_unexpected_features")


def check_receiving_all_expected_features():
    Log().log.info("start check_receiving_all_expected_features")
    Log().log.info("end check_receiving_all_expected_features")


def check_receiving_unexpected_feature_values():
    Log().log.info("start check_receiving_unexpected_feature_values")
    Log().log.info("end check_receiving_unexpected_feature_values")


# Check data values skews
def check_data_values_skews():
    Log().log.info("start check_data_values_skews")
    Log().log.info("end check_data_values_skews")


# combine
def validate_data():
    Log().log.info("start validate_data")
    check_receiving_unexpected_features()
    check_receiving_all_expected_features()
    check_receiving_unexpected_feature_values()
    check_data_values_skews()
    Log().log.info("end validate_data")


if __name__ == "__main__":
    validate_data()
