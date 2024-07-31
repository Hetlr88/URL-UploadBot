import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7330436352:AAHUJUNGytd9bTY1otHe7EVwJlN4km0usXw")
    
    API_ID = int(os.environ.get("API_ID", 13384432))
    
    API_HASH = os.environ.get("API_HASH"",ea9db4503ed7088b788e06dfd818e00e")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "6169288210"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mrhex86:mrhex86@cluster0.8pxiirj.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
