import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# temp 폴더 경로를 설정합니다.
path_to_watch = os.environ['TEMP']

# 차단할 확장자 리스트를 정의합니다.
blocked_extensions = ['.dll', '.exe', '.bat']

class BlockFileCreation(FileSystemEventHandler):
    def process(self, event):
        # 파일이 생성되었거나 수정되었는지 확인합니다.
        if event.event_type in ['created', 'modified']:
            # 파일 확장자가 차단할 확장자 리스트에 포함되어 있는지 확인합니다.
            for extension in blocked_extensions:
                if event.src_path.endswith(extension):
                    # 차단된 파일 삭제 코드
                    try:
                        os.remove(event.src_path)
                        print(f"차단된 파일 삭제: {event.src_path}")
                    except OSError as e:
                        print(e)
                    break  # 이미 확장자가 차단 리스트에 있는 경우 반복문을 종료합니다.
                
    def on_modified(self, event):
        self.process(event)
        
    def on_created(self, event):
        self.process(event)

if __name__ == "__main__":
    event_handler = BlockFileCreation()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
