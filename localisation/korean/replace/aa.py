import os

def change_language_in_files():
    """
    현재 폴더 내에서 파일 이름과 파일 내용의 'l_english'를 'l_korean'으로 변경합니다.
    """
    current_dir = os.getcwd()
    print(f"현재 작업 디렉토리: {current_dir}\n")

    # 1. 파일 내용 변경 및 파일명 변경을 위한 반복 작업
    for filename in os.listdir(current_dir):
        # .yml 파일이고 'l_english'가 포함된 파일만 처리
        if filename.endswith('.yml') and 'l_english' in filename:
            old_filepath = os.path.join(current_dir, filename)
            
            print(f"--- 파일 처리 시작: {filename} ---")
            
            # 목표 2: 파일 내부의 l_english를 l_korean으로 바꿀 것
            try:
                # 파일을 읽어서 내용 변경
                with open(old_filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content.replace('l_english:', 'l_korean:')
                
                # 변경된 내용을 다시 파일에 쓰기
                with open(old_filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                if 'l_english:' in content:
                    print("✅ 파일 내부 내용: 'l_english:' -> 'l_korean:'으로 변경 완료.")
                else:
                    print("ℹ️ 파일 내부에 'l_english:' 문자열이 없습니다. 내용 변경 생략.")

            except Exception as e:
                print(f"❌ 파일 내용 변경 중 오류 발생 ({filename}): {e}")
                continue # 오류 발생 시 다음 파일로 이동

            # 목표 1: 파일명의 l_english를 l_korean으로 바꿀 것
            new_filename = filename.replace('l_english', 'l_korean')
            new_filepath = os.path.join(current_dir, new_filename)
            
            try:
                os.rename(old_filepath, new_filepath)
                print(f"✅ 파일 이름 변경: '{filename}' -> '{new_filename}'")
            except Exception as e:
                print(f"❌ 파일 이름 변경 중 오류 발생 ({filename}): {e}")
            
            print("--------------------------------------\n")
        
        elif filename.endswith('.yml') and 'l_korean' in filename:
            print(f"--- 파일 처리 건너뛰기: {filename} (이미 'l_korean'이 포함되어 있음) ---\n")
            
    print("======================================")
    print("🎉 모든 파일 처리 완료.")
    print("======================================")

if __name__ == "__main__":
    change_language_in_files()