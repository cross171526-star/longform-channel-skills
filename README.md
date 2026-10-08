# 롱폼 채널 스킬 공유본

2026-10-08 프로젝트 원본에서 추출한 Codex 스킬 5종입니다. 제작 지침·Python/셸 코드·참조 문서·Remotion 템플릿은 수정하지 않았습니다.

## 다운로드와 설치

이 저장소의 `longform-channel-skills.zip`을 다운로드하고 압축을 풉니다. 압축 안에는 아래 스킬 폴더 5개와 프로젝트 `AGENTS.md`, 설치 스크립트, 파일 해시가 있습니다.

- longform-channel-cloner: 전체 절차
- longform-channel-analysis: 레퍼런스 분석
- longform-channel-planning: 주제와 대본
- longform-channel-production: 음성·자료·편집·렌더
- longform-channel-review: 사용자 피드백 수정

터미널에서 압축을 푼 `longform-channel-skills` 폴더로 이동한 뒤 실행합니다.

```bash
bash install-skills.sh
```

현재 배포 대상의 설치 위치는 `${CODEX_HOME:-$HOME/.codex}/skills`입니다. 기존 동명 스킬이 있으면 덮어쓰지 않고 멈춥니다. 설치 후 Codex의 새 채팅에서 `longform-channel-cloner` 스킬이 보이는지 확인하세요. 보이지 않으면 앱을 다시 시작하고 설치 경로를 확인하세요. 프로젝트 공통 지시도 유지하려면 이 압축 해제 폴더를 작업 프로젝트로 여세요.

## 실행 환경

기존 자동 환경 설정은 Apple Silicon 맥 기준입니다. Intel 맥은 ffmpeg와 Python 환경을 별도로 준비해야 합니다. 원본 설치 스크립트에는 Python 3.11 이상으로 표기되어 있지만 일부 코드가 Python 3.12 이상의 문법을 사용하므로 Python 3.12 이상을 준비하세요. Node.js는 22 이상이 필요합니다.

```bash
bash longform-channel-cloner/scripts/setup_env.sh
bash longform-channel-cloner/scripts/fetch_fonts.sh
npm ci --prefix longform-channel-cloner/assets/remotion-template
```

위 명령은 프로그램·폰트·패키지를 다운로드합니다. 라이브러리 버전은 원본에 고정된 값을 유지했으며, 새 맥에서 전체 설치와 렌더를 재검증한 배포본은 아닙니다.

기본 Typecast 음성 합성에는 본인의 `TYPECAST_API_KEY`가 필요합니다. 선택한 자료 서비스에 따라 `PEXELS_API_KEY`, `PIXABAY_API_KEY` 등도 설정합니다. 원본 스크립트는 환경변수 또는 사용자 홈의 `~/.longform-cloner/secrets.env`를 읽습니다. 키는 GitHub에 올리지 마세요.

`assets/fixed-bgm.json`에는 원본 컴퓨터의 절대경로가 보존돼 있습니다. 해당 BGM 파일은 이 묶음에 없습니다. 수신자 컴퓨터에서 문서에 지정된 음원을 준비한 후 설치된 사본의 경로를 실제 파일 위치로 맞춰야 합니다. 외부 영상·음원·폰트의 이용 조건은 해당 출처에서 확인하세요.

스킬의 지정 모델은 `gpt-6.1-sol`, 추론 수준은 `high`입니다. 파일 설치만으로 앱 모델 설정이 변경되지는 않습니다. 수신자가 사용 가능한 모델과 설정을 직접 확인해야 합니다.

## 사용 예시

Codex에서 다음과 같이 요청하세요.

> longform-channel-cloner 스킬로 이 유튜브 채널을 분석하고 3분 테스트를 만들어 줘: 채널 URL

제목 기반 테스트 주제를 먼저 제안하고, 사용자 승인 뒤 정밀 분석과 제작을 진행하도록 되어 있습니다.

## 공유 범위와 검증

인증정보·쿠키·개인 작업 로그·과거 리뷰 스냅샷·다운로드 영상·렌더 결과·캐시·가상환경·node_modules는 포함하지 않았습니다. 별별역사 등 채널 전용 스킬도 이 묶음의 범위가 아닙니다.

`SOURCE_SHA256SUMS`는 원본 파일 129개의 해시이며, `SHA256SUMS`는 설치 안내와 설치 스크립트를 포함한 압축 내 파일의 해시입니다. 원본과 사본의 바이트 일치, Python 문법, 스킬 형식을 확인했습니다. 원본 프로젝트와 현재 설치된 스킬은 변경하지 않았습니다.

비공개 저장소이므로 받는 사람의 GitHub 계정을 저장소 협업자로 초대해야 링크로 접근할 수 있습니다.
