from logging import Handler, getLogger
from traceback import print_exc
from crud import Crud
from models import User, Levels


class DBHandler(Handler):
    backup_logger = None

    def __init__(self, level=0, backup_logger_name=None):
        super().__init__(level)
        if backup_logger_name:
            self.backup_logger = getLogger(backup_logger_name)

    def emit(self, record):

        try:

            message = self.format(record)
            try:

                last_line = message.rsplit("\n", 1)[-1]
            except:
                last_line = None

            try:
                my_crud = Crud()
                with my_crud:
                    level = my_crud.get_or_create(Levels, level_name=record.levelname)

                    new_log = Log(
                        module=record.module,
                        thread_name=record.threadName,
                        file_name=record.filename,
                        func_name=record.funcName,
                        line_no=record.lineno,
                        process_name=record.processName,
                        message=message,
                        last_line=last_line,
                        level_id=level.id,
                    )

                    my_crud.insert(instances=new_log)

            except Exception as ex:
                if self.backup_logger:
                    try:
                        getattr(self.backup_logger, record.levelname.lower())(
                            record.message
                        )
                    except:
                        print_exc()
                else:
                    print_exc()

        except:
            print_exc()
