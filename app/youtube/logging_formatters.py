from pythonjsonlogger import jsonlogger
from datetime import datetime
from zoneinfo import ZoneInfo

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            log_record['timestamp'] = datetime.now(ZoneInfo('Asia/Dhaka')).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname
            
        log_record['filename'] = record.filename
        log_record['message'] = record.msg





