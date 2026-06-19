# Demo Upgrade 001 Runbook

## 목표

`demo-upgrade-001` 이슈를 기준으로 GitHub MCP 기반 PR 자동 요약과 리뷰 병목 감지 흐름을 시험한다.

## 실행 순서

1. GitHub에 `type:upgrade` 이슈 생성
   - 본문은 `ops/github-issue-demo-upgrade-001.md` 사용

2. Chief Agent가 실험 승인
   - 성공 기준과 롤백 조건 확인

3. Upgrade Agent가 PR 자동 요약 생성
   - `ops/pr-auto-summary-template.md` 형식 사용
   - `_get_pr_info`, `_fetch_pr`, `_list_pull_request_review_threads` 활용

4. 결과를 업그레이드 이슈에 기록
   - `ops/upgrade-issue-comment-template.md` 형식 사용

5. 실제 PR 3건 정도에 적용
   - 콘텐츠 PR
   - 운영 문서 PR
   - 업그레이드 PR

6. 실험 결과 평가
   - 요약 정확도
   - 리뷰 병목 감지 정확도
   - 대표 에이전트의 판단 시간 단축 여부

## 성공 기준

- PR 요약 형식이 일관되게 유지된다.
- unresolved 리뷰 스레드 유무를 빠르게 판단할 수 있다.
- 대표 에이전트가 PR 우선순위를 더 쉽게 정할 수 있다.

## 실패 기준

- 요약이 자주 핵심 리스크를 놓친다.
- PR 본문 품질이 낮을 때 요약 품질도 크게 흔들린다.
- 실험 운영 비용이 절감 효과보다 더 크다.
