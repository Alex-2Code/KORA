# KORA 운영 코디네이터 핸드북

작성일: `2026-05-06`

## 1. 목적

이 문서는 한국 운영 담당자가 개발자가 아니어도 GitHub 중심으로 KORA 운영을 도울 수 있게 하기 위한 안내서입니다.

KORA 운영 담당자는 코드를 직접 작성하는 사람이 아니라, GitHub 이슈, 보드, 주간 리포트, 관심자 정리, 문서 정리를 통해 프로젝트 흐름을 안정적으로 만드는 역할입니다.

## 2. 역할 정의

역할 이름:

- KORA Operations Coordinator

역할 성격:

- 개발 담당이 아니라 운영/정리/프로젝트 관리 담당입니다.
- 영어가 약해도 GitHub board, issue, weekly report, lead tracking, 문서 정리를 담당할 수 있습니다.
- 중요한 claim, 외부 공개 문구, 투자자/EIC/파트너 관련 표현은 Albert review로 넘깁니다.

## 3. 주요 업무

- GitHub Project board 정리
- issue 상태 업데이트
- weekly community sync 정리
- Sumanta와 Albert 사이 follow-up 정리
- 지원자/관심자 목록 정리
- EOD/SOD 자료 정리
- 한국어 내부 운영 문서 관리
- claim-sensitive 내용은 Albert review로 넘김

## 4. 하면 안 되는 일

- `main` branch에 직접 push
- release/tag 생성
- claim 임의 확장
- partnership/government validation 표현
- 투자자/EIC 문구 임의 작성
- 개인정보를 public issue에 올리기

## 5. 주간 루틴

월요일:

- board 정리
- 지난주 미완료 issue 확인
- blocked 상태 확인

수요일:

- review queue 정리
- Albert review가 필요한 항목 모으기
- Sumanta follow-up 확인

금요일:

- weekly summary 작성
- 다음 주 action 정리
- EOD/SOD 문서 확인

## 6. GitHub 초보 운영 가이드

Issues:

- 해야 할 일을 하나씩 정리하는 공간입니다.
- 각 issue에는 목표, 담당자, 완료 기준이 있어야 합니다.

Pull Requests:

- 코드나 문서 변경을 main에 합치기 전에 검토하는 공간입니다.
- 운영 담당자는 PR 상태를 확인하고 review가 필요한 사람에게 알려줄 수 있습니다.

Projects:

- 여러 issue와 PR의 진행 상태를 한눈에 보는 보드입니다.
- Backlog, In Progress, Needs Review, Done 같은 칸으로 관리합니다.

Discussions:

- 질문, 아이디어, 커뮤니티 대화를 위한 공간입니다.
- 바로 작업할 일이 되면 issue로 옮깁니다.

Wiki:

- 초보자용 안내서나 handbook을 두기 좋은 공간입니다.
- 공식 claim/evidence 문서는 repo의 `docs/`에 둡니다.

Labels:

- issue나 PR의 종류를 표시하는 태그입니다.
- 예: `community`, `benchmark`, `needs-albert-review`, `claim-sensitive`

## 7. Albert에게 Review 요청해야 하는 경우

- 숫자/benchmark claim
- partner/government/investor/EIC 표현
- 외부 공개 문구
- 논문 저자/기여자 관련 내용
- release note 또는 public announcement
- claim registry와 충돌할 수 있는 표현
