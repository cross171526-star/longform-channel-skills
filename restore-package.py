#!/usr/bin/env python3
"""같은 폴더의 검증된 코드·자산 ZIP을 하나의 제작 패키지로 복원한다."""
from pathlib import Path
import hashlib,json,shutil,tempfile,zipfile

def main():
    root=Path(__file__).resolve().parent
    config=json.loads((root/'package-parts.json').read_text(encoding='utf-8'))
    name=config['package']
    if Path(name).name!=name or name in {'.','..'}:raise ValueError('Invalid package name')
    destination=root/name
    if destination.exists():raise FileExistsError(f'기존 폴더를 보존합니다: {destination}')
    for row in config['archives']:
        file=root/row['file']
        if file.parent!=root or not file.is_file():raise FileNotFoundError(row['file'])
        if hashlib.sha256(file.read_bytes()).hexdigest()!=row['sha256']:raise ValueError(f'ZIP 해시 불일치: {file.name}')
    with tempfile.TemporaryDirectory(prefix='.restore-',dir=root) as directory:
        temp=Path(directory);seen=set()
        for row in config['archives']:
            with zipfile.ZipFile(root/row['file']) as archive:
                for member in archive.infolist():
                    path=(temp/member.filename).resolve()
                    if not path.is_relative_to(temp/name) or member.filename in seen:raise ValueError('중복 또는 외부 경로')
                    seen.add(member.filename)
                    archive.extract(member,temp)
        for line in (temp/name/'SHA256SUMS').read_text().splitlines():
            digest,relative=line.split('  ',1)
            path=(temp/name/relative).resolve()
            if not path.is_relative_to(temp/name) or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:raise ValueError(f'파일 검증 실패: {relative}')
        if destination.exists():raise FileExistsError(destination)
        (temp/name).rename(destination)
    print(f'복원·해시 검사 완료: {destination}\n다음: cd {name} && python3 lfc.py install')

if __name__=='__main__':main()
