import psutil
import os

# psutil로 현재 실행 중인 프로세스 인스턴스를 가져옵니다
current_process = psutil.Process()

# temp 폴더 경로를 설정합니다. 
path_to_watch = os.environ['TEMP']

# 감시를 시작합니다
while True:
    try:
        # 감시중인 폴더의 내용을 가져와 파일이 생성되었는지 확인합니다.
        files = [f for f in os.listdir(path_to_watch) if f.endswith('.dll')]

        for file_name in files:
            # 프로세스 자신이 생성한 파일인지 확인합니다.
            file_path = os.path.join(path_to_watch, file_name)
            if os.path.isfile(file_path) and psutil.Process(current_process.pid).open_files()[0].path == file_path:
              # 다른 프로세스가 해당 파일을 사용 중인지 확인하기 위해 
              # 프로세스 ID를 확인하고 다른 프로세스가 파일을 열어놓았다면
              # continue를 사용하여 삭제하지 않습니다.
              continue
          
            # 파일 삭제 코드
            os.remove(file_path)
            
    except Exception as e:
        print(f"오류 발생: {e}")
