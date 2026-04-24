# Launch Sequence

## 1단계

이 로컬 폴더를 실제 GitHub 저장소로 만든다.

## 2단계

아래 항목을 레포 초기 세팅으로 반영한다.

- `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/labels-policy.md`
- `agents/`
- `reviews/`
- `ops/`

## 3단계

첫 번째 테스트 이슈를 만든다.

예시:
- 제목: `[콘텐츠] 24개월 아이가 밥을 잘 안 먹을 때 부모가 바로 해볼 수 있는 방법`
- 라벨: `type:content`, `source:demand`, `status:research`

## 4단계

아래 순서로 에이전트를 실행한다.

1. Demand Agent가 이슈 정리
2. Research Agent가 조사 노트 작성
3. Writer Agent가 PR 생성
4. Safety Agent가 PR 검수
5. Chief Agent가 최종 판단
6. Distribution Agent가 배포문 생성

## 5단계

대표자는 매일 아래만 확인하면 된다.

- 새 이슈 수
- 리뷰 대기 PR 수
- unresolved review thread 수
- 배포 완료 콘텐츠 수

## 6단계

첫 업그레이드 루프도 함께 시작한다.

추천 첫 안건:

- `issues/demo-upgrade-001.md`

추천 흐름:

1. Upgrade Agent가 업그레이드 이슈 정리
2. Chief Agent가 실험 우선순위 승인
3. 실험용 PR 자동 요약 형식 정의
4. GitHub MCP 기반 병목 감지 루프 테스트
