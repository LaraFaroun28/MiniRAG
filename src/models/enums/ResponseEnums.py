from enum import Enum
class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "File_Validate_Successfully"
    FTLE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXEEDED = "File Size Exceeded"
    FILE_UPLOAD_SUCCESS = "File_Upload_Success"
    FILE_UPLOAD_FAILD = "File_Upload_Failed"
