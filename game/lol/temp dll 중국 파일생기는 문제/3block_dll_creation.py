import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# temp 폴더 경로를 설정합니다.
path_to_watch = os.environ['TEMP']

class BlockDLLCreation(FileSystemEventHandler):
    def process(self, event):
        # 파일이 생성되었거나 수정되었는지 확인하고 파일 확장자가 '.dll'인지 확인합니다.
        if event.event_type in ['created', 'modified'] and event.src_path.endswith('.dll'):
            # 파일 삭제 코드
            try:
                os.remove(event.src_path)
            except OSError as e:
                print(e)
                
    def on_modified(self, event):
        self.process(event)
        
    def on_created(self, event):
        self.process(event)

if __name__ == "__main__":
    event_handler = BlockDLLCreation()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
